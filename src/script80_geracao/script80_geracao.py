"""No de geracao: escreve o .gobr a partir da descricao normalizada, dos exemplos e do recorte do manual.

O no nao confere, nao corrige e nao escreve em disco nem no BigQuery. A saida e um objeto devolvido pela funcao;
conferir e corrigir e o no 90, persistir e outro no. Aqui o texto devolvido pelo modelo segue intacto.
O prompt vem do BigQuery e e carregado uma vez, em `construir_contexto`.
Nenhuma funcao deste modulo le configuracao global: o config entra so em `construir_contexto`, como parametro.

Reexecucao: com `gobr_anterior` e `pedido`, o prompt do banco recebe o adendo de reexecucao (linha ativa da tabela de prompts,
tipo TIPO_ADENDO_NO80) e a mensagem passa a levar o .gobr anterior e o pedido.

Uso:
    ctx = construir_contexto(config)
    resultado = gerar_gobr(descricao, rec.exemplos, rec.secoes_manual, rec.apoio, ctx)
    resultado = gerar_gobr(descricao, ..., ctx, gobr_anterior=anterior, pedido="troque X por Y")
"""
import hashlib
import os
import time
from dataclasses import dataclass, field
from datetime import datetime
from types import ModuleType

ARQ_CONFIG = "config.py"


class ErroConfig(ValueError):
    """Configuracao ou argumento invalido; diz o valor recebido, os aceitos e onde configurar."""


class ErroContexto(RuntimeError):
    """Dado do BigQuery fora do numero de linhas esperado; o no para sem escolher por conta propria."""


class ErroTeto(RuntimeError):
    """Projecao de custo acima do teto da execucao; a chamada nao acontece."""


@dataclass(frozen=True)
class Contexto:
    """Lido uma vez na partida. Imutavel, salvo o acumulador de gasto, que e da execucao."""
    cliente: object
    prompt: str
    adendo_reexecucao: str
    id_adendo: str
    id_prompt: str
    hash_prompt: str
    modelo: str
    preco_entrada: float
    preco_saida: float
    max_tokens_saida: int
    caracteres_por_token: float
    teto_gasto_usd: float
    gasto: list = field(default_factory=lambda: [0.0])  # acumulado da execucao (um elemento mutavel)


@dataclass
class Resultado:
    """Saida de um turno. `resposta_crua` vai sempre, inclusive quando a chamada falha ou e cortada."""
    ok: bool
    texto_gobr: str | None   # a resposta do modelo, sem nenhum tratamento; None se cortada ou se a API falhou
    metadados: dict
    erros: list
    resposta_crua: str


def _sha256(texto: str) -> str:
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()


def _ler_prompt_ativo(bq, tabela: str, tipo: str) -> dict:
    """Linha ativa do `tipo` na tabela de prompts; exige exatamente uma e hash que regere do texto."""
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

    variavel = cfg.VARIAVEL_CHAVE
    chave = os.environ.get(variavel, "").strip()
    if not chave:
        raise ErroConfig(f"Variavel de ambiente {variavel} ausente ou vazia. Defina-a no ambiente "
                         f"(nome configurado em {ARQ_CONFIG}).")
    if cfg.MODELO_NO80 not in cfg.MODELOS_NO80:
        raise ErroConfig(f"MODELO_NO80 recebido: {cfg.MODELO_NO80!r}. Aceitos: {list(cfg.MODELOS_NO80)}. "
                         f"Configure em {ARQ_CONFIG}.")
    tabela = f"{cfg.PROJETO_GCP}.{cfg.DATASET}.{cfg.TABELA_PROMPTS}"
    bq = bigquery.Client(project=cfg.PROJETO_GCP)
    linha = _ler_prompt_ativo(bq, tabela, cfg.TIPO_PROMPT_NO80)
    adendo = _ler_prompt_ativo(bq, tabela, cfg.TIPO_ADENDO_NO80)
    info = cfg.MODELOS[cfg.MODELO_NO80]
    return Contexto(
        cliente=OpenAI(api_key=chave), prompt=linha["texto"], id_prompt=linha["arquivo"], hash_prompt=linha["hash"],
        adendo_reexecucao=adendo["texto"], id_adendo=adendo["arquivo"],
        modelo=cfg.MODELO_NO80, preco_entrada=info["entrada_por_milhao"], preco_saida=info["saida_por_milhao"],
        max_tokens_saida=cfg.MAX_TOKENS_SAIDA, caracteres_por_token=cfg.CARACTERES_POR_TOKEN_PESSIMISTA,
        teto_gasto_usd=float(cfg.TETO_GASTO_NO80_USD),
    )


