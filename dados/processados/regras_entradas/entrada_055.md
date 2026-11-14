---
regra_id: 055
arquivo_regra: regra_055.gobr
hash_regra_sha256: bcb0e0a02a1168a0f1a7ac89bd6642bdddd2b9a5040f0c31cab6b282c097e0a8
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2725
tokens_saida: 403
custo_usd: 0.004740
tempo_segundos: 6.59
timestamp: 2026-11-13T19:41:18-03:00
---

Atendemos os clientes fixos de cada vendedor. No televendas, participam todos os vendedores de televendas. No interior, atendem os vendedores 27, 35 e 34; na capital, todos os vendedores de campo, exceto 27, 35 e 34.

Para os clientes do televendas, seguimos esta ordem: os adimplentes são atendidos a cada 14 dias; depois, os inadimplentes ativos para o próprio vendedor, a cada 30 dias; em seguida, os clientes sem venda, a cada 30 dias; e os inadimplentes inativos para o próprio vendedor não são agendados. Se um cliente se encaixar em mais de uma dessas situações, vale a primeira.

Na capital, também seguimos a ordem: clientes sem venda são atendidos a cada 30 dias, depois os inadimplentes a cada 30 dias e todos os demais a cada 14 dias. No interior, todos os clientes são atendidos a cada 30 dias.
