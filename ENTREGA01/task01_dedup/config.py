from pathlib import Path

BASE = Path(__file__).parent

# Pasta de origem dos arquivos .gobr
CAMINHO_ENTRADA = BASE / "dados_originais"
# Pasta de destino; apagada a cada execucao. Trocar o caminho escreve em outro lugar
CAMINHO_SAIDA = BASE / "dados_deduplicados"
# Similaridade igual ou acima deste valor significa o mesmo caso
LIMIAR_SIMILARIDADE = 0.95
# False ignora linhas de comentario (#) na comparacao; True as conta
CONSIDERAR_COMENTARIOS = False
# "par_a_par" ou "transitivo"
MODO_AGRUPAMENTO = "par_a_par"
# Valor da linha version inserida quando o arquivo nao declara
VERSAO_PADRAO = "1.0"
