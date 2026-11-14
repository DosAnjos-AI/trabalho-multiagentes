---
regra_id: 076
arquivo_regra: regra_076.gobr
hash_regra_sha256: 9f0ebfb8eb287c49f5cf31c04f251f00e4f1a0930a8557870d475bab34bf2f6d
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2625
tokens_saida: 333
custo_usd: 0.004290
tempo_segundos: 5.10
timestamp: 2026-11-13T19:44:38-03:00
---

Os vendedores de televendas habilitados no sistema atendem os clientes seguindo esta ordem de prioridade: primeiro, não agendamos os inadimplentes, os bloqueados, os inativos para a empresa nem os que compraram com qualquer vendedor da empresa nos últimos 20 dias.

Entre os demais, atendemos diariamente quem tem data de rota hoje. Depois, atendemos a cada 7 dias os clientes que nunca compraram com a empresa e, a cada 15 dias, os que fizeram uma única compra com a empresa.

Para quem comprou com qualquer vendedor da empresa nos últimos 30 dias e tem frequência histórica de compra menor que 30 dias, seguimos o intervalo histórico, respeitando o mínimo de 5 dias e o máximo de 30 dias. Quem comprou com qualquer vendedor da empresa entre 31 e 90 dias atrás é atendido a cada 15 dias. Todo o resto não é agendado.
