---
regra_id: 213
arquivo_regra: regra_213.gobr
hash_regra_sha256: 1993d541254c8283ce6d13d71317a3724a846128343ec90b5899e5c2e75105da
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2974
tokens_saida: 350
custo_usd: 0.004724
tempo_segundos: 6.01
timestamp: 2026-11-13T19:47:36-03:00
---

Trabalhamos com os vendedores de televendas habilitados no sistema e os clientes fixos de cada um. Primeiro, os clientes que são filiais não devem ser agendados.

Separamos os demais clientes pelos códigos de rota: 24, 523, 524, 525 e 526 para segunda; 3, 4, 17, 500, 512, 514 e 515 para terça; 502, 530 e 531 para quarta; 20, 501, 504, 505, 506, 508, 513, 516, 527 e 528 para quinta; e 5, 19, 510, 511 e 521 para sexta.

Em cada um desses grupos, os clientes ativos para o próprio vendedor são atendidos semanalmente. Os demais são atendidos a cada 28 dias. O atendimento é fixo, com preferência pelo dia correspondente ao grupo.

Para os clientes das rotas 10 e 11, o atendimento é semanal, sem dia específico.
