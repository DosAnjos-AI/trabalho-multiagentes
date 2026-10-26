"""Configuração central: caminhos, modelo, coleção e constantes.

Nada disso deve aparecer espalhado pelo código. Trocar de ambiente é mudar
um valor aqui, nunca uma linha de lógica.
"""
from pathlib import Path

# Raiz do projeto derivada da posição deste arquivo (indexacao/config.py), e não
# do diretório de execução, para os scripts funcionarem de qualquer cwd.
RAIZ_PROJETO = Path(__file__).resolve().parent.parent
PASTA_SIMULACAO = RAIZ_PROJETO / "simulacao"
PASTA_INDEXACAO = RAIZ_PROJETO / "indexacao"
PASTA_DADOS = PASTA_INDEXACAO / "dados"
PASTA_CHROMA = PASTA_DADOS / "chroma"
ARQUIVO_INDICE_LEXICO = PASTA_DADOS / "indice_lexico.json"

# Guarda de local: o corpus tem exatamente regra_001 .. regra_249.
TOTAL_PASTAS = 249
PREFIXO_PASTA = "regra_"
NOME_NORMALIZADO = "normalizado.md"

# Modelo de embeddings. O e5 exige prefixos distintos para documento e consulta;
# sem eles a qualidade da recuperação cai de forma silenciosa.
NOME_MODELO = "intfloat/multilingual-e5-base"
DIMENSAO_VETOR = 768
PREFIXO_PASSAGEM = "passage: "
PREFIXO_CONSULTA = "query: "

# Coleção do Chroma. Cosseno porque os vetores saem normalizados do modelo.
NOME_COLECAO = "regras_govendas"
METRICA_DISTANCIA = "cosine"
TAMANHO_LOTE = 32

# Formato dos arquivos
VERSAO_ORIGEM = "3.1"
VERSAO_DESTINO = "4.0"

# Vocabulário fechado de tipos de critério. "capacidade" ficou de fora porque
# tem zero ocorrências no corpus.
TIPOS_CRITERIO = (
    "tempo_sem_comprar",
    "tempo_sem_visita",
    "estagio_relacionamento",
    "carteira",
    "situacao_financeira",
    "situacao_cadastro",
    "valor_cliente",
    "localizacao",
    "agenda_rota",
    "segmento",
    "periodo_vigencia",
    "identificacao",
)

# Valores padrão omitidos no formato 4.0 (enxugamento).
UNIDADE_PADRAO = "none"
ALCANCE_PADRAO = "nao_informado"

# Documento usado pelo teste de fumaça.
ID_TESTE_FUMACA = "regra_166"
