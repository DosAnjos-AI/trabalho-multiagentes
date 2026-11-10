"""Recebe um pedido em português e devolve a lista de documentos que iriam ao LLM gerador.

Uso (da raiz do projeto):
    .venv/bin/python retriever/recuperar.py <entrada.md> [--top-n N] [--rerank]

O script para na lista: não gera .gobr, não monta o prompt do gerador e só lê o
banco do Chroma. O rastro completo de cada execução vai para retriever/saidas/.
"""
import argparse
import datetime as dt
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path, PurePath

# Sem isto, importar os módulos de indexacao/ deixaria __pycache__ dentro dela.
sys.dont_write_bytecode = True

import config_retriever as cfg  # noqa: E402

# indexacao/ entra na frente do caminho porque seus módulos fazem 'import config'
# e precisam achar indexacao/config.py, não outro arquivo de mesmo nome.
sys.path.insert(0, str(cfg.PASTA_INDEXACAO))

import yaml  # noqa: E402

import config as cfg_idx  # noqa: E402
from conversao.escritor_v40 import escrever_v40  # noqa: E402
from conversao.leitor_v31 import ErroConversao, dividir_secoes, extrair_yaml, ler_v31  # noqa: E402
from indice import embeddings, lexico, vetorial  # noqa: E402

PASTA_CHROMA_ORIGINAL = cfg_idx.PASTA_CHROMA


class ErroRetriever(Exception):
    """Falha que deve parar a execução, com mensagem que diz o que fazer."""


# ---------------------------------------------------------------- normalização

def ler_prompt() -> tuple[str, str, str]:
    """Texto entre as cercas de NORMALIZACAO.md e seu sha256, conferido contra o esperado."""
    linhas = cfg.ARQUIVO_NORMALIZACAO.read_text(encoding="utf-8").split("\n")
    partes = []
    for ini, fim in (cfg.LINHAS_PROMPT_SISTEMA, cfg.LINHAS_PROMPT_USUARIO):
        for n in (ini - 1, fim + 1):
            if not linhas[n - 1].startswith("~~~~"):
                raise ErroRetriever(
                    f"{cfg.ARQUIVO_NORMALIZACAO}: linha {n} deveria ser a cerca '~~~~' e é "
                    f"{linhas[n - 1][:40]!r}. Recorte configurado em retriever/config_retriever.py "
                    "(LINHAS_PROMPT_SISTEMA, LINHAS_PROMPT_USUARIO)."
                )
        partes.append("\n".join(linhas[ini - 1:fim]))
    sistema, usuario = partes
    sha = hashlib.sha256((sistema + "\n" + usuario).encode("utf-8")).hexdigest()
    if sha != cfg.PROMPT_SHA256_ESPERADO:
        raise ErroRetriever(
            f"prompt_sha256 {sha} difere do esperado {cfg.PROMPT_SHA256_ESPERADO}: NORMALIZACAO.md "
            "mudou e as medições anteriores não valem para ele. Revise PROMPT_SHA256_ESPERADO em "
            "retriever/config_retriever.py só depois de remedir."
        )
    return sistema, usuario, sha


def ler_chave() -> str:
    """Lê a chave do .env. Nunca a devolve em mensagem: só diz se existe."""
    if not cfg.ARQUIVO_ENV.exists():
        raise ErroRetriever(f"arquivo {cfg.ARQUIVO_ENV} ausente (configurado em ARQUIVO_ENV)")
    for linha in cfg.ARQUIVO_ENV.read_text(encoding="utf-8").splitlines():
        if linha.startswith(cfg.NOME_CHAVE_ENV + "="):
            valor = linha.split("=", 1)[1].strip().strip('"').strip("'")
            if valor:
                return valor
            raise ErroRetriever(f"{cfg.NOME_CHAVE_ENV} está vazia em {cfg.ARQUIVO_ENV}")
    raise ErroRetriever(f"{cfg.NOME_CHAVE_ENV} ausente em {cfg.ARQUIVO_ENV}")


def montar_usuario(modelo: str, id_consulta: str, origem: str, texto: str) -> str:
    campos = {"{id}": id_consulta, "{caminho_do_input}": origem, **cfg.CAMPOS_CONSULTA, "{texto_do_input}": texto}
    for k, v in campos.items():
        modelo = modelo.replace(k, v)
    return modelo


