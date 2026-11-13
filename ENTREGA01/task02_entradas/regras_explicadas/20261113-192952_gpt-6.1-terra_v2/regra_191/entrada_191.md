---
regra_id: 191
arquivo_regra: regra_191.gobr
hash_regra_sha256: 2fc7c5eeebf66435fda575e7a963606923dafa47c409c48a992bd9b40925b72e
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2569
tokens_saida: 406
custo_usd: 0.004599
tempo_segundos: 6.64
timestamp: 2026-11-13T19:42:50-03:00
---

O atendimento é feito pelos vendedores de televendas habilitados. Primeiro, não agendamos clientes com situação baixada na Receita Federal nem clientes inadimplentes.

Para os demais, seguimos esta ordem: clientes que nunca compraram com a empresa são atendidos a cada 21 dias. Depois, quem comprou com o próprio vendedor nos últimos 7 dias também é atendido a cada 21 dias. Quem comprou com esse vendedor nos últimos 30 dias é atendido conforme o intervalo habitual entre suas compras, acrescido de 3 dias, respeitando o mínimo de 14 e o máximo de 30 dias.

Em seguida, quem comprou com o próprio vendedor nos últimos 45 dias é atendido a cada 7 dias, assim como quem comprou com ele nos últimos 60 dias. Todos os demais clientes também são atendidos a cada 7 dias. Se o cliente se encaixar em mais de uma dessas situações, vale a primeira.
