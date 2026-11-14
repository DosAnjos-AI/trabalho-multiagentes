# Filtros temporais de calendário (manual seção 5, p.18-20)

Definem quando uma regra de parametrização ou alerta executa. Vêm logo após a referência ao time ou carteira. Todos combinam com `e`.

```
na carteira("televendas")
no dia 2 e no dia 12 e
           no domingo e na segunda e
           na primeira semana e
           no segundo semestre
```
Executa se o dia for 2 ou 12, e domingo ou segunda, na primeira semana do mês, no segundo semestre.

**Ordem obrigatória:** (1) dia do mês, (2) dia da semana, (3) semana do mês, (4) mês do ano, (5) horário. Não é obrigatório usar todos.

## Dia do mês
| Filtro | Efeito |
|---|---|
| `no dia 10` | só no dia 10 de cada mês |
| `no ultimo dia do mês` | só no último dia do mês |
| `antes do dia 20` | dias 1 a 19 |
| `depois do dia 15` | dia 16 ao último |
| `a partir do dia 12` | dia 12 ao último |
| `entre os dias 12 e 30` | dias 12 a 30 |

## Dia da semana
| Filtro | Efeito |
|---|---|
| `na segunda` / `na terça` / `na quarta` / `na quinta` / `na sexta` | só naquele dia |
| `no sabado` / `no domingo` | só naquele dia |
| `todos os dias` | todos os dias |
| `nos dias uteis` | segunda a sexta |
| `no fim de semana` | sábado e domingo |

## Semana do mês
| Filtro | Efeito |
|---|---|
| `na primeira semana` | dias 1 a 7 |
| `na segunda semana` | dias 8 a 14 |
| `na terceira semana` | dias 15 a 21 |
| `na quarta semana` | dias 22 a 28 |
| `na ultima semana` | últimos 7 dias do mês |
| `na primeira quinzena` | dias 1 a 15 |
| `na segunda quinzena` | dia 16 ao fim do mês |

## Mês do ano
Meses individuais: `em janeiro`, `em fevereiro`, ..., `em dezembro`.
| Filtro | Meses |
|---|---|
| `no primeiro bimestre` | jan-fev |
| `no segundo bimestre` | mar-abr |
| `no terceiro bimestre` | mai-jun |
| `no quarto bimestre` | jul-ago |
| `no quinto bimestre` | set-out |
| `no sexto bimestre` | nov-dez |
| `no primeiro trimestre` | jan-mar |
| `no segundo trimestre` | abr-jun |
| `no terceiro trimestre` | jul-set |
| `no quarto trimestre` | out-dez |
| `no primeiro semestre` | jan-jun |
| `no segundo semestre` | jul-dez |
