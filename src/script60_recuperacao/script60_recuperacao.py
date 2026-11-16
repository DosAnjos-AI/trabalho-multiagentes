"""No de recuperacao: dada uma consulta normalizada, devolve os exemplos .gobr mais proximos e o recorte do manual.

So le o BigQuery; nao grava nada nem em disco nem na nuvem. A saida e um objeto devolvido pela funcao.
Na partida (`construir_contexto`) carrega uma vez: o manual inteiro (para nao consultar o banco a cada turno), os
tres arquivos de apoio separados, os exemplos filtrados com seus vetores e a credencial do embedding.
O manual inteiro fica em memoria, mas NUNCA e devolvido: sai so o recorte (ver `recuperar`).
Nenhuma funcao deste modulo le configuracao global: o config entra so em `construir_contexto`, como parametro.

Uso:
    ctx = construir_contexto(config)
    rec = recuperar(texto_normalizado, regras_extraidas_da_consulta, ctx)
"""
import time
from dataclasses import dataclass, field
from types import ModuleType

import numpy as np

ARQ_CONFIG = "config.py"
# Valores da coluna `tipo` da tabela manual (parte do esquema, nao configuracao).
TIPO_SECAO = "secao"
TIPOS_APOIO = ("conceitos", "invariantes", "mapa")
# Repeticao curta em 429 e 5xx do embedding; detalhe de rede, nao parametro de negocio.
TENTATIVAS_API = 5


class ErroConfig(ValueError):
    """Argumento invalido; diz o valor recebido, os aceitos e onde configurar."""


class ErroContexto(RuntimeError):
    """Dado do BigQuery fora do esquema esperado; o no para sem escolher por conta propria."""


class ErroManual(ValueError):
    """Caminho citado em regras_extraidas que nao existe como secao no manual carregado."""


class ErroTeto(RuntimeError):
    """Projecao de custo do embedding acima do teto da execucao."""


@dataclass(frozen=True)
class Contexto:
    """Lido uma vez na partida. Imutavel, salvo o acumulador de gasto, que e da execucao."""
    credenciais: object
    secoes: dict          # caminho -> texto, so tipo 'secao'
    apoio: dict           # caminho -> texto, os tres arquivos de apoio
    ids: tuple            # exemplo_id, na ordem das linhas de `matriz`
    exemplos: dict        # exemplo_id -> {explicacao_normalizada, regras_extraidas, sem_chave, gobr}
    matriz: object        # numpy (n, dimensoes), cada linha ja dividida pela norma
    n1_denso: int
    n2_jaccard: int
    modelo_embedding: str
    dimensoes: int
    endpoint: str
    projeto: str
    prefixo: str
    usd_por_milhao: float
    caracteres_por_token: float
    teto_gasto_usd: float
    gasto: list = field(default_factory=lambda: [0.0])  # acumulado da execucao (um elemento mutavel)


@dataclass
class Recuperacao:
    """Saida de um turno. `registro` diz por que cada exemplo entrou; sem ele nao ha como depurar."""
    exemplos: list          # dicts: exemplo_id, explicacao_normalizada, regras_extraidas, sem_chave, gobr
    secoes_manual: dict     # caminho -> texto: so o recorte (consulta + exemplos), sem duplicata
    apoio: dict             # os tres arquivos de apoio, sempre
    registro: list          # por exemplo: ramos, cosseno, jaccard, posicao em cada ramo
    caminhos_recorte: list  # ordem estavel de insercao
    empate_jaccard: dict    # candidatos com o mesmo Jaccard do ultimo escolhido no ramo Jaccard
    tokens_embedding: int
    custo_usd: float


def jaccard(a: set, b: set) -> float:
    """Sobreposicao entre dois conjuntos de caminhos. Dois conjuntos vazios valem 0 (nao ha o que comparar)."""
    uniao = a | b
    return len(a & b) / len(uniao) if uniao else 0.0


