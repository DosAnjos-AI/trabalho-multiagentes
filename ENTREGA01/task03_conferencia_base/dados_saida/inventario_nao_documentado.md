# Inventario de construcoes nao documentadas pelo manual

Uma linha por construcao, da mais usada para a menos usada (por quantidade de arquivos).
Valores concretos aparecem abstraidos: `"<texto>"`, `<N>`, `'<data>'`.
Nao e falha do arquivo: por decisao do Mestre, onde o manual nao documenta, a base sobrepoe o manual.

- Construcoes distintas: 34
- Ocorrencias (= achados `construcao_nao_documentada` no laudo): 301
- Soma das quantidades de arquivos por construcao: 172
- Arquivos com ao menos uma construcao nao documentada: 116 de 193

Ocorrencias superam a soma de arquivos porque o mesmo arquivo repete a mesma construcao em varios blocos.

## 1. `filtro: sem venda`

Arquivos: 45 | Ocorrencias: 61

Exemplo real (regra_007.gobr, linha 22):

```
quando sem venda
```

## 2. `filtro: sem vendas`

Arquivos: 21 | Ocorrencias: 28

Exemplo real (regra_023.gobr, linha 23):

```
quando sem vendas
```

## 3. `frequencia: frequencia do historico ou no minimo de <N> dias e no maximo de <N> dias`

Arquivos: 20 | Ocorrencias: 24

Exemplo real (regra_076.gobr, linha 51):

```
frequencia do historico ou no minimo de 5 dias e no maximo de 30 dias
```

## 4. `fonte: do time("<texto>", ...)`

Arquivos: 12 | Ocorrencias: 47

Exemplo real (regra_116.gobr, linha 16):

```
do time("televendas","campo")
```

## 5. `filtro: sem venda do vendedor`

Arquivos: 9 | Ocorrencias: 17

Exemplo real (regra_140.gobr, linha 58):

```
quando sem venda do vendedor
```

## 6. `filtro: e o cliente filial`

Arquivos: 8 | Ocorrencias: 8

Exemplo real (regra_116.gobr, linha 17):

```
quando e o cliente filial
```

## 7. `preferencia: do vendedor`

Arquivos: 6 | Ocorrencias: 22

Exemplo real (regra_053.gobr, linha 47):

```
preferencia do vendedor
```

## 8. `frequencia: frequencia do historico ou no maximo de <N> dias`

Arquivos: 6 | Ocorrencias: 8

Exemplo real (regra_058.gobr, linha 28):

```
frequencia do historico ou no maximo de 14 dias
```

## 9. `fonte: da carteira("<texto>", ...)`

Arquivos: 5 | Ocorrencias: 12

Exemplo real (regra_032.gobr, linha 38):

```
da carteira("sul_sudeste_centrooeste","norte_nordeste")
```

## 10. `filtro: é o cliente filial`

Arquivos: 4 | Ocorrencias: 4

Exemplo real (regra_129.gobr, linha 17):

```
quando é o cliente filial
```

## 11. `sem choque: sem choque no time("<texto>")`

Arquivos: 3 | Ocorrencias: 8

Exemplo real (regra_063.gobr, linha 42):

```
sem choque no time("time campo")
```

## 12. `filtro: frequencia historica de <N> dias`

Arquivos: 3 | Ocorrencias: 7

Exemplo real (regra_146.gobr, linha 22):

```
quando ramo de atividade igual("41","4","25") e frequencia historica de 7 dias
```

## 13. `filtro: inatividade global maior que <N> dias`

Arquivos: 3 | Ocorrencias: 3

Exemplo real (regra_126.gobr, linha 23):

```
quando inatividade global maior que 31 dias
```

## 14. `frequencia: frequencia do historico mais <N> dias ou no minimo de <N> dias e no maximo de <N> dias`

Arquivos: 3 | Ocorrencias: 3

Exemplo real (regra_191.gobr, linha 38):

```
frequencia do historico mais 3 dias ou no minimo de 14 dias e no maximo de 30 dias
```

## 15. `filtro: tem visita da empresa na semana anterior`

Arquivos: 2 | Ocorrencias: 4

Exemplo real (regra_186.gobr, linha 44):

```
quando data da rota ha 7 dias atras e tem visita da empresa na semana anterior e tem venda da empresa entre 7 dias e 30 dias
```

## 16. `filtro: sem venda da empresa`

Arquivos: 2 | Ocorrencias: 2

Exemplo real (regra_186.gobr, linha 26):

```
quando sem venda da empresa
```

