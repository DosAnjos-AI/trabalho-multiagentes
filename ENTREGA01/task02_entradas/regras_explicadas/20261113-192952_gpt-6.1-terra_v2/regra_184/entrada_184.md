---
regra_id: 184
arquivo_regra: regra_184.gobr
hash_regra_sha256: f89a5f91e4f82435bbdc9a8c256348ef79528424b935a6e0136545f63d676b6e
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 3002
tokens_saida: 611
custo_usd: 0.006057
tempo_segundos: 10.65
timestamp: 2026-11-13T19:48:07-03:00
---

Trabalhamos com duas equipes: uma com os vendedores de televendas habilitados, exceto os de códigos 39, 11, 63, 8, 49, 31, 29 e 10; e outra formada pelos vendedores desses mesmos códigos, que chamamos de equipe de São Paulo.

Para o televendas, seguimos a ordem a seguir quando um cliente se encaixa em mais de uma situação. Quem fez uma única compra com a empresa e comprou com seu vendedor neste mês é atendido a cada 5 dias. Para quem comprou com seu vendedor entre 1 e 7 dias atrás, seguimos o intervalo do histórico, respeitando o mínimo de 1 e o máximo de 5 dias, com preferência por segunda e terça. Entre 7 e 14 dias, seguimos o histórico, com intervalo mínimo de 7 e máximo de 12 dias; entre 14 e 30 dias, também seguimos o histórico, com mínimo de 14 e máximo de 28 dias. Quem comprou com seu vendedor entre 31 e 90 dias atrás é atendido a cada 14 dias, assim como quem comprou entre 91 e 180 dias atrás. Quem não comprou com seu vendedor nos últimos 360 dias é atendido a cada 21 dias.

Para a equipe de São Paulo, quem tem histórico de atendimento a cada 7, 14, 28, 56 ou 84 dias continua sendo atendido, respectivamente, a cada 7, 14, 28, 56 ou 84 dias, em dias fixos e com maior preferência pela segunda-feira.

Os demais clientes das duas equipes são atendidos a cada 30 dias.
