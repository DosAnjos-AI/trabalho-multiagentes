---
regra_id: 201
arquivo_regra: regra_201.gobr
hash_regra_sha256: 0437aa8a5270bd495162053555ef6a50fd7c41da153bd9b617f21a09548a55e1
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2770
tokens_saida: 439
custo_usd: 0.004965
tempo_segundos: 6.65
timestamp: 2026-11-13T19:47:22-03:00
---

Os vendedores de televendas habilitados atendem seus clientes seguindo esta ordem de prioridade: primeiro, não agendamos clientes com situação baixada na Receita Federal, inadimplentes, bloqueados ou que sejam filiais.

Entre os demais, atendemos a cada 7 dias os clientes que ainda não compraram com seu vendedor. Os que não compraram com ele nos últimos 90 dias são atendidos a cada 28 dias. Quem está cadastrado há 60 dias e fez uma única compra com seu vendedor é atendido a cada 30 dias.

Para os demais, considerando as compras com o próprio vendedor, quem comprou nos últimos 30 dias e tem intervalo histórico entre compras menor que 30 dias é atendido a cada 30 dias. Quem comprou nos últimos 30 dias e tem intervalo histórico entre compras menor que 90 dias também é atendido a cada 30 dias. Quem comprou entre 30 e 60 dias atrás é atendido a cada 10 dias, e quem comprou entre 61 e 90 dias atrás, a cada 14 dias.

Quando um cliente se encaixa em mais de uma dessas situações, vale a primeira. Todos os demais não são agendados.
