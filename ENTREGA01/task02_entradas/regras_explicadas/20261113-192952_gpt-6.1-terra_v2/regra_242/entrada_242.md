---
regra_id: 242
arquivo_regra: regra_242.gobr
hash_regra_sha256: e654a5bfb82445903c3cd0e4d7f1907c261cb9a29c95fe0e40047e0b00f1c050
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2794
tokens_saida: 472
custo_usd: 0.005154
tempo_segundos: 6.65
timestamp: 2026-11-13T19:40:53-03:00
---

A equipe é formada pelos vendedores de televendas habilitados no sistema. Para os clientes de cada vendedor, consideramos a frequência histórica das compras e o tempo desde a última compra com esse próprio vendedor. Seguimos a ordem abaixo: se o cliente se encaixar em mais de uma situação, vale a primeira.

Com frequência histórica de 0 a 30 dias e última compra entre 20 e 30 dias atrás, atendemos a cada 21 dias. Com frequência histórica de 31 a 60 dias, atendemos a cada 21 dias tanto quem comprou pela última vez entre 29 e 44 dias atrás quanto quem comprou entre 44 e 60 dias atrás.

Com frequência histórica de 61 a 90 dias, atendemos a cada 15 dias quem comprou pela última vez entre 61 e 90 dias atrás; quem comprou entre 90 e 180 dias atrás é atendido a cada 21 dias.

Com frequência histórica de 91 a 180 dias, atendemos a cada 21 dias quem comprou pela última vez entre 44 e 120 dias atrás; quem comprou entre 120 e 180 dias atrás é atendido a cada 15 dias.
