---
regra_id: 232
arquivo_regra: regra_232.gobr
hash_regra_sha256: 46a66834eb61d23bf1054281b6221200e6fedfc883a17beceafd0558e7683597
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2575
tokens_saida: 418
custo_usd: 0.004665
tempo_segundos: 7.81
timestamp: 2026-11-13T19:40:41-03:00
---

Os vendedores de televendas habilitados atendem seus clientes. Primeiro, não agendamos clientes que sejam filiais nem clientes inadimplentes. Entre os demais, atendemos a cada 21 dias os que nunca compraram com a empresa.

Depois, para quem comprou com seu próprio vendedor nos últimos 29 dias, seguimos o histórico, com intervalo mínimo de 14 dias e máximo de 30 dias. Quem comprou com esse vendedor entre 30 e 59 dias atrás é atendido a cada 21 dias; o mesmo vale para quem comprou entre 60 e 89 dias atrás. Todos os demais também são atendidos a cada 21 dias.
