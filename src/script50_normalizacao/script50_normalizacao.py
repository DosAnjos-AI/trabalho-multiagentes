"""No de normalizacao: limpa o texto de um turno e indica quais arquivos do manual ele exige.

O no nao escreve em disco nem no BigQuery. A saida e um objeto devolvido pela funcao; quem persiste e outro no.
Prompt, auxiliar e caminhos do manual vem do BigQuery e sao carregados uma vez, em `construir_contexto`.
Nenhuma funcao deste modulo le configuracao global: o config entra so em `construir_contexto`, como parametro.

Uso:
    ctx = construir_contexto(config)
    resultado = normalizar_turno("texto da entrada", "usuario", "texto", "sessao1-turno3", ctx)
"""
import difflib
import hashlib
import json
import os
import re
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from types import ModuleType

ARQ_CONFIG = "config.py"
# Valores da coluna `tipo` da tabela de prompts (parte do esquema, nao configuracao).
TIPO_PROMPT = "normalizador"
TIPO_AUXILIAR = "auxiliar_manual"


class ErroConfig(ValueError):
    """Configuracao ou argumento invalido; sempre diz o valor recebido, os aceitos e onde configurar."""


class ErroEntrada(ValueError):
    """Entrada ou resposta fora do formato esperado."""


class ErroContexto(RuntimeError):
    """Dado do BigQuery fora do esquema ou do numero de linhas esperado; o no para sem escolher por conta propria."""


class ErroTeto(RuntimeError):
    """Projecao de custo da chamada acima do teto por turno."""


@dataclass(frozen=True)
class Contexto:
    """Tudo o que o no precisa, lido uma vez na partida. Imutavel: nenhum turno altera o contexto."""
    cliente: object
    prompt: str
    auxiliar: str
    chaves: tuple[str, ...]
    caminhos_manual: frozenset[str]
    id_prompt: str
    hash_prompt: str
    id_auxiliar: str
    hash_auxiliar: str
    hash_normalizador: str
    versao_normalizador: str
    modelo: str
    rotulo_temperatura: str
    preco_entrada: float
    preco_saida: float
    max_tokens_saida: int
    teto_gasto_usd: float
    caracteres_por_token: float
    tipos_entrada: tuple[str, ...]
    origens: tuple[str, ...]
    secoes: tuple[str, str]
    prefixo_sem_chave: str
    campo_regras: str
    campo_sem_chave: str
    campos_metadados: tuple[str, ...]


@dataclass
class Resultado:
    """Saida de um turno. `resposta_crua` vai sempre, inclusive quando a validacao falha (chamada paga nao se perde)."""
    ok: bool
    texto_normalizado: str | None
    regras_extraidas: dict | None
    metadados: dict
    erros: list[str]
    resposta_crua: str


def chaves_do_auxiliar(texto: str) -> list[str]:
    """Chaves declaradas no arquivo auxiliar (antes de '## Sem entrada'), na ordem do arquivo.

    Copiada de verificar_chaves.py (commit 0e43c8a). A mesma lista decide se a chave devolvida pelo modelo existe.
    """
    corpo = texto.partition("## Sem entrada")[0]
    return re.findall(r"^- chave: (.+)$", corpo, flags=re.M)


def _sha256(texto: str) -> str:
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()


def _ler_prompt_ativo(bq, tabela: str, tipo: str) -> dict:
    """Linha unica ativa do tipo. Zero ou mais de uma linha e parada: o no nao escolhe sozinho."""
    from google.cloud import bigquery

    consulta = (f"SELECT arquivo, versao, texto, `hash` FROM `{tabela}` WHERE tipo = @tipo AND ativo")
    config_job = bigquery.QueryJobConfig(query_parameters=[bigquery.ScalarQueryParameter("tipo", "STRING", tipo)])
    linhas = [dict(r) for r in bq.query(consulta, job_config=config_job).result()]
    if len(linhas) != 1:
        raise ErroContexto(f"{tabela}: {len(linhas)} linhas ativas para tipo={tipo!r}; esperada exatamente 1.")
    linha = linhas[0]
    # O hash gravado precisa regerar do texto: senao o metadado hash_prompt mentiria sobre o que foi enviado.
    if _sha256(linha["texto"]) != linha["hash"]:
        raise ErroContexto(f"{tabela}: tipo={tipo!r} arquivo={linha['arquivo']!r}: hash gravado nao confere com o texto.")
    return linha


