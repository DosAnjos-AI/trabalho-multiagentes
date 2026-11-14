"""Caminhos e parametros da tarefa 03: conferencia da base .gobr contra o manual.

Todo valor e validado por script_conferencia.validar_config antes de qualquer leitura.
"""

from pathlib import Path

PASTA_TAREFA = Path(__file__).resolve().parent
RAIZ = PASTA_TAREFA.parents[1]

# O conferidor vive em src/ porque sera reaproveitado pelo agente; este script so importa.
PASTA_SRC = RAIZ / "src"

PASTA_ENTRADA = RAIZ / "ENTREGA01" / "task02_entradas" / "regras_originais"
EXTENSAO_ENTRADA = ".gobr"
# Saida da tarefa 01 (dedup). Contagem diferente aborta: conferir a base errada
# produz laudo que parece valido e nao e.
CONTAGEM_ESPERADA = 193

PASTA_SAIDA = PASTA_TAREFA / "dados_saida"

# Etapas a executar, nesta ordem. "conferencia" exige "calibracao": numero de
# instrumento nao calibrado nao vale.
ETAPAS_ACEITAS = ("calibracao", "conferencia", "cenarios")
ETAPAS = ("calibracao", "conferencia", "cenarios")

# Casos conhecidos da calibracao (passo 3 da rodada).
CALIBRACAO_PARENTESE = {
    "arquivo": "regra_032.gobr",
    "itens_esperados": ("parenteses_balanceados", "parametros_tem_atendimento"),
}
CALIBRACAO_CAIXA = {
    "arquivo": "regra_228.gobr",
    "item": "grafia_documentada",
    "categoria": "divergencia_com_manual",
    "trecho": "curva c",
}
# A tarefa 01 garantiu a linha version em todo arquivo: espera-se zero achados destes itens.
CALIBRACAO_VERSION_ITENS = ("version_no_inicio", "version_unica")

# Cenarios nao previstos (secao 11). Extensao .txt para nao criar arquivo .gobr.
CENARIOS = {
    "cenario_vazio.txt": "",
    "cenario_so_comentarios.txt": "# comentario 1\n# comentario 2\n   # comentario indentado\n",
    "cenario_version_duplicada.txt": (
        "version 1.0\n"
        "version 1.0\n"
        "\n"
        'time "televendas":\n'
        "    vendedores todostelevendas\n"
        "\n"
        'parametros "semanal":\n'
        '    do time("televendas")\n'
        "    frequencia semanal()\n"
    ),
}
