"""Configuração do retriever: o que indexacao/config.py não cobre.

Tudo o que é caminho, modelo ou preço fica aqui, declarado por extenso. O código
não tem valor padrão escondido: se um caminho daqui estiver errado, o script falha
nomeando o arquivo, em vez de ler outra coisa em silêncio.
"""
from pathlib import Path

RAIZ_PROJETO = Path(__file__).resolve().parent.parent
PASTA_INDEXACAO = RAIZ_PROJETO / "indexacao"
PASTA_SAIDAS = RAIZ_PROJETO / "retriever" / "saidas"

# Prompt de normalização. O texto usado é exatamente o que está entre as cercas
# '~~~~' (numeração 1-based); as linhas das cercas são conferidas antes do uso, para
# que uma edição em NORMALIZACAO.md não desloque o recorte sem ninguém notar.
ARQUIVO_NORMALIZACAO = RAIZ_PROJETO / "NORMALIZACAO.md"
LINHAS_PROMPT_SISTEMA = (26, 175)
LINHAS_PROMPT_USUARIO = (181, 194)
# Hash do prompt com que os ciclos anteriores foram medidos. Se divergir, as medições
# não valem para o prompt atual: o script para e pede que este valor seja revisto.
PROMPT_SHA256_ESPERADO = "dc4fe4b851fbcf3be8499114e363beca6fc46386ef7ca0c054a47046780a4108"

# Campos do prompt de usuário em tempo de consulta (NORMALIZACAO.md, seção 7).
CAMPOS_CONSULTA = {
    "{caminho_do_gobr_ou_null}": "null",
    "{tipo_input}": "texto_corrido",
    "{true_false_ou_null}": "null",
    "{true_ou_false}": "false",
    "{corpus_sintetico_corpus_real_ou_consulta}": "consulta",
    "{url_ou_null}": "null",
}

# API de normalização. gemini-2.5-flash está indisponível (HTTP 404); este é o
# modelo com que o ciclo 3 mediu custo, latência e a taxa de conversão.
ARQUIVO_ENV = RAIZ_PROJETO / ".env"
NOME_CHAVE_ENV = "CHAVE_OPENAI"
URL_API = "https://api.openai.com/v1/chat/completions"
MODELO_NORMALIZACAO = "gpt-4.1-mini-2025-04-14"
TEMPERATURA = 0
SEMENTE = 42
MAX_TOKENS_SAIDA = 16000
TIMEOUT_API_S = 180
# USD por token, os mesmos do ciclo 3 (developers.openai.com, gpt-4.1-mini).
PRECO_ENTRADA_USD = 0.40 / 1e6
PRECO_SAIDA_USD = 1.60 / 1e6

# Recuperação
TOP_N_PADRAO = 10
MODELO_RERANK = "cross-encoder/mmarco-mMiniLMv2-L12-H384-v1"

# Manual. Os fixos vão sempre; os chaveados saem do mapa, lido do arquivo.
PASTA_MANUAL = RAIZ_PROJETO / "manual"
PASTA_SECOES = PASTA_MANUAL / "03-secoes"
ARQUIVO_MAPA = PASTA_MANUAL / "03-mapa.md"
SECAO_MAPA_TIPOS = "## Critérios de seleção"
MANUAL_FIXOS = (
    PASTA_MANUAL / "02-invariantes.md",
    PASTA_SECOES / "10-gramatica.md",
)
