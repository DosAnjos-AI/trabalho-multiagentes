---
regra_id: 058
arquivo_regra: regra_058.gobr
hash_regra_sha256: 5388eba33dd17fb0b96caaabc77de49fe5e42ff8050be73150cab63f497a59d8
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2573
tokens_saida: 274
custo_usd: 0.003943
tempo_segundos: 4.20
timestamp: 2026-11-13T19:35:27-03:00
---

Os vendedores de televendas e os vendedores de campo atendem, cada um, seus próprios clientes fixos. Em cada equipe, seguimos a ordem abaixo: quando um cliente se encaixa em mais de uma situação, vale a primeira.

No televendas, atendemos os clientes inadimplentes a cada 14 dias. Para os demais, usamos o intervalo do histórico de vendas, limitado a no máximo 14 dias.

No campo, atendemos os clientes adimplentes a cada 7 dias. Os inadimplentes que estão ativos com seu próprio vendedor são atendidos a cada 14 dias; os inadimplentes que estão inativos com seu próprio vendedor, a cada 60 dias. Depois dessas situações, os clientes sem venda são atendidos a cada 14 dias.
