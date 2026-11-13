---
regra_id: 228
arquivo_regra: regra_228.gobr
hash_regra_sha256: f9de548ddf01743b402eceb1dbf15bf969118a38f07bd83e87cb674bdfe69406
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-5-mini-2025-08-07
fornecedor: openai
temperatura: 1.0 (padrao fixo do modelo)
tokens_entrada: 2508
tokens_saida: 3667
custo_usd: 0.007961
tempo_segundos: 33.98
timestamp: 2026-11-13T18:10:35-03:00
---

Isso vale só para os vendedores da equipe televendas que estejam ativos no sistema. A lógica é aplicada em sequência: quem encaixa num critério anterior não entra nos seguintes. Primeiro separamos os prospects do próprio vendedor: cliente que é prospect do vendedor recebe visita a cada 28 dias. Depois vêm os clientes que fizeram uma única compra com o vendedor (contagem só com o próprio vendedor): esses são atendidos a cada 21 dias. Em seguida tratamos quem teve compra nos últimos 90 dias; entre esses há prioridade para quem é curva c com a empresa — cliente que comprou nos últimos 90 dias e que está em curva c com a empresa recebe visita a cada 7 dias (a curva é considerada pela empresa toda). Os demais que compraram nos últimos 90 dias (ou seja, compraram nos últimos 90 dias, contado com qualquer vendedor da empresa, mas que não se enquadram na condição de curva c acima) são atendidos a cada 14 dias. Depois vêm os clientes que compraram entre 91 dias e 180 dias atrás (contagem igualmente sobre a empresa): esses são visitados a cada 28 dias. E todo o resto que não foi capturado pelas regras anteriores fica para “resgatar cliente inativo”, atendido a cada 45 dias.
