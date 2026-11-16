"""Normalizador de explicacoes: limpa o texto e indica quais chaves do manual ele exige.

A mesma funcao `normalizar` serve ao corpus (193 explicacoes sinteticas) e a consulta de um usuario;
so muda quem chama. Uso:
    .venv/bin/python -B ENTREGA02/task01_normalizacao_explicacao/script_normalizacao.py --estimar
    .venv/bin/python -B ENTREGA02/task01_normalizacao_explicacao/script_normalizacao.py --executar
"""
import argparse
import difflib
import hashlib
import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from types import ModuleType

import config
from verificar_chaves import chaves_do_auxiliar

ARQ_CONFIG = "ENTREGA02/task01_normalizacao_explicacao/config.py"
NULO = "null"


class ErroConfig(ValueError):
    """Configuracao invalida; sempre diz o valor recebido, os aceitos e onde configurar."""


class ErroEntrada(ValueError):
    """Arquivo de entrada fora do formato esperado."""


def _obter(cfg: ModuleType, nome: str):
    """Le um valor do config; ausente falha com mensagem completa em vez de AttributeError."""
    if not hasattr(cfg, nome):
        raise ErroConfig(f"{nome} ausente. Defina em {ARQ_CONFIG}.")
    return getattr(cfg, nome)


def _exigir_em(cfg: ModuleType, nome: str, aceitos) -> object:
    valor = _obter(cfg, nome)
    if valor not in aceitos:
        raise ErroConfig(f"{nome} recebido: {valor!r}. Aceitos: {list(aceitos)}. Configure em {ARQ_CONFIG}.")
    return valor


def validar_config(cfg: ModuleType = config) -> None:
    """Valida tudo o que da para validar antes de ler qualquer arquivo ou chamar qualquer modelo.

    Nao olha o teto de gasto: o modo --estimar nao precisa dele (ver exigir_teto).
    """
    catalogo = _obter(cfg, "MODELOS")
    modelo = _obter(cfg, "MODELO")
    if not modelo or modelo not in catalogo:
        raise ErroConfig(f"MODELO recebido: {modelo!r}. Aceitos: {sorted(catalogo)}. Configure em {ARQ_CONFIG}.")
    info = catalogo[modelo]
    _exigir_em(cfg, "FORNECEDOR", _obter(cfg, "FORNECEDORES_ACEITOS"))
    if _obter(cfg, "FORNECEDOR") != info["fornecedor"]:
        raise ErroConfig(f"FORNECEDOR recebido: {cfg.FORNECEDOR!r}, mas {modelo} e do fornecedor "
                         f"{info['fornecedor']!r}. Configure em {ARQ_CONFIG}.")
    faixa = info.get("temperatura_aceita")
    temperatura = _obter(cfg, "TEMPERATURA")
    if faixa is None or not (faixa[0] <= temperatura <= faixa[1]):
        raise ErroConfig(f"TEMPERATURA recebido: {temperatura!r}. Aceito para {modelo}: {faixa}. "
                         f"Configure em {ARQ_CONFIG}.")
    tipos = _obter(cfg, "TIPOS_ENTRADA")
    _exigir_em(cfg, "TIPO_ENTRADA_CORPUS", tipos)
    if not set(_obter(cfg, "ORIGENS")) == {"sintetico", "usuario"}:
        raise ErroConfig(f"ORIGENS recebido: {cfg.ORIGENS!r}. Aceito: ('sintetico', 'usuario'). Configure em {ARQ_CONFIG}.")
    _exigir_em(cfg, "RETOMADA", _obter(cfg, "RETOMADAS_ACEITAS"))
    maximo = _obter(cfg, "MAX_TOKENS_SAIDA")
    if not isinstance(maximo, int) or maximo < 1:
        raise ErroConfig(f"MAX_TOKENS_SAIDA recebido: {maximo!r}. Aceita inteiro >= 1. Configure em {ARQ_CONFIG}.")
    teto = _obter(cfg, "TETO_GASTO_USD")
    if teto is not None and (not isinstance(teto, (int, float)) or teto <= 0):
        raise ErroConfig(f"TETO_GASTO_USD recebido: {teto!r}. Aceita vazio (None) ou numero > 0, em dolares. "
                         f"Configure em {ARQ_CONFIG}.")
    if len(_obter(cfg, "CAMPOS_METADADOS")) != 17 or len(set(cfg.CAMPOS_METADADOS)) != 17:
        raise ErroConfig(f"CAMPOS_METADADOS recebido: {cfg.CAMPOS_METADADOS!r}. Aceita 17 campos distintos. "
                         f"Configure em {ARQ_CONFIG}.")
    if tuple(_obter(cfg, "SECOES_OBRIGATORIAS")) != ("## explicacao_normalizada", "## regras_extraidas"):
        raise ErroConfig(f"SECOES_OBRIGATORIAS recebido: {cfg.SECOES_OBRIGATORIAS!r}. Aceito: "
                         f"('## explicacao_normalizada', '## regras_extraidas'). Configure em {ARQ_CONFIG}.")
    # Existencia dos arquivos so depois dos valores: so checa se existem, nao le o conteudo.
    if not Path(_obter(cfg, "CAMINHO_MANUAL")).is_dir():
        raise ErroConfig(f"CAMINHO_MANUAL recebido: {cfg.CAMINHO_MANUAL!s}. Aceita pasta existente. Configure em {ARQ_CONFIG}.")
    for nome in ("CAMINHO_PROMPT", "CAMINHO_AUXILIAR"):
        if not Path(_obter(cfg, nome)).is_file():
            raise ErroConfig(f"{nome} recebido: {getattr(cfg, nome)!s}. Aceita arquivo existente. Configure em {ARQ_CONFIG}.")
    for nome in ("CAMINHO_ENTRADA", "CAMINHO_SAIDA", "CAMINHO_REJEITADOS", "CAMPO_REGRAS", "CAMPO_SEM_CHAVE"):
        _obter(cfg, nome)


