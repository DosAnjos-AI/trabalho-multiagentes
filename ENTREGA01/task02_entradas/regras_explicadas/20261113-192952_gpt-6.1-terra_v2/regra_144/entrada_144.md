---
regra_id: 144
arquivo_regra: regra_144.gobr
hash_regra_sha256: 7f1b52138ba2254ad91c7173f36408e57b653330d33330028d109d720606b674
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2883
tokens_saida: 942
custo_usd: 0.007593
tempo_segundos: 13.52
timestamp: 2026-11-13T19:41:51-03:00
---

Trabalhamos com todos os vendedores habilitados no sistema. Também temos as equipes de fabricantes, com os vendedores F, L e A; de segmentos de revendas/manutenção, com J; de consumidor final recorrente e de compra exporadica, ambas com LC; e de consumidor final de grande porte, com A. Assim, LC participa de duas equipes e A também.

Para os vendedores habilitados, seguimos a ordem abaixo quando um cliente se encaixa em mais de uma situação: vale o primeiro atendimento indicado. Quem ainda não comprou com a empresa é atendido a cada 14 dias. Depois, atendemos a cada 21 dias os clientes inadimplentes. Quem fez uma única compra com a empresa e está cadastrado há 30 dias é atendido a cada 28 dias.

Em seguida, quem comprou com seu próprio vendedor entre 31 e 60 dias atrás é atendido a cada 30 dias; quem comprou com ele entre 61 e 90 dias atrás, a cada 10 dias. Os clientes inativos considerando a empresa são atendidos a cada 21 dias.

Para os vendedores F, L, A e J, os clientes que compraram com seu próprio vendedor nos últimos 30 dias são atendidos a cada 21 dias. Para LC e A, esses clientes são atendidos a cada 28 dias. Como A participa dos dois conjuntos, para ele prevalece o atendimento a cada 21 dias nessa situação.
