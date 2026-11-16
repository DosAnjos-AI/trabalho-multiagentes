"""Configuracao do projeto. Uma secao por no do agente; hoje so existe a da normalizacao.

Nao ha credencial aqui: a chave da OpenAI vem do ambiente (variavel nomeada em VARIAVEL_CHAVE).
A validacao roda na importacao: parametro ausente ou fora da lista aceita impede o modulo de carregar,
antes de qualquer leitura no BigQuery ou chamada paga.
"""

# ============================================================================
# PROJETO (endereco dos dados; sem valor padrao no codigo do no)
# ============================================================================
PROJETO_GCP = "multiagentes-514823"
DATASET = "govendas_gobr"
TABELA_PROMPTS = "prompts"
TABELA_MANUAL = "manual"

# ============================================================================
# NO 50 - NORMALIZACAO
# ============================================================================
# Lista fechada de modelos aceitos, so OpenAI (o no so implementa chat.completions da OpenAI).
# Precos em dolares por 1 milhao de tokens, conferidos em 2026-11-13 nas paginas oficiais de preco.
# Envelhece: reconferir antes de uso em escala. "temperatura_aceita": faixa que a API aceita; os modelos
# da geracao 6 recusam qualquer valor diferente de 1 (erro da API: "Only the default (1) value is supported").
MODELOS = {
    "gpt-6-luna": {"fornecedor": "openai", "entrada_por_milhao": 0.10, "saida_por_milhao": 0.50,
                   "temperatura_aceita": (1.0, 1.0)},
    "gpt-6.1-terra": {"fornecedor": "openai", "entrada_por_milhao": 1.00, "saida_por_milhao": 5.00,
                      "temperatura_aceita": (1.0, 1.0)},
    "gpt-6.1-sol": {"fornecedor": "openai", "entrada_por_milhao": 2.00, "saida_por_milhao": 10.00,
                    "temperatura_aceita": (1.0, 1.0)},
    "gpt-6-astra": {"fornecedor": "openai", "entrada_por_milhao": 10.00, "saida_por_milhao": 50.00,
                    "temperatura_aceita": (1.0, 1.0)},
}
MODELO = "gpt-6.1-terra"
FORNECEDOR = "openai"
# O no nao envia o parametro (o modelo so aceita 1); o valor entra apenas nos metadados.
TEMPERATURA = 1.0

TIPOS_ENTRADA = ("texto", "imagem", "audio", "documento", "misto")
ORIGENS = ("sintetico", "usuario")

# Limite de tokens de saida por chamada; tambem entra na projecao de custo antes da chamada.
MAX_TOKENS_SAIDA = 16000
# Teto de gasto por turno, em dolares. O acumulado por sessao e do orquestrador.
# Valor desta rodada, definido pelo Mestre.
TETO_GASTO_USD = 0.10

SECOES_OBRIGATORIAS = ("## explicacao_normalizada", "## regras_extraidas")
PREFIXO_SEM_CHAVE = "sem_chave:"
CAMPO_REGRAS = "regras_extraidas"  # arquivos do manual, sem `#Titulo`, sem repeticao
CAMPO_SEM_CHAVE = "sem_chave"      # descricoes livres das regras sem arquivo no manual
# Campos de metadados na ordem do formato; escritos pelo no, nunca pelo modelo.
CAMPOS_METADADOS = (
    "origem", "tipo_entrada", "id_sessao_turno", "id_explicacao", "id_prompt", "hash_prompt",
    "id_auxiliar_manual", "hash_auxiliar_manual", "versao_normalizador", "hash_normalizador",
    "modelo", "temperatura", "tokens_entrada", "tokens_saida", "custo_usd", "tempo_segundos", "timestamp",
)

# Alem dos treze parametros do contexto medido, o no usa tres (declarados na entrega):
# - CARACTERES_POR_TOKEN_PESSIMISTA: projecao de custo antes da chamada (sem tokenizador local);
#   3.0 e pessimista para portugues acentuado com markdown.
# - VERSAO_NORMALIZADOR: campo versao_normalizador dos metadados.
# - VARIAVEL_CHAVE: nome da variavel de ambiente com a chave (o valor nunca fica aqui).
CARACTERES_POR_TOKEN_PESSIMISTA = 3.0
VERSAO_NORMALIZADOR = "v4"
VARIAVEL_CHAVE = "CHAVE_OPENAI"

# ============================================================================
# NO 60 - RECUPERACAO
# ============================================================================
TABELA_EXEMPLOS = "exemplos"
# Filtro da busca: so entra exemplo com esta origem e este status de revisao.
ORIGEM_BUSCA = "sintetico"
STATUS_BUSCA = "aprovado"
# Quantos exemplos cada ramo traz. Independentes: a uniao tem ate N1_DENSO + N2_JACCARD (menos se os ramos coincidirem).
N1_DENSO = 2
N2_JACCARD = 2
# Lista fechada de modelos de embedding. O preco e HIPOTESE de referencia (US$ por 1M de tokens), nao conferido na
# pagina oficial; o custo real usa os tokens que a API devolve.
MODELOS_EMBEDDING = {
    "gemini-embedding-2": {"dimensoes": 3072, "usd_por_milhao": 0.20},
}
MODELO_EMBEDDING = "gemini-embedding-2"
DIMENSOES = 3072
LOCALIZACAO_EMBEDDING = "us"
# Mesmo prefixo dos documentos em `exemplos` (formato B do teste de prefixo); mudar aqui exige recalcular os documentos.
PREFIXO_EMBEDDING = "task: sentence similarity | query: "
# Teto de gasto do embedding por execucao, em dolares. Valor desta rodada, definido pelo Mestre.
TETO_GASTO_NO60_USD = 0.10