def exigir_teto(cfg: ModuleType = config) -> float:
    """Recusa chamada paga com teto vazio: o Mestre preenche depois de ver a estimativa."""
    teto = _obter(cfg, "TETO_GASTO_USD")
    if teto is None:
        raise ErroConfig(f"TETO_GASTO_USD recebido: None (vazio). Chamada paga recusada. Aceita numero > 0, "
                         f"em dolares, preenchido pelo Mestre depois da estimativa. Configure em {ARQ_CONFIG}.")
    return float(teto)


def sha256_bytes(caminho: Path) -> str:
    """SHA-256 do conteudo em bytes (o nome do arquivo nao entra)."""
    return hashlib.sha256(Path(caminho).read_bytes()).hexdigest()


def ler_entrada_sintetica(caminho: Path) -> str:
    """Devolve so o texto da explicacao, sem o bloco de metadados do topo.

    O bloco antigo (hash, custo, tokens) contaminaria o texto enviado ao modelo. Formato aceito: a primeira
    linha e `---`, ha exatamente duas linhas `---` no arquivo. Qualquer outra coisa e rejeitada, sem adivinhar.
    """
    linhas = Path(caminho).read_text(encoding="utf-8").splitlines()
    marcas = [i for i, linha in enumerate(linhas) if linha.strip() == "---"]
    if not linhas or linhas[0].strip() != "---":
        raise ErroEntrada(f"{caminho}: sem bloco de metadados no topo (primeira linha deve ser '---'). "
                          f"Recebido: {linhas[0][:40]!r}." if linhas else f"{caminho}: arquivo vazio.")
    if len(marcas) != 2:
        raise ErroEntrada(f"{caminho}: esperadas exatamente 2 linhas '---' (abre e fecha o bloco de metadados), "
                          f"encontradas {len(marcas)} nas linhas {[m + 1 for m in marcas]}.")
    texto = "\n".join(linhas[marcas[1] + 1:]).strip()
    if not texto:
        raise ErroEntrada(f"{caminho}: texto vazio depois do bloco de metadados.")
    return texto


