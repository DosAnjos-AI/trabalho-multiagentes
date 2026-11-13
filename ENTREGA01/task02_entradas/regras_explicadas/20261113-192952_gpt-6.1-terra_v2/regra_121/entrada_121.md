---
regra_id: 121
arquivo_regra: regra_121.gobr
hash_regra_sha256: 45fed006255e99b4ac0fcf640ca07964a09db43a5f95c14c1b056b45ce8443be
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2649
tokens_saida: 523
custo_usd: 0.005264
tempo_segundos: 8.46
timestamp: 2026-11-13T19:43:40-03:00
---

Os vendedores do televendas habilitados no sistema atendem seus clientes seguindo esta ordem: primeiro, não agendamos clientes com situação baixada na Receita Federal nem clientes que sejam filiais.

Entre os demais, atendemos a cada 3 dias os clientes reativados com a empresa e também os que fizeram uma única compra com a empresa. Depois, para quem comprou com o próprio vendedor nos últimos 30 dias, seguimos o histórico de atendimento, com intervalo mínimo de 3 dias e máximo de 21 dias.

Para quem ainda não se enquadrou nas situações anteriores, atendemos a cada 14 dias se comprou com o próprio vendedor nos últimos 60 dias; a cada 21 dias se comprou nos últimos 90 dias; e a cada 14 dias se comprou nos últimos 120 dias. Os demais clientes são atendidos a cada 7 dias.
