---
regra_id: 158
arquivo_regra: regra_158.gobr
hash_regra_sha256: 5290cc0a6255853f8dbee54ccfa51bda1de09ceb0be6eddfbc81dd1d68f360ba
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2742
tokens_saida: 413
custo_usd: 0.004807
tempo_segundos: 6.56
timestamp: 2026-11-13T19:44:03-03:00
---

Os vendedores do televendas cuidam dos seus clientes. Primeiro, não agendamos os inadimplentes nem os que estão com situação baixada na Receita Federal. Para os demais, seguimos a ordem abaixo: se o cliente se encaixar em mais de uma situação, vale a primeira.

Quem nunca comprou com a empresa é atendido a cada 30 dias. Quem fez uma única compra com a empresa, comprou com qualquer vendedor nos últimos 45 dias e está cadastrado há 120 dias é atendido a cada 21 dias.

Depois, quem comprou com qualquer vendedor nos últimos 45 dias e tem intervalo histórico entre compras menor que 30 dias é atendido a cada 14 dias. Quem comprou com qualquer vendedor nos últimos 120 dias e tem intervalo histórico entre compras menor que 120 dias é atendido a cada 30 dias.

Para quem ainda não se encaixou nas situações anteriores, atendemos a cada 30 dias os que fizeram a última compra com qualquer vendedor da empresa entre 45 e 70 dias atrás, e a cada 21 dias os que fizeram essa compra entre 71 e 120 dias atrás. Quem não comprou com nenhum vendedor da empresa nos últimos 120 dias é atendido a cada 30 dias.
