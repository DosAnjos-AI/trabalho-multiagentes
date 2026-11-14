# Filtros de atividade e inatividade (manual 6.1, p.22-23)

Usados após `quando`, combinados com `e`. Estado do cliente quanto a compras e visitas.

```
quando adimplentes
       e ativos para o vendedor
       e recencia de visita entre 10 dias e 90 dias
```

| Filtro | Descrição |
|---|---|
| `ativos` | ativos pelos critérios padrão do sistema |
| `ativos para o vendedor` | ativos segundo o histórico do vendedor específico |
| `ativos para a empresa` | ativos segundo o histórico de qualquer vendedor |
| `inativos` | inativos pelos critérios padrão |
| `inativos para o vendedor` | sem compra com o vendedor há tempo suficiente para ser inativo |
| `inativos para a empresa` | sem compra com nenhum vendedor da empresa |
| `inatividade de <N> dias` | sem compra há pelo menos N dias (tempo) |
| `inatividade global de <N> dias` | sem compra com a empresa toda há pelo menos N dias (tempo) |
| `sem venda ou prospects` | nunca compraram |
| `unica compra com a empresa` | uma única compra com a empresa |
| `unica compra com o vendedor` | uma única compra com o vendedor |
| `prospects do vendedor` | nunca compraram com o vendedor |
| `prospects da empresa` | nunca compraram com a empresa |
| `tem venda do vendedor <condicional de tempo>` | comprou do vendedor no período, não necessariamente a última compra |
| `não tem venda <condicional de tempo>` | sem venda de nenhum vendedor do mesmo grupo no período |
| `tem venda da empresa <condicional de tempo>` | comprou de qualquer vendedor no período |
| `tem <N>% de visita remota <tempo>` | pelo menos N% de visitas remotas em relação às presenciais no tempo |
| `tem <N>% de visita incerta <tempo>` | pelo menos N% de visitas sem saber se remotas ou presenciais |
| `atividade global de <tempo>` | comprou no tempo especificado |
| `atividade do vendedor de <tempo>` | comprou do vendedor no tempo |
| `atividade de <tempo>` | comprou de algum vendedor do grupo no tempo |

Em "venda" a opção é `do vendedor` ou `da empresa`. `<tempo>` e `<condicional de tempo>`: ver 06-12-opcoes-de-tempo.md.
