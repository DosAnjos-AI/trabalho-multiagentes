---
regra_id: 221
arquivo_regra: regra_221.gobr
hash_regra_sha256: 10d5bc58321f31c69ac887abb55154319cdfc836c6f05e09634a66cf1361f549
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2678
tokens_saida: 398
custo_usd: 0.004668
tempo_segundos: 5.67
timestamp: 2026-11-14T20:56:17-03:00
---

Os vendedores habilitados do televendas atendem seus clientes com preferência por dias úteis e sábado. Seguimos a ordem abaixo quando um cliente se encaixa em mais de uma situação.

Quem ainda não comprou com o próprio vendedor deve ser atendido a cada 21 dias. Quem fez uma única compra com esse vendedor e não comprou com ele nos últimos 30 dias deve ser atendido a cada 14 dias.

Para os demais, quem comprou com o próprio vendedor nos últimos 30 dias, mas não nos últimos 21 dias, deve ser atendido a cada 14 dias. Quem está entre 31 e 60 dias sem comprar com ele também deve ser atendido a cada 14 dias; entre 61 e 90 dias, a cada 7 dias; e entre 91 e 360 dias, a cada 28 dias.
