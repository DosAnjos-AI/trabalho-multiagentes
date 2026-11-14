---
regra_id: 140
arquivo_regra: regra_140.gobr
hash_regra_sha256: 608502f120b13ab385e337d6785c87c49d8de4934ab02af4b5664595ad96a05f
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 4014
tokens_saida: 826
custo_usd: 0.008144
tempo_segundos: 11.64
timestamp: 2026-11-13T19:50:06-03:00
---

Os vendedores do televendas cuidam dos seus clientes fixos, separados pelos códigos de rota: 8, 9, 10 e 11 ficam juntos; 3 e 4 ficam juntos; e 5, 6 e 7 ficam cada um em seu grupo. Um cliente que tenha códigos de mais de um desses grupos pode aparecer nos grupos correspondentes.

Para toda a equipe, não agendamos clientes que sejam pessoa física, filial ou estejam inadimplentes. Também não agendamos, em nenhum desses grupos de rotas, clientes que receberam visita nos últimos 3 dias.

Nos grupos de rotas, atendemos semanalmente quem ainda não comprou com o próprio vendedor, quem comprou com esse vendedor nos últimos 21 dias, quem teve a última compra com qualquer vendedor da empresa entre 21 e 41 dias ou entre 41 e 90 dias, e quem não comprou com nenhum vendedor da empresa nos últimos 90 dias.

Para as rotas 8, 9, 10 e 11, o atendimento semanal não tem dia fixo definido. Nas rotas 3 e 4, ele é fixo na segunda; na rota 5, na terça; na rota 6, na quarta; e na rota 7, na sexta.

Depois desses tratamentos, os demais clientes da equipe também são atendidos semanalmente, sem dia fixo definido.
