---
regra_id: 082
arquivo_regra: regra_082.gobr
hash_regra_sha256: 50e32e194b4858d4375667345f87646e73f391292615aa5f4d51e4327f7f15cc
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2512
tokens_saida: 219
custo_usd: 0.003607
tempo_segundos: 4.70
timestamp: 2026-11-13T19:33:24-03:00
---

Todos os vendedores atendem seus próprios clientes fixos. Seguimos esta ordem para definir o atendimento: clientes ativos para o seu vendedor e adimplentes são atendidos uma vez por semana; os ativos para o seu vendedor e inadimplentes, a cada 14 dias; os inativos para o seu vendedor e adimplentes, a cada 30 dias; e os inativos para o seu vendedor e inadimplentes não são agendados.

Os clientes sem vendas são atendidos a cada 30 dias. Se um cliente se encaixar em mais de uma dessas situações, vale a primeira. Para todos os atendimentos, damos preferência aos dias úteis.
