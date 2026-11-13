---
regra_id: 159
arquivo_regra: regra_159.gobr
hash_regra_sha256: 365f7c6401db0884130c088fc1ce1a73e22fbcaa658444a9e3fdd5991ad0b8bd
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2676
tokens_saida: 410
custo_usd: 0.004726
tempo_segundos: 6.48
timestamp: 2026-11-13T19:42:15-03:00
---

Trabalhamos com todos os vendedores. Para os vendedores 2095 e 2152, atendemos a cada 45 dias os clientes cujo faturamento total no ano com a empresa seja menor que R$ 10000 ou não esteja definido. Depois, atendemos a cada 15 dias os que tenham faturamento total no ano acima de R$ 30000. Todos os demais clientes desses vendedores são atendidos a cada 30 dias.

Para os vendedores 2150 e 2151, atendemos a cada 45 dias os clientes cujo faturamento total no ano com a empresa seja menor que R$ 5000 ou não esteja definido. Depois, atendemos a cada 15 dias os que tenham faturamento total no ano acima de R$ 20000. Todos os demais clientes desses vendedores são atendidos a cada 30 dias.

Essas condições têm prioridade para os vendedores indicados. Para os demais vendedores, os clientes ativos com o próprio vendedor são atendidos a cada 7 dias, e todo o resto a cada 15 dias.