def construir_contexto(cfg: ModuleType) -> Contexto:
    """Le o BigQuery e cria o cliente da OpenAI, uma vez. Falha alto, antes de qualquer chamada paga."""
    from google.cloud import bigquery
    from openai import OpenAI

    variavel = cfg.VARIAVEL_CHAVE
    chave = os.environ.get(variavel, "").strip()
    if not chave:
        raise ErroConfig(f"Variavel de ambiente {variavel} ausente ou vazia. Defina-a no ambiente "
                         f"(nome configurado em {ARQ_CONFIG}).")
    bq = bigquery.Client(project=cfg.PROJETO_GCP)
    base = f"{cfg.PROJETO_GCP}.{cfg.DATASET}"
    prompt = _ler_prompt_ativo(bq, f"{base}.{cfg.TABELA_PROMPTS}", TIPO_PROMPT)
    auxiliar = _ler_prompt_ativo(bq, f"{base}.{cfg.TABELA_PROMPTS}", TIPO_AUXILIAR)
    caminhos = frozenset(r["caminho"] for r in bq.query(f"SELECT caminho FROM `{base}.{cfg.TABELA_MANUAL}`").result())
    if not caminhos:
        raise ErroContexto(f"{base}.{cfg.TABELA_MANUAL}: nenhuma linha; o manual e necessario para conferir as chaves.")
    chaves = chaves_do_auxiliar(auxiliar["texto"])
    if not chaves:
        raise ErroContexto(f"auxiliar {auxiliar['arquivo']!r}: nenhuma linha '- chave:' encontrada.")
    info = cfg.MODELOS[cfg.MODELO]
    rotulo = "1.0 (padrao imposto pelo modelo)" if info["temperatura_aceita"] == (1.0, 1.0) else f"{cfg.TEMPERATURA}"
    return Contexto(
        cliente=OpenAI(api_key=chave),
        prompt=prompt["texto"], auxiliar=auxiliar["texto"], chaves=tuple(chaves), caminhos_manual=caminhos,
        id_prompt=prompt["arquivo"], hash_prompt=prompt["hash"],
        id_auxiliar=auxiliar["arquivo"], hash_auxiliar=auxiliar["hash"],
        # hash do proprio codigo: prova qual versao do no gerou o resultado
        hash_normalizador=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        versao_normalizador=cfg.VERSAO_NORMALIZADOR, modelo=cfg.MODELO, rotulo_temperatura=rotulo,
        preco_entrada=info["entrada_por_milhao"], preco_saida=info["saida_por_milhao"],
        max_tokens_saida=cfg.MAX_TOKENS_SAIDA, teto_gasto_usd=float(cfg.TETO_GASTO_USD),
        caracteres_por_token=cfg.CARACTERES_POR_TOKEN_PESSIMISTA,
        tipos_entrada=tuple(cfg.TIPOS_ENTRADA), origens=tuple(cfg.ORIGENS), secoes=tuple(cfg.SECOES_OBRIGATORIAS),
        prefixo_sem_chave=cfg.PREFIXO_SEM_CHAVE, campo_regras=cfg.CAMPO_REGRAS, campo_sem_chave=cfg.CAMPO_SEM_CHAVE,
        campos_metadados=tuple(cfg.CAMPOS_METADADOS),
    )


def montar_mensagem_usuario(auxiliar: str, tipo_entrada: str, texto: str) -> str:
    """Corpo da mensagem do usuario: auxiliar inteiro, tipo e texto. O prompt vai na mensagem de sistema."""
    return (f"=== ARQUIVO AUXILIAR (material de consulta) ===\n{auxiliar.strip()}\n\n"
            f"=== TIPO_ENTRADA ===\n{tipo_entrada}\n\n"
            f"=== TEXTO_DA_ENTRADA ===\n{texto.strip()}\n")


def validar_resposta(resposta: str, chaves: list[str], id_auxiliar: str, secoes: tuple[str, str],
                     prefixo_sem_chave: str) -> list[str]:
    """Lista de erros da resposta do modelo; vazia quando e valida."""
    erros: list[str] = []
    linhas = resposta.strip().splitlines()
    cab_texto, cab_regras = secoes
    for cab in secoes:
        n = sum(1 for linha in linhas if linha.rstrip() == cab)
        if n != 1:
            erros.append(f"cabecalho {cab!r} aparece {n} vez(es); esperado exatamente 1")
    extras = [linha for linha in linhas if linha.startswith("## ") and linha.rstrip() not in secoes]
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
        if linha.startswith(prefixo_sem_chave):
            if not linha[len(prefixo_sem_chave):].strip():
                erros.append(f"linha {linha!r}: 'sem_chave:' sem descricao")
        elif linha not in chaves:
            perto = difflib.get_close_matches(linha, chaves, n=1, cutoff=0.8)
            dica = f" Chave mais proxima: {perto[0]!r}." if perto else ""
            erros.append(f"chave recebida {linha!r} nao existe no arquivo auxiliar; procurar a linha "
                         f"'- chave:' correspondente em {id_auxiliar}.{dica}")
        if linha in vistas:
            erros.append(f"chave repetida: {linha!r}")
        vistas.add(linha)
    return erros


