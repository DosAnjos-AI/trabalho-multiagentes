# Outros filtros úteis (manual 6.11, p.31-33)

| Filtro | Descrição |
|---|---|
| `positivado de hoje` | positivado hoje (tempo ou tempo fixo) |
| `atendimento remoto em 5 dias` | teve atendimento remoto nos últimos 5 dias |
| `sem perfil com o vendedor` | não marcado para não agendar para o vendedor, nem excluído, nem baixado na Receita Federal |
| `sem perfil com a empresa` | não marcado para não agendar para qualquer vendedor, nem excluído, nem baixado na Receita |
| `total de compras com o vendedor maior que <N>` | pelo menos N compras com o vendedor |
| `total de compras com a empresa menor que <N> ou indefinido` | no máximo N compras com a empresa, ou valor não calculado |
| `compras no mês com o vendedor maior que <N>` | pelo menos N compras com o vendedor no período |
| `compras no semestre com a empresa menor que <N> ou indefinido` | no máximo N compras com a empresa no período, ou não calculado |
| `queda de faturamento menor que <N>%` | queda de faturamento até N% |
| `queda de faturamento maior que <N>%` | queda de faturamento acima de N% |
| `cadastrado faz 90 dias` | cadastrado no ERP há no mínimo 90 dias (tempo) |
| `cadastrado a partir do dia '2026-02-10'` | cadastrado após o dia informado |
| `elegivel` | não excluído, ativo e marcado para agendar |
| `elegivel incluindo roteirizavel` | idem, e marcado para roteirizar |
| `data da próxima visita do representante em 2 semanas` | data de visita no ERP de vendedor externo só daqui a 2 semanas (tempo ou tempo futuro) |
| `data da última visita do representante na semana anterior` | data de visita no ERP de vendedor externo foi na semana passada |
| `data da rota no mês anterior` | data de rota compreende somente o mês anterior |
| `data da rota futura em 5 dias a frente` | data de rota somente após 5 dias a partir de hoje |
| `data da rota futura do vendedor nos próximos 2 dias` | data de rota nos próximos 2 dias, associada ao vendedor dono do cliente |

- Total de compras e compras no período: `maior que`, `menor que`, `ou indefinido`, ou `maior que <N> e menor que <N>`.
- Período de análise: `<tempo>` (valorado), `<tempo fixo>` ou `<tempo futuro>`.
- `<periodo>`: mês, bimestre, trimestre, semestre, ano.
- Data: `'yyyy-mm-dd'` ou `'dd-mm-yyyy'`.
