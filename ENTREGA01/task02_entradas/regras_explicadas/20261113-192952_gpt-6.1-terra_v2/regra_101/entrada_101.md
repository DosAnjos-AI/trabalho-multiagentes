---
regra_id: 101
arquivo_regra: regra_101.gobr
hash_regra_sha256: ef4ce6fc8cb1872f2c13f73e46859ef8e8651e1db78973d1d379608ef3b183fb
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2829
tokens_saida: 309
custo_usd: 0.004374
tempo_segundos: 5.32
timestamp: 2026-11-13T19:46:09-03:00
---

Dividimos o atendimento entre todos os vendedores de televendas, os vendedores de campo da capital e os do interior. Na capital ficam todos os vendedores de campo, exceto os de códigos 17, 18 e 13; no interior ficam os vendedores 17, 18 e 13.

No televendas, atendemos a cada 7 dias os clientes ativos para o próprio vendedor e os clientes sem venda. Os clientes inativos para o próprio vendedor são atendidos a cada 30 dias.

Na capital, atendemos a cada 7 dias os clientes ativos para o próprio vendedor. Os inativos para esse vendedor que estão em dia são atendidos a cada 14 dias, e os inadimplentes não são agendados. Os clientes sem venda são atendidos a cada 14 dias.

No interior, atendemos a cada 14 dias os clientes ativos para o próprio vendedor. Os inativos para esse vendedor que estão em dia são atendidos a cada 30 dias, e os inadimplentes não são agendados. Os clientes sem venda são atendidos a cada 30 dias.