# ============================================================================
# VALIDACAO (roda na importacao)
# ============================================================================
ARQ_CONFIG = "config.py"
_AUSENTE = object()


class ErroConfig(ValueError):
    """Configuracao invalida; diz o parametro, o valor recebido, os aceitos e onde configurar."""


def _valor(nome: str):
    valor = globals().get(nome, _AUSENTE)
    if valor is _AUSENTE:
        raise ErroConfig(f"{nome} recebido: ausente. Defina em {ARQ_CONFIG}.")
    return valor


def _em(nome: str, aceitos) -> object:
    valor = _valor(nome)
    if valor not in aceitos:
        raise ErroConfig(f"{nome} recebido: {valor!r}. Aceitos: {list(aceitos)}. Configure em {ARQ_CONFIG}.")
    return valor


def _texto(nome: str) -> str:
    valor = _valor(nome)
    if not isinstance(valor, str) or not valor.strip():
        raise ErroConfig(f"{nome} recebido: {valor!r}. Aceita texto nao vazio. Configure em {ARQ_CONFIG}.")
    return valor


def _numero_positivo(nome: str, tipos=(int, float)) -> None:
    valor = _valor(nome)
    if isinstance(valor, bool) or not isinstance(valor, tipos) or valor <= 0:
        raise ErroConfig(f"{nome} recebido: {valor!r}. Aceita numero > 0. Configure em {ARQ_CONFIG}.")


def _validar() -> None:
    for nome in ("PROJETO_GCP", "DATASET", "TABELA_PROMPTS", "TABELA_MANUAL", "VARIAVEL_CHAVE", "VERSAO_NORMALIZADOR",
                 "CAMPO_REGRAS", "CAMPO_SEM_CHAVE", "PREFIXO_SEM_CHAVE"):
        _texto(nome)
    modelos = _valor("MODELOS")
    modelo = _em("MODELO", modelos)
    info = modelos[modelo]
    for nome in ("fornecedor", "entrada_por_milhao", "saida_por_milhao", "temperatura_aceita"):
        if nome not in info:
            raise ErroConfig(f"MODELOS[{modelo!r}] recebido sem o campo {nome!r}. Configure em {ARQ_CONFIG}.")
    _em("FORNECEDOR", ("openai",))
    if _valor("FORNECEDOR") != info["fornecedor"]:
        raise ErroConfig(f"FORNECEDOR recebido: {FORNECEDOR!r}, mas {modelo} e do fornecedor "
                         f"{info['fornecedor']!r}. Configure em {ARQ_CONFIG}.")
    faixa = info["temperatura_aceita"]
    if not (faixa[0] <= _valor("TEMPERATURA") <= faixa[1]):
        raise ErroConfig(f"TEMPERATURA recebido: {TEMPERATURA!r}. Aceito para {modelo}: {faixa}. "
                         f"Configure em {ARQ_CONFIG}.")
    if tuple(_valor("TIPOS_ENTRADA")) != ("texto", "imagem", "audio", "documento", "misto"):
        raise ErroConfig(f"TIPOS_ENTRADA recebido: {TIPOS_ENTRADA!r}. Aceito: lista fechada texto, imagem, audio, "
                         f"documento, misto. Configure em {ARQ_CONFIG}.")
    if set(_valor("ORIGENS")) != {"sintetico", "usuario"}:
        raise ErroConfig(f"ORIGENS recebido: {ORIGENS!r}. Aceito: ('sintetico', 'usuario'). Configure em {ARQ_CONFIG}.")
    _numero_positivo("MAX_TOKENS_SAIDA", (int,))
    _numero_positivo("TETO_GASTO_USD")
    _numero_positivo("CARACTERES_POR_TOKEN_PESSIMISTA")
    if tuple(_valor("SECOES_OBRIGATORIAS")) != ("## explicacao_normalizada", "## regras_extraidas"):
        raise ErroConfig(f"SECOES_OBRIGATORIAS recebido: {SECOES_OBRIGATORIAS!r}. Aceito: "
                         f"('## explicacao_normalizada', '## regras_extraidas'). Configure em {ARQ_CONFIG}.")
    campos = _valor("CAMPOS_METADADOS")
    if len(campos) != 17 or len(set(campos)) != 17:
        raise ErroConfig(f"CAMPOS_METADADOS recebido: {campos!r}. Aceita 17 campos distintos. "
                         f"Configure em {ARQ_CONFIG}.")


_validar()


def _validar_no60() -> None:
    """Validacao do no 60; roda na importacao, depois da validacao do no 50."""
    for nome in ("TABELA_EXEMPLOS", "ORIGEM_BUSCA", "STATUS_BUSCA", "LOCALIZACAO_EMBEDDING", "PREFIXO_EMBEDDING"):
        _texto(nome)
    _em("ORIGEM_BUSCA", ("sintetico",))
    _em("STATUS_BUSCA", ("aprovado",))
    _numero_positivo("N1_DENSO", (int,))
    _numero_positivo("N2_JACCARD", (int,))
    _numero_positivo("TETO_GASTO_NO60_USD")
    modelos = _valor("MODELOS_EMBEDDING")
    modelo = _em("MODELO_EMBEDDING", modelos)
    info = modelos[modelo]
    for nome in ("dimensoes", "usd_por_milhao"):
        if nome not in info:
            raise ErroConfig(f"MODELOS_EMBEDDING[{modelo!r}] recebido sem o campo {nome!r}. Configure em {ARQ_CONFIG}.")
    if _valor("DIMENSOES") != info["dimensoes"]:
        raise ErroConfig(f"DIMENSOES recebido: {DIMENSOES!r}. Aceito para {modelo}: {info['dimensoes']}. "
                         f"Configure em {ARQ_CONFIG}.")


_validar_no60()