def normalizar(sistema: str, usuario: str, chave: str) -> dict:
    """Uma chamada à API; no máximo uma repetição, e só para falha transitória.

    Repetir mais que isso esconde instabilidade e multiplica custo sem aviso.
    """
    corpo = json.dumps({
        "model": cfg.MODELO_NORMALIZACAO, "temperature": cfg.TEMPERATURA, "seed": cfg.SEMENTE,
        "max_tokens": cfg.MAX_TOKENS_SAIDA,
        "messages": [{"role": "system", "content": sistema}, {"role": "user", "content": usuario}],
    }).encode("utf-8")
    falhas = []
    for tentativa in (1, 2):
        req = urllib.request.Request(cfg.URL_API, data=corpo, method="POST", headers={
            "Authorization": f"Bearer {chave}", "Content-Type": "application/json"})
        t0 = time.perf_counter()
        try:
            with urllib.request.urlopen(req, timeout=cfg.TIMEOUT_API_S) as r:
                j = json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            detalhe = e.read().decode("utf-8", "replace")[:300].replace(chave, "***")
            falhas.append(f"tentativa {tentativa}: HTTP {e.code}: {detalhe}")
            if e.code != 429 and e.code < 500:
                break  # erro do pedido ou da credencial: repetir não muda nada
            continue
        except (urllib.error.URLError, TimeoutError) as e:
            falhas.append(f"tentativa {tentativa}: {type(e).__name__}: {str(e).replace(chave, '***')}")
            continue
        uso = j.get("usage", {})
        ti, to = uso.get("prompt_tokens", 0), uso.get("completion_tokens", 0)
        escolha = j["choices"][0]
        return {
            "texto": escolha["message"]["content"] or "",
            "modelo_resposta": j.get("model"),
            "finish_reason": escolha.get("finish_reason"),
            "tokens_entrada": ti, "tokens_saida": to,
            "usd": ti * cfg.PRECO_ENTRADA_USD + to * cfg.PRECO_SAIDA_USD,
            "latencia_s": round(time.perf_counter() - t0, 3),
            "tentativas": tentativa, "falhas_anteriores": falhas,
        }
    raise ErroRetriever(
        f"API de normalização falhou ({cfg.URL_API}, modelo {cfg.MODELO_NORMALIZACAO}): "
        + " | ".join(falhas) + ". Modelo e URL em retriever/config_retriever.py."
    )


# ---------------------------------------------------------------- validação e conversão

def ler_vocabulario() -> dict[str, set[str]]:
    """Vocabulários fechados lidos da seção 4 de NORMALIZACAO.md, que é o contrato.

    Lidos do arquivo, e não copiados aqui, porque indexacao/config.py já mostra o
    custo da cópia: declara 12 tipos onde o contrato declara 13.
    """
    texto = cfg.ARQUIVO_NORMALIZACAO.read_text(encoding="utf-8")
    m42 = re.search(r"### 4\.2 .*?\n(.*?)### 4\.3", texto, re.S)
    m43 = re.search(r"### 4\.3 .*?\n(.*?)\n---", texto, re.S)
    if not (m42 and m43):
        raise ErroRetriever(f"{cfg.ARQUIVO_NORMALIZACAO}: seções 4.2/4.3 de vocabulário não encontradas")
    vocab = {"criterios.tipo": set(re.findall(r"^\| `([a-z_]+)` \|", m42.group(1), re.M))}
    for campo, valores in re.findall(r"^\| ([^|]+?) \| (.+) \|$", m43.group(1), re.M):
        vocab[campo.strip("`")] = set(re.findall(r"`([^`]+)`", valores))
    exigidos = ("criterios.tipo", "criterios.operador", "criterios.unidade", "criterios.alcance",
                "acao.tipo", "acao.frequencia_tipo", "acao.frequencia_unidade", "Categoria do dicionário")
    faltam = [c for c in exigidos if not vocab.get(c)]
    if faltam:
        raise ErroRetriever(f"{cfg.ARQUIVO_NORMALIZACAO}: vocabulário ausente para {faltam}")
    return vocab