def construir_contexto(cfg: ModuleType) -> Contexto:
    """Le o BigQuery e prepara a credencial, uma vez. Falha alto, antes de qualquer chamada paga."""
    import google.auth
    from google.cloud import bigquery

    bq = bigquery.Client(project=cfg.PROJETO_GCP)
    base = f"{cfg.PROJETO_GCP}.{cfg.DATASET}"
    linhas = [dict(r) for r in bq.query(f"SELECT caminho, tipo, texto FROM `{base}.{cfg.TABELA_MANUAL}`").result()]
    secoes = {r["caminho"]: r["texto"] for r in linhas if r["tipo"] == TIPO_SECAO}
    apoio = {r["caminho"]: r["texto"] for r in linhas if r["tipo"] in TIPOS_APOIO}
    faltam = [t for t in TIPOS_APOIO if t not in {r["tipo"] for r in linhas}]
    if faltam or len(apoio) != len(TIPOS_APOIO):
        raise ErroContexto(f"{base}.{cfg.TABELA_MANUAL}: arquivos de apoio de tipo {faltam or 'duplicado'} "
                           f"ausentes ou fora de um por tipo (esperados: {list(TIPOS_APOIO)}). "
                           f"Tabela configurada em {ARQ_CONFIG} (TABELA_MANUAL).")
    if not secoes:
        raise ErroContexto(f"{base}.{cfg.TABELA_MANUAL}: nenhuma linha com tipo={TIPO_SECAO!r}.")

    # Filtro como parametro de consulta: a lista de aceitos vem do config, nao do SQL.
    consulta = (f"SELECT exemplo_id, explicacao_normalizada, regras_extraidas, sem_chave, gobr, embedding "
                f"FROM `{base}.{cfg.TABELA_EXEMPLOS}` WHERE status_revisao = @status "
                f"ORDER BY exemplo_id")
    params = [bigquery.ScalarQueryParameter("status", "STRING", cfg.STATUS_BUSCA)]
    config_job = bigquery.QueryJobConfig(query_parameters=params)
    ex = [dict(r) for r in bq.query(consulta, job_config=config_job).result()]
    if not ex:
        raise ErroContexto(f"{base}.{cfg.TABELA_EXEMPLOS}: nenhuma linha com "
                           f"status_revisao={cfg.STATUS_BUSCA!r}. Filtro configurado em {ARQ_CONFIG}.")
    ruins = [r["exemplo_id"] for r in ex if len(r["embedding"]) != cfg.DIMENSOES]
    if ruins:
        raise ErroContexto(f"{len(ruins)} exemplos com embedding de tamanho diferente de {cfg.DIMENSOES} "
                           f"(DIMENSOES em {ARQ_CONFIG}); primeiro: {ruins[0]!r}.")
    matriz = np.array([r["embedding"] for r in ex], dtype=np.float64)
    # Normaliza aqui para o cosseno virar produto interno; nao se presume que o banco ja normalizou.
    matriz = matriz / np.linalg.norm(matriz, axis=1, keepdims=True)
    exemplos = {r["exemplo_id"]: {"exemplo_id": r["exemplo_id"], "explicacao_normalizada": r["explicacao_normalizada"],
                                  "regras_extraidas": list(r["regras_extraidas"]), "sem_chave": list(r["sem_chave"]),
                                  "gobr": r["gobr"]} for r in ex}
    credenciais, _ = google.auth.default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
    endpoint = (f"https://aiplatform.googleapis.com/v1/projects/{cfg.PROJETO_GCP}/locations/"
                f"{cfg.LOCALIZACAO_EMBEDDING}/publishers/google/models/{cfg.MODELO_EMBEDDING}:embedContent")
    info = cfg.MODELOS_EMBEDDING[cfg.MODELO_EMBEDDING]
    return Contexto(
        credenciais=credenciais, secoes=secoes, apoio=apoio, ids=tuple(r["exemplo_id"] for r in ex),
        exemplos=exemplos, matriz=matriz, n1_denso=cfg.N1_DENSO, n2_jaccard=cfg.N2_JACCARD,
        modelo_embedding=cfg.MODELO_EMBEDDING, dimensoes=cfg.DIMENSOES, endpoint=endpoint, projeto=cfg.PROJETO_GCP,
        prefixo=cfg.PREFIXO_EMBEDDING, usd_por_milhao=info["usd_por_milhao"],
        caracteres_por_token=cfg.CARACTERES_POR_TOKEN_PESSIMISTA, teto_gasto_usd=float(cfg.TETO_GASTO_NO60_USD),
    )


