---
regra_id: 169
arquivo_regra: regra_169.gobr
hash_regra_sha256: 3b14794143b1e84bd2c4b44f4c61e555851867a71d70f51099f494f8af54faaa
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2850
tokens_saida: 907
custo_usd: 0.007385
tempo_segundos: 14.74
timestamp: 2026-11-13T19:44:18-03:00
---

Trabalhamos com o vendedor 341 e com duas equipes de televendas: uma formada pelos vendedores 203, 466, 314 e 291, e outra pelos vendedores 132, 232 e 145.

Para a primeira equipe, separamos os clientes em dia com os pagamentos que passam do vendedor 341 para ela por ruptura de compra em 7 dias, além dos prospects. Em outro grupo ficam os clientes fixos dessa equipe que estão em dia com os pagamentos e não tiveram venda em 7 dias. Quem já está no primeiro grupo não entra no segundo.

Para os clientes desses dois grupos, damos prioridade ao atendimento a cada 14 dias quando nunca compraram da empresa; quando compraram com qualquer vendedor da empresa nos últimos 30, 60 ou 90 dias; ou quando a última compra com qualquer vendedor da empresa foi entre 90 e 180 dias atrás.

Depois disso, para as duas equipes, não agendamos os clientes que compraram com qualquer vendedor da empresa nos últimos 7 dias nem os inadimplentes. Entre os que ainda não receberam um tratamento, não agendamos os clientes da primeira equipe; os demais clientes da segunda equipe atendemos a cada 14 dias.