def converter_regras(linhas: list[str], caminhos_manual: frozenset[str], prefixo_sem_chave: str,
                     campo_regras: str, campo_sem_chave: str) -> dict:
    """Linhas validadas (uma chave por linha) -> {regras_extraidas: [arquivos], sem_chave: [textos]}.

    Corta o `#Titulo` porque o destino quer so o nome do arquivo do manual; deduplica porque varias secoes
    do mesmo arquivo viram uma entrada. Sem LLM: o validador ja garantiu chave exata. Confere o arquivo no
    conjunto do manual carregado porque o auxiliar pode ter ficado para tras do manual.
    """
    regras: list[str] = []
    sem_chave: list[str] = []
    for linha in linhas:
        linha = linha.strip()
        if not linha:
            continue
        if linha.startswith(prefixo_sem_chave):
            texto = linha[len(prefixo_sem_chave):].strip()
            if texto not in sem_chave:
                sem_chave.append(texto)
            continue
        arquivo = linha.partition("#")[0].strip()
        if arquivo not in caminhos_manual:
            raise ErroEntrada(f"regra {linha!r}: arquivo {arquivo!r} nao existe no manual carregado do BigQuery.")
        if arquivo not in regras:
            regras.append(arquivo)
    return {campo_regras: regras, campo_sem_chave: sem_chave}


def substituir_secao_regras(texto: str, secoes: tuple[str, str], caminhos_manual: frozenset[str],
                            prefixo_sem_chave: str, campo_regras: str, campo_sem_chave: str) -> str:
    """Troca o corpo de `## regras_extraidas` (linhas) pelo JSON. Idempotente: se ja e JSON, devolve igual."""
    cab = secoes[1]
    linhas = texto.rstrip("\n").split("\n")
    indices = [i for i, linha in enumerate(linhas) if linha.rstrip() == cab]
    if len(indices) != 1:
        raise ErroEntrada(f"cabecalho {cab!r} aparece {len(indices)} vez(es); esperado exatamente 1.")
    corpo = linhas[indices[0] + 1:]
    if "".join(corpo).strip().startswith("{"):
        return texto
    obj = converter_regras(corpo, caminhos_manual, prefixo_sem_chave, campo_regras, campo_sem_chave)
    return "\n".join(linhas[:indices[0] + 1]) + "\n" + json.dumps(obj, ensure_ascii=False, indent=2) + "\n"


def custo(tok_in: float, tok_out: float, preco_entrada: float, preco_saida: float) -> float:
    """Custo em dolares; precos por milhao de tokens."""
    return (tok_in * preco_entrada + tok_out * preco_saida) / 1_000_000


def projetar_custo(ctx: Contexto, caracteres_entrada: int) -> float:
    """Projecao pessimista da chamada: entrada no pior caso e saida no limite maximo."""
    return custo(caracteres_entrada / ctx.caracteres_por_token, ctx.max_tokens_saida,
                 ctx.preco_entrada, ctx.preco_saida)


def _chamar_modelo(ctx: Contexto, usuario: str) -> tuple[str, int, int, bool]:
    """Devolve (texto, tokens_entrada, tokens_saida, cortada)."""
    r = ctx.cliente.chat.completions.create(
        model=ctx.modelo,
        messages=[{"role": "system", "content": ctx.prompt}, {"role": "user", "content": usuario}],
        # os modelos da geracao 6 so aceitam temperatura 1 (padrao): nao enviar o parametro
        max_completion_tokens=ctx.max_tokens_saida,
    )
    cortada = r.choices[0].finish_reason == "length"
    return r.choices[0].message.content or "", r.usage.prompt_tokens, r.usage.completion_tokens, cortada


