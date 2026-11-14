---
regra_id: 221
arquivo_regra: regra_221.gobr
hash_regra_sha256: b2e50de1f8689e97b575cb6cf278a49699fe6f839d5958ef28e692a5556a58b1
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2679
tokens_saida: 416
custo_usd: 0.004759
tempo_segundos: 6.28
timestamp: 2026-11-13T19:37:35-03:00
---

Os vendedores de televendas habilitados atendem seus clientes com preferência pelos dias úteis e pelo sábado. Seguimos a ordem abaixo: se o cliente se encaixar em mais de uma situação, vale a primeira.

Quem ainda não comprou com seu vendedor é atendido a cada 21 dias. Quem fez uma única compra com esse vendedor e não comprou nos últimos 30 dias é atendido a cada 14 dias. Também atendemos a cada 14 dias quem comprou com seu vendedor nos últimos 30 dias, mas não nos últimos 21 dias, e quem está entre 31 e 60 dias sem comprar com ele.

Quem está entre 61 e 90 dias sem comprar com seu vendedor é atendido a cada 7 dias; quem está entre 91 e 360 dias sem comprar com ele é atendido a cada 28 dias.
