---
regra_id: 183
arquivo_regra: regra_183.gobr
hash_regra_sha256: 3827edd4f7f6580076a5aa3cf4007d92e296f65f6e5ed6d8149bfad457eae3aa
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2578
tokens_saida: 508
custo_usd: 0.005118
tempo_segundos: 6.86
timestamp: 2026-11-13T19:36:36-03:00
---

Os vendedores de televendas são 522, 353, 519, 520 e 523. Primeiro, não agendamos os clientes inadimplentes. Para os demais, seguimos a ordem abaixo quando um cliente se encaixa em mais de uma situação.

Quem ainda não comprou com a empresa é atendido a cada 21 dias. Para clientes ativos com seu vendedor e com intervalo histórico de compras menor que 30 dias, seguimos esse intervalo, com mínimo de 5 e máximo de 30 dias.

Para clientes ativos com seu vendedor e com intervalo histórico de compras maior que 30 dias, atendemos a cada 14 dias. Esse mesmo prazo de 14 dias também vale para os que, além dessas condições, tiveram atividade do vendedor nos últimos 30 dias.

Por fim, clientes inativos com a empresa são atendidos a cada 21 dias.
