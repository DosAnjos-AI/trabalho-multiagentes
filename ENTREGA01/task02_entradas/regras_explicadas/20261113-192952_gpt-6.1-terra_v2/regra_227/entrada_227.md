---
regra_id: 227
arquivo_regra: regra_227.gobr
hash_regra_sha256: db66e0f1e61631b2b78aeecb69baf893e3396b4da576a94fa29ddb4d62052212
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2532
tokens_saida: 382
custo_usd: 0.004442
tempo_segundos: 6.67
timestamp: 2026-11-13T19:38:00-03:00
---

Os vendedores de televendas habilitados atendem seus clientes, com exceção dos vendedores de códigos 518, 519, 521, 626, 503, 624 e 623. Para decidir o atendimento, seguimos a ordem abaixo: quando um cliente se encaixa em mais de uma situação, vale a primeira.

Primeiro, os clientes cuja data da rota foi há 7 dias devem ser atendidos a cada 1 dia, de forma fixa. Depois, não agendamos os clientes que compraram com qualquer vendedor da empresa nos últimos 30 dias. Para quem nunca comprou com a empresa, o atendimento é a cada 60 dias. Para quem comprou com qualquer vendedor da empresa entre 30 e 90 dias atrás, atendemos a cada 15 dias.

Todos os demais clientes são atendidos a cada 10 dias. Quem não for contemplado por essas situações não deve ser agendado.