def montar_mensagem_usuario(descricao: str, exemplos: list, secoes_manual: dict, apoio: dict,
                            gobr_anterior: str | None = None, pedido: str | None = None) -> str:
    """Corpo da mensagem do usuario, na ordem do prompt: descricao, exemplos, manual e apoio. O prompt vai no sistema.

    Na reexecucao o .gobr anterior e o pedido vao no fim, depois de tudo que o prompt de primeira geracao descreve.
    """
    partes = [f"=== DESCRICAO NORMALIZADA ===\n{descricao.strip()}\n"]
    for i, ex in enumerate(exemplos, 1):
        partes.append(f"=== EXEMPLO {i} (descricao) ===\n{ex['explicacao_normalizada'].strip()}\n\n"
                      f"=== EXEMPLO {i} (.gobr) ===\n{ex['gobr'].strip()}\n")
    for caminho, texto in secoes_manual.items():
        partes.append(f"=== MANUAL: {caminho} ===\n{texto.strip()}\n")
    for caminho, texto in apoio.items():
        partes.append(f"=== APOIO: {caminho} ===\n{texto.strip()}\n")
    if gobr_anterior is not None:
        partes.append(f"=== GOBR ANTERIOR ===\n{gobr_anterior.strip()}\n")
        partes.append(f"=== PEDIDO DE MUDANCA ===\n{pedido.strip()}\n")
    return "\n".join(partes)


def custo(tok_in: float, tok_out: float, preco_entrada: float, preco_saida: float) -> float:
    """Custo em dolares; precos por milhao de tokens."""
    return (tok_in * preco_entrada + tok_out * preco_saida) / 1_000_000


def gerar_gobr(descricao: str, exemplos: list, secoes_manual: dict, apoio: dict, ctx: Contexto, *,
               gobr_anterior: str | None = None, pedido: str | None = None) -> Resultado:
    """Um turno: uma chamada ao modelo. Nao grava nada: devolve o resultado para quem chamou decidir.

    `gobr_anterior` e `pedido` vao juntos: com os dois e reexecucao, sem nenhum e primeira geracao.
    """
    if not descricao or not descricao.strip():
        raise ErroConfig("descricao vazia.")
    reexecucao = gobr_anterior is not None or pedido is not None
    if reexecucao and not (gobr_anterior and gobr_anterior.strip() and pedido and pedido.strip()):
        raise ErroConfig(f"reexecucao exige gobr_anterior e pedido nao vazios; recebido gobr_anterior="
                         f"{gobr_anterior!r}, pedido={pedido!r}.")
    # O adendo completa o prompt do banco em vez de repeti-lo: as regras de forma continuam numa fonte so.
    sistema = f"{ctx.prompt}\n\n---\n\n{ctx.adendo_reexecucao}" if reexecucao else ctx.prompt
    id_prompt = f"{ctx.id_prompt}+{ctx.id_adendo}" if reexecucao else ctx.id_prompt
    hash_prompt = _sha256(sistema) if reexecucao else ctx.hash_prompt
    usuario = montar_mensagem_usuario(descricao, exemplos, secoes_manual, apoio, gobr_anterior, pedido)
    # Projecao pessimista antes da chamada paga (entrada no pior caso, saida no limite), somada ao acumulado.
    projecao = custo((len(sistema) + len(usuario)) / ctx.caracteres_por_token, ctx.max_tokens_saida,
                     ctx.preco_entrada, ctx.preco_saida)
    if ctx.gasto[0] + projecao > ctx.teto_gasto_usd:
        raise ErroTeto(f"projecao {ctx.gasto[0] + projecao:.4f} USD (acumulado {ctx.gasto[0]:.4f} + chamada "
                       f"{projecao:.4f}) acima do teto {ctx.teto_gasto_usd} USD. Configure TETO_GASTO_NO80_USD "
                       f"ou MAX_TOKENS_SAIDA em {ARQ_CONFIG}.")
    momento = datetime.now().astimezone().isoformat(timespec="seconds")
    inicio = time.monotonic()
    erros: list = []
    resposta, tok_in, tok_out = "", 0, 0
    try:
        r = ctx.cliente.chat.completions.create(
            model=ctx.modelo,
            messages=[{"role": "system", "content": sistema}, {"role": "user", "content": usuario}],
            # os modelos da geracao 6 so aceitam temperatura 1 (padrao): nao enviar o parametro
            max_completion_tokens=ctx.max_tokens_saida,
        )
        resposta = r.choices[0].message.content or ""
        tok_in, tok_out = r.usage.prompt_tokens, r.usage.completion_tokens
        if r.choices[0].finish_reason == "length":
            erros.append(f"resposta cortada no limite de {ctx.max_tokens_saida} tokens de saida")
    except Exception as e:  # a falha da API vira erro do resultado; nada pago e perdido em silencio
        erros.append(f"falha na chamada: {type(e).__name__}: {str(e)[:300]}")
    tempo = time.monotonic() - inicio
    gasto = custo(tok_in, tok_out, ctx.preco_entrada, ctx.preco_saida)
    ctx.gasto[0] += gasto
    metadados = {"modelo": ctx.modelo, "tokens_entrada": tok_in, "tokens_saida": tok_out,
                 "custo_usd": f"{gasto:.6f}", "tempo_segundos": f"{tempo:.2f}", "id_prompt": id_prompt,
                 "hash_prompt": hash_prompt, "timestamp": momento}
    return Resultado(ok=not erros, texto_gobr=resposta if not erros else None, metadados=metadados, erros=erros,
                     resposta_crua=resposta)