def _conferir_caminhos(regras: list, secoes: dict, origem: str) -> None:
    """Falha alto: caminho citado que o manual nao tem como secao. Roda antes da chamada paga."""
    for caminho in regras:
        if caminho not in secoes:
            raise ErroManual(f"{origem}: caminho {caminho!r} nao existe como secao no manual carregado do BigQuery. "
                             f"Confira regras_extraidas da consulta, ou a tabela configurada em "
                             f"{ARQ_CONFIG} (TABELA_MANUAL).")


def embutir_consulta(ctx: Contexto, texto: str) -> tuple[np.ndarray, int, float]:
    """Embedding da consulta com o mesmo prefixo dos documentos. Devolve (vetor normalizado, tokens, custo usd)."""
    import google.auth.transport.requests
    import requests

    enviado = f"{ctx.prefixo}{texto}"
    # Projecao pessimista antes da chamada paga, somada ao acumulado da execucao.
    projecao = len(enviado) / ctx.caracteres_por_token / 1e6 * ctx.usd_por_milhao
    if ctx.gasto[0] + projecao > ctx.teto_gasto_usd:
        raise ErroTeto(f"projecao {ctx.gasto[0] + projecao:.6f} USD acima do teto {ctx.teto_gasto_usd} USD. "
                       f"Configure TETO_GASTO_NO60_USD em {ARQ_CONFIG}.")
    corpo = {"content": {"parts": [{"text": enviado}]}, "outputDimensionality": ctx.dimensoes}
    for tentativa in range(1, TENTATIVAS_API + 1):
        if not ctx.credenciais.valid:
            ctx.credenciais.refresh(google.auth.transport.requests.Request())
        r = requests.post(ctx.endpoint, json=corpo, timeout=60, headers={
            "Authorization": f"Bearer {ctx.credenciais.token}", "x-goog-user-project": ctx.projeto})
        if r.status_code == 200:
            j = r.json()
            vetor = np.array(j["embedding"]["values"], dtype=np.float64)
            if vetor.shape != (ctx.dimensoes,):
                raise ErroContexto(f"embedding da consulta com {vetor.shape[0]} dimensoes; esperadas {ctx.dimensoes}.")
            tokens = int(j["usageMetadata"]["promptTokenCount"])
            gasto = tokens / 1e6 * ctx.usd_por_milhao
            ctx.gasto[0] += gasto
            return vetor / np.linalg.norm(vetor), tokens, gasto
        if r.status_code in (429, 500, 502, 503, 504) and tentativa < TENTATIVAS_API:
            time.sleep(2 ** tentativa)
            continue
        raise RuntimeError(f"embedContent HTTP {r.status_code}: {r.text[:300]}")


