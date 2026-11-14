---
regra_id: 204
arquivo_regra: regra_204.gobr
hash_regra_sha256: 6107fdc46844e01a5bb11bef2700161f0853234d0259141dceaf899d8668a1ff
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2464
tokens_saida: 257
custo_usd: 0.003749
tempo_segundos: 4.67
timestamp: 2026-11-13T19:34:41-03:00
---

Os vendedores habilitados do televendas atendem seus clientes considerando as compras feitas com o próprio vendedor de cada cliente. Primeiro, quem comprou nos últimos 7 dias não deve ser agendado.

Entre os demais, quem comprou nos últimos 30 dias ou entre 31 e 60 dias deve ser atendido a cada 14 dias. Quem comprou entre 61 e 90 dias deve ser atendido a cada 7 dias. Para todos os outros clientes, o atendimento será a cada 21 dias.
