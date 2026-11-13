# task01_dedup

Remove duplicados e quase-duplicados de regras `.gobr`.

## Entrada e saida

- Entrada: `dados_originais/`, arquivos `.gobr` (copiados de `simulacao/` e, se diferentes, de `exemplos/`).
- Saida: `dados_deduplicados/`, arquivos `.gobr` mantidos com o nome original (sem reenumerar) e `000_relatorio_dedup.csv`.

## Tecnologias

- `difflib.SequenceMatcher(None, a, b, autojunk=False)` sobre listas de linhas normalizadas. O `.gobr` e orientado a linha. `autojunk=False` e obrigatorio: o padrao descarta linhas muito repetidas e distorce a similaridade no grupo de arquivos quase iguais.
- `pathlib`: caminhos portaveis entre Linux e Windows.
- Apenas biblioteca padrao do Python.

## Estrutura

- `config.py`: parametros da execucao.
- `script.py`: normaliza, compara, agrupa e escreve a saida.
- `readme.md`: este arquivo.
- `dados_originais/`: entrada, somente `.gobr`.
- `dados_deduplicados/`: saida, reescrita a cada execucao.

## Configuracao (`config.py`)

- `CAMINHO_ENTRADA`: pasta de origem dos `.gobr`.
- `CAMINHO_SAIDA`: pasta de destino; trocar o caminho escreve em outro lugar.
- `LIMIAR_SIMILARIDADE` (0.95): similaridade igual ou acima disso conta como o mesmo caso. Subir remove menos; baixar remove mais.
- `CONSIDERAR_COMENTARIOS` (`False`): `False` ignora linhas iniciadas por `#` na comparacao; `True` as conta. A escolha de quem fica usa sempre o texto bruto.
- `MODO_AGRUPAMENTO` (`"par_a_par"`): `"par_a_par"` descarta um arquivo so se bater o limiar com um ja mantido; `"transitivo"` forma grupos conectados e mantem um por grupo. Valor invalido aborta com erro.

- `VERSAO_PADRAO` (`"1.0"`): valor da linha `version` inserida quando o arquivo nao a declara.

Garantia da linha `version` (na saida, nunca na entrada): se a primeira linha que nao e vazia nem comentario for `version`, nada muda. Se nao for, mas `version` existir em outra posicao, nada e inserido e o arquivo e apontado como posicao inesperada na execucao. Se nao existir, `version <VERSAO_PADRAO>` entra como primeira linha de conteudo, depois do bloco de comentarios do topo. A linha nunca fica duplicada.

Ordem do processamento: garantir `version` -> normalizar -> comparar. A diferenca de valor de `version` conta como diferenca real. O criterio de tamanho usa o texto bruto ja com a linha garantida.

Criterio de quem fica: mais caracteres no texto bruto; empate, menor numero de regra.

## Uso

    python script.py

## Aviso

**A pasta de saida e apagada por completo a cada execucao.** A pasta de entrada nunca e alterada.
