---
regra_id: 200
arquivo_regra: regra_200.gobr
hash_regra_sha256: 9684df135094f823efd986dcb95c7a0b19b89e008b40f54d286c9c955124e89d
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2618
tokens_saida: 518
custo_usd: 0.005208
tempo_segundos: 7.68
timestamp: 2026-11-13T19:39:58-03:00
---

Os vendedores do televendas atendem seus clientes, com exceção do vendedor de código 1. Quando um cliente se encaixar em mais de uma situação, seguimos a primeira delas nesta ordem.

Os clientes que nunca compraram com a empresa são atendidos a cada 21 dias. Os que fizeram uma única compra com a empresa são atendidos a cada 10 dias. Para quem comprou com qualquer vendedor da empresa nos últimos 30 dias, usamos o intervalo do histórico de compras acrescido de 5 dias, limitado a no máximo 30 dias.

Depois, atendemos a cada 14 dias os clientes que compraram com o próprio vendedor nos últimos 30 dias. Quem comprou com qualquer vendedor da empresa entre 31 e 60 dias atrás é atendido a cada 7 dias, assim como quem comprou entre 61 e 90 dias atrás. Todos os demais clientes são atendidos a cada 21 dias.
