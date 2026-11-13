# Comparação: gpt-6.1-terra, regra_032

Critério: `../CRITERIO_AVALIACAO_v1.md`. Original: `regras_originais/regra_032.gobr`. Reconstrução: `reconstrucoes/gpt-6.1-terra/regra_032.gobr`.

| Medida | Todos os blocos | Sem `time` |
|---|---|---|
| Regras capturadas | 78/78 | 77/77 |
| Regras inventadas | 0 | 0 |
| Regra inteira correta | 3/78 | 2/77 |
| Inteira correta ignorando caixa dos valores (leitura auxiliar, fora do critério) | 21/78 | 20/77 |

## Faltaram

Nenhuma.

## Inventadas

Nenhuma.

## Capturadas mas não inteiras corretas

- Carteiras `sul_sudeste_centrooeste` e `norte_nordeste`: o original usa `carteira livre`; nenhuma descrição menciona que o cliente pode ficar em mais de uma carteira
- `Prospects`: o original usa `da carteira("sul_sudeste_centrooeste","norte_nordeste")` (duas carteiras como fonte); reconstruí `do time("televendas")`
- Matcon (18 blocos): a descrição traduziu `MATCON` para "material de construção"; reconstruí `"material de construcao"`, valor diferente
- Atacado (18 blocos): a descrição fala em "atacado e distribuidores"; o original filtra só `"ATACADO"`
- Corporativo (18 blocos): "corporativo e consumidor final" x `"CONS. FINAL"`
- EPI e Licitação (18 blocos): só caixa (`"licitacao"` x `"LICITACAO"`); ignorando caixa, os 18 batem
- `Pré-inativos Curva C (Sul... Matcon...)`: a descrição chamou a exceção de "compra vinculada ao vendedor", o que levou a `recencia de positivacao do vendedor`; o original é `recencia de positivacao` (vendedores do grupo)
