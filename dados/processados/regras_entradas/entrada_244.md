---
regra_id: 244
arquivo_regra: regra_244.gobr
hash_regra_sha256: f677bd3951f17bac678df1e9c5560fd735b90dc36dd5dff2983931276dfe1a3c
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2595
tokens_saida: 345
custo_usd: 0.004320
tempo_segundos: 6.15
timestamp: 2026-11-13T19:43:15-03:00
---

No televendas, trabalhamos com todos os vendedores habilitados. Para cada cliente, seguimos esta ordem: primeiro, não agendamos clientes que são filiais nem clientes inadimplentes. Se o cliente se encaixar em mais de uma situação, vale a primeira.

Os clientes que ainda não compraram com o próprio vendedor são atendidos a cada 14 dias. Quem fez uma única compra com esse vendedor é atendido a cada 7 dias. Para os clientes ativos em relação ao próprio vendedor, cuja frequência histórica de compra seja menor que 8 dias, seguimos essa frequência, respeitando o mínimo de 5 e o máximo de 7 dias.

Depois, para os demais clientes, consideramos o tempo desde a última compra com o próprio vendedor: entre 8 e 30 dias, atendemos a cada 14 dias; entre 31 e 60 dias, a cada 7 dias; e, se não compraram com ele nos últimos 60 dias, a cada 14 dias.
