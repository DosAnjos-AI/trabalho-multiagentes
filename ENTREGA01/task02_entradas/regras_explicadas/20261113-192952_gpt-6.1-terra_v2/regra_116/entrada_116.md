---
regra_id: 116
arquivo_regra: regra_116.gobr
hash_regra_sha256: ff14e9f3d0aaffc95348ed22ed2c5a6befd7790b498ee3cc187eeeae378ffdbe
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2599
tokens_saida: 256
custo_usd: 0.003879
tempo_segundos: 4.54
timestamp: 2026-11-13T19:38:57-03:00
---

Trabalhamos com todos os vendedores de televendas e todos os vendedores de campo. Primeiro, não agendamos atendimento para clientes que são filiais, em nenhuma das duas equipes.

Para os demais clientes do televendas, o atendimento é a cada 7 dias, preferencialmente nos dias úteis e no sábado, sem coincidir com o atendimento da equipe de campo.

No campo, atendemos a cada 7 dias os clientes ativos para o vendedor e adimplentes, e a cada 14 dias os ativos para o vendedor e inadimplentes. Os inativos para o vendedor e adimplentes são atendidos a cada 30 dias, e os inativos para o vendedor e inadimplentes, a cada 60 dias. Os clientes sem vendas são atendidos a cada 7 dias.
