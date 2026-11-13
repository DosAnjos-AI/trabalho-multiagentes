---
regra_id: 070
arquivo_regra: regra_070.gobr
hash_regra_sha256: 6cb9bd75da2cde51ebd6b429b35148caab3c36a6bf31149598cc20c51b7dae75
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2661
tokens_saida: 247
custo_usd: 0.003896
tempo_segundos: 4.23
timestamp: 2026-11-13T19:38:53-03:00
---

Trabalhamos com todos os vendedores de televendas e todos os vendedores de campo. No televendas, cada vendedor cuida dos seus clientes fixos. Seguimos a ordem abaixo caso um cliente se encaixe em mais de uma situação.

No televendas, não agendamos os clientes que estão inativos para o vendedor e inadimplentes. Atendemos a cada 14 dias os clientes ativos para o vendedor e, a cada 30 dias, os inativos para o vendedor que estão em dia e os clientes sem venda. Preferimos fazer esses atendimentos em dias úteis.

Para os vendedores de campo, atendemos a cada 14 dias os clientes ativos para o vendedor e a cada 30 dias os inativos para o vendedor, com preferência por dias úteis. Não agendamos os clientes sem venda.
