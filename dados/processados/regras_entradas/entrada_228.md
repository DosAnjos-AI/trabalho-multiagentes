---
regra_id: 228
arquivo_regra: regra_228.gobr
hash_regra_sha256: fb3ab8cb11674c44275b76c01b64325facddc6aa746a37d52bd6576bbd6982e0
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2508
tokens_saida: 647
custo_usd: 0.005743
tempo_segundos: 8.54
timestamp: 2026-11-14T20:55:57-03:00
---

Os vendedores de televendas habilitados atendem seus clientes seguindo esta ordem: se um cliente se encaixar em mais de uma situação, vale a primeira.

Quem ainda não comprou com o próprio vendedor é atendido a cada 28 dias. Quem fez uma única compra com esse vendedor é atendido a cada 21 dias.

Dos demais, quem comprou com qualquer vendedor da empresa nos últimos 90 dias e é curva C considerando a empresa toda é atendido a cada 7 dias. Os outros que compraram com qualquer vendedor da empresa nos últimos 90 dias são atendidos a cada 14 dias.

Quem comprou com qualquer vendedor da empresa entre 91 e 180 dias atrás é atendido a cada 28 dias. Todo o resto é atendido a cada 45 dias.