def recontar_total_regras(texto: str) -> tuple[str, object, int]:
    """Troca o total_regras escrito pelo modelo pelo número real de regras.

    No ciclo 3, 111 de 249 saídas (44,6%) foram perdidas porque o conversor aborta
    quando os dois divergem. O número escrito é opinião do modelo; a contagem é fato.
    """
    bruto_cab, secoes = dividir_secoes(texto)
    original = (yaml.safe_load(bruto_cab) or {}).get("total_regras")
    if "Representação estruturada" not in secoes:
        raise ErroConversao("consulta", "seção ausente: Representação estruturada")
    estrutura = extrair_yaml(secoes["Representação estruturada"], "consulta", "Representação estruturada")
    regras = estrutura.get("regras")
    if not isinstance(regras, list):
        raise ErroConversao("consulta", f"'regras' deveria ser lista, é {type(regras).__name__}")
    recontado = len(regras)
    if original != recontado:
        # count=1 e âncora de linha: a primeira ocorrência é a do cabeçalho, no topo do arquivo.
        texto, n = re.subn(r"^total_regras:.*$", f"total_regras: {recontado}", texto, count=1, flags=re.M)
        if n != 1:
            raise ErroConversao("consulta", "cabeçalho sem a linha total_regras")
    return texto, original, recontado


def conferir_vocabulario(dados: dict, vocab: dict[str, set[str]]) -> list[dict]:
    """Não conformidades que não impedem a conversão: registradas, nunca silenciadas."""
    achados = []

    def conferir(campo: str, valor, onde: str):
        if valor not in vocab[campo]:
            achados.append({"campo": campo, "valor": valor, "onde": onde})

    for r in dados["regras"]:
        nome = r.get("nome")
        for c in r.get("criterios") or []:
            conferir("criterios.tipo", c.get("tipo"), nome)
            conferir("criterios.operador", c.get("operador"), nome)
            conferir("criterios.unidade", c.get("unidade"), nome)
            conferir("criterios.alcance", c.get("alcance"), nome)
        acao = r.get("acao") or {}
        conferir("acao.tipo", acao.get("tipo"), nome)
        conferir("acao.frequencia_tipo", acao.get("frequencia_tipo"), nome)
        conferir("acao.frequencia_unidade", acao.get("frequencia_unidade"), nome)
    for termo, categoria, _ in dados["dicionario"]:
        if termo.strip().lower() != "nenhum":  # linha-marcador de tabela vazia
            conferir("Categoria do dicionário", categoria, termo)
    return achados


class _NormalizadoEmMemoria:
    """Imita o Path que ler_v31 espera (parent.name e read_text).

    Assim o leitor versionado roda sem alteração e com todas as suas validações,
    sem gravar o normalizado em disco só para relê-lo.
    """

    def __init__(self, id_consulta: str, texto: str):
        self.parent = PurePath(id_consulta)
        self._texto = texto

    def read_text(self, encoding: str = "utf-8") -> str:
        return self._texto


def converter(id_consulta: str, texto: str) -> tuple[dict, str]:
    try:
        dados = ler_v31(_NormalizadoEmMemoria(id_consulta, texto))
        return dados, escrever_v40(dados)
    except (ErroConversao, KeyError, TypeError, ValueError, AttributeError) as e:
        raise ErroRetriever(
            f"o normalizado não converte: {type(e).__name__}: {e}. Esperado: formato 3.1 de "
            f"{cfg.ARQUIVO_NORMALIZACAO.name} (seção 3.1), lido por indexacao/conversao/leitor_v31.py "
            "e escrito por escritor_v40.py. O texto recebido está no rastro JSON "
            "(normalizacao.texto_bruto). Prompt e modelo em retriever/config_retriever.py."
        ) from e


def extrair(texto_v40: str, dados: dict) -> tuple[str, list[str]]:
    _, secoes = dividir_secoes(texto_v40)
    linhas = [l for l in secoes.get("Regras", "").splitlines() if l.strip()]
    if not linhas:
        # Consulta vazia devolveria "os mais próximos de nada": qualquer documento.
        raise ErroRetriever("a seção ## Regras saiu vazia após a conversão; não há o que consultar")
    tipos = []
    for r in dados["regras"]:
        for c in r.get("criterios") or []:
            if c["tipo"] not in tipos:
                tipos.append(c["tipo"])
    return "\n".join(linhas), tipos


# ---------------------------------------------------------------- recuperação

