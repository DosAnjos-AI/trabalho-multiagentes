---
regra_id: 228
arquivo_regra: regra_228.gobr
hash_regra_sha256: f9de548ddf01743b402eceb1dbf15bf969118a38f07bd83e87cb674bdfe69406
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6-luna
fornecedor: openai
temperatura: 1.0 (padrao fixo do modelo)
tokens_entrada: 2508
tokens_saida: 1524
custo_usd: 0.001013
tempo_segundos: 16.44
timestamp: 2026-11-13T18:08:41-03:00
---

A gente atende os clientes dos vendedores do televendas que estão habilitados. Para clientes que ainda estão como prospect na relação com o próprio vendedor, a visita é a cada 28 dias. Se o cliente fez uma única compra com o vendedor que o atende, a visita é a cada 21 dias. Para quem teve compra nos últimos 90 dias e está na curva c considerando a empresa toda, a visita é a cada 7 dias. Os demais clientes com compra nos últimos 90 dias são atendidos a cada 14 dias.

Depois, clientes cuja compra mais recente foi entre 91 e 180 dias atrás são atendidos a cada 28 dias. Para todo o restante dos clientes desses vendedores, a visita é a cada 45 dias. Quando um cliente se encaixar em mais de uma dessas situações, vale a primeira que aparecer nessa ordem.
