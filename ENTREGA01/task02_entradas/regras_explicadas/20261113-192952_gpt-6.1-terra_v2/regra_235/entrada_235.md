---
regra_id: 235
arquivo_regra: regra_235.gobr
hash_regra_sha256: 899d1c3ed5bdabe3af0995900cf2be88a6ace508089f7cc131dd97020c60bc96
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 3211
tokens_saida: 848
custo_usd: 0.007451
tempo_segundos: 10.80
timestamp: 2026-11-13T19:48:58-03:00
---

Atendemos com os vendedores de televendas habilitados, exceto 503, 518, 519, 521, 623, 624 e 626. Também atendemos com os vendedores 519, 503, 518, 521, 623, 624 e 626; para 521, 623 e 624 há ainda um atendimento temporário específico. As situações abaixo seguem a ordem de prioridade: quando o cliente se encaixar em mais de uma, vale a primeira.

Primeiro, não agendamos clientes cuja situação na Receita Federal esteja baixada. Para os vendedores 519, 503, 518, 521, 623, 624 e 626, também não agendamos clientes com rota prevista para os próximos 7 dias ou que compraram com o próprio vendedor nos últimos 7 dias. Para os demais vendedores de televendas habilitados, não agendamos quem comprou com o próprio vendedor nos últimos 30 dias.

Depois desses impedimentos, para 521, 623 e 624, atendemos a cada 1 dia os clientes com 5% de crédito cuja rota foi há exatamente 14 dias. Para os demais vendedores de televendas habilitados, atendemos a cada 15 dias quem comprou com o próprio vendedor entre 30 e 90 dias atrás; todo o restante é atendido a cada 10 dias.

Para os vendedores 519, 503, 518, 521, 623 e 624 e 626, atendemos a cada 14 dias os clientes com 5% de crédito e rota nos últimos 7 dias. Em seguida, considerando compras com qualquer vendedor da empresa e sempre exigindo 5% de crédito, atendemos a cada 14 dias quem comprou entre 7 e 30 dias atrás ou entre 31 e 60 dias atrás; a cada 7 dias quem comprou entre 61 e 89 dias atrás; e a cada 14 dias quem comprou entre 90 e 179 dias atrás. Os demais clientes desses vendedores que tenham 5% de crédito são atendidos a cada 21 dias.

Em todos os atendimentos com intervalo definido, damos preferência aos dias úteis e ao sábado. Os clientes que não se encaixarem nas situações acima não são agendados.