def recuperar(texto: str, regras_consulta: list, ctx: Contexto, *, excluir_ids: frozenset = frozenset(),
              vetor_consulta: np.ndarray | None = None) -> Recuperacao:
    """Um turno: dois ramos (denso e Jaccard), uniao sem duplicata e recorte do manual.

    `excluir_ids` tira candidatos (leave-one-out do corpus). `vetor_consulta` permite reaproveitar um embedding ja
    pago (o ensaio roda a mesma consulta com outros n1/n2 sem pagar de novo); None gera o embedding.
    Ordem de entrada: ramo denso primeiro, depois os do Jaccard que ainda nao estavam.
    """
    if not texto or not texto.strip():
        raise ErroConfig("texto da consulta vazio.")
    regras = list(dict.fromkeys(regras_consulta))
    _conferir_caminhos(regras, ctx.secoes, "regras_extraidas da consulta")

    tokens, custo_emb = 0, 0.0
    if vetor_consulta is None:
        vetor_consulta, tokens, custo_emb = embutir_consulta(ctx, texto)
    cosseno = ctx.matriz @ vetor_consulta  # produto interno de vetores normalizados = cosseno
    validos = [i for i, eid in enumerate(ctx.ids) if eid not in excluir_ids]
    cos = {ctx.ids[i]: float(cosseno[i]) for i in validos}
    conj_consulta = set(regras)
    jac = {eid: jaccard(conj_consulta, set(ctx.exemplos[eid]["regras_extraidas"])) for eid in cos}

    # Ramo denso: maior cosseno; o id so desempata a ordem de impressao, nao a escolha (cossenos reais nao empatam).
    ordem_denso = sorted(cos, key=lambda e: (-cos[e], e))
    # Ramo Jaccard: maior sobreposicao; empate resolvido pela similaridade densa; id so como ultimo recurso.
    ordem_jac = sorted(cos, key=lambda e: (-jac[e], -cos[e], e))
    escolhidos_denso = ordem_denso[:ctx.n1_denso]
    escolhidos_jac = ordem_jac[:ctx.n2_jaccard]

    entrada: dict = {}
    for ramo, lista, ordem in (("denso", escolhidos_denso, ordem_denso), ("jaccard", escolhidos_jac, ordem_jac)):
        for eid in lista:
            reg = entrada.setdefault(eid, {"exemplo_id": eid, "ramos": [], "cosseno": cos[eid], "jaccard": jac[eid],
                                           "posicao_denso": ordem_denso.index(eid) + 1,
                                           "posicao_jaccard": ordem_jac.index(eid) + 1})
            reg["ramos"].append(ramo)

    # Empate no Jaccard: todos com a pontuacao do ultimo escolhido. `residual` = mesmo Jaccard e mesmo cosseno
    # na borda do corte; ai o id decidiu, e isso precisa ser declarado por quem usa o resultado.
    corte = jac[escolhidos_jac[-1]]
    empatados = [e for e in ordem_jac if jac[e] == corte]
    residual = False
    if len(ordem_jac) > ctx.n2_jaccard:
        residual = (jac[ordem_jac[ctx.n2_jaccard - 1]] == jac[ordem_jac[ctx.n2_jaccard]]
                    and cos[ordem_jac[ctx.n2_jaccard - 1]] == cos[ordem_jac[ctx.n2_jaccard]])
    empate = {"jaccard_do_corte": corte, "qtd_empatados": len(empatados),
              "empatados": [{"exemplo_id": e, "cosseno": cos[e]} for e in empatados],
              "empate_residual_apos_denso": residual}

    # Recorte: regras da consulta + regras dos exemplos da uniao, sem duplicata. Nunca o manual inteiro.
    caminhos = list(regras)
    for eid in entrada:
        for c in ctx.exemplos[eid]["regras_extraidas"]:
            _conferir_caminhos([c], ctx.secoes, f"regras_extraidas do exemplo {eid}")
            if c not in caminhos:
                caminhos.append(c)
    recorte = {c: ctx.secoes[c] for c in caminhos}

    return Recuperacao(
        exemplos=[ctx.exemplos[e] for e in entrada], secoes_manual=recorte, apoio=dict(ctx.apoio),
        registro=list(entrada.values()), caminhos_recorte=caminhos, empate_jaccard=empate,
        tokens_embedding=tokens, custo_usd=custo_emb,
    )
