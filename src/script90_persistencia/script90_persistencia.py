"""No de persistencia: grava na tabela `exemplos` a regra que a pessoa aprovou, com status pendente de revisao.

Unica operacao de escrita do projeto no BigQuery: um INSERT por parametro de consulta, uma linha por aprovacao.
O no nao confere, nao corrige e nao inventa valor: metadado que a execucao nao produziu fica NULL.
Nenhuma funcao deste modulo le configuracao global: o config entra so em `construir_contexto`, como parametro.

Uso:
    ctx = construir_contexto(config)
    g = gravar_regra("conversa1-turno1", entrada, descricao, regras, sem_chave, gobr, meta_norm, meta_ger, ctx)
"""
import hashlib
import time
from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from types import ModuleType

ARQ_CONFIG = "config.py"
# Repeticao curta em 429 e 5xx do embedding; detalhe de rede, nao parametro de negocio.
TENTATIVAS_API = 5


class ErroConfig(ValueError):
    """Argumento invalido; diz o valor recebido e onde configurar."""


class ErroTeto(RuntimeError):
    """Projecao de custo do embedding acima do teto da execucao."""


class ErroGravacao(RuntimeError):
    """O BigQuery nao confirmou a linha gravada; o no para sem escolher por conta propria."""


@dataclass(frozen=True)
class Contexto:
    """Lido uma vez na partida. Imutavel, salvo o acumulador de gasto, que e da execucao."""
    bq: object
    tabela: str
    credenciais: object
    endpoint: str
    projeto: str
    origem: str
    status: str
    modelo_embedding: str
    dimensoes: int
    prefixo: str
    usd_por_milhao: float
    caracteres_por_token: float
    teto_gasto_usd: float
    gasto: list = field(default_factory=lambda: [0.0])  # acumulado da execucao (um elemento mutavel)


@dataclass
class Gravacao:
    """Saida: o id da linha, se esta chamada gravou (False = a linha ja existia) e o custo do embedding."""
    exemplo_id: str
    gravada: bool
    custo_usd: float
    tokens_embedding: int


def construir_contexto(cfg: ModuleType) -> Contexto:
    """Cria o cliente do BigQuery e a credencial do embedding, uma vez. Falha alto, antes de qualquer chamada paga."""
    import google.auth
    from google.cloud import bigquery

    credenciais, _ = google.auth.default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
    endpoint = cfg.ENDERECO_EMBEDDING.format(projeto=cfg.PROJETO_GCP, localizacao=cfg.LOCALIZACAO_EMBEDDING,
                                             modelo=cfg.MODELO_EMBEDDING)
    return Contexto(
        bq=bigquery.Client(project=cfg.PROJETO_GCP),
        tabela=f"{cfg.PROJETO_GCP}.{cfg.DATASET}.{cfg.TABELA_GRAVACAO}", credenciais=credenciais, endpoint=endpoint,
        projeto=cfg.PROJETO_GCP, origem=cfg.ORIGEM_GRAVACAO, status=cfg.STATUS_GRAVACAO,
        modelo_embedding=cfg.MODELO_EMBEDDING, dimensoes=cfg.DIMENSOES, prefixo=cfg.PREFIXO_EMBEDDING,
        usd_por_milhao=cfg.MODELOS_EMBEDDING[cfg.MODELO_EMBEDDING]["usd_por_milhao"],
        caracteres_por_token=cfg.CARACTERES_POR_TOKEN_PESSIMISTA, teto_gasto_usd=float(cfg.TETO_GASTO_NO90_USD),
    )


def _sha256(texto: str) -> str:
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()