def montar_mensagem_usuario(auxiliar: str, tipo_entrada: str, texto: str) -> str:
    """Corpo da mensagem do usuario: auxiliar inteiro, tipo e texto. O prompt vai na mensagem de sistema."""
    return (f"=== ARQUIVO AUXILIAR (material de consulta) ===\n{auxiliar.strip()}\n\n"
            f"=== TIPO_ENTRADA ===\n{tipo_entrada}\n\n"
            f"=== TEXTO_DA_ENTRADA ===\n{texto.strip()}\n")


def validar_resposta(resposta: str, chaves: list[str], caminho_auxiliar: Path, cfg: ModuleType = config) -> list[str]:
    """Lista de erros da resposta do modelo; vazia quando e valida."""
    erros: list[str] = []
    linhas = resposta.strip().splitlines()
    cab_texto, cab_regras = cfg.SECOES_OBRIGATORIAS
    for cab in cfg.SECOES_OBRIGATORIAS:
        n = sum(1 for linha in linhas if linha.rstrip() == cab)
        if n != 1:
            erros.append(f"cabecalho {cab!r} aparece {n} vez(es); esperado exatamente 1")
    extras = [linha for linha in linhas if linha.startswith("## ") and linha.rstrip() not in cfg.SECOES_OBRIGATORIAS]
    erros += [f"cabecalho inesperado {e!r}" for e in extras]
    if erros:
        return erros
    i_texto = next(i for i, linha in enumerate(linhas) if linha.rstrip() == cab_texto)
    i_regras = next(i for i, linha in enumerate(linhas) if linha.rstrip() == cab_regras)
    if i_texto != 0:
        erros.append(f"ha conteudo antes de {cab_texto!r} (primeira linha: {linhas[0][:40]!r})")
    if i_regras < i_texto:
        erros.append(f"{cab_regras!r} aparece antes de {cab_texto!r}")
        return erros
    if not "".join(linhas[i_texto + 1:i_regras]).strip():
        erros.append(f"secao {cab_texto!r} vazia")
    vistas: set[str] = set()
    corpo_regras = [linha.strip() for linha in linhas[i_regras + 1:] if linha.strip()]
    if not corpo_regras:
        erros.append(f"secao {cab_regras!r} vazia")
    for linha in corpo_regras:
        if linha.startswith(config.PREFIXO_SEM_CHAVE):
            if not linha[len(config.PREFIXO_SEM_CHAVE):].strip():
                erros.append(f"linha {linha!r}: 'sem_chave:' sem descricao")
        elif linha not in chaves:
            perto = difflib.get_close_matches(linha, chaves, n=1, cutoff=0.8)
            dica = f" Chave mais proxima: {perto[0]!r}." if perto else ""
            erros.append(f"chave recebida {linha!r} nao existe no arquivo auxiliar; procurar a linha "
                         f"'- chave:' correspondente em {caminho_auxiliar}.{dica}")
        if linha in vistas:
            erros.append(f"chave repetida: {linha!r}")
        vistas.add(linha)
    return erros


def converter_regras(linhas: list[str], cfg: ModuleType = config) -> dict:
    """Linhas validadas (uma chave por linha) -> {regras_extraidas: [arquivos], sem_chave: [textos]}.

    Corta o `#Titulo` porque o destino quer so o nome do arquivo do manual; deduplica porque varias secoes
    do mesmo arquivo viram uma entrada. Sem LLM: o validador ja garantiu chave exata. Confere o arquivo no disco
    porque o auxiliar pode ter ficado para tras do manual.
    """
    regras: list[str] = []
    sem_chave: list[str] = []
    for linha in linhas:
        linha = linha.strip()
        if not linha:
            continue
        if linha.startswith(cfg.PREFIXO_SEM_CHAVE):
            texto = linha[len(cfg.PREFIXO_SEM_CHAVE):].strip()
            if texto not in sem_chave:
                sem_chave.append(texto)
            continue
        arquivo = linha.partition("#")[0].strip()
        if not (Path(cfg.CAMINHO_MANUAL) / arquivo).is_file():
            raise ErroEntrada(f"regra {linha!r}: arquivo {arquivo!r} nao existe em {cfg.CAMINHO_MANUAL}.")
        if arquivo not in regras:
            regras.append(arquivo)
    return {cfg.CAMPO_REGRAS: regras, cfg.CAMPO_SEM_CHAVE: sem_chave}


