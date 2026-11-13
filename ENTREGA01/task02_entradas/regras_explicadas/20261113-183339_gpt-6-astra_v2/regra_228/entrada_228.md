---
regra_id: 228
arquivo_regra: regra_228.gobr
hash_regra_sha256: f9de548ddf01743b402eceb1dbf15bf969118a38f07bd83e87cb674bdfe69406
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6-astra
fornecedor: openai
temperatura: 1.0 (padrao fixo do modelo)
tokens_entrada: 2508
tokens_saida: 291
custo_usd: 0.039630
tempo_segundos: 7.52
timestamp: 2026-11-13T18:35:22-03:00
---

A gente trabalha com todos os vendedores do televendas que estão habilitados no sistema. Para os clientes atendidos por eles, seguimos esta ordem de prioridade: quem ainda não comprou com o próprio vendedor recebe atendimento a cada 28 dias; depois, quem fez uma única compra com esse vendedor recebe atendimento a cada 21 dias. Cada cliente fica com o primeiro tratamento em que se encaixar, sem passar para os seguintes.

Dos clientes restantes, quem comprou com qualquer vendedor da empresa nos últimos 90 dias e está na curva c, considerando a empresa toda, recebe atendimento a cada 7 dias. Os demais que compraram com qualquer vendedor da empresa nos últimos 90 dias recebem atendimento a cada 14 dias, sem outra exigência de curva. Depois, quem fez a última compra com qualquer vendedor da empresa entre 91 e 180 dias atrás recebe atendimento a cada 28 dias. Todos os demais recebem atendimento a cada 45 dias.
