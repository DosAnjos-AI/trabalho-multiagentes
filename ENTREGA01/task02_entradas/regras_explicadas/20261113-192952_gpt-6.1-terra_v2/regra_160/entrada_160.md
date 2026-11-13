---
regra_id: 160
arquivo_regra: regra_160.gobr
hash_regra_sha256: 9dc5c53b3f2fa95e7a64d3d4286da2083e9a9816c04c6a50faf67c7071fe56c5
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 3261
tokens_saida: 598
custo_usd: 0.006251
tempo_segundos: 7.77
timestamp: 2026-11-13T19:48:48-03:00
---

Trabalhamos com os vendedores de televendas habilitados, exceto 2136, 2179, 2134 e 1865, e também com os vendedores 2136, 2179, 2134 e 1865. Cada um atende seus clientes. Quando um cliente se encaixa em mais de uma situação, seguimos a primeira situação na ordem abaixo.

Primeiro, para os clientes pessoa jurídica com data da rota no próximo 1 dia e cuja última visita ocorreu entre 4 e 3000 dias atrás, o atendimento é a cada 1 dia. Isso vale para quem ainda não comprou com o próprio vendedor, para quem comprou com ele entre 31 e 60 dias atrás ou entre 61 e 90 dias atrás, para quem está ativo para ele considerando 30 dias, para quem está inativo para ele e também para os demais clientes que atendam às condições da rota e da visita.

Depois disso, para pessoa jurídica que ainda não comprou com o próprio vendedor, atendemos a cada 7 dias quando o vendedor é 2136, 2179, 2134 ou 1865; com os demais vendedores de televendas habilitados, atendemos a cada 14 dias.

Ainda entre os clientes pessoa jurídica, quem comprou com o próprio vendedor entre 61 e 90 dias atrás é atendido a cada 7 dias; quem comprou entre 31 e 60 dias atrás, a cada 14 dias. Quem está ativo para o próprio vendedor considerando 30 dias é atendido a cada 14 dias, e quem está inativo para ele, a cada 21 dias.

Os clientes pessoa física são atendidos a cada 14 dias. Todo o resto também é atendido a cada 14 dias.