def substituir_secao_regras(texto: str, cfg: ModuleType = config) -> str:
    """Troca o corpo de `## regras_extraidas` (linhas) pelo JSON. Idempotente: se ja e JSON, devolve igual."""
    cab = cfg.SECOES_OBRIGATORIAS[1]
    linhas = texto.rstrip("\n").split("\n")
    indices = [i for i, linha in enumerate(linhas) if linha.rstrip() == cab]
    if len(indices) != 1:
        raise ErroEntrada(f"cabecalho {cab!r} aparece {len(indices)} vez(es); esperado exatamente 1.")
    corpo = linhas[indices[0] + 1:]
    if "".join(corpo).strip().startswith("{"):
        return texto
    obj = converter_regras(corpo, cfg)
    return "\n".join(linhas[:indices[0] + 1]) + "\n" + json.dumps(obj, ensure_ascii=False, indent=2) + "\n"


def custo(cfg: ModuleType, tok_in: float, tok_out: float) -> float:
    """Custo em dolares; precos por milhao de tokens vindos do catalogo do config."""
    m = cfg.MODELOS[cfg.MODELO]
    return (tok_in * m["entrada_por_milhao"] + tok_out * m["saida_por_milhao"]) / 1_000_000


def projetar_custo(cfg: ModuleType, caracteres_entrada: int) -> float:
    """Projecao pessimista da proxima chamada: entrada estimada no pior caso e saida no limite maximo."""
    return custo(cfg, caracteres_entrada / cfg.CARACTERES_POR_TOKEN_PESSIMISTA, cfg.MAX_TOKENS_SAIDA)


def carregar_env(cfg: ModuleType = config) -> None:
    """Carrega o .env para os.environ sem sobrescrever; so e chamado na execucao paga."""
    if not cfg.CAMINHO_ENV.exists():
        return
    for linha in cfg.CAMINHO_ENV.read_text(encoding="utf-8").splitlines():
        linha = linha.strip()
        if not linha or linha.startswith("#") or "=" not in linha:
            continue
        chave, valor = linha.split("=", 1)
        os.environ.setdefault(chave.strip(), valor.strip().strip("\"'"))


def chamar_openai(modelo: str, prompt: str, usuario: str) -> tuple[str, int, int, bool]:
    """Chama a OpenAI e devolve (texto, tokens_entrada, tokens_saida, cortada). Nao e usada nos testes."""
    from openai import OpenAI

    carregar_env()
    variavel = config.VARIAVEL_CHAVE["openai"]
    if not os.environ.get(variavel, "").strip():
        raise ErroConfig(f"Chave de API ausente ou vazia. Variavel esperada: {variavel}. "
                         f"Defina em {config.CAMINHO_ENV} (arquivo .env da raiz).")
    cliente = OpenAI(api_key=os.environ[variavel])
    r = cliente.chat.completions.create(
        model=modelo,
        messages=[{"role": "system", "content": prompt}, {"role": "user", "content": usuario}],
        # o gpt-6.1-terra so aceita temperatura 1 (padrao): nao enviar o parametro
        max_completion_tokens=config.MAX_TOKENS_SAIDA,
    )
    cortada = r.choices[0].finish_reason == "length"
    return r.choices[0].message.content or "", r.usage.prompt_tokens, r.usage.completion_tokens, cortada


def rotulo_temperatura(cfg: ModuleType) -> str:
    """Diz o que aconteceu com a temperatura, no mesmo padrao da tarefa 02."""
    if cfg.MODELOS[cfg.MODELO].get("temperatura_aceita") == (1.0, 1.0):
        return "1.0 (padrao imposto pelo modelo)"
    return f"{cfg.TEMPERATURA}"


