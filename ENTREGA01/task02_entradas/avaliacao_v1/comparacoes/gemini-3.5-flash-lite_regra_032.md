# Comparação: gemini-3.5-flash-lite, regra_032

Critério: `../CRITERIO_AVALIACAO_v1.md`. Original: `regras_originais/regra_032.gobr`. Reconstrução: `reconstrucoes/gemini-3.5-flash-lite/regra_032.gobr`.

| Medida | Todos os blocos | Sem `time` |
|---|---|---|
| Regras capturadas | 76/78 | 75/77 |
| Regras inventadas | 0 | 0 |
| Regra inteira correta | 2/78 | 2/77 |

## Faltaram

- `carteira livre "sul_sudeste_centrooeste"` e `carteira livre "norte_nordeste"`: a descrição fala em "duas grandes regiões geográficas", sem dizer que são carteiras; reconstruí a região como filtro `uf do estado` dentro de cada bloco

## Inventadas

Nenhuma.

## Capturadas mas não inteiras corretas

- `time "televendas"`: faltou `ativados` (a descrição não menciona vendedores ativos)
- `Prospects`: fonte `do time` em vez de `da carteira(...)` das duas regiões
- 72 blocos de segmento: todos com componentes errados: fonte `do time` + filtro `uf` em vez de `da carteira`; filtro extra `curva A/B/C com a empresa` (a descrição trata "Curva A" como condição, quando no original é só o rótulo da faixa de faturamento); `recencia de positivacao` sem `global`; valores de ramo por nome em vez de código

## Notas

- Os 72 blocos foram pareados por papel (região + ramo + estágio + faixa) e contam como capturados.
