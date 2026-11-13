---
regra_id: 202
arquivo_regra: regra_202.gobr
hash_regra_sha256: ce0189a5e24f09ac0347617620a237474ebe89c1e7efb80ccf8dd6839ac4a063
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2517
tokens_saida: 484
custo_usd: 0.004937
tempo_segundos: 7.17
timestamp: 2026-11-13T19:34:36-03:00
---

Os vendedores habilitados do televendas atendem seus clientes seguindo esta ordem de prioridade: primeiro, quem está há mais de 60 dias sem comprar com seu vendedor é atendido a cada 7 dias. Depois, quem ainda não comprou com seu vendedor também é atendido a cada 7 dias.

Para quem fez uma única compra com seu vendedor e está há mais de 7 dias sem comprar com ele, o atendimento é a cada 7 dias. Quem comprou com seu vendedor nos últimos 30 dias é atendido conforme o histórico de compras, com intervalo máximo de 30 dias. Por fim, quem está sem comprar com seu vendedor entre 31 e 60 dias é atendido a cada 7 dias. Quando um cliente se encaixa em mais de uma dessas situações, vale a primeira em que ele se enquadrar.
