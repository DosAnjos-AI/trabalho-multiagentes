---
regra_id: 128
arquivo_regra: regra_128.gobr
hash_regra_sha256: 7041767ef635dad5e8de6cb4c5ee3d29d6043aebcf6055d534ab84ef43c0a3d2
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 5173
tokens_saida: 640
custo_usd: 0.008373
tempo_segundos: 8.91
timestamp: 2026-11-13T19:49:54-03:00
---

No televendas, o vendedor 291 atende os clientes fixos dos vendedores externos 283 e 279; o 292, os dos externos 286 e 284; o 294, os dos externos 275 e 277; o 375, os dos externos 278 e 280; o 900, os dos externos 273 e 274; e o 901, os dos externos 282 e 276. Um mesmo cliente pode aparecer em mais de um desses grupos.

Para todos esses vendedores de televendas, primeiro não agendamos clientes com situação baixada na Receita Federal. Depois, para cada grupo de clientes dos externos atendido pelo respectivo vendedor de televendas, seguimos esta ordem: quem nunca comprou com a empresa é atendido a cada 7 dias; quem comprou com qualquer vendedor da empresa nos últimos 60 dias é atendido a cada 5 dias, a partir do dia 16 de cada mês; quem comprou com qualquer vendedor da empresa nos últimos 90 dias é atendido a cada 7 dias; e os demais desse grupo também são atendidos a cada 7 dias.

Em seguida, para os clientes desses vendedores de televendas que ainda não tenham recebido um tratamento, atendemos a cada 7 dias quem nunca comprou com a empresa, depois quem comprou com qualquer vendedor da empresa nos últimos 60 dias e depois quem comprou com qualquer vendedor da empresa nos últimos 90 dias. Também atendemos a cada 7 dias os demais que não pertençam a nenhum dos seis grupos de clientes dos externos. Os clientes que sobrarem depois disso não são agendados.
