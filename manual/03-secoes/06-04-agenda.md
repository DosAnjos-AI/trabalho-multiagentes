# Filtros de agenda (manual 6.4, p.25-26)

Verificam se o cliente já está, ou não, em agendas.

| Filtro | Descrição |
|---|---|
| `na agenda de hoje` | na agenda padrão de hoje (tempo fixo) |
| `na agenda do vendedor de ontem` | estava agendado para o vendedor ontem |
| `na agenda na semana` | agendado na semana atual |
| `fora da agenda de hoje` | não agendado para hoje |
| `na agenda do vendedor de hoje` | na agenda do vendedor específico hoje |
| `na agenda global de hoje` | na agenda de qualquer vendedor hoje |
| `fora da agenda padrão em 5 dias` | não agendado na agenda padrão nos últimos 5 dias (tempo) |
| `na agenda de ruptura de hoje` | na agenda de ruptura do dia |
| `na agenda complementar de hoje` | na agenda complementar do dia |
| `agendavel` | marcado como agendável (parametrizado para agendar) |
| `não agendavel` | marcado como não agendável |
| `reagendado` | reagendado para algum vendedor do grupo |
| `não reagendado para a empresa` | não reagendado por nenhum vendedor da empresa |

- Tipos de agenda: padrão, ruptura, complementar. Sem especificar vale a padrão.
- Reagendado: `para o vendedor` ou `para a empresa`.
- Período de análise: `<tempo>` (valorado) ou `<tempo fixo>` (ver 06-12-opcoes-de-tempo.md).