def abrir_copia_do_banco(destino: str):
    """Abre a coleção a partir de uma cópia descartável de indexacao/dados/chroma/.

    O PersistentClient regrava chroma.sqlite3 e os .bin do HNSW ao fechar, mesmo
    sem nenhuma inserção (medido: sha256 mudou, tamanho não). O banco não é
    versionado e o remoto não o restaura, então o original nunca é aberto aqui.
    """
    copia = Path(destino) / "chroma"
    shutil.copytree(PASTA_CHROMA_ORIGINAL, copia)
    cfg_idx.PASTA_CHROMA = copia  # vetorial.abrir_colecao lê o caminho deste módulo
    return vetorial.abrir_colecao(criar=False)


def prefiltro_lexico(dados: dict, todos_ids: list[str]) -> tuple[list[str], dict]:
    """Pool de candidatos pelos termos do Dicionário do normalizado.

    A fonte é o Dicionário, não a prosa de ## Regras: foi o que a variante E mediu
    (0 falso negativo em 138); tokens de ## Regras medem 43 falsos negativos em 138.
    Não há filtro duro por crit_*: ele exclui o documento certo em 21% dos casos.
    """
    indice = lexico.carregar(cfg_idx.ARQUIVO_INDICE_LEXICO)
    chaves = set()
    for termo, _, _ in dados["dicionario"]:
        if termo.strip().lower() != "nenhum":
            chaves |= lexico.separar_celula(termo)
    por_termo = {c: lexico.consultar(indice, c) for c in sorted(chaves)}
    pool = sorted(set().union(*por_termo.values())) if por_termo else []
    registro = {
        "termos_extraidos": len(chaves),
        "termos_casados": sum(1 for v in por_termo.values() if v),
        "tamanho_por_termo": {c: len(v) for c, v in por_termo.items()},
        "pool_lexico": len(pool),
        "pool_vazio_caiu_para_todos": not pool,
    }
    if not pool:
        # Pool vazio nunca pode virar resposta vazia: sem termo casado, busca-se em tudo.
        pool = list(todos_ids)
    registro["pool_usado"] = len(pool)
    registro["ids_pool"] = pool
    return pool, registro


def buscar(colecao, texto_regras: str, pool: list[str], top_n: int) -> list[dict]:
    vetor = embeddings.embeddar_consultas([texto_regras])[0]  # prefixo 'query: ' vem do módulo
    r = colecao.query(query_embeddings=[vetor], n_results=min(top_n, len(pool)), ids=pool,
                      include=["documents", "distances", "metadatas"])
    return [
        {"id": i, "pasta": str(PurePath(m["normalizado_path"]).parent), "distancia": d,
         "similaridade": 1 - d, "documento": doc, "posicao_vetorial": k}
        for k, (i, d, doc, m) in enumerate(
            zip(r["ids"][0], r["distances"][0], r["documents"][0], r["metadatas"][0]), 1)
    ]


def deduplicar(candidatos: list[dict]) -> tuple[list[dict], list[dict]]:
    """Mantém, por texto idêntico de ## Regras, só o de melhor pontuação.

    O corpus tem 7 grupos de cópias, o maior com 18 membros: sem isto um único
    exemplo ocupa o contexto inteiro do gerador. Não se repõe o top-N com cópias.
    """
    mantidos, removidos, representante = [], [], {}
    for c in candidatos:  # já em ordem de distância crescente
        if c["documento"] in representante:
            rep = representante[c["documento"]]
            removidos.append({"id": c["id"], "copia_de": rep["id"], "distancia": c["distancia"],
                              "similaridade": c["similaridade"], "posicao_vetorial": c["posicao_vetorial"]})
        else:
            representante[c["documento"]] = c
            mantidos.append(c)
    return mantidos, removidos


def reranquear(texto_regras: str, mantidos: list[dict]) -> list[dict]:
    try:
        from sentence_transformers import CrossEncoder

        modelo = CrossEncoder(cfg.MODELO_RERANK, device="cpu")
    except Exception as e:
        # Cair em silêncio para o resultado sem rerank faria o rastro mentir sobre o que rodou.
        raise ErroRetriever(
            f"reranking pedido, mas o modelo {cfg.MODELO_RERANK} não carregou: {type(e).__name__}: {e}. "
            "Modelo em retriever/config_retriever.py (MODELO_RERANK); rode sem --rerank para pular."
        ) from e
    notas = modelo.predict([(texto_regras, c["documento"]) for c in mantidos], show_progress_bar=False)
    for k, (c, s) in enumerate(zip(mantidos, notas), 1):
        c["rerank"] = float(s)
        c["posicao_antes"] = k
    novos = sorted(mantidos, key=lambda c: -c["rerank"])  # sorted é estável: empate mantém a ordem vetorial
    for k, c in enumerate(novos, 1):
        c["posicao_depois"] = k
    return novos


