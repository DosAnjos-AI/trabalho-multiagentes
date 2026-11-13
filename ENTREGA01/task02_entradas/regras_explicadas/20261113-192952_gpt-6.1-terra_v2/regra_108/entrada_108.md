---
regra_id: 108
arquivo_regra: regra_108.gobr
hash_regra_sha256: 68f2ef443fa380c876329627fd219c0c3b573d62ca02e6e086b816a2f10699d1
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2816
tokens_saida: 580
custo_usd: 0.005716
tempo_segundos: 8.69
timestamp: 2026-11-13T19:44:47-03:00
---

No televendas, trabalhamos com todos os vendedores habilitados no sistema. Para os clientes deles, seguimos a ordem abaixo: quando um cliente se encaixa em mais de uma situação, vale a primeira.

Primeiro, não agendamos os clientes inadimplentes. Depois, atendemos a cada 7 dias quem nunca comprou com o próprio vendedor. Quem fez uma única compra com esse vendedor e é do ramo 37 é atendido a cada 21 dias; os demais que fizeram uma única compra com ele são atendidos a cada 7 dias.

Para quem tem frequência histórica de compra menor que 11 dias, o atendimento é a cada 7 dias. Depois, para os clientes do ramo 37 cuja última compra com o próprio vendedor foi entre 60 e 89 dias atrás, atendemos a cada 14 dias; se foi entre 11 e 59 dias atrás, atendemos a cada 21 dias.

Os clientes inativos em relação ao próprio vendedor são atendidos a cada 21 dias. Os que não compraram com esse vendedor nos últimos 90 dias são atendidos a cada 7 dias. Para todos os demais, o atendimento também é a cada 7 dias.
