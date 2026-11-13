---
regra_id: 155
arquivo_regra: regra_155.gobr
hash_regra_sha256: 6a66bbe3a811013d6043f02b788a87c1b46bea69fa27d2f2eec4d4f704ef9f81
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 3002
tokens_saida: 711
custo_usd: 0.006557
tempo_segundos: 9.53
timestamp: 2026-11-13T19:48:40-03:00
---

Os vendedores habilitados do televendas cuidam dos clientes atendidos pela equipe. Seguimos esta ordem: primeiro não agendamos pessoas físicas, filiais, clientes com situação baixada na Receita Federal, inadimplentes ou clientes que compraram com o próprio vendedor nos últimos 30 dias.

Entre os demais, atendemos a cada 7 dias os clientes que nunca compraram com a empresa e foram cadastrados há 30 dias. Os outros que nunca compraram com a empresa são atendidos a cada 21 dias. Depois, os clientes que fizeram uma única compra com o próprio vendedor são atendidos a cada 7 dias.

Em seguida, para os clientes cuja última compra com qualquer vendedor da empresa não foi entre 30 e 45 dias atrás, atendemos a cada 14 dias os de curva A, considerando a empresa toda, e a cada 28 dias os de curva B, também considerando a empresa toda. Os demais nessa mesma situação são atendidos a cada 45 dias, sem exigência de curva.

Depois disso, atendemos a cada 28 dias quem não teve a última compra com qualquer vendedor da empresa entre 46 e 60 dias atrás e, em seguida, a cada 21 dias quem não teve essa última compra entre 61 e 90 dias atrás. Todo o resto é atendido a cada 14 dias. Quando um cliente se encaixa em mais de uma dessas situações, vale a primeira que aparecer nessa ordem.