# ---------------------------------------------------------------- manual

def ler_mapa(caminho: Path) -> dict[str, list[str]]:
    """Tabela tipo -> arquivos da seção de critérios de seleção do mapa, lida do arquivo."""
    if not caminho.exists():
        raise ErroRetriever(f"mapa do manual ausente: {caminho} (ARQUIVO_MAPA em retriever/config_retriever.py)")
    texto = caminho.read_text(encoding="utf-8")
    m = re.search(re.escape(cfg.SECAO_MAPA_TIPOS) + r"\n(.*?)(?:\n## |\Z)", texto, re.S)
    if not m:
        raise ErroRetriever(f"{caminho}: seção {cfg.SECAO_MAPA_TIPOS!r} não encontrada")
    mapa = {}
    for linha in m.group(1).splitlines():
        celulas = [c.strip() for c in linha.strip().strip("|").split("|")]
        if not linha.startswith("|") or len(celulas) != 2 or celulas[0] in ("Tipo", "") or set(celulas[0]) <= set("-"):
            continue
        mapa[celulas[0]] = [a.strip() for a in celulas[1].split(",") if a.strip()]
    if not mapa:
        raise ErroRetriever(f"{caminho}: tabela de {cfg.SECAO_MAPA_TIPOS!r} sem linhas")
    return mapa


def chavear_manual(tipos: list[str]) -> dict:
    mapa = ler_mapa(cfg.ARQUIVO_MAPA)
    fora = [t for t in tipos if t not in mapa]
    if fora:
        raise ErroRetriever(
            f"tipo(s) de critério fora da lista fechada do mapa: {fora}. Aceitos ({len(mapa)}): "
            f"{sorted(mapa)}. Lista lida de {cfg.ARQUIVO_MAPA}."
        )
    arquivos: dict[str, list[str]] = {}
    for t in tipos:
        for stem in mapa[t]:
            arquivos.setdefault(stem, []).append(t)
    tokenizador = embeddings.carregar_modelo().tokenizer

    def item(caminho: Path, trazido_por: list[str]) -> dict:
        if not caminho.exists():
            raise ErroRetriever(f"arquivo do manual ausente: {caminho} (citado por {trazido_por})")
        texto = caminho.read_text(encoding="utf-8")
        return {"arquivo": str(caminho.relative_to(cfg.RAIZ_PROJETO)), "trazido_por": trazido_por,
                "tokens": len(tokenizador(texto, add_special_tokens=False)["input_ids"])}

    fixos = [item(p, ["fixo"]) for p in cfg.MANUAL_FIXOS]
    nomes_fixos = {f["arquivo"] for f in fixos}
    chaveados = []
    for stem, ts in arquivos.items():
        it = item(cfg.PASTA_SECOES / f"{stem}.md", ts)
        if it["arquivo"] not in nomes_fixos:  # arquivo fixo citado no mapa não entra duas vezes
            chaveados.append(it)
    return {
        "mapa": str(cfg.ARQUIVO_MAPA),
        # Sem tipo, só a parte fixa: mandar os 18 arquivos "por garantia" encheria o contexto à toa.
        "sem_tipos_so_fixos": not tipos,
        "fixos": fixos, "chaveados": chaveados,
        "total_arquivos": len(fixos) + len(chaveados),
        "total_tokens": sum(i["tokens"] for i in fixos + chaveados),
        "tokenizador": cfg_idx.NOME_MODELO,
        "nao_chaveado_por_este_script": "parâmetros de atendimento e itens transversais do mapa",
    }


# ---------------------------------------------------------------- saída

