---
regra_id: 182
arquivo_regra: regra_182.gobr
hash_regra_sha256: f51a309e70fd224f54fd38462e600edc124deb986fc01554ae8c22a21b5a2a80
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 4085
tokens_saida: 578
custo_usd: 0.006975
tempo_segundos: 7.92
timestamp: 2026-11-13T19:50:14-03:00
---

Os vendedores de televendas habilitados atendem os clientes da equipe. Primeiro, não agendamos pessoas físicas, clientes inadimplentes, clientes com situação baixada na Receita Federal ou clientes que compraram com o próprio vendedor nos últimos 7 dias.

Depois, atendemos a cada 7 dias os clientes que nunca compraram com a empresa e são dos ramos 089, 090, 091, 092, 093, 094, 095, 096, 097, 098, 099, 100, 101, 102 ou 103.

Para os demais clientes desses ramos, consideramos as compras feitas com o próprio vendedor. Quem comprou no prazo indicado recebe a primeira frequência; os demais daquele ramo recebem a segunda:

Nos ramos 089, 091, 093, 099 e 102, quem comprou nos últimos 45 dias é atendido a cada 14 dias; os demais, a cada 7 dias. Nos ramos 090, 097 e 098, quem comprou nos últimos 60 dias é atendido a cada 21 dias; os demais, a cada 10 dias. Nos ramos 092, 094, 101 e 103, quem comprou nos últimos 90 dias é atendido a cada 28 dias; os demais, a cada 14 dias.

No ramo 095, quem comprou nos últimos 75 dias é atendido a cada 21 dias; os demais, a cada 14 dias. No ramo 096, quem comprou nos últimos 75 dias é atendido a cada 28 dias; os demais, a cada 14 dias. No ramo 100, quem comprou nos últimos 75 dias é atendido a cada 28 dias; os demais, a cada 7 dias.
