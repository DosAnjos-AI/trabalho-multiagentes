---
regra_id: 237
arquivo_regra: regra_237.gobr
hash_regra_sha256: 0e754c9699c8cdb84ce0b06c14abf4bc77daf601a0e23b2531bcc2ca73ac7f11
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2531
tokens_saida: 547
custo_usd: 0.005266
tempo_segundos: 7.45
timestamp: 2026-11-13T19:35:10-03:00
---

Os vendedores de televendas habilitados atendem seus clientes seguindo esta ordem de prioridade: quem se encaixar em uma situação fica com aquele atendimento e não passa para as seguintes.

Clientes que ainda não compraram com seu vendedor são atendidos a cada 14 dias. Para quem comprou com seu vendedor nos últimos 30 dias e tem intervalo histórico entre compras menor que 30 dias, usamos esse intervalo histórico para o atendimento, com mínimo de 0 dias e máximo de 30 dias.

Quem comprou com seu vendedor entre 30 e 60 dias atrás é atendido a cada 14 dias. Depois, atendemos a cada 14 dias quem não comprou com seu vendedor nos últimos 60 dias e tem intervalo histórico entre compras maior que 30 dias. Os demais que não compraram com seu vendedor nos últimos 60 dias também são atendidos a cada 14 dias.