def _validar_argumentos(texto: str, origem: str, tipo_entrada: str, id_sessao_turno: str | None,
                        id_explicacao: str | None, ctx: Contexto) -> None:
    """Falha alto antes de qualquer chamada paga."""
    if tipo_entrada not in ctx.tipos_entrada:
        raise ErroConfig(f"tipo_entrada recebido: {tipo_entrada!r}. Aceitos: {list(ctx.tipos_entrada)}. "
                         f"Configure em {ARQ_CONFIG}.")
    if origem not in ctx.origens:
        raise ErroConfig(f"origem recebido: {origem!r}. Aceitos: {list(ctx.origens)}. Configure em {ARQ_CONFIG}.")
    if origem == "sintetico" and (id_sessao_turno is not None or not id_explicacao):
        raise ErroEntrada("origem sintetico exige id_explicacao e id_sessao_turno vazio (None).")
    if origem == "usuario" and (id_explicacao is not None or not id_sessao_turno):
        raise ErroEntrada("origem usuario exige id_sessao_turno e id_explicacao vazio (None).")
    if not texto or not texto.strip():
        raise ErroEntrada("texto da entrada vazio.")


def normalizar_turno(texto: str, origem: str, tipo_entrada: str, id_sessao_turno: str | None, ctx: Contexto,
                     *, id_explicacao: str | None = None) -> Resultado:
    """Normaliza um turno. Nao grava nada: devolve o resultado para quem chamou decidir.

    `id_explicacao` e so para origem sintetico (corpus); para usuario fica None, como no formato dos metadados.
    """
    _validar_argumentos(texto, origem, tipo_entrada, id_sessao_turno, id_explicacao, ctx)
    usuario = montar_mensagem_usuario(ctx.auxiliar, tipo_entrada, texto)
    projecao = projetar_custo(ctx, len(ctx.prompt) + len(usuario))
    if projecao > ctx.teto_gasto_usd:
        raise ErroTeto(f"projecao de custo {projecao:.4f} USD acima do teto por turno {ctx.teto_gasto_usd} USD. "
                       f"Configure TETO_GASTO_USD ou MAX_TOKENS_SAIDA em {ARQ_CONFIG}.")
    momento = datetime.now().astimezone().isoformat(timespec="seconds")  # momento da chamada ao modelo
    inicio = time.monotonic()
    resposta, tok_in, tok_out, cortada = _chamar_modelo(ctx, usuario)
    tempo = time.monotonic() - inicio
    gasto = custo(tok_in, tok_out, ctx.preco_entrada, ctx.preco_saida)
    valores = {
        "origem": origem, "tipo_entrada": tipo_entrada, "id_sessao_turno": id_sessao_turno,
        "id_explicacao": id_explicacao, "id_prompt": ctx.id_prompt, "hash_prompt": ctx.hash_prompt,
        "id_auxiliar_manual": ctx.id_auxiliar, "hash_auxiliar_manual": ctx.hash_auxiliar,
        "versao_normalizador": ctx.versao_normalizador, "hash_normalizador": ctx.hash_normalizador,
        "modelo": ctx.modelo, "temperatura": ctx.rotulo_temperatura, "tokens_entrada": tok_in,
        "tokens_saida": tok_out, "custo_usd": f"{gasto:.6f}", "tempo_segundos": f"{tempo:.2f}", "timestamp": momento,
    }
    metadados = {campo: valores[campo] for campo in ctx.campos_metadados}
    resultado = Resultado(ok=False, texto_normalizado=None, regras_extraidas=None, metadados=metadados,
                          erros=[], resposta_crua=resposta)
    if cortada:
        resultado.erros.append(f"resposta cortada no limite de {ctx.max_tokens_saida} tokens de saida")
        return resultado
    resultado.erros = validar_resposta(resposta, list(ctx.chaves), ctx.id_auxiliar, ctx.secoes, ctx.prefixo_sem_chave)
    if resultado.erros:
        return resultado
    try:
        corpo = substituir_secao_regras(resposta.strip(), ctx.secoes, ctx.caminhos_manual, ctx.prefixo_sem_chave,
                                        ctx.campo_regras, ctx.campo_sem_chave)
    except ErroEntrada as e:
        resultado.erros.append(str(e))
        return resultado
    cab_texto, cab_regras = ctx.secoes
    parte_texto, _, parte_regras = corpo.partition(cab_regras)
    resultado.texto_normalizado = parte_texto.partition(cab_texto)[2].strip()
    resultado.regras_extraidas = json.loads(parte_regras)
    resultado.ok = True
    return resultado
