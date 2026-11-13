---
regra_id: 145
arquivo_regra: regra_145.gobr
hash_regra_sha256: cf8120f991ad51145363806c976809da5e278f7ceb92bd03a38fe68153320a31
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2784
tokens_saida: 431
custo_usd: 0.004939
tempo_segundos: 8.25
timestamp: 2026-11-13T19:42:00-03:00
---

Todos os vendedores habilitados no sistema participam do atendimento. Não agendamos clientes que sejam filiais.

Para os demais clientes, seguimos esta ordem: pessoas jurídicas que são prospects em relação ao próprio vendedor são atendidas a cada 10 dias. Depois, entre as pessoas jurídicas que ainda não compraram com seu vendedor, atendemos as do ramo 2 a cada 14 dias e as do ramo 1 a cada 7 dias.

Em seguida, atendemos a cada 14 dias as pessoas jurídicas adimplentes cuja última compra com o próprio vendedor foi entre 31 e 60 dias atrás. As pessoas jurídicas adimplentes que compraram com seu vendedor nos últimos 30 dias são atendidas a cada 21 dias. Já as adimplentes cuja última compra com esse vendedor foi entre 61 e 90 dias atrás são atendidas a cada 7 dias.

As demais pessoas jurídicas são atendidas a cada 21 dias. Se um cliente se encaixar em mais de uma dessas situações, vale a primeira que aparecer nessa ordem.