def imprimir(r: dict) -> None:
    n, lx = r["normalizacao"], r["prefiltro_lexico"]
    print(f"PEDIDO: {r['entrada']['caminho']}\n")
    print("NORMALIZAÇÃO")
    print(f"  modelo {n['modelo_resposta']}, {n['latencia_s']} s, US$ {n['usd']:.5f}, "
          f"total_regras {n['total_regras_original']} -> {n['total_regras_recontado']}")
    print(f"  não conformidades: {len(n['nao_conformidades'])}")
    for a in n["nao_conformidades"]:
        print(f"    {a['campo']} = {a['valor']!r} ({a['onde']})")
    print("\nPRÉ-FILTRO LÉXICO")
    extra = " (VAZIO: caiu para todos)" if lx["pool_vazio_caiu_para_todos"] else ""
    print(f"  termos casados: {lx['termos_casados']} de {lx['termos_extraidos']} | "
          f"pool: {lx['pool_usado']} de {r['total_documentos']}{extra}")
    print(f"\nEXEMPLOS RECUPERADOS (após dedup: {len(r['exemplos'])} de top-{r['parametros']['top_n']})")
    print("  similaridade = 1 - distância de cosseno do Chroma")
    print(f"  {'#':>2}  {'pasta':<22}{'similaridade':>13}{'distância':>11}{'rerank':>9}  posição antes->depois")
    for k, c in enumerate(r["exemplos"], 1):
        rr = f"{c['rerank']:9.4f}" if "rerank" in c else f"{'-':>9}"
        mv = f"{c['posicao_antes']}->{c['posicao_depois']}" if "rerank" in c else "-"
        print(f"  {k:>2}  {c['pasta']:<22}{c['similaridade']:13.4f}{c['distancia']:11.4f}{rr}  {mv}")
    rem = ", ".join(f"{d['id']} (cópia de {d['copia_de']})" for d in r["removidos_dedup"]) or "nenhum"
    print(f"  removidos por dedup: {rem}")
    m = r["manual"]
    print("\nMANUAL RECUPERADO")
    print(f"  fixos:     {', '.join(f['arquivo'] for f in m['fixos'])}")
    if m["sem_tipos_so_fixos"]:
        print("  por tipo:  nenhum tipo de critério no normalizado; só a parte fixa")
    for c in m["chaveados"]:
        print(f"  por tipo:  {', '.join(c['trazido_por'])} -> {c['arquivo']}")
    print(f"  total: {m['total_arquivos']} arquivos, {m['total_tokens']} tokens ({m['tokenizador']})")
    print("\nLISTA FINAL PARA O GERADOR")
    for p in r["lista_final"]:
        print(f"  {p}")


