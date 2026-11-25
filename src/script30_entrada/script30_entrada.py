"""No de entrada: converte a entrada da pessoa em texto e decide se ela traz o minimo para seguir.

O no nao escreve em disco nem no BigQuery; devolve um objeto. Nao limpa o texto, nao escreve regra e nao fala com a
pessoa: quem pergunta o que falta e o agente.py, a partir dos tokens de `faltantes`.
Prompt vem da tabela `prompts` (tipo configurado em config.py), lido uma vez em `construir_contexto`.
Nenhuma funcao deste modulo le configuracao global: o config entra so em `construir_contexto`, como parametro.

Uso:
    ctx = construir_contexto(config)
    r = classificar_entrada("texto", "primeiro", "Atender a cada 15 dias.", ctx)
"""
import base64
import hashlib
import os
from dataclasses import dataclass
from pathlib import Path
from types import ModuleType

ARQ_CONFIG = "config.py"
# Conjuntos fechados do contrato com o prompt (parte do esquema do prompt, nao configuracao).
TIPOS = ("texto", "audio", "imagem", "documento", "misto")
TURNOS = ("primeiro", "mudanca")
STATUS = ("aprovado", "incompleto", "fora_de_escopo")
FALTANTES = ("quem_atende", "desfecho", "conflito")
CABECALHOS = ("## tipo", "## texto", "## status", "## faltantes")


class ErroConfig(ValueError):
    """Configuracao ou argumento invalido; diz o valor recebido, os aceitos e onde configurar."""


class ErroEntrada(ValueError):
    """Entrada ou resposta do modelo fora do formato esperado."""


class ErroContexto(RuntimeError):
    """Dado do BigQuery fora do esquema ou do numero de linhas esperado."""


class ErroTeto(RuntimeError):
    """Projecao de custo da chamada acima do teto."""


@dataclass(frozen=True)
class Contexto:
    cliente: object
    prompt: str
    id_prompt: str
    hash_prompt: str
    modelo: str
    preco_entrada: float
    preco_saida: float
    max_tokens_saida: int
    caracteres_por_token: float
    teto_gasto_usd: float
    tipos_implementados: tuple
    extensoes: dict
    limites_bytes: dict
    tokens_projecao_midia: dict


@dataclass
class Entrada:
    """Saida do no: os quatro campos do prompt e o custo da chamada."""
    tipo: str
    texto: str
    status: str
    faltantes: list[str]
    custo_usd: float


def _sha256(texto: str) -> str:
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()


def _ler_prompt_ativo(bq, tabela: str, tipo: str) -> dict:
    """Linha ativa do `tipo`; exige exatamente uma e hash que regere do texto."""
    from google.cloud import bigquery

    consulta = f"SELECT arquivo, texto, `hash` FROM `{tabela}` WHERE tipo = @tipo AND ativo"
    job = bigquery.QueryJobConfig(query_parameters=[bigquery.ScalarQueryParameter("tipo", "STRING", tipo)])
    linhas = [dict(r) for r in bq.query(consulta, job_config=job).result()]
    if len(linhas) != 1:
        raise ErroContexto(f"{tabela}: {len(linhas)} linhas ativas para tipo={tipo!r}; esperada exatamente 1. "
                           f"Tipo configurado em {ARQ_CONFIG}.")
    linha = linhas[0]
    # O hash gravado precisa regerar do texto: senao o metadado hash_prompt mentiria sobre o que foi enviado.
    if _sha256(linha["texto"]) != linha["hash"]:
        raise ErroContexto(f"{tabela}: arquivo={linha['arquivo']!r}: hash gravado nao confere com o texto.")
    return linha


