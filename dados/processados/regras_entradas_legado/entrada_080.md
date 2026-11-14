---
regra_id: 080
arquivo_regra: regra_080.gobr
hash_regra_sha256: 28eed7badaa8259d53ab7d02484f97e281912ae5848516559467ee6e3332b9bd
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 2503
tokens_saida: 359
custo_usd: 0.004298
tempo_segundos: 5.63
timestamp: 2026-11-13T19:33:13-03:00
---

Todos os vendedores da empresa atendem seus próprios clientes fixos, respeitando a preferência de cada vendedor.

Seguimos esta ordem quando um cliente se encaixa em mais de uma situação: primeiro, atendemos mensalmente os clientes inativos para o vendedor cujo CNAE no cadastro do ERP começa com 03, 47 ou 27. Depois, os demais clientes inativos para o vendedor são atendidos a cada 15 dias. Os clientes ativos para o vendedor são atendidos mensalmente.

Em seguida, consideramos novamente os clientes inativos para o vendedor, com atendimento a cada 15 dias. Por fim, os clientes sem vendas são atendidos mensalmente.
