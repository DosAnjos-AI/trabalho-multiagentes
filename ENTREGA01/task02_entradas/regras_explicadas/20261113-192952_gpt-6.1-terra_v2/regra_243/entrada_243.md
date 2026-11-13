---
regra_id: 243
arquivo_regra: regra_243.gobr
hash_regra_sha256: bf45544b7aa91eaaeeba1b86a8d49042107e9711f6971626f2a5c08dcbe8d24c
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2557
tokens_saida: 363
custo_usd: 0.004372
tempo_segundos: 7.07
timestamp: 2026-11-13T19:35:23-03:00
---

Os vendedores de televendas habilitados atendem seus clientes seguindo esta ordem de prioridade: pessoas jurídicas que ainda não compraram com o próprio vendedor são atendidas a cada 21 dias. As que compraram com ele nos últimos 20 dias são atendidas a cada 3 dias.

Para as pessoas jurídicas cuja última compra com o próprio vendedor foi entre 20 e 33 dias atrás, usamos o intervalo do histórico do cliente acrescido de 2 dias, respeitando o mínimo de 20 dias e o máximo de 33 dias. Nesses atendimentos, preferimos dias úteis e sábado.

As demais pessoas jurídicas não são agendadas, assim como todos os outros clientes.
