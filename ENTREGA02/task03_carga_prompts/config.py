"""Constantes da carga da tabela `prompts` no BigQuery. Sem logica: o script valida antes de qualquer carga."""
from pathlib import Path

BASE = Path(__file__).resolve().parent
RAIZ = BASE.parents[1]

# Saida (nunca apagada): uma pasta por execucao, com carimbo no nome.
CAMINHO_SAIDA = BASE / "saida"

PROJETO = "multiagentes-514823"
DATASET = "govendas_gobr"
TABELA = "prompts"
TABELA_EXEMPLOS = "exemplos"
LOCALIZACAO_BQ = "US"

TIPOS_ACEITOS = ("geracao_explicacao", "normalizador", "auxiliar_manual")

_N = RAIZ / "ENTREGA02" / "task01_normalizacao_explicacao"
_L = _N / "legados"
_E = RAIZ / "ENTREGA01" / "task02_entradas"

# Uma entrada por hash. `arquivo` e o nome do arquivo (so leitura humana); `versao` vem do nome do arquivo.
# As copias de legados/prompts/duplicatas_raiz/ ficam de fora (mesmo hash dos arquivos de legados/prompts/).
# `ativo` e true so nos 3 em uso; deve haver exatamente 1 ativo por tipo.
PROMPTS = (
    {"caminho": _E / "prompt_v2.md", "tipo": "geracao_explicacao", "versao": "v2", "ativo": True},
    {"caminho": _N / "prompt_normalizador_v3.md", "tipo": "normalizador", "versao": "v3", "ativo": True},
    {"caminho": _N / "regras_para_normalizador_v2.md", "tipo": "auxiliar_manual", "versao": "v2", "ativo": True},
    {"caminho": _E / "prompt_legados" / "prompt_v1.md", "tipo": "geracao_explicacao", "versao": "v1", "ativo": False},
    {"caminho": _L / "prompts" / "prompt_normalizador_v1.md", "tipo": "normalizador", "versao": "v1", "ativo": False},
    {"caminho": _L / "prompts" / "prompt_normalizador_v2.md", "tipo": "normalizador", "versao": "v2", "ativo": False},
    {"caminho": _L / "prompts" / "prompt_normalizador_v1_rascunho.md", "tipo": "normalizador",
     "versao": "v1_rascunho", "ativo": False},
    {"caminho": _L / "regras_para_normalizador_v1.md", "tipo": "auxiliar_manual", "versao": "v1", "ativo": False},
)
