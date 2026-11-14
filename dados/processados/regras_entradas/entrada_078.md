---
regra_id: 078
arquivo_regra: regra_078.gobr
hash_regra_sha256: 422e9660d9143e15b8d1841a65dd214cadeffffc2fa0587a9968420f45ab5a0d
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2527
tokens_saida: 185
custo_usd: 0.003452
tempo_segundos: 3.42
timestamp: 2026-11-13T19:33:07-03:00
---

Todos os vendedores atendem seus próprios clientes fixos, com preferência por dias úteis. Seguimos esta ordem: os clientes ativos para o vendedor e inadimplentes são atendidos a cada 14 dias; os demais ativos para o vendedor, a cada 7 dias. Os clientes inativos para o vendedor e inadimplentes são atendidos a cada 30 dias; os demais inativos para o vendedor, a cada 14 dias. Por fim, os clientes sem vendas são atendidos a cada 14 dias. Se um cliente se encaixar em mais de uma dessas situações, vale a primeira que se aplicar.