def montar_metadados(valores: dict, cfg: ModuleType = config) -> str:
    """Bloco de metadados na ordem fixa; campo vazio vira null. Escrito pelo script, nunca pelo modelo."""
    linhas = ["---"] + [f"{c}: {NULO if valores[c] is None else valores[c]}" for c in cfg.CAMPOS_METADADOS] + ["---"]
    return "\n".join(linhas) + "\n\n"


def normalizar(texto: str, tipo_entrada: str, id_saida: str, *, origem: str, id_explicacao: str | None,
               id_sessao_turno: str | None, chamar, cfg: ModuleType = config) -> dict:
    """Normaliza uma entrada. Nao grava nada: devolve o resultado para quem chamou decidir.

    `chamar(modelo, prompt, usuario)` devolve (texto, tokens_entrada, tokens_saida, cortada). Nos testes e uma
    funcao falsa; no lote real e chamar_openai. Mesmo codigo para corpus e usuario: so muda quem chama.
    Devolve dict com: id, ok, erros, resposta, markdown (so se ok), tokens_entrada, tokens_saida, custo_usd.
    """
    if tipo_entrada not in cfg.TIPOS_ENTRADA:
        raise ErroConfig(f"tipo_entrada recebido: {tipo_entrada!r}. Aceitos: {list(cfg.TIPOS_ENTRADA)}. "
                         f"Configure em {ARQ_CONFIG}.")
    if origem not in cfg.ORIGENS:
        raise ErroConfig(f"origem recebido: {origem!r}. Aceitos: {list(cfg.ORIGENS)}. Configure em {ARQ_CONFIG}.")
    if origem == "sintetico" and (id_sessao_turno is not None or not id_explicacao):
        raise ErroEntrada("origem sintetico exige id_explicacao e id_sessao_turno vazio (null).")
    if origem == "usuario" and (id_explicacao is not None or not id_sessao_turno):
        raise ErroEntrada("origem usuario exige id_sessao_turno e id_explicacao vazio (null).")
    prompt = Path(cfg.CAMINHO_PROMPT).read_text(encoding="utf-8")
    auxiliar = Path(cfg.CAMINHO_AUXILIAR).read_text(encoding="utf-8")
    usuario = montar_mensagem_usuario(auxiliar, tipo_entrada, texto)
    inicio = time.monotonic()
    resposta, tok_in, tok_out, cortada = chamar(cfg.MODELO, prompt, usuario)
    tempo = time.monotonic() - inicio
    c = custo(cfg, tok_in, tok_out)
    resultado = {"id": id_saida, "ok": False, "erros": [], "resposta": resposta, "markdown": None,
                 "tokens_entrada": tok_in, "tokens_saida": tok_out, "custo_usd": c}
    if cortada:
        resultado["erros"].append(f"resposta cortada no limite de {cfg.MAX_TOKENS_SAIDA} tokens de saida")
    else:
        resultado["erros"] = validar_resposta(resposta, chaves_do_auxiliar(auxiliar), Path(cfg.CAMINHO_AUXILIAR), cfg)
    if resultado["erros"]:
        return resultado
    meta = montar_metadados({
        "origem": origem, "tipo_entrada": tipo_entrada, "id_sessao_turno": id_sessao_turno,
        "id_explicacao": id_explicacao, "id_prompt": cfg.ID_PROMPT,
        "hash_prompt": sha256_bytes(cfg.CAMINHO_PROMPT), "id_auxiliar_manual": cfg.ID_AUXILIAR_MANUAL,
        "hash_auxiliar_manual": sha256_bytes(cfg.CAMINHO_AUXILIAR), "versao_normalizador": cfg.VERSAO_NORMALIZADOR,
        # hash do proprio script: prova qual codigo gerou o arquivo
        "hash_normalizador": sha256_bytes(Path(__file__)), "modelo": cfg.MODELO,
        "temperatura": rotulo_temperatura(cfg), "tokens_entrada": tok_in, "tokens_saida": tok_out,
        "custo_usd": f"{c:.6f}", "tempo_segundos": f"{tempo:.2f}",
        "timestamp": datetime.now().astimezone().isoformat(timespec="seconds"),
    }, cfg)
    try:
        corpo = substituir_secao_regras(resposta.strip(), cfg)
    except ErroEntrada as e:
        resultado["erros"].append(str(e))
        return resultado
    resultado["ok"] = True
    resultado["markdown"] = meta + corpo
    return resultado


