---
regra_id: 175
arquivo_regra: regra_175.gobr
hash_regra_sha256: 4e40284921ed06009c29caab3404cbbd7ac70312282a4c802e5f739707c9d0dc
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2662
tokens_saida: 526
custo_usd: 0.005292
tempo_segundos: 8.16
timestamp: 2026-11-13T19:42:37-03:00
---

Os vendedores habilitados do televendas cuidam dos seus clientes fixos. Para os clientes dos ramos de atividade 1, 2, 3, 4, 8, 18 e 23, seguimos a ordem abaixo: se um cliente se encaixar em mais de uma situação, vale a primeira.

Primeiro, não agendamos clientes que sejam filiais, que estejam inadimplentes ou que tenham comprado com seu próprio vendedor nos últimos 30 dias. Depois, atendemos a cada 14 dias os clientes ativos na empresa e, a cada 21 dias, os inativos na empresa.

Para quem ainda não tiver sido contemplado, atendemos a cada 21 dias os clientes que tiveram venda com a empresa no ano anterior e não tiveram venda no ano atual. Atendemos a cada 30 dias aqueles cuja última compra com o próprio vendedor ocorreu entre 2023-01-01 e 2023-12-31.

Todos os demais clientes dos vendedores do televendas não são agendados.