def _embutir(ctx: Contexto, enviado: str) -> tuple[list[float], int, float]:
    """Embedding do texto ja com prefixo, como nas linhas do corpus: vetor cru da API, sem renormalizar."""
    import google.auth.transport.requests
    import requests

    projecao = len(enviado) / ctx.caracteres_por_token / 1e6 * ctx.usd_por_milhao
    if ctx.gasto[0] + projecao > ctx.teto_gasto_usd:
        raise ErroTeto(f"projecao {ctx.gasto[0] + projecao:.6f} USD acima do teto {ctx.teto_gasto_usd} USD. "
                       f"Configure TETO_GASTO_NO90_USD em {ARQ_CONFIG}.")
    corpo = {"content": {"parts": [{"text": enviado}]}, "outputDimensionality": ctx.dimensoes}
    for tentativa in range(1, TENTATIVAS_API + 1):
        if not ctx.credenciais.valid:
            ctx.credenciais.refresh(google.auth.transport.requests.Request())
        r = requests.post(ctx.endpoint, json=corpo, timeout=60, headers={
            "Authorization": f"Bearer {ctx.credenciais.token}", "x-goog-user-project": ctx.projeto})
        if r.status_code == 200:
            j = r.json()
            vetor = [float(v) for v in j["embedding"]["values"]]
            if len(vetor) != ctx.dimensoes:
                raise ErroGravacao(f"embedding com {len(vetor)} dimensoes; esperadas {ctx.dimensoes}.")
            tokens = int(j["usageMetadata"]["promptTokenCount"])
            gasto = tokens / 1e6 * ctx.usd_por_milhao
            ctx.gasto[0] += gasto
            return vetor, tokens, gasto
        if r.status_code in (429, 500, 502, 503, 504) and tentativa < TENTATIVAS_API:
            time.sleep(2 ** tentativa)
            continue
        raise RuntimeError(f"embedContent HTTP {r.status_code}: {r.text[:300]}")


def _existe(ctx: Contexto, exemplo_id: str) -> bool:
    from google.cloud import bigquery

    job = bigquery.QueryJobConfig(query_parameters=[bigquery.ScalarQueryParameter("id", "STRING", exemplo_id)])
    linhas = list(ctx.bq.query(f"SELECT 1 FROM `{ctx.tabela}` WHERE exemplo_id = @id", job_config=job).result())
    return bool(linhas)