def gravar_resultado(resultado: dict, pasta_saida: Path, pasta_rejeitados: Path) -> Path:
    """Grava normalizado_{id}.md (ok) ou a resposta crua em rejeitados. Nunca sobrescreve (modo 'x')."""
    if resultado["ok"]:
        pasta_saida.mkdir(parents=True, exist_ok=True)
        destino = pasta_saida / f"normalizado_{resultado['id']}.md"
        with destino.open("x", encoding="utf-8", newline="\n") as f:
            f.write(resultado["markdown"])
        return destino
    pasta_rejeitados.mkdir(parents=True, exist_ok=True)
    # carimbo no nome: duas rejeicoes do mesmo id (rodadas diferentes) nao se sobrescrevem
    carimbo = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    destino = pasta_rejeitados / f"rejeitado_{resultado['id']}_{carimbo}.txt"
    with destino.open("x", encoding="utf-8", newline="\n") as f:
        f.write(resultado["resposta"])
    return destino


def listar_entradas(cfg: ModuleType, ids: list[str] | None = None) -> list[tuple[str, Path]]:
    """(id, caminho) das explicacoes sinteticas, em ordem de id; `ids` restringe a lista (amostra).

    Id pedido que nao existe falha alto: amostra silenciosamente menor que a pedida seria erro de custo.
    """
    achados = []
    for caminho in sorted(Path(cfg.CAMINHO_ENTRADA).glob("entrada_*.md")):
        m = re.fullmatch(r"entrada_(\d+)\.md", caminho.name)
        if m:
            achados.append((m.group(1), caminho))
    if ids is not None:
        faltam = sorted(set(ids) - {i for i, _ in achados})
        if faltam:
            raise ErroEntrada(f"ids recebidos sem arquivo em {cfg.CAMINHO_ENTRADA}: {faltam}")
        achados = [a for a in achados if a[0] in ids]
    return achados


def executar_lote(chamar, cfg: ModuleType = config, ids: list[str] | None = None) -> int:
    """Lote das explicacoes sinteticas. Devolve codigo de saida: 0 sem rejeitado, 1 com rejeitado ou teto."""
    validar_config(cfg)
    teto = exigir_teto(cfg)
    prompt_chars = len(Path(cfg.CAMINHO_PROMPT).read_text(encoding="utf-8"))
    aux_chars = len(Path(cfg.CAMINHO_AUXILIAR).read_text(encoding="utf-8"))
    sucessos = pulados = rejeitados = 0
    gasto = 0.0
    parou_teto = False
    for id_, caminho in listar_entradas(cfg, ids):
        destino = Path(cfg.CAMINHO_SAIDA) / f"normalizado_{id_}.md"
        if destino.exists():  # retomada: nunca sobrescreve e nao paga de novo
            pulados += 1
            print(f"pulado {id_}: {destino.name} ja existe")
            continue
        try:
            texto = ler_entrada_sintetica(caminho)
        except ErroEntrada as e:
            rejeitados += 1
            print(f"REJEITADO {id_}: {e}")
            continue
        projecao = projetar_custo(cfg, prompt_chars + aux_chars + len(texto))
        if gasto + projecao > teto:
            print(f"TETO: gasto {gasto:.4f} + projecao {projecao:.4f} > {teto} USD. Parando.")
            parou_teto = True
            break
        try:
            r = normalizar(texto, cfg.TIPO_ENTRADA_CORPUS, id_, origem="sintetico", id_explicacao=caminho.name,
                           id_sessao_turno=None, chamar=chamar, cfg=cfg)
        except Exception as e:  # falha de uma chamada nao derruba o lote; e contada e impressa
            rejeitados += 1
            print(f"REJEITADO {id_}: {type(e).__name__}: {str(e)[:300]}")
            continue
        gasto += r["custo_usd"]
        # grava logo apos a chamada: resposta paga nao se perde
        arquivo = gravar_resultado(r, Path(cfg.CAMINHO_SAIDA), Path(cfg.CAMINHO_REJEITADOS))
        if r["ok"]:
            sucessos += 1
            print(f"ok {id_} in={r['tokens_entrada']} out={r['tokens_saida']} usd={r['custo_usd']:.6f}")
        else:
            rejeitados += 1
            print(f"REJEITADO {id_}: {'; '.join(r['erros'])} (resposta crua em {arquivo})")
    print(f"sucessos={sucessos} pulados={pulados} rejeitados={rejeitados} gasto_total_usd={gasto:.6f} "
          f"teto_atingido={parou_teto}")
    return 1 if (rejeitados or parou_teto) else 0


