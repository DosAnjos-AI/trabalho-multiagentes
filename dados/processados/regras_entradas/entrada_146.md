---
regra_id: 146
arquivo_regra: regra_146.gobr
hash_regra_sha256: 1655af5f6662050af6d2607955bcd0a1fbaa157d1054161c3bcaff6986fa3e85
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2582
tokens_saida: 642
custo_usd: 0.005792
tempo_segundos: 8.90
timestamp: 2026-11-13T19:42:08-03:00
---

Os vendedores de televendas habilitados no sistema atendem seus clientes seguindo esta ordem de prioridade: primeiro, não agendamos os inadimplentes. Depois, atendemos a cada 7 dias os clientes dos ramos 37, 43 e 15. Também atendemos a cada 7 dias os clientes dos ramos 41, 4 e 25 cujo histórico de compras indica frequência de 7 dias.

Quem ainda não comprou com seu vendedor é atendido a cada 30 dias. Também atendemos a cada 30 dias quem fez uma única compra com seu vendedor e comprou nos últimos 30 dias.

Para os demais, quem tem frequência histórica de compra menor que 21 dias é atendido a cada 21 dias. Quem comprou com seu vendedor entre 30 e 45 dias atrás também é atendido a cada 21 dias. Quem não comprou com seu vendedor nos últimos 46 dias é atendido a cada 45 dias. Se o cliente se encaixar em mais de uma dessas situações, vale a primeira na ordem apresentada.
