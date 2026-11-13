---
regra_id: 163
arquivo_regra: regra_163.gobr
hash_regra_sha256: 4b9ebdcbbc1f8eb2d6797107dbea2be29cf919366bee9b1922282f88f58dd82c
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2943
tokens_saida: 625
custo_usd: 0.006068
tempo_segundos: 8.49
timestamp: 2026-11-13T19:47:08-03:00
---

Os vendedores de televendas habilitados atendem os clientes fixos de cada um. Separamos esses clientes em dois grupos: um para os ramos de atividade 3, 6, 15 e 16 e outro para os demais ramos. Em cada grupo, seguimos a ordem abaixo: quem se encaixa em uma situação recebe aquele atendimento e não passa para as seguintes.

Para os clientes dos ramos 3, 6, 15 e 16, primeiro não agendamos quem comprou com qualquer vendedor da empresa nos últimos 30 dias. Depois, atendemos a cada 30 dias quem ainda não comprou com seu próprio vendedor. Quem fez uma única compra com seu vendedor e não comprou com nenhum vendedor da empresa nos últimos 60 dias é atendido a cada 21 dias. Quem fez a última compra com seu vendedor entre 31 e 60 dias atrás é atendido a cada 28 dias; se foi entre 61 e 90 dias atrás, a cada 14 dias. Todos os demais são atendidos a cada 21 dias.

Para os clientes dos outros ramos, atendemos a cada 7 dias quem ainda não comprou com seu próprio vendedor. Quem fez uma única compra com seu vendedor e não comprou com nenhum vendedor da empresa nos últimos 30 dias é atendido a cada 14 dias. Para quem fez a última compra com qualquer vendedor da empresa entre 7 e 30 dias atrás, seguimos o histórico, com intervalo mínimo de 7 e máximo de 30 dias. Quem fez a última compra com seu próprio vendedor entre 31 e 60 dias atrás é atendido a cada 14 dias; se foi entre 61 e 90 dias atrás, a cada 7 dias. Todos os demais são atendidos a cada 7 dias.