def _metadados_antigos(caminho: Path) -> dict:
    """Campos chave: valor do bloco de metadados da tarefa 02 (usado so no cruzamento de preco)."""
    linhas = caminho.read_text(encoding="utf-8").splitlines()
    fim = linhas[1:].index("---") + 1
    return dict(linha.split(": ", 1) for linha in linhas[1:fim])


def cruzar_preco(cfg: ModuleType) -> dict:
    """Fonte (b): preco implicito nos tokens e custos reais gravados nas 193 explicacoes.

    Minimos quadrados de custo = a*tokens_entrada + b*tokens_saida (2 incognitas, sem numpy: KISS).
    """
    sxx = sxy = syy = sxc = syc = 0.0
    n = 0
    for _id, caminho in listar_entradas(cfg):
        m = _metadados_antigos(caminho)
        x, y, c = int(m["tokens_entrada"]), int(m["tokens_saida"]), float(m["custo_usd"])
        sxx += x * x; sxy += x * y; syy += y * y; sxc += x * c; syc += y * c
        n += 1
    det = sxx * syy - sxy * sxy
    a = (sxc * syy - syc * sxy) / det
    b = (syc * sxx - sxc * sxy) / det
    return {"n": n, "entrada_por_milhao": a * 1e6, "saida_por_milhao": b * 1e6}


def estimar(cfg: ModuleType = config, ids: list[str] | None = None) -> int:
    """Estimativa de custo das 193 explicacoes SEM chamar o modelo (contagem local aproximada)."""
    validar_config(cfg)
    prompt = Path(cfg.CAMINHO_PROMPT).read_text(encoding="utf-8")
    auxiliar = Path(cfg.CAMINHO_AUXILIAR).read_text(encoding="utf-8")
    n = 0
    tot_in_min = tot_in_max = tot_out_min = tot_out_max = 0.0
    erros = []
    for id_, caminho in listar_entradas(cfg, ids):
        try:
            texto = ler_entrada_sintetica(caminho)
        except ErroEntrada as e:
            erros.append(str(e))
            continue
        chars_in = len(prompt) + len(montar_mensagem_usuario(auxiliar, cfg.TIPO_ENTRADA_CORPUS, texto))
        tot_in_min += chars_in / cfg.CARACTERES_POR_TOKEN_OTIMISTA
        tot_in_max += chars_in / cfg.CARACTERES_POR_TOKEN_PESSIMISTA
        tot_out_min += len(texto) / cfg.CARACTERES_POR_TOKEN_OTIMISTA + cfg.TOKENS_CHAVES_MIN
        tot_out_max += len(texto) * cfg.TOKENS_SAIDA_POR_CARACTERE_MAX + cfg.TOKENS_CHAVES_MAX
        n += 1
    m = cfg.MODELOS[cfg.MODELO]
    c_min, c_max = custo(cfg, tot_in_min, tot_out_min), custo(cfg, tot_in_max, tot_out_max)
    c_teto = custo(cfg, tot_in_max, n * cfg.MAX_TOKENS_SAIDA)
    cruz = cruzar_preco(cfg)
    print(f"modelo={cfg.MODELO} preco(a) config: entrada={m['entrada_por_milhao']} saida={m['saida_por_milhao']} US$/milhao")
    print(f"preco(b) implicito nas {cruz['n']} explicacoes: entrada={cruz['entrada_por_milhao']:.4f} "
          f"saida={cruz['saida_por_milhao']:.4f} US$/milhao")
    print(f"entradas={n} (erros de formato: {len(erros)})")
    print(f"tokens_entrada: min={tot_in_min:,.0f} max={tot_in_max:,.0f}  [HIPOTESE: sem tokenizador local; "
          f"{cfg.CARACTERES_POR_TOKEN_OTIMISTA} e {cfg.CARACTERES_POR_TOKEN_PESSIMISTA} caracteres por token]")
    print(f"tokens_saida projetados: min={tot_out_min:,.0f} max={tot_out_max:,.0f}")
    print(f"custo_usd: min={c_min:.4f} max={c_max:.4f}  (pior caso, cada chamada no limite de "
          f"{cfg.MAX_TOKENS_SAIDA} tokens de saida: {c_teto:.4f})")
    for e in erros:
        print("ERRO de formato:", e)
    return 1 if erros else 0


