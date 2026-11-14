---
regra_id: 226
arquivo_regra: regra_226.gobr
hash_regra_sha256: d0badb40e720e3e2c173e34ad2e607a65806fc91a63216a936cbfbb866781292
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2585
tokens_saida: 443
custo_usd: 0.004800
tempo_segundos: 7.20
timestamp: 2026-11-13T19:37:53-03:00
---

Os vendedores de televendas habilitados atendem seus clientes seguindo esta ordem: quando um cliente se encaixar em mais de uma situação, vale o primeiro atendimento aplicável.

Quem nunca comprou com a empresa deve ser atendido a cada 7 dias. Quem comprou com qualquer vendedor da empresa nos últimos 30 dias e fez uma única compra com a empresa deve ser atendido a cada 14 dias. Quem tem frequência histórica de compra de 30 dias e comprou com qualquer vendedor da empresa nos últimos 120 dias deve ser atendido a cada 28 dias.

Quem comprou com o próprio vendedor entre 20 e 30 dias atrás deve ser atendido no intervalo indicado pelo histórico, limitado a no máximo 60 dias. Quem está há mais de 120 dias sem comprar com qualquer vendedor da empresa deve ser atendido a cada 14 dias. Quem está há mais de 180 dias sem comprar com qualquer vendedor da empresa deve ser atendido a cada 28 dias, respeitando a prioridade das situações anteriores.
