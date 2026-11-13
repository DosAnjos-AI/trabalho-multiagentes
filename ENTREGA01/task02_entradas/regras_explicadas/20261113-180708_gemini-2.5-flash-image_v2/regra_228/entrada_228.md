---
regra_id: 228
arquivo_regra: regra_228.gobr
hash_regra_sha256: f9de548ddf01743b402eceb1dbf15bf969118a38f07bd83e87cb674bdfe69406
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gemini-2.5-flash-image
fornecedor: gemini
temperatura: 0.3
tokens_entrada: 2636
tokens_saida: 223
custo_usd: 0.001348
tempo_segundos: 2.05
timestamp: 2026-11-13T18:10:44-03:00
---

Aqui na empresa, a gente atende os clientes de televendas. Primeiro, separamos os clientes que ainda não compraram nada com o vendedor atual: esses são os nossos prospects e a gente vai entrar em contato com eles a cada 28 dias. Depois, pegamos os clientes que já fizeram uma única compra com o vendedor atual, e para esses a frequência de contato é de 21 dias.

Aí a gente olha os clientes que compraram nos últimos 90 dias. Se o cliente for de curva C com a empresa, a gente atende a cada 7 dias. Os clientes de curva A e B que também compraram nos últimos 90 dias são atendidos a cada 14 dias.

Para os clientes que estão caminhando para a inatividade, ou seja, que compraram entre 91 e 180 dias atrás, a gente define uma frequência de 28 dias. E para todos os outros clientes, que são os inativos, a frequência de contato é de 45 dias para tentar resgatá-los.
