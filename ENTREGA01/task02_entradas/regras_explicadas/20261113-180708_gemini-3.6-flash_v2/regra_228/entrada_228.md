---
regra_id: 228
arquivo_regra: regra_228.gobr
hash_regra_sha256: f9de548ddf01743b402eceb1dbf15bf969118a38f07bd83e87cb674bdfe69406
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gemini-3.6-flash
fornecedor: gemini
temperatura: 0.3
tokens_entrada: 2636
tokens_saida: 2746
custo_usd: 0.012275
tempo_segundos: 14.88
timestamp: 2026-11-13T18:09:02-03:00
---

Nossa equipe de televendas, considerando todos os vendedores que estão ativos, atende os clientes de acordo com uma ordem clara de prioridade.

Primeiro, olhamos para os clientes que ainda estão no ciclo de vida de prospect com o próprio vendedor, estipulando que o atendimento seja a cada 28 dias. Logo depois, quem fez uma única compra com o seu vendedor passa a ser atendido a cada 21 dias.

Em seguida, vêm os clientes recentes. Para quem comprou nos últimos 90 dias e é curva C considerando a empresa toda, a frequência de atendimento é de 7 dias. Já para os demais clientes que também compraram nos últimos 90 dias, o contato deve ocorrer a cada 14 dias.

Para os clientes que estão com a última compra realizada no intervalo entre 91 e 180 dias, definimos o atendimento a cada 28 dias. Por fim, todos os demais clientes dessa equipe que sobram entram na frequência de 45 dias.
