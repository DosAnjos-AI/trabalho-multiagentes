---
regra_id: 195
arquivo_regra: regra_195.gobr
hash_regra_sha256: cacb426897a2da433ee3c7da81d4f955a6648679a2a132eb1517d9c683d375df
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2645
tokens_saida: 291
custo_usd: 0.004100
tempo_segundos: 5.02
timestamp: 2026-11-13T19:44:23-03:00
---

Os vendedores de televendas habilitados atendem os clientes seguindo esta prioridade: primeiro, não agendamos pessoas físicas, clientes com situação baixada na Receita Federal ou clientes que compraram com qualquer vendedor da empresa nos últimos 7 dias.

Entre os demais, quem comprou com qualquer vendedor da empresa entre 7 e 30 dias atrás é atendido a cada 21 dias. Quem nunca comprou com a empresa é atendido a cada 14 dias; quem fez uma única compra com a empresa, a cada 21 dias.

Depois, considerando as compras feitas somente com o vendedor que cuida do cliente, atendemos a cada 21 dias quem comprou entre 31 e 60 dias atrás e a cada 7 dias quem comprou entre 61 e 90 dias atrás. Todo o resto é atendido a cada 14 dias. Se um cliente se encaixar em mais de uma dessas situações, vale a primeira.
