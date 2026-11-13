---
regra_id: 228
arquivo_regra: regra_228.gobr
hash_regra_sha256: f9de548ddf01743b402eceb1dbf15bf969118a38f07bd83e87cb674bdfe69406
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-4.1-mini-2025-04-14
fornecedor: openai
temperatura: 1.0 (padrao fixo do modelo)
tokens_entrada: 2509
tokens_saida: 333
custo_usd: 0.001536
tempo_segundos: 3.74
timestamp: 2026-11-13T18:09:11-03:00
---

Os vendedores do televendas atendem todos os clientes que estão sob sua responsabilidade, sem divisão por carteira fixa, e consideram a situação de cada cliente em relação ao vendedor que os atende.

Primeiro, a gente trata os clientes que ainda são prospects para o vendedor, ou seja, que ainda não compraram com ele: esses clientes devem ser visitados a cada 28 dias para tentar ativar a compra. Depois, para os clientes que fizeram só uma compra com o vendedor, o atendimento fica mais frequente, com visitas a cada 21 dias.

Para os clientes que compram com regularidade e foram positivados — isto é, fizeram uma compra — nos últimos 90 dias, a frequência depende da curva de compra deles analisada em relação a toda a empresa: se estiverem na curva C, que são clientes com menor volume, visitamos a cada 7 dias; se estiverem nas curvas A ou B, que indicam maior movimentação, a visita acontece a cada 14 dias.

Quando o cliente está caminhando para a inatividade — ou seja, sua última compra foi feita entre 91 e 180 dias atrás — a visita é mais espaçada, a cada 28 dias, para tentar reengajá-lo sem insistência exagerada.

Por fim, os clientes considerados inativos, que não tiveram compra recente além desse intervalo, recebem uma visita a cada 45 dias como estratégia para recuperação.

Assim, a gente prioriza o atendimento conforme o relacionamento e histórico do cliente com o vendedor, sempre buscando ativar ou reativar clientes, e atendendo com maior frequência aqueles que compram regularmente para manter o volume.
