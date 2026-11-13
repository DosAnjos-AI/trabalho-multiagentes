---
regra_id: 228
arquivo_regra: regra_228.gobr
hash_regra_sha256: f9de548ddf01743b402eceb1dbf15bf969118a38f07bd83e87cb674bdfe69406
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gemini-4-carbon
fornecedor: gemini
temperatura: 0.3
tokens_entrada: 2631
tokens_saida: 3928
custo_usd: 0.044542
tempo_segundos: 44.49
timestamp: 2026-11-13T18:35:14-03:00
---

No nosso atendimento, trabalhamos com todos os vendedores do televendas que estão habilitados no sistema e organizamos os contatos com os clientes dessa equipe seguindo uma ordem de prioridade, em que cada cliente recebe apenas o tratamento da primeira situação em que se encaixar.

Primeiro, o cliente que ainda nunca comprou com o vendedor dele é atendido a cada 28 dias. Em seguida, quem fez uma única compra com esse vendedor é atendido a cada 21 dias.

Depois, entre os que sobram, olhamos quem comprou com o próprio vendedor nos últimos 90 dias: se for cliente da curva C considerando a empresa toda, fazemos o atendimento a cada 7 dias; já os demais que compraram com o próprio vendedor nos últimos 90 dias são atendidos a cada 14 dias.

Para quem não entrou nos casos anteriores e fez a última compra com o vendedor dele entre 91 e 180 dias atrás, o atendimento acontece a cada 28 dias. Por fim, todo o resto dos clientes da equipe é atendido a cada 45 dias.
