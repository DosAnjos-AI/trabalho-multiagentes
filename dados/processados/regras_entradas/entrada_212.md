---
regra_id: 212
arquivo_regra: regra_212.gobr
hash_regra_sha256: b68152f82f20c50cdacae335aee8cefa543ecce1316e75f953b97f92f356157c
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2787
tokens_saida: 407
custo_usd: 0.004822
tempo_segundos: 5.94
timestamp: 2026-11-13T19:44:29-03:00
---

Os vendedores de televendas habilitados no sistema cuidam desses atendimentos. Seguimos a ordem abaixo: quando um cliente se encaixa em mais de uma situação, vale a primeira.

Primeiro, não agendamos clientes que tenham rota prevista para os próximos 7 dias, nem os que compraram com qualquer vendedor da empresa nos últimos 14 dias.

Para clientes cuja rota foi há 7 dias e que receberam visita da empresa na semana anterior, atendemos a cada 7 dias se a última compra com qualquer vendedor da empresa foi entre 14 e 30 dias atrás; se foi entre 31 e 60 dias atrás, atendemos a cada 20 dias.

Clientes que ainda não têm vendas são atendidos a cada 14 dias. Também atendemos a cada 14 dias os que compraram com qualquer vendedor da empresa no ano passado e cuja última compra foi entre 180 e 360 dias atrás.

Quem fez a última compra com qualquer vendedor da empresa entre 61 e 90 dias atrás é atendido a cada 7 dias. O mesmo vale para quem fez a última compra entre 91 e 180 dias atrás. Todos os demais clientes são atendidos a cada 7 dias.
