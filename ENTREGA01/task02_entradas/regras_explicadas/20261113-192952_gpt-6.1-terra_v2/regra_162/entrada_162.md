---
regra_id: 162
arquivo_regra: regra_162.gobr
hash_regra_sha256: c426849477087f568935997b7ea4401acb32e51329e5da2582a52297d1651801
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2519
tokens_saida: 419
custo_usd: 0.004614
tempo_segundos: 6.60
timestamp: 2026-11-13T19:35:55-03:00
---

No televendas, consideramos todos os vendedores habilitados no sistema. Primeiro, não agendamos clientes que sejam pessoas físicas nem os inadimplentes.

Para os demais, seguimos esta ordem: os clientes prospect são atendidos a cada 14 dias; depois, os clientes inativos para o vendedor que cuida deles também são atendidos a cada 14 dias. Em seguida, os que não compraram nos últimos 45 dias são atendidos a cada 30 dias.

Para todo o resto, usamos o intervalo do histórico, respeitando o mínimo de 14 e o máximo de 45 dias entre atendimentos. Se o cliente se encaixar em mais de uma situação, vale a primeira dessa ordem.
