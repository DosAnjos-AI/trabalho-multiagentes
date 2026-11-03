# Conflito, semana pivot e roteirização (manual 7.3.8-7.3.10, 7.5; p.42-45)

## Evitar choque entre televendas e campo
```
parametros "televendas sem choque com campo":
     da carteira("carteira televendas")
     quando inatividade de 90 dias
     frequencia do vendedor ou de qualquer vendedor ou de 35 dias
     preferência do historico ou nos dias uteis
     sem choque na carteira("carteira campo")
```
A preferência de dias dos televendas não coincide com a do campo para os mesmos clientes. Refinamento:
```
sem choque na rota e na pasta do time("time maria")
```
- `na rota`: só clientes roteirizáveis do time.
- `fora da rota`: só clientes não roteirizáveis.
- `na pasta`: só clientes dentro da mesma pasta dos vendedores.

## Semana pivot (restrito)
```
parametros "pivot segunda semana":
     da carteira("carteira televendas")
     quando inatividade de 90 dias
     frequencia do vendedor ou de 35 dias
     restrito a partir da segunda semana
     preferência do historico ou nos dias uteis
```
Cliente só aparece na agenda a partir da segunda segunda-feira do mês.

| Regra | Descrição |
|---|---|
| `a partir da primeira semana` | desde a primeira semana do mês |
| `a partir da segunda semana` | a partir da segunda semana |
| `a partir da terceira semana` | a partir da terceira |
| `a partir da quarta semana` | a partir da quarta |
| `ate a primeira semana` | somente na primeira semana |
| `ate a segunda semana` | até a segunda |
| `ate a terceira semana` | até a terceira |
| `ate a quarta semana` | até a quarta |

## Roteirização e fixação
```
parametros "campo roteirizavel fixo":
     da carteira("carteira campo")
     quando inatividade de 90 dias
     frequencia do vendedor ou de 35 dias
     preferência do historico ou nos dias uteis
     roteirizavel
     fixo
```
- `roteirizavel`: cliente entra na otimização de rota de visita presencial.
- `fixo`: parametrização marcada como fixa, restrição mais rígida de frequência e preferência para o gerador de agendas.
- Padrão sem as opções: não roteirizável e não fixo.