def gravar(rastro: dict, nome: str, agora: dt.datetime) -> Path:
    cfg.PASTA_SAIDAS.mkdir(parents=True, exist_ok=True)
    caminho = cfg.PASTA_SAIDAS / f"{agora:%Y%m%dT%H%M%S_%f}Z_{nome}.json"
    with open(caminho, "x", encoding="utf-8") as f:  # 'x': rastro sobrescrito não é rastro
        json.dump(rastro, f, ensure_ascii=False, indent=1)
    return caminho


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("entrada", type=Path)
    ap.add_argument("--top-n", type=int, default=cfg.TOP_N_PADRAO)
    ap.add_argument("--rerank", action="store_true", help="liga o reranking (desligado por padrão)")
    args = ap.parse_args()

    agora = dt.datetime.now(dt.timezone.utc)
    entrada = args.entrada.resolve()
    id_consulta = entrada.parent.name
    try:
        origem = str(entrada.relative_to(cfg.RAIZ_PROJETO))
    except ValueError:
        origem = f"{entrada.parent.name}/{entrada.name}"  # caminho absoluto não vai para a API
    rastro = {
        "timestamp_utc": agora.isoformat(),
        "commit": subprocess.run(["git", "-C", str(cfg.RAIZ_PROJETO), "rev-parse", "HEAD"],
                                 capture_output=True, text=True).stdout.strip(),
        "entrada": {"caminho": str(entrada), "id_consulta": id_consulta, "origem_enviada": origem},
        "parametros": {"top_n": args.top_n, "rerank": args.rerank},
        "tempos_s": {},
        "etapas_concluidas": [],
    }

    def etapa(nome: str, t0: float) -> None:
        rastro["tempos_s"][nome] = round(time.perf_counter() - t0, 3)
        rastro["etapas_concluidas"].append(nome)

    codigo = 0
    pasta_temp = tempfile.TemporaryDirectory(prefix="retriever_chroma_")
    try:
        if args.top_n < 1:
            raise ErroRetriever(f"--top-n deve ser >= 1, recebeu {args.top_n}")
        texto_entrada = entrada.read_text(encoding="utf-8").strip()
        rastro["entrada"]["texto"] = texto_entrada

        t = time.perf_counter()
        sistema, modelo_usuario, sha = ler_prompt()
        rastro["prompt_sha256"] = sha
        n = normalizar(sistema, montar_usuario(modelo_usuario, id_consulta, origem, texto_entrada), ler_chave())
        rastro["normalizacao"] = {"modelo_pedido": cfg.MODELO_NORMALIZACAO, "temperatura": cfg.TEMPERATURA,
                                  "semente": cfg.SEMENTE, **{k: v for k, v in n.items() if k != "texto"},
                                  "texto_bruto": n["texto"]}
        etapa("1_normalizar", t)

        t = time.perf_counter()
        try:
            texto_corr, original, recontado = recontar_total_regras(n["texto"])
        except (ErroConversao, ValueError) as e:
            raise ErroRetriever(f"o normalizado não converte: não foi possível recontar as regras: {e}. "
                                "Esperado: formato 3.1 de NORMALIZACAO.md, seção 3.1. Texto recebido "
                                "no rastro JSON (normalizacao.texto_bruto).") from e
        rastro["normalizacao"].update(total_regras_original=original, total_regras_recontado=recontado,
                                      total_regras_divergiu=original != recontado)
        etapa("2_validar", t)

        t = time.perf_counter()
        dados, texto_v40 = converter(id_consulta, texto_corr)
        rastro["normalizacao"]["nao_conformidades"] = conferir_vocabulario(dados, ler_vocabulario())
        rastro["normalizado_v40"] = texto_v40
        etapa("3_converter", t)

        t = time.perf_counter()
        texto_regras, tipos = extrair(texto_v40, dados)
        rastro["consulta"] = {"texto_regras": texto_regras, "tipos_criterio": tipos}
        etapa("4_extrair", t)

        t = time.perf_counter()
        colecao = abrir_copia_do_banco(pasta_temp.name)
        todos = colecao.get(include=[])["ids"]
        rastro["banco"] = {"original": str(PASTA_CHROMA_ORIGINAL.relative_to(cfg.RAIZ_PROJETO)),
                           "lido_de": "cópia temporária, descartada ao final"}
        rastro["total_documentos"] = len(todos)
        if len(todos) != cfg_idx.TOTAL_PASTAS:
            raise ErroRetriever(f"coleção {cfg_idx.NOME_COLECAO} tem {len(todos)} documentos, "
                                f"esperado {cfg_idx.TOTAL_PASTAS} (indexacao/config.py)")
        pool, rastro["prefiltro_lexico"] = prefiltro_lexico(dados, todos)
        etapa("5_prefiltro_lexico", t)

        t = time.perf_counter()
        candidatos = buscar(colecao, texto_regras, pool, args.top_n)
        rastro["candidatos_vetoriais"] = [{k: v for k, v in c.items() if k != "documento"} for c in candidatos]
        etapa("6_busca_vetorial", t)

        t = time.perf_counter()
        mantidos, rastro["removidos_dedup"] = deduplicar(candidatos)
        etapa("7_dedup", t)

        if args.rerank:
            t = time.perf_counter()
            mantidos = reranquear(texto_regras, mantidos)
            etapa("8_rerank", t)
        rastro["exemplos"] = [{k: v for k, v in c.items() if k != "documento"} for c in mantidos]

        t = time.perf_counter()
        rastro["manual"] = chavear_manual(tipos)
        etapa("9_manual", t)

        m = rastro["manual"]
        rastro["lista_final"] = ([c["pasta"] for c in mantidos]
                                 + [i["arquivo"] for i in m["fixos"] + m["chaveados"]])
        imprimir(rastro)
    except ErroRetriever as e:
        rastro["erro"] = str(e)
        print(f"ERRO: {e}", file=sys.stderr)
        codigo = 1
    except Exception as e:
        rastro["erro"] = f"inesperado: {type(e).__name__}: {e}"
        raise
    finally:
        pasta_temp.cleanup()
        caminho = gravar(rastro, id_consulta, agora)
        print(f"\nRASTRO: {caminho.relative_to(cfg.RAIZ_PROJETO)}")
    return codigo


if __name__ == "__main__":
    sys.exit(main())
