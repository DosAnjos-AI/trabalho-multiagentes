# Comparação: gemini-3.6-flash, regra_032

Critério: `../CRITERIO_AVALIACAO_v1.md`. Original: `regras_originais/regra_032.gobr`. Reconstrução: `reconstrucoes/gemini-3.6-flash/regra_032.gobr`.

| Medida | Todos os blocos | Sem `time` |
|---|---|---|
| Regras capturadas | 78/78 | 77/77 |
| Regras inventadas | 0 | 0 |
| Regra inteira correta | 73/78 | 72/77 |

## Faltaram

Nenhuma.

## Inventadas

Nenhuma.

## Capturadas mas não inteiras corretas

- Carteiras `sul_sudeste_centrooeste` e `norte_nordeste`: o original usa `carteira livre`; nenhuma descrição menciona que o cliente pode ficar em mais de uma carteira
- `Prospects`: o original usa `da carteira("sul_sudeste_centrooeste","norte_nordeste")` (duas carteiras como fonte); reconstruí `do time("televendas")`
- `Pré-inativos Curva C (Sul... Matcon...)`: o original usa `recencia de positivacao em 150 dias` (sem `global`), exceção única no arquivo; a descrição não a menciona
- `Inativos Curva C (Norte e Nordeste - Corporativo/ Consumidor)`: o original não tem frequência (bloco incompleto, parêntese não fechado); a descrição diz só "há ainda o caso registrado" e eu completei com `frequencia de 28 dias` por padrão

## Notas

- Valores de ramo (`"MATCON"`, `"CONS. FINAL"` etc.) idênticos ao original: a descrição os trouxe em caixa alta, literais.
