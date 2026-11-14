---
regra_id: 132
arquivo_regra: regra_132.gobr
hash_regra_sha256: d1505dbfc74a12a94eaf8a73726e9f5a2c7b8241ffabe970400fe80922ee6874
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2600
tokens_saida: 308
custo_usd: 0.004140
tempo_segundos: 5.12
timestamp: 2026-11-13T19:39:09-03:00
---

Os vendedores de televendas habilitados atendem seus clientes conforme a seguinte prioridade: primeiro, não agendamos os inadimplentes. Depois, atendemos a cada 7 dias os clientes que ainda não compraram com o próprio vendedor e os que fizeram uma única compra com ele.

Entre os que sobrarem, atendemos a cada 14 dias quem tem frequência histórica de compra menor que 11 dias. Em seguida, atendemos a cada 10 dias quem comprou com o próprio vendedor pela última vez entre 11 e 59 dias atrás, e a cada 7 dias quem comprou com ele pela última vez entre 60 e 89 dias atrás. Todos os demais são atendidos a cada 10 dias.
