---
regra_id: 139
arquivo_regra: regra_139.gobr
hash_regra_sha256: 9fa5fa4db8f9c3d2f3d702c19046da22c26f66ad33c020725160607bce9169dc
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2842
tokens_saida: 517
custo_usd: 0.005427
tempo_segundos: 7.61
timestamp: 2026-11-13T19:44:55-03:00
---

Os vendedores de televendas habilitados, exceto 10185 e 1824, cuidam da ativação de novos clientes. Os vendedores 10185 e 1824 cuidam da venda na base.

Nas duas equipes, não agendamos clientes inadimplentes ou bloqueados. Para 10185 e 1824, também não agendamos clientes que nunca compraram com a empresa.

Na ativação de novos clientes, seguimos esta ordem: quando o intervalo histórico de compras é menor que 31 dias, atendemos conforme esse intervalo, limitado a no máximo 30 dias. Se o intervalo histórico está entre 31 e 90 dias, atendemos a cada 21 dias. Todos os demais são atendidos a cada 30 dias.

Na venda na base, também seguimos a ordem: clientes cuja última compra com o próprio vendedor foi entre 45 e 90 dias atrás são atendidos a cada 30 dias; entre 91 e 180 dias, a cada 25 dias. Depois, os clientes inativos para o próprio vendedor são atendidos a cada 21 dias. Entre os que sobrarem, se o intervalo histórico de compras for menor que 45 dias, atendemos conforme esse intervalo, respeitando o mínimo de 40 e o máximo de 45 dias. Para os demais, ainda não definimos de quanto em quanto tempo atender.
