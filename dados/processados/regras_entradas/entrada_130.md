---
regra_id: 130
arquivo_regra: regra_130.gobr
hash_regra_sha256: dd15d2a262fb6890640137a53f441009c73915be05f7a31edd23a02c170a166d
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2643
tokens_saida: 327
custo_usd: 0.004278
tempo_segundos: 5.22
timestamp: 2026-11-13T19:41:38-03:00
---

Trabalhamos com todos os vendedores de televendas e todos os vendedores de campo, cada um com seus clientes.

No televendas, primeiro não agendamos pessoas físicas, inclusive as que não têm compras. Para os demais, atendemos a cada 7 dias os clientes ativos para o próprio vendedor. Os inativos para esse vendedor que estão em dia com os pagamentos são atendidos a cada 15 dias; os inadimplentes não são agendados. As pessoas jurídicas sem compras são atendidas a cada 20 dias. Quando um cliente se encaixa em mais de uma dessas situações, seguimos essa ordem.

Para os vendedores de campo, atendemos os clientes ativos para o próprio vendedor em intervalos fixos de 7 dias. Todos os demais são atendidos em intervalos fixos de 15 dias.
