# Comparação: gpt-6-luna, regra_032

Critério: `../CRITERIO_AVALIACAO_v1.md`. Original: `regras_originais/regra_032.gobr`. Reconstrução: `reconstrucoes/gpt-6-luna/regra_032.gobr`.

| Medida | Todos os blocos | Sem `time` |
|---|---|---|
| Regras capturadas | 78/78 | 77/77 |
| Regras inventadas | 0 | 0 |
| Regra inteira correta | 3/78 | 2/77 |
| Inteira correta ignorando caixa dos valores (leitura auxiliar, fora do critério) | 57/78 | 56/77 |

## Faltaram

Nenhuma.

## Inventadas

Nenhuma.

## Capturadas mas não inteiras corretas

- Carteiras `sul_sudeste_centrooeste` e `norte_nordeste`: o original usa `carteira livre`; nenhuma descrição menciona que o cliente pode ficar em mais de uma carteira
- `Prospects`: o original usa `da carteira("sul_sudeste_centrooeste","norte_nordeste")` (duas carteiras como fonte); reconstruí `do time("televendas")`
- 72 blocos de segmento: valores de ramo em caixa diferente (`"Matcon"` x `"MATCON"`, `"Atacado"` x `"ATACADO"`, `"Licitacao"` x `"LICITACAO"`) e, em Corporativo, valor diferente (`"Consumidor Final"` x `"CONS. FINAL"`). Pelo critério estrito, nenhum dos 72 é inteiro correto
- Ignorando caixa: 54 dos 72 batem; os 18 de Corporativo continuam errados pelo valor `"Consumidor Final"`

## Notas

- A exceção `recencia de positivacao em 150 dias` sem `global` foi descrita explicitamente e reconstruída corretamente.
- O bloco final sem frequência foi descrito como "não especifica intervalo" e reconstruído sem frequência, como no original.
