---
regra_id: 149
arquivo_regra: regra_149.gobr
hash_regra_sha256: c88ffa7e13b34c6bb4a28301e21181d3e7b3a245c27ede5801d6de0cf8cdbb81
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2606
tokens_saida: 343
custo_usd: 0.004321
tempo_segundos: 8.65
timestamp: 2026-11-13T19:35:44-03:00
---

Os vendedores de televendas habilitados atendem seus clientes seguindo esta ordem de prioridade. Primeiro, não agendamos quem comprou com o próprio vendedor nos últimos 7 dias. Depois, atendemos a cada 14 dias os clientes que nunca compraram com a empresa.

Em seguida, atendemos a cada 14 dias quem comprou com o próprio vendedor nos últimos 30 dias; depois, quem comprou com ele nos últimos 60 dias; e, em seguida, quem comprou com ele nos últimos 90 dias. Quem já se encaixou em uma dessas situações não passa para as seguintes. Todos os demais clientes também são atendidos a cada 14 dias. Para todos os atendimentos agendados, damos preferência aos dias úteis e ao sábado.
