---
regra_id: 206
arquivo_regra: regra_206.gobr
hash_regra_sha256: 79988d85b1a5178205a77f6ea8c10cd843a29f0912379ce026de308378548442
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2928
tokens_saida: 527
custo_usd: 0.005563
tempo_segundos: 7.70
timestamp: 2026-11-13T19:47:30-03:00
---

Os vendedores de televendas habilitados, exceto o vendedor 135, cuidam dos seus clientes fixos. Separamos esses clientes pelo tempo desde a última compra com qualquer vendedor da empresa: de um lado, os que compraram nos últimos 90 dias; de outro, os que compraram entre 91 e 180 dias atrás. Um cliente não fica nos dois grupos ao mesmo tempo. O vendedor 135 atende seus próprios clientes.

Antes de definir a frequência, não agendamos filiais nem clientes inadimplentes, tanto para os vendedores de televendas quanto para o vendedor 135. Os vendedores de televendas, exceto o 135, também não agendam clientes que nunca compraram com a empresa.

Para os clientes dos dois grupos e também para os clientes do vendedor 135, depois dessas exclusões, atendemos a cada 7 dias quem tem ramo de atividade com código 1, 2, 4 ou 12; a cada 15 dias quem tem código 3; e a cada 28 dias os demais.
