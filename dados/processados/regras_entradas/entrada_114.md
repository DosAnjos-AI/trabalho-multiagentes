---
regra_id: 114
arquivo_regra: regra_114.gobr
hash_regra_sha256: 50a158921808fc10401a5e078a38061c8e0407b3ee842914d61c63ccf569a175
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 3089
tokens_saida: 493
custo_usd: 0.005554
tempo_segundos: 7.07
timestamp: 2026-11-13T19:47:49-03:00
---

Trabalhamos com os vendedores 39, 16, 40, 6 e 45 no interior. Na capital, entram todos os vendedores de campo, exceto 39, 16, 40, 6, 45 e 55. No televendas, consideramos todos os vendedores, exceto 4 e 54. Os vendedores 4, 54 e 55 têm atendimento separado. Em cada caso, seguimos a ordem abaixo: quem já recebeu um tratamento não passa para os seguintes.

Para o vendedor 4, atendemos todos os clientes a cada 15 dias, com preferência por dias úteis.

Para o vendedor 55, não agendamos clientes cuja última compra com qualquer vendedor da empresa tenha ocorrido entre 0 e 30 dias atrás. Todos os demais são atendidos a cada 14 dias.

Para o vendedor 54, primeiro não agendamos clientes cuja última compra com qualquer vendedor da empresa tenha ocorrido entre 0 e 30 dias atrás. Também não agendamos os clientes bloqueados. Todos os demais são atendidos a cada 14 dias.

No interior, não agendamos clientes que estejam inativos para o próprio vendedor e inadimplentes. Todos os demais são atendidos a cada 30 dias, com preferência por dias úteis.

Na capital, não agendamos clientes que estejam inativos para o próprio vendedor e inadimplentes. Os ativos para o próprio vendedor que estejam inadimplentes são atendidos a cada 30 dias. Todos os demais são atendidos a cada 14 dias. Nos dois casos, preferimos dias úteis.

No televendas, atendemos os clientes ativos para o próprio vendedor a cada 15 dias e todos os demais a cada 7 dias, com preferência por dias úteis.