def construir_contexto(cfg: ModuleType) -> Contexto:
    """Le o prompt no BigQuery e cria o cliente da OpenAI, uma vez. Falha alto, antes de qualquer chamada paga."""
    from google.cloud import bigquery
    from openai import OpenAI

    chave = os.environ.get(cfg.VARIAVEL_CHAVE, "").strip()
    if not chave:
        raise ErroConfig(f"Variavel de ambiente {cfg.VARIAVEL_CHAVE} ausente ou vazia. Defina-a no ambiente "
                         f"(nome configurado em {ARQ_CONFIG}).")
    if cfg.MODELO_NO30 not in cfg.MODELOS:
        raise ErroConfig(f"MODELO_NO30 recebido: {cfg.MODELO_NO30!r}. Aceitos: {list(cfg.MODELOS)}. "
                         f"Configure em {ARQ_CONFIG}.")
    bq = bigquery.Client(project=cfg.PROJETO_GCP)
    linha = _ler_prompt_ativo(bq, f"{cfg.PROJETO_GCP}.{cfg.DATASET}.{cfg.TABELA_PROMPTS}", cfg.TIPO_PROMPT_NO30)
    info = cfg.MODELOS[cfg.MODELO_NO30]
    return Contexto(
        cliente=OpenAI(api_key=chave), prompt=linha["texto"], id_prompt=linha["arquivo"], hash_prompt=linha["hash"],
        modelo=cfg.MODELO_NO30, preco_entrada=info["entrada_por_milhao"], preco_saida=info["saida_por_milhao"],
        max_tokens_saida=cfg.MAX_TOKENS_SAIDA, caracteres_por_token=cfg.CARACTERES_POR_TOKEN_PESSIMISTA,
        teto_gasto_usd=float(cfg.TETO_GASTO_USD), tipos_implementados=tuple(cfg.TIPOS_ENTRADA_IMPLEMENTADOS),
        extensoes=dict(cfg.EXTENSOES_ENTRADA), limites_bytes=dict(cfg.LIMITE_BYTES_ENTRADA),
        tokens_projecao_midia=dict(cfg.TOKENS_PROJECAO_MIDIA),
    )


def montar_mensagem_usuario(tipo_entrada: str, turno: str, conteudo: str) -> str:
    return (f"=== TIPO DE ENTRADA ===\n{tipo_entrada}\n\n=== TURNO ===\n{turno}\n\n"
            f"=== ENTRADA ===\n{conteudo.strip()}\n")


def montar_parte_midia(tipo_entrada: str, caminho: str, ctx: Contexto) -> dict:
    """Le o arquivo e devolve o bloco de conteudo da API. Confere existencia, extensao e tamanho antes de ler."""
    arq = Path(caminho.strip())
    if not arq.is_file():
        raise ErroEntrada(f"arquivo de {tipo_entrada} inexistente: {str(arq)!r}.")
    tipo_ext, mime = ctx.extensoes.get(arq.suffix.lower(), (None, None))
    if tipo_ext != tipo_entrada:
        raise ErroEntrada(f"extensao {arq.suffix!r} recebida para tipo {tipo_entrada!r}. Aceitas para o tipo: "
                          f"{[e for e, (t, _) in ctx.extensoes.items() if t == tipo_entrada]}. Configure em {ARQ_CONFIG}.")
    tamanho, limite = arq.stat().st_size, ctx.limites_bytes[tipo_entrada]
    if tamanho > limite:
        raise ErroEntrada(f"arquivo de {tipo_entrada} com {tamanho} bytes; limite {limite} bytes. "
                          f"Limite configurado em {ARQ_CONFIG} (LIMITE_BYTES_ENTRADA).")
    dados = base64.b64encode(arq.read_bytes()).decode("ascii")
    if tipo_entrada == "imagem":
        return {"type": "image_url", "image_url": {"url": f"data:{mime};base64,{dados}"}}
    return {"type": "file", "file": {"filename": arq.name, "file_data": f"data:{mime};base64,{dados}"}}


def custo(tok_in: float, tok_out: float, preco_entrada: float, preco_saida: float) -> float:
    return (tok_in * preco_entrada + tok_out * preco_saida) / 1_000_000


