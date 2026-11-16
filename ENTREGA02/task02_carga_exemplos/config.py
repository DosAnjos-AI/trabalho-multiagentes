"""Constantes da carga da tabela `exemplos` no BigQuery. Sem logica: o script valida antes de qualquer chamada."""
from pathlib import Path

BASE = Path(__file__).resolve().parent
RAIZ = BASE.parents[1]

# ============================================================================
# 1. CAMINHOS (fontes so de leitura)
# ============================================================================
CAMINHO_NORMALIZADOS = RAIZ / "dados" / "processados" / "regras_normalizadas"
CAMINHO_ENTRADAS = RAIZ / "dados" / "processados" / "regras_entradas"
CAMINHO_GOBR = RAIZ / "dados" / "processados" / "regras_gobr"
# Cache do teste de prefixo: so as linhas do formato B sao copiadas para a pasta desta carga.
CAMINHO_CACHE_TESTE = RAIZ / "ENTREGA02" / "task02_teste_prefixo_embedding" / "embeddings.jsonl"
CHAVE_FORMATO_B_NO_TESTE = "B"
# Saida (nunca apagada): uma pasta por execucao, com carimbo, modelo e dimensoes no nome.
CAMINHO_SAIDA = BASE / "saida"

# ============================================================================
# 2. BIGQUERY
# ============================================================================
PROJETO = "multiagentes-514823"
DATASET = "govendas_gobr"
TABELA = "exemplos"
LOCALIZACAO_BQ = "US"

# ============================================================================
# 3. EMBEDDING
# ============================================================================
MODELO_EMBEDDING = "gemini-embedding-2"
DIMENSOES = 3072
ENDPOINT = (f"https://aiplatform.googleapis.com/v1/projects/{PROJETO}/locations/us/publishers/google/models/"
            f"{MODELO_EMBEDDING}:embedContent")
# Formato B. Consultas futuras DEVEM usar o mesmo prefixo (ver readme.md).
PREFIXO_EMBEDDING = "task: sentence similarity | query: "

# ============================================================================
# 4. CUSTO
# ============================================================================
# [HIPOTESE] preco de referencia em US$ por 1M de tokens; os tokens vem do usageMetadata da API.
USD_POR_MILHAO = 0.20
TETO_GASTO_USD = 2.00
# Caracteres por token usados so na projecao (calibracoes do config.py da normalizacao).
CARACTERES_POR_TOKEN_PESSIMISTA = 3.0
TENTATIVAS_API = 5

# ============================================================================
# 5. VALIDACAO
# ============================================================================
TOTAL_ESPERADO = 193
# Exemplos usados na prova de VECTOR_SEARCH (primeiro, do meio e ultimo dos ids).
IDS_VECTOR_SEARCH = ("003", "135", "246")
