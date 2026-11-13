---
regra_id: 047
arquivo_regra: regra_047.gobr
hash_regra_sha256: 634cc2d512d43763e5366b1d74c12933749f1a11836f6e290931a35e2b89ce85
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2529
tokens_saida: 250
custo_usd: 0.003779
tempo_segundos: 4.30
timestamp: 2026-11-13T19:32:50-03:00
---

Todos os vendedores habilitados no sistema atendem seus próprios clientes fixos. Se um cliente se encaixar em mais de uma situação, vale a primeira na ordem abaixo.

Primeiro, não agendamos pessoas físicas. Depois, atendemos a cada 7 dias os clientes ativos para o vendedor e adimplentes. Os ativos para o vendedor e inadimplentes são atendidos a cada 14 dias, assim como os inativos para o vendedor e adimplentes. Não agendamos os inativos para o vendedor que estejam inadimplentes. Por fim, atendemos a cada 14 dias os clientes sem vendas que não tenham sido enquadrados nas situações anteriores.
