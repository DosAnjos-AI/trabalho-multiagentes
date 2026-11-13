---
regra_id: 142
arquivo_regra: regra_142.gobr
hash_regra_sha256: ad7b98b19207008790dce1f9ca97935cffb1d859a09278b761ef08d169a1afc4
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 3216
tokens_saida: 445
custo_usd: 0.005441
tempo_segundos: 6.24
timestamp: 2026-11-13T19:49:45-03:00
---

Trabalhamos com os vendedores habilitados no sistema, exceto os de código 10, 5 e 3, que têm atendimentos próprios: Yara, Lúcia e Wanderson, respectivamente. Em cada caso, seguimos a ordem abaixo; se um cliente se encaixar em mais de uma situação, vale a primeira.

Para os clientes da Yara, considerando a curva na empresa toda, atendemos os de curva A a cada 3 dias, os de curva B a cada 7 dias e os de curva C a cada 14 dias. Todos os demais são atendidos a cada 14 dias.

Para os clientes da Lúcia, também considerando a curva na empresa toda, atendemos os de curva A a cada 2 dias, os de curva B a cada 7 dias e os de curva C a cada 14 dias. Todos os demais são atendidos a cada 7 dias.

Para os clientes do Wanderson, considerando a curva na empresa toda, atendemos os de curva A a cada 4 dias, os de curva B a cada 7 dias e os de curva C a cada 9 dias. Todos os demais são atendidos a cada 14 dias.

Para os demais vendedores habilitados, primeiro não agendamos os clientes inadimplentes. Entre os que sobrarem, atendemos os dos ramos 001 e 002 a cada 14 dias, os do ramo 003 a cada 7 dias e os do ramo 004 a cada 21 dias. Não agendamos os dos ramos 005, 006 e 100. Depois disso, os clientes ativos para o próprio vendedor são atendidos a cada 7 dias, e todos os demais, a cada 15 dias.
