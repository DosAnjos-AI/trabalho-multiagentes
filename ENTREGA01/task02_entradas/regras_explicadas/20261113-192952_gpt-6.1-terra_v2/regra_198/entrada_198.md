---
regra_id: 198
arquivo_regra: regra_198.gobr
hash_regra_sha256: 369f1f725b029b22c3722c9a0b0bce22916848911d31bd37afed16bfc4d6eee0
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2508
tokens_saida: 281
custo_usd: 0.003913
tempo_segundos: 4.91
timestamp: 2026-11-13T19:34:29-03:00
---

Os vendedores de televendas habilitados atendem os clientes seguindo esta prioridade: quem nunca comprou com a empresa é atendido a cada 25 dias. Em seguida, quem fez uma única compra com a empresa e não comprou com o próprio vendedor nos últimos 30 dias é atendido a cada 14 dias.

Para quem comprou com o próprio vendedor nos últimos 30 dias, usamos o intervalo de atendimento baseado no histórico, com mínimo de 7 e máximo de 30 dias. Depois disso, os clientes ativos na empresa são atendidos a cada 14 dias, e todos os demais, a cada 21 dias. Quem se encaixar em mais de uma situação segue a primeira que se aplicar.