def converter_existentes(cfg: ModuleType = config, ids: list[str] | None = None, simular: bool = False) -> int:
    """Reescreve a secao regras_extraidas dos normalizado_*.md ja gerados (sem LLM, sem custo).

    Mexe so na secao; metadados e explicacao ficam byte a byte. Arquivo ja em JSON e pulado. Sem `simular`,
    a copia original fica no git (saida paga nao se perde); com `simular` nada e gravado.
    """
    convertidos = pulados = erros = 0
    for caminho in sorted(Path(cfg.CAMINHO_SAIDA).glob("normalizado_*.md")):
        id_ = caminho.stem.removeprefix("normalizado_")
        if ids is not None and id_ not in ids:
            continue
        antigo = caminho.read_bytes().decode("utf-8")
        try:
            novo = substituir_secao_regras(antigo, cfg)
        except ErroEntrada as e:
            erros += 1
            print(f"ERRO {id_}: {e}")
            continue
        if novo == antigo:
            pulados += 1
            continue
        convertidos += 1
        if simular:
            print(f"--- {id_} (simulado)\n{novo.split(cfg.SECOES_OBRIGATORIAS[1], 1)[1].strip()}")
        else:
            caminho.write_text(novo, encoding="utf-8", newline="\n")
    print(f"convertidos={convertidos} pulados={pulados} erros={erros} simulado={simular}")
    return 1 if erros else 0


def main() -> int:
    ap = argparse.ArgumentParser(add_help=False, description="Normalizador de explicacoes (corpus sintetico).")
    ap.add_argument("--ajuda", "-h", action="help", help="mostra esta ajuda")
    ap.add_argument("--ids", help="ids separados por virgula (ex.: 037,057); restringe a lista, para amostra")
    grupo = ap.add_mutually_exclusive_group(required=True)
    grupo.add_argument("--estimar", action="store_true", help="estima tokens e custo das explicacoes; NAO chama o modelo")
    grupo.add_argument("--executar", action="store_true",
                       help="roda o lote real (chamada paga; exige TETO_GASTO_USD preenchido no config)")
    grupo.add_argument("--converter-existentes", action="store_true",
                       help="reescreve regras_extraidas dos normalizados ja gravados no formato JSON; sem chamada paga")
    ap.add_argument("--simular", action="store_true", help="com --converter-existentes: mostra, sem gravar")
    args = ap.parse_args()
    try:
        ids = [i.strip() for i in args.ids.split(",") if i.strip()] if args.ids else None
        if args.converter_existentes:
            validar_config(config)
            return converter_existentes(config, ids, args.simular)
        return estimar(config, ids) if args.estimar else executar_lote(chamar_openai, config, ids)
    except (ErroConfig, ErroEntrada) as e:
        print(f"FALHA: {e}")
        return 2


if __name__ == "__main__":
    sys.exit(main())
