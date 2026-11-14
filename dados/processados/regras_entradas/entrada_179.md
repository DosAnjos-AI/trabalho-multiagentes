---
regra_id: 179
arquivo_regra: regra_179.gobr
hash_regra_sha256: 4427fa706c03f145217ab78fb9a201bf9a74bb66d19e47900b58a56e79af33d3
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 3508
tokens_saida: 839
custo_usd: 0.007703
tempo_segundos: 10.53
timestamp: 2026-11-13T19:49:09-03:00
---

Os vendedores de televendas habilitados atendem os clientes fixos de cada um. Nós os dividimos pelo ramo de atividade em três grupos, sem sobreposição.

No grupo construtora ficam os ramos 10207004, 10301009, 10101016, 10301016, 10207001, 10301010, 10207002, 10301011, 10207003, 10301015, 10205001, 10205002 e 10204002. No grupo matcon ficam 10103004, 10202002, 10201004, 10201006, 10201009, 10201003, 10201011, 10201005, 10201002, 10201001, 10101013, 10103003, 10102004, 10202005, 10201007, 10205003, 10301001, 10101019, 10301019, 10301002, 10301007, 10301004, 10101006 e 10301006. O terceiro grupo reúne os clientes cujo ramo é diferente de todos esses códigos.

A ordem abaixo é a prioridade: se o cliente se encaixar em mais de uma situação, seguimos a primeira que se aplicar. Nos três grupos, quem nunca comprou com o próprio vendedor é atendido a cada 7 dias. Depois, para quem fez uma única compra com esse vendedor, o atendimento é a cada 14 dias no grupo construtora e a cada 7 dias nos outros dois grupos.

Em seguida, nos grupos matcon e de outros ramos, quem comprou com o próprio vendedor entre 7 e 30 dias atrás é atendido conforme o histórico, com intervalo mínimo de 7 e máximo de 30 dias. No grupo construtora, quem comprou com o próprio vendedor nos últimos 30 dias é atendido a cada 7 dias; quem não comprou com ele nesse período, a cada 14 dias.

Nas situações seguintes, consideramos as compras com qualquer vendedor da empresa. Para quem comprou entre 30 e 60 dias atrás, o atendimento é a cada 7 dias no grupo matcon e a cada 14 dias nos outros dois. Para quem comprou entre 60 e 89 dias atrás, é a cada 7 dias no matcon, 14 dias no construtora e 21 dias no grupo de outros ramos. Para quem comprou entre 90 e 179 dias atrás, é a cada 7 dias no matcon, 21 dias no construtora e 14 dias no grupo de outros ramos. Por fim, quem não comprou com nenhum vendedor da empresa nos últimos 180 dias é atendido a cada 14 dias nos grupos matcon e de outros ramos, e a cada 28 dias no construtora.
