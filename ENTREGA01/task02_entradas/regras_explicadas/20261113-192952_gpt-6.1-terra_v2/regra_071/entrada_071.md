---
regra_id: 071
arquivo_regra: regra_071.gobr
hash_regra_sha256: 4bc279e2ff5f4c7fabfc8f8c63d029531a6ef6875a588c9dfb442b31d175095e
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 3272
tokens_saida: 861
custo_usd: 0.007577
tempo_segundos: 11.35
timestamp: 2026-11-13T19:45:58-03:00
---

Na Palmed, temos os vendedores de televendas ligados ao supervisor 2736, os ligados ao supervisor 2731, os vendedores 435, 261, 385, 276, 438, 63 e 164, todos os vendedores de televendas e todos os vendedores de campo. Para os grupos dos supervisores e para os vendedores identificados pelos códigos, consideramos os clientes fixos de cada vendedor. Um vendedor e seus clientes podem aparecer tanto em um desses grupos quanto no grupo geral de televendas; a entrada em um grupo não impede a participação em outro.

Seguimos a ordem das situações abaixo quando um cliente se encaixar em mais de uma. Para os clientes fixos dos grupos dos supervisores 2736 e 2731, se o cliente estiver inativo para o próprio vendedor e inadimplente, atendemos a cada 14 dias, de preferência em dias úteis. Para os demais clientes fixos do grupo do supervisor 2736, seguimos o histórico de atendimento, sem ultrapassar 7 dias entre atendimentos, com preferência por dias úteis e sábado. Para os demais do grupo do supervisor 2731, fazemos o mesmo, mas com preferência por dias úteis. Em todos esses casos, evitamos que o atendimento coincida com a rota da equipe de campo.

Para os clientes fixos dos vendedores 435, 261, 385, 276, 438, 63 e 164, os que estiverem inativos para o próprio vendedor e inadimplentes são atendidos a cada 14 dias, de preferência em dias úteis. Para os demais, seguimos o histórico, sem ultrapassar 7 dias entre atendimentos, de preferência em dias úteis e sábado. Também evitamos coincidência com a rota da equipe de campo.

Para os clientes dos vendedores de televendas em geral, os ativos para o próprio vendedor e adimplentes são atendidos conforme o histórico, sem ultrapassar 7 dias entre atendimentos, de preferência em dias úteis. Os ativos para o próprio vendedor e inadimplentes são atendidos a cada 14 dias, também de preferência em dias úteis. Para os inativos para o próprio vendedor e adimplentes, seguimos o histórico, sem ultrapassar 7 dias, de preferência de segunda a sexta. Para os inativos para o próprio vendedor e inadimplentes, atendemos a cada 30 dias, de preferência de segunda a sexta. Todos os demais clientes do televendas são atendidos conforme o histórico, sem ultrapassar 7 dias, de preferência de segunda a sexta.

Para todos os clientes da equipe de campo, o atendimento é semanal.
