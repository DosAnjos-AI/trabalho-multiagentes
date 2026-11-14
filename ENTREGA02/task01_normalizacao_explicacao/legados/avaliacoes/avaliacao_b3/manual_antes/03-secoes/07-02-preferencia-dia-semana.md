# Preferência de dia da semana (manual 7.2, 7.3.2, 7.3.3, 7.3.5; p.38-41)

Valor numérico por dia: 0 = não deve visitar; 1 = menor preferência; 2 = preferência normal; 3 = maior preferência.

## Dias com valor 2
```
parametros "mensal alberto com preferencia":
     da carteira("carteira fixa")
     quando inatividade de 90 dias
     frequencia mensal()
     preferencia na segunda e na terça
```
Segunda e terça = 2; os demais dias = 0.

## Intensidades por dia
```
parametros "mensal alberto com intensidades":
     da carteira("carteira fixa")
     quando inatividade de 90 dias
     frequencia mensal()
     preferencia
           maior na segunda e
           menor na terça e
           normal na quinta e
           na sexta-feira e
           menor no sábado
```
Resultado: segunda = 3; quinta e sexta = 2; terça e sábado = 1; quarta e domingo = 0.
Modificadores: `maior` = 3; `normal` (ou sem modificador) = 2; `menor` = 1.

## Outras formas
- `preferência nos dias úteis`: 2 de segunda a sexta.
- `preferência do historico ou remover`: do histórico de visitas, ou remove.
- `preferência do historico ou nos dias uteis`.
- Padrão sem preferência: 1 de segunda a sexta, 0 em sábado e domingo.
