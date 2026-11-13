---
regra_id: 228
arquivo_regra: regra_228.gobr
hash_regra_sha256: f9de548ddf01743b402eceb1dbf15bf969118a38f07bd83e87cb674bdfe69406
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-5.4-mini
fornecedor: openai
temperatura: 1.0 (padrao fixo do modelo)
tokens_entrada: 2508
tokens_saida: 232
custo_usd: 0.002925
tempo_segundos: 2.53
timestamp: 2026-11-13T18:10:38-03:00
---

Nós trabalhamos com os vendedores do televendas que estão ativados no sistema, e cada um atende a própria carteira de clientes. Para esse time, a gente separa os clientes primeiro pelo estágio de compra e depois pela última compra feita com o vendedor.

Para quem ainda está no ciclo de vida prospect com o vendedor, a gente atende a cada 28 dias. Se o cliente já fez uma única compra com o vendedor, ele passa para atendimento a cada 21 dias. Para os clientes que têm compra recente, se a última compra foi nos últimos 90 dias e o cliente está na curva C com a empresa, o atendimento é a cada 7 dias. Se a última compra foi nos últimos 90 dias, mas sem separar por curva, o atendimento é a cada 14 dias, valendo para a curva A e B.

Depois disso, quem teve a última compra entre 91 dias e 180 dias entra na fase de cliente caminhando para inatividade e é atendido a cada 28 dias. E, por fim, todo o resto vai para resgate de cliente inativo, com atendimento a cada 45 dias.
