---
regra_id: 056
arquivo_regra: regra_056.gobr
hash_regra_sha256: f29e5f5a314bb3105cc34dd6dbbc486f5f7f53f670a116b5a77cfe2ee082f5fc
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2716
tokens_saida: 357
custo_usd: 0.004501
tempo_segundos: 5.84
timestamp: 2026-11-13T19:38:48-03:00
---

Os vendedores 50 e 53 cuidam dos seus próprios clientes fixos. Para os clientes sem vendas, o atendimento é a cada 30 dias, respeitando a preferência do vendedor. Os demais clientes desses vendedores não devem ser agendados.

Todos os outros vendedores cuidam também dos seus respectivos clientes fixos. Para eles, seguimos esta ordem: clientes ativos para o próprio vendedor e adimplentes são atendidos a cada 14 dias; clientes inativos para o próprio vendedor e adimplentes, a cada 30 dias; clientes ativos para o próprio vendedor e inadimplentes, a cada 30 dias; e clientes inativos para o próprio vendedor e inadimplentes não são agendados. Depois dessas situações, os clientes sem vendas são atendidos a cada 30 dias. Nos atendimentos, respeitamos a preferência do vendedor.
