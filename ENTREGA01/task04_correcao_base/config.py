"""Caminhos e parametros da tarefa 04: validacao do conferidor e correcao da base .gobr.

Todo valor e validado por script_correcao.validar_config antes de qualquer leitura.
"""

from pathlib import Path

PASTA_TAREFA = Path(__file__).resolve().parent
RAIZ = PASTA_TAREFA.parents[1]
PASTA_SRC = RAIZ / "src"

# Somente leitura: e a referencia que sobra para rever as inferencias.
PASTA_ENTRADA = RAIZ / "ENTREGA01" / "task02_entradas" / "regras_originais"
EXTENSAO_ENTRADA = ".gobr"
CONTAGEM_ESPERADA = 193

PASTA_SAIDA = PASTA_TAREFA / "dados_saida"
PASTA_BASE_CORRIGIDA = PASTA_SAIDA / "base_corrigida"

# Etapas, nesta ordem. "correcao" so roda com VALIDACAO_APROVADA = True.
ETAPAS_ACEITAS = ("amostra", "correcao")
ETAPAS = ("amostra", "correcao")

# Semente fixa: amostra que muda a cada execucao nao pode ser reconferida por outra pessoa.
SEMENTE_AMOSTRA = 20261113
TAMANHO_AMOSTRA = 10

# Portao da segunda restricao: so vira True depois que a conferencia manual dos 10
# arquivos (dados_saida/amostra_validacao.md) terminou sem divergencia.
VALIDACAO_APROVADA = True

TIPOS_CORRECAO = ("deterministica", "inferencia", "nao_inferivel")

# Numeros do laudo anterior (tarefa 03), usados para detectar perda ou ganho de achados.
FALHAS_LAUDO_ANTERIOR = 11
NAO_DOCUMENTADAS_LAUDO_ANTERIOR = 301