## 17. `filtro: tem venda em <N> dias`

Arquivos: 2 | Ocorrencias: 2

Exemplo real (regra_151.gobr, linha 15):

```
quando tem venda em 60 dias
```

## 18. `frequencia: frequencia do historico mais <N> dias ou no maximo de <N> dias`

Arquivos: 2 | Ocorrencias: 2

Exemplo real (regra_200.gobr, linha 25):

```
frequencia do historico mais 5 dias ou no maximo de 30 dias
```

## 19. `filtro: cnae é igual("<texto>", ...)`

Arquivos: 1 | Ocorrencias: 9

Exemplo real (regra_131.gobr, linha 18):

```
quando cnae é igual("8411600","8424800")
```

## 20. `frequencia: frequencia do historico ou no maximo semanal()`

Arquivos: 1 | Ocorrencias: 6

Exemplo real (regra_071.gobr, linha 50):

```
frequencia do historico ou no maximo semanal()
```

## 21. `fonte: da segmentacao("<texto>") e da carteira("<texto>")`

Arquivos: 1 | Ocorrencias: 5

Exemplo real (regra_169.gobr, linha 31):

```
da segmentacao("televendas ruptura de fornecedor") e da carteira("televendas consumidor")
```

## 22. `sem choque: sem choque na rota com time("<texto>")`

Arquivos: 1 | Ocorrencias: 5

Exemplo real (regra_071.gobr, linha 44):

```
sem choque na rota com time("campo")
```

## 23. `filtro: tem venda no mes`

Arquivos: 1 | Ocorrencias: 3

Exemplo real (regra_190.gobr, linha 35):

```
quando curva A com a empresa e tem venda no mês
```

## 24. `clientes: clientes ruptura("<texto>" para "<texto>") de positivacao(entre <N> dias e <N> dias)`

Arquivos: 1 | Ocorrencias: 1

Exemplo real (regra_151.gobr, linha 19):

```
clientes ruptura("de campo" para "televendas") de positivacao(entre 7 dias e 60 dias)
```

## 25. `filtro: cadastrado ha <N> dias`

Arquivos: 1 | Ocorrencias: 1

Exemplo real (regra_171.gobr, linha 41):

```
quando unica compra com a empresa e cadastrado há 30 dias
```

## 26. `filtro: cnae do erp inicia com("<texto>", ...)`

Arquivos: 1 | Ocorrencias: 1

Exemplo real (regra_080.gobr, linha 13):

```
quando inativos para o vendedor e cnae do erp inicia com("03","47","27")
```

## 27. `filtro: data da rota hoje`

Arquivos: 1 | Ocorrencias: 1

Exemplo real (regra_076.gobr, linha 34):

```
quando data da rota hoje
```

## 28. `filtro: fora da recencia de venda do vendedor em <N> dias`

Arquivos: 1 | Ocorrencias: 1

Exemplo real (regra_198.gobr, linha 19):

```
quando unica compra com a empresa e fora da recencia de venda do vendedor em 30 dias
```

## 29. `filtro: id do cliente principal é diferente("<texto>")`

Arquivos: 1 | Ocorrencias: 1

Exemplo real (regra_203.gobr, linha 19):

```
quando cliente filial e id do cliente principal é diferente("36979")
```

## 30. `filtro: prospect`

Arquivos: 1 | Ocorrencias: 1

Exemplo real (regra_162.gobr, linha 26):

```
quando prospect
```

## 31. `filtro: recencia de positivacao global no ano passado`

Arquivos: 1 | Ocorrencias: 1

Exemplo real (regra_212.gobr, linha 45):

```
quando recencia de positivacao global no ano passado e recencia de positivacao global entre 180 dias e 360 dias
```

## 32. `filtro: tem venda da empresa no ano passado`

Arquivos: 1 | Ocorrencias: 1

Exemplo real (regra_189.gobr, linha 30):

```
quando não tem venda da empresa no ano e tem venda da empresa no ano passado
```

## 33. `filtro: tem venda no ano passado`

Arquivos: 1 | Ocorrencias: 1

Exemplo real (regra_186.gobr, linha 31):

```
quando tem venda no ano passado e recencia de positivacao entre 180 dias e 360 dias
```

## 34. `frequencia: frequencia do historico menos <N> dias ou no minimo de <N> dias e no maximo de <N> dias`

Arquivos: 1 | Ocorrencias: 1

Exemplo real (regra_245.gobr, linha 199):

```
frequencia do historico menos 1 dias ou no minimo de 1 dias e no maximo de 7 dias
```
