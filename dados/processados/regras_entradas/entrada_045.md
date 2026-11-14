---
regra_id: 045
arquivo_regra: regra_045.gobr
hash_regra_sha256: 111568d128c667fdd5819c5702928f371993c758ef503d5a7fb19498fd4d2a95
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2510
tokens_saida: 252
custo_usd: 0.003770
tempo_segundos: 4.81
timestamp: 2026-11-13T19:31:49-03:00
---

Cada vendedor atende seus clientes fixos. Separamos a Sandra, de código 945, dos demais vendedores. Os clientes dela são atendidos semanalmente.

Para os clientes dos outros vendedores, damos prioridade aos que estão inativos em relação ao próprio vendedor e inadimplentes: eles são atendidos a cada 30 dias. Os demais clientes inativos em relação ao próprio vendedor são atendidos a cada 7 dias, e todos os outros, a cada 14 dias.

Em todos os casos, damos preferência aos dias úteis.
