# Filtros financeiros (manual 6.3, p.24-25)

| Filtro | Descrição |
|---|---|
| `adimplentes` | sem pendências financeiras em aberto |
| `inadimplentes` | com pendências financeiras em aberto |
| `tem credito` | com crédito disponível |
| `não tem credito` | sem crédito disponível |
| `com limite de R$ <valor> de credito` | limite de crédito maior ou igual ao valor |
| `com R$ <valor> de credito` | pelo menos o valor de crédito |
| `com menos de R$ <valor> de credito disponivel` | crédito disponível abaixo do valor |
| `com <N>% de credito` | porcentagem de crédito em relação ao limite maior ou igual a N |
| `com ticket medio maior que R$ <valor>` | ticket médio acima do valor |
| `com ticket medio igual a R$ <valor>` | ticket médio igual ao valor |
| `total faturado no <periodo> com a empresa maior que R$ <valor>` | faturamento acima do valor no período |
| `total faturado no <periodo> com a empresa menor que R$ <valor> e maior que R$ <valor>` | faturamento dentro dos valores no período |
| `media faturada no <periodo> com a empresa menor que R$ <valor> e maior que R$ <valor>` | faturamento médio por mês no período dentro dos valores |

- Em ticket médio e faturamento, `ou indefinido` ao final inclui clientes cujo valor é desconhecido.
- `maior que`, `menor que` e `igual a` combinam com `e`.
- `<periodo>`: mês, bimestre, trimestre, semestre, ano.
