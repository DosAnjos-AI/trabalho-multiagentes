"""Constantes da carga da tabela `manual` no BigQuery. Sem logica: o script valida antes de qualquer carga."""
from pathlib import Path

BASE = Path(__file__).resolve().parent
RAIZ = BASE.parents[1]

# Saida (nunca apagada): uma pasta por execucao, com carimbo no nome.
CAMINHO_SAIDA = BASE / "saida"

PROJETO = "multiagentes-514823"
DATASET = "govendas_gobr"
TABELA = "manual"
TABELA_EXEMPLOS = "exemplos"
LOCALIZACAO_BQ = "US"

CAMINHO_MANUAL = RAIZ / "manual"
CAMINHO_SECOES = CAMINHO_MANUAL / "03-secoes"
# Auxiliar do normalizador: seus caminhos-chave precisam existir na tabela.
CAMINHO_AUXILIAR = RAIZ / "ENTREGA02" / "task01_normalizacao_explicacao" / "regras_para_normalizador_v2.md"

# Arquivos de raiz que entram, com o tipo de cada. CORRECOES_MANUAL.md fica de fora (historico humano).
ARQUIVOS_RAIZ = (
    ("01-conceitos.md", "conceitos"),
    ("02-invariantes.md", "invariantes"),
    ("03-mapa.md", "mapa"),
)
TIPO_SECAO = "secao"
TOTAL_ESPERADO = 30
TOTAL_SECOES_ESPERADO = 27