def interpretar_resposta(resposta: str, tipo_entrada: str) -> tuple[str, str, str, list[str]]:
    """Extrai (tipo, texto, status, faltantes) das quatro secoes. Qualquer desvio levanta ErroEntrada."""
    linhas = resposta.strip().splitlines()
    indices = []
    for cab in CABECALHOS:
        achados = [i for i, linha in enumerate(linhas) if linha.rstrip() == cab]
        if len(achados) != 1:
            raise ErroEntrada(f"cabecalho {cab!r} aparece {len(achados)} vez(es); esperado exatamente 1. "
                              f"Resposta: {resposta[:300]!r}")
        indices.append(achados[0])
    if indices != sorted(indices) or indices[0] != 0:
        raise ErroEntrada(f"cabecalhos fora de ordem ou com conteudo antes de {CABECALHOS[0]!r}: {indices}.")
    limites = indices + [len(linhas)]
    corpo = [linhas[limites[k] + 1:limites[k + 1]] for k in range(4)]
    tipo = " ".join(corpo[0]).strip()
    texto = "\n".join(corpo[1]).strip()
    status = " ".join(corpo[2]).strip()
    faltantes = [linha.strip() for linha in corpo[3] if linha.strip()]
    if tipo != tipo_entrada:
        raise ErroEntrada(f"tipo devolvido: {tipo!r}; o prompt manda repetir {tipo_entrada!r}.")
    if status not in STATUS:
        raise ErroEntrada(f"status recebido: {status!r}. Aceitos: {list(STATUS)}.")
    fora = [f for f in faltantes if f not in FALTANTES]
    if fora:
        raise ErroEntrada(f"faltantes recebido: {fora!r}. Aceitos: {list(FALTANTES)}.")
    if not texto:
        raise ErroEntrada("secao '## texto' vazia.")
    return tipo, texto, status, faltantes


def classificar_entrada(tipo_entrada: str, turno: str, conteudo: str, ctx: Contexto) -> Entrada:
    """Converte a entrada em texto e classifica os minimos.

    Para `texto`, `conteudo` e o que a pessoa disse. Para `imagem` e `documento`, e o caminho do arquivo: o tipo vem
    do chamador (o no nao adivinha) e a conversao em texto e do modelo.
    """
    if tipo_entrada not in TIPOS:
        raise ErroConfig(f"tipo_entrada recebido: {tipo_entrada!r}. Aceitos: {list(TIPOS)}.")
    if tipo_entrada not in ctx.tipos_implementados:
        raise ErroConfig(f"tipo_entrada recebido: {tipo_entrada!r}. Implementados: {list(ctx.tipos_implementados)}. "
                         f"O tipo nao foi provado possivel com o modelo {ctx.modelo!r}; implementa-lo depende de "
                         f"decisao do Mestre (lista em {ARQ_CONFIG}, TIPOS_ENTRADA_IMPLEMENTADOS).")
    if turno not in TURNOS:
        raise ErroConfig(f"turno recebido: {turno!r}. Aceitos: {list(TURNOS)}.")
    if not conteudo or not conteudo.strip():
        raise ErroEntrada("conteudo da entrada vazio.")
    midia = tipo_entrada != "texto"
    # Em midia, o texto da mensagem so avisa que o anexo e a entrada; o conteudo real vai no bloco anexado.
    usuario = montar_mensagem_usuario(tipo_entrada, turno, "(midia anexada a esta mensagem)" if midia else conteudo)
    mensagem = usuario
    if midia:
        mensagem = [{"type": "text", "text": usuario}, montar_parte_midia(tipo_entrada, conteudo, ctx)]
    # Projecao pessimista antes da chamada paga: entrada no pior caso, saida no limite maximo.
    tokens_midia = ctx.tokens_projecao_midia[tipo_entrada] if midia else 0
    projecao = custo((len(ctx.prompt) + len(usuario)) / ctx.caracteres_por_token + tokens_midia,
                     ctx.max_tokens_saida, ctx.preco_entrada, ctx.preco_saida)
    if projecao > ctx.teto_gasto_usd:
        raise ErroTeto(f"projecao de custo {projecao:.4f} USD acima do teto {ctx.teto_gasto_usd} USD. "
                       f"Configure TETO_GASTO_USD ou MAX_TOKENS_SAIDA em {ARQ_CONFIG}.")
    r = ctx.cliente.chat.completions.create(
        model=ctx.modelo,
        messages=[{"role": "system", "content": ctx.prompt}, {"role": "user", "content": mensagem}],
        max_completion_tokens=ctx.max_tokens_saida,
    )
    resposta = r.choices[0].message.content or ""
    gasto = custo(r.usage.prompt_tokens, r.usage.completion_tokens, ctx.preco_entrada, ctx.preco_saida)
    if r.choices[0].finish_reason == "length":
        raise ErroEntrada(f"resposta cortada no limite de {ctx.max_tokens_saida} tokens de saida.")
    tipo, texto, status, faltantes = interpretar_resposta(resposta, tipo_entrada)
    return Entrada(tipo=tipo, texto=texto, status=status, faltantes=faltantes, custo_usd=gasto)
