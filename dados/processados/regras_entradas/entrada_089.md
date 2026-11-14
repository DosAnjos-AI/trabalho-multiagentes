---
regra_id: 089
arquivo_regra: regra_089.gobr
hash_regra_sha256: 5d08e1f4a3eeb75c1393b48791b980bffd2101e3db9b91917d0f26bbcdf8b13f
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2492
tokens_saida: 247
custo_usd: 0.003727
tempo_segundos: 5.12
timestamp: 2026-11-13T19:33:31-03:00
---

Para os vendedores de televendas habilitados no sistema, atendemos primeiro os clientes que nunca compraram com a empresa a cada 7 dias. Em seguida, os clientes ativos para o próprio vendedor e adimplentes também são atendidos a cada 7 dias. Os demais clientes ativos para esse vendedor são atendidos a cada 14 dias.

Depois, os demais clientes adimplentes são atendidos a cada 7 dias, e todo o resto, a cada 14 dias. Quem já se encaixou em uma dessas situações segue o prazo indicado nela, sem passar para as seguintes.
