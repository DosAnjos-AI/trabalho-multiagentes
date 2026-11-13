---
regra_id: 230
arquivo_regra: regra_230.gobr
hash_regra_sha256: d76249ed6acb39378e2b82ffefbbfac985453edfc1e165dde00c96cec5370795
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2620
tokens_saida: 390
custo_usd: 0.004570
tempo_segundos: 6.32
timestamp: 2026-11-13T19:40:26-03:00
---

Os vendedores de televendas cuidam dos seus clientes. Primeiro, não agendamos atendimento para os inadimplentes. Para os demais, seguimos a ordem abaixo: se o cliente se encaixar em mais de uma situação, vale a primeira.

Quem ainda não comprou com seu vendedor é atendido a cada 14 dias. Quem fez uma única compra com esse vendedor é atendido a cada 7 dias. Os clientes ativos para seu vendedor, com frequência histórica de compras inferior a 16 dias, são atendidos a cada 14 dias.

Quem fez a última compra com seu vendedor entre 16 e 45 dias atrás é atendido a cada 14 dias. Quem fez a última compra com ele entre 60 e 89 dias atrás é atendido a cada 7 dias. Por fim, quem não comprou com seu vendedor nos últimos 60 dias é atendido a cada 21 dias.
