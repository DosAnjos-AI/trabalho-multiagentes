---
regra_id: 174
arquivo_regra: regra_174.gobr
hash_regra_sha256: 6172bf6fc521f952e3138f9b5f1dbbcb6a1a75920f6afbde49af6c914d13a7f5
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 3006
tokens_saida: 513
custo_usd: 0.005571
tempo_segundos: 7.37
timestamp: 2026-11-13T19:47:15-03:00
---

No televendas, todos os vendedores atendem seus clientes. Primeiro, não agendamos clientes inadimplentes nem os que constam como baixada na Receita Federal. Para os demais, seguimos a ordem abaixo: se um cliente se encaixar em mais de uma situação, vale a primeira.

Clientes que ainda não compraram com o próprio vendedor são atendidos a cada 14 dias. Os que fizeram uma única compra com esse vendedor e estão cadastrados há 60 dias são atendidos a cada 21 dias.

Para quem comprou com seu vendedor nos últimos 30 dias e tem frequência histórica de compra menor que 14 dias, seguimos essa frequência histórica, respeitando o mínimo de 10 e o máximo de 14 dias. Para quem comprou com seu vendedor nos últimos 60 dias e tem frequência histórica de compra menor que 30 dias, atendemos os clientes dos ramos 9 e 18 conforme a frequência histórica, com mínimo de 14 e máximo de 21 dias; os de outros ramos são atendidos a cada 28 dias.

Entre os demais que compraram com seu vendedor entre 21 e 60 dias atrás, os dos ramos 9 e 18 são atendidos a cada 14 dias, e os de outros ramos, a cada 21 dias. Entre os que compraram com seu vendedor entre 61 e 90 dias atrás, tanto os dos ramos 9 e 18 quanto os de outros ramos são atendidos a cada 14 dias. Por fim, os que não compraram com seu vendedor nos últimos 90 dias são atendidos a cada 21 dias.
