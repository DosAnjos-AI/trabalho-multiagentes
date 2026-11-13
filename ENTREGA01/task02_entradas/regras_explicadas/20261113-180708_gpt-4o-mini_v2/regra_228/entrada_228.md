---
regra_id: 228
arquivo_regra: regra_228.gobr
hash_regra_sha256: f9de548ddf01743b402eceb1dbf15bf969118a38f07bd83e87cb674bdfe69406
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-4o-mini
fornecedor: openai
temperatura: 1.0 (padrao fixo do modelo)
tokens_entrada: 2509
tokens_saida: 267
custo_usd: 0.000537
tempo_segundos: 3.53
timestamp: 2026-11-13T18:09:14-03:00
---

Os vendedores do televendas atendem a diversos grupos de clientes com base em suas atividades de compra e ciclo de vida. Para os clientes que estão no ciclo de vida de prospect com o vendedor, nós os visitamos a cada 28 dias, com o objetivo de ativar esse novo cliente. Uma vez que o cliente realiza uma única compra com seu vendedor, a frequência de atendimento passa a ser a cada 21 dias, pois queremos reforçar o relacionamento logo após a primeira compra.

Clientes que apresentam uma regularidade de compras, classificados na curva C, e que compraram nos últimos 90 dias recebem um atendimento a cada 7 dias. Aqueles que pertencem às curvas A e B, também com uma recência de compra dentro dos mesmos 90 dias, são atendidos a cada 14 dias. Para os clientes que estão caminhando para a inatividade, ou seja, que não compraram nos últimos 91 a 180 dias, nós aumentamos a frequência de visitas para a cada 28 dias, com o intuito de reengajá-los.

Finalmente, para resgatar clientes que estão inativos, que não compram há mais de 180 dias, nós estabelecemos um atendimento a cada 45 dias. Essa estratégia é vital para tentarmos trazê-los de volta para o ciclo de compras.
