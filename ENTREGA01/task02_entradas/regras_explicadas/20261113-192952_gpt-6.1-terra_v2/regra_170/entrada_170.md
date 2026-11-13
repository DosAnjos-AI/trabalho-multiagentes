---
regra_id: 170
arquivo_regra: regra_170.gobr
hash_regra_sha256: 215b3a0564eff22d68849fe47cccf17924ff4375ec302d3404524a071fd070f3
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2538
tokens_saida: 545
custo_usd: 0.005263
tempo_segundos: 8.50
timestamp: 2026-11-13T19:36:07-03:00
---

Todos os vendedores seguem a mesma prioridade de atendimento: se um cliente se encaixar em mais de uma situação, vale a primeira.

Primeiro, atendemos a cada 15 dias os clientes ativos para o próprio vendedor, do ramo DISTRIBUIDOR, que não compraram com ele nos últimos 60 dias. Depois, atendemos a cada 21 dias os que não compraram com nenhum vendedor da empresa nos últimos 10 dias e cujo intervalo histórico entre compras é menor que 7 dias.

Entre os que sobrarem, não agendamos os clientes ativos para o próprio vendedor do ramo DISTRIBUIDOR. Em seguida, atendemos a cada 15 dias os clientes ativos para o próprio vendedor que não compraram com ele nos últimos 30 dias. Os demais clientes ativos para o próprio vendedor não são agendados. Todo o resto é atendido uma vez por mês.
