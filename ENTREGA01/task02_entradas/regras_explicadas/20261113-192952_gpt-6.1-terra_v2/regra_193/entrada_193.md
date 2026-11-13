---
regra_id: 193
arquivo_regra: regra_193.gobr
hash_regra_sha256: 09f4704e3d9dc3acbc79dcd90a3f3350bf773a69fce0c6e19c7c2eaae0686f41
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2769
tokens_saida: 410
custo_usd: 0.004819
tempo_segundos: 5.58
timestamp: 2026-11-13T19:36:42-03:00
---

Trabalhamos com os vendedores de televendas habilitados no sistema e os clientes fixos de cada um. Separamos esses clientes em dois grupos pelo ramo de atividade: no primeiro ficam os de códigos 30, 583, 33, 26, 42, 34, 7, 21, 2, 29, 43, 4, 40, 52, 20, 584, 110, 124, 39, 120, 75, 57, 240, 366, 470, 237, 58, 69, 242, 46, 298 e 56; no segundo ficam os de ramos diferentes desses. Um cliente não fica nos dois grupos.

Antes de definir a frequência, não agendamos clientes que sejam filiais, que estejam com situação baixada na Receita Federal ou que tenham data de rota futura do vendedor nos próximos 21 dias e tenham comprado com qualquer vendedor da empresa nos últimos 60 dias.

Entre os que sobrarem, atendemos a cada 14 dias os clientes do primeiro grupo que compraram com qualquer vendedor da empresa nos últimos 60 dias. Para os do segundo grupo que também compraram com qualquer vendedor da empresa nesse período, o atendimento é a cada 21 dias. Todos os demais clientes são atendidos a cada 7 dias.
