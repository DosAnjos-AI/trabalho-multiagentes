---
regra_id: 106
arquivo_regra: regra_106.gobr
hash_regra_sha256: 6ca39a6ba723549c6588bb29216f260b4b29f79e74c442d0a9d948b0d580d5d4
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2770
tokens_saida: 374
custo_usd: 0.004640
tempo_segundos: 7.30
timestamp: 2026-11-13T19:43:31-03:00
---

Trabalhamos com todos os vendedores de televendas e todos os vendedores de campo, cada um atendendo seus clientes fixos. Quando um cliente se encaixar em mais de uma situação, seguimos a ordem abaixo.

No televendas, os clientes ativos para o próprio vendedor e em dia são atendidos a cada 10 dias; os ativos para o vendedor e inadimplentes, a cada 21 dias. Os inativos para o vendedor e em dia são atendidos a cada 14 dias; os inativos para o vendedor e inadimplentes, a cada 60 dias. Por último, atendemos os clientes sem venda a cada 30 dias.

No campo, atendemos os clientes ativos para o próprio vendedor e em dia a cada 30 dias e os inativos para o vendedor e em dia a cada 14 dias. Não agendamos os inadimplentes. Por último, atendemos os clientes sem venda a cada 30 dias.
