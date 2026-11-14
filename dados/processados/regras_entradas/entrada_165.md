---
regra_id: 165
arquivo_regra: regra_165.gobr
hash_regra_sha256: bc61014bea041dbf9709dcd573fe2732ac929060104cbd07bcc087f86a1012f1
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2874
tokens_saida: 821
custo_usd: 0.006979
tempo_segundos: 10.77
timestamp: 2026-11-13T19:39:31-03:00
---

No televendas, trabalhamos com os vendedores habilitados, e no atendimento de campo com todos os vendedores. Entre os clientes fixos dos vendedores de campo, separamos os que têm histórico de pedidos em intervalos de 1 a 7 dias, de 16 a 30 dias, de 31 a 45 dias e de 61 a 90 dias.

Para os clientes atendidos pelo televendas, seguimos esta ordem: primeiro, não agendamos os que estão inativos na empresa e inadimplentes. Depois, atendemos a cada 7 dias os que estão há mais de 90 dias sem comprar com o próprio vendedor de televendas.

Em seguida, entre os clientes fixos de campo separados pelo histórico de pedidos, atendemos a cada 14 dias os que têm intervalos históricos de 1 a 7 dias e estão entre 8 e 15 dias sem comprar com seu vendedor de televendas; a cada 28 dias os que têm intervalos de 16 a 30 dias e estão entre 31 e 45 dias sem comprar com esse vendedor; e a cada 21 dias os que têm intervalos de 31 a 45 dias e estão entre 46 e 60 dias sem comprar com esse vendedor. Para os que têm intervalos históricos de 61 a 90 dias e estão há mais de 90 dias sem comprar com seu vendedor de televendas, o atendimento seria a cada 15 dias.

Cada cliente fica com o primeiro tratamento em que se encaixar nessa ordem. Os demais não são agendados.