def gravar_regra(id_sessao_turno: str, entrada: str, explicacao: str, regras: list, sem_chave: list, gobr: str,
                 meta_normalizado: dict, meta_geracao: dict, ctx: Contexto) -> Gravacao:
    """Grava uma linha em `exemplos`. Aprovar o mesmo turno de novo nao grava outra: o id e conferido antes.

    `meta_normalizado` e `meta_geracao` sao os metadados que os nos 50 e 80 devolveram; chave ausente levanta KeyError.
    Campo do esquema que esses nos nao devolvem (fornecedor e temperatura da geracao) grava NULL.
    """
    from google.cloud import bigquery

    for nome, valor in (("id_sessao_turno", id_sessao_turno), ("entrada", entrada), ("explicacao", explicacao),
                        ("gobr", gobr)):
        if not valor or not valor.strip():
            raise ErroConfig(f"{nome} vazio; nada a gravar.")
    exemplo_id = f"{ctx.origem}:{id_sessao_turno}"
    if _existe(ctx, exemplo_id):
        return Gravacao(exemplo_id, False, 0.0, 0)

    texto_embedding = f"{ctx.prefixo}{explicacao}"
    vetor, tokens, custo_emb = _embutir(ctx, texto_embedding)
    n, g = meta_normalizado, meta_geracao
    p = bigquery.ScalarQueryParameter
    parametros = [
        p("exemplo_id", "STRING", exemplo_id), p("origem", "STRING", ctx.origem),
        p("regra_id", "STRING", id_sessao_turno), p("id_sessao_turno", "STRING", id_sessao_turno),
        p("entrada", "STRING", entrada), p("explicacao", "STRING", explicacao),
        bigquery.ArrayQueryParameter("regras", "STRING", list(regras)),
        bigquery.ArrayQueryParameter("sem_chave", "STRING", list(sem_chave)),
        p("gobr", "STRING", gobr), p("hash_gobr", "STRING", _sha256(gobr)),
        bigquery.ArrayQueryParameter("embedding", "FLOAT64", vetor),
        p("embedding_modelo", "STRING", ctx.modelo_embedding), p("hash_texto", "STRING", _sha256(texto_embedding)),
        p("status", "STRING", ctx.status),
        # metadados_normalizado, na ordem do esquema; id_explicacao e do corpus e fica NULL para origem usuario
        p("n_tipo_entrada", "STRING", n["tipo_entrada"]), p("n_id_explicacao", "STRING", n["id_explicacao"]),
        p("n_id_prompt", "STRING", n["id_prompt"]), p("n_hash_prompt", "STRING", n["hash_prompt"]),
        p("n_id_auxiliar", "STRING", n["id_auxiliar_manual"]),
        p("n_hash_auxiliar", "STRING", n["hash_auxiliar_manual"]),
        p("n_versao", "STRING", n["versao_normalizador"]), p("n_hash_normalizador", "STRING", n["hash_normalizador"]),
        p("n_modelo", "STRING", n["modelo"]), p("n_temperatura", "STRING", n["temperatura"]),
        p("n_tokens_in", "INT64", int(n["tokens_entrada"])), p("n_tokens_out", "INT64", int(n["tokens_saida"])),
        p("n_custo", "NUMERIC", Decimal(n["custo_usd"])), p("n_tempo", "FLOAT64", float(n["tempo_segundos"])),
        p("n_timestamp", "TIMESTAMP", datetime.fromisoformat(n["timestamp"])),
        # metadados_geracao; fornecedor e temperatura nao saem do no 80, entao ficam NULL
        p("g_arquivo", "STRING", g["id_prompt"]), p("g_hash_prompt", "STRING", g["hash_prompt"]),
        p("g_modelo", "STRING", g["modelo"]), p("g_fornecedor", "STRING", None), p("g_temperatura", "STRING", None),
        p("g_tokens_in", "INT64", int(g["tokens_entrada"])), p("g_tokens_out", "INT64", int(g["tokens_saida"])),
        p("g_custo", "NUMERIC", Decimal(g["custo_usd"])), p("g_tempo", "FLOAT64", float(g["tempo_segundos"])),
        p("g_timestamp", "TIMESTAMP", datetime.fromisoformat(g["timestamp"])),
    ]
    sql = f"""INSERT INTO `{ctx.tabela}`
  (exemplo_id, origem, regra_id, id_sessao_turno, entrada, explicacao_normalizada, regras_extraidas, sem_chave, gobr,
   hash_gobr, embedding, embedding_modelo, hash_texto_embedding, metadados_normalizado, metadados_geracao,
   status_revisao)
VALUES (@exemplo_id, @origem, @regra_id, @id_sessao_turno, @entrada, @explicacao, @regras, @sem_chave, @gobr,
   @hash_gobr, @embedding, @embedding_modelo, @hash_texto,
   STRUCT(@n_tipo_entrada, @n_id_explicacao, @n_id_prompt, @n_hash_prompt, @n_id_auxiliar, @n_hash_auxiliar,
          @n_versao, @n_hash_normalizador, @n_modelo, @n_temperatura, @n_tokens_in, @n_tokens_out, @n_custo,
          @n_tempo, @n_timestamp),
   STRUCT(@g_arquivo, @g_hash_prompt, @g_modelo, @g_fornecedor, @g_temperatura, @g_tokens_in, @g_tokens_out,
          @g_custo, @g_tempo, @g_timestamp),
   @status)"""
    # Sem tratamento: erro do BigQuery sobe com a mensagem dele, e nada fica gravado pela metade (um INSERT so).
    job = ctx.bq.query(sql, job_config=bigquery.QueryJobConfig(query_parameters=parametros))
    job.result()
    if job.num_dml_affected_rows != 1:
        raise ErroGravacao(f"INSERT afetou {job.num_dml_affected_rows} linhas; esperada 1 ({exemplo_id}).")
    return Gravacao(exemplo_id, True, custo_emb, tokens)
