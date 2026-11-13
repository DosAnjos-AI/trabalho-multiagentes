---
regra_id: 143
arquivo_regra: regra_143.gobr
hash_regra_sha256: ab27f0d3c40789be9326e40d24822edc346e04c9433f844723c40ccecfc2ec53
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2790
tokens_saida: 513
custo_usd: 0.005355
tempo_segundos: 8.60
timestamp: 2026-11-13T19:43:57-03:00
---

Os vendedores de televendas habilitados no sistema cuidam dos clientes atendidos pela equipe. Seguimos esta ordem: primeiro, não agendamos clientes que sejam filiais nem clientes que tenham comprado com qualquer vendedor da empresa nos últimos 30 dias.

Entre os que restarem, atendemos a cada 28 dias os que nunca compraram com a empresa. Para os clientes ativos na empresa cuja última compra com qualquer vendedor esteja fora do intervalo entre 30 e 45 dias atrás, atendemos a cada 7 dias os de curva A e a cada 14 dias os de curva B, considerando a curva na empresa toda. Os demais clientes ativos cuja última compra esteja fora desse mesmo intervalo são atendidos a cada 21 dias.

Depois, entre os que ainda não receberam atendimento, os clientes ativos cuja última compra com qualquer vendedor da empresa esteja fora do intervalo entre 45 e 60 dias atrás são atendidos a cada 14 dias. Os demais clientes ativos são atendidos a cada 7 dias e, por fim, todo o resto também é atendido a cada 7 dias.
