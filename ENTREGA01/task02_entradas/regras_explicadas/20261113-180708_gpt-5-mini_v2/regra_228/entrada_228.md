---
regra_id: 228
arquivo_regra: regra_228.gobr
hash_regra_sha256: f9de548ddf01743b402eceb1dbf15bf969118a38f07bd83e87cb674bdfe69406
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-5-mini
fornecedor: openai
temperatura: 1.0 (padrao fixo do modelo)
tokens_entrada: 2508
tokens_saida: 4852
custo_usd: 0.010331
tempo_segundos: 42.82
timestamp: 2026-11-13T18:10:01-03:00
---

Todas as regras de agendamento valem para os vendedores do time televendas que estão ativos. A gente aplica as regras em ordem: o cliente é testado na primeira condição; se cumprir, recebe aquele tratamento e não é avaliado nas regras seguintes; se não cumprir, vai para a próxima condição, e assim por diante.

Primeiro, atendemos os clientes que são prospect do vendedor responsável por eles; esses prospects devem ser visitados/contatados a cada 28 dias.

Em seguida vêm os clientes que fizeram uma única compra com o vendedor responsável (ou seja, a contagem dessa condição é somente sobre compras feitas com o próprio vendedor): esses clientes são atendidos a cada 21 dias.

Depois olhamos os clientes cuja última positivação foi nos últimos 90 dias e que estão em curva c com a empresa; para esses clientes atendemos a cada 7 dias. Nessa regra a curva é explicitamente "curva c com a empresa", e a recência da positivação não restringe quem vendeu (é a positivação considerada sobre a conta, não limitada ao vendedor).

A próxima regra também pega clientes cuja última positivação foi nos últimos 90 dias, mas aqui não há nenhuma exigência de curva; atendemos esses clientes a cada 14 dias. Na prática isso significa que, depois de aplicar o critério anterior (curva c), qualquer outro cliente com positivação nos últimos 90 dias cai nessa regra e recebe atendimento a cada 14 dias.

Depois temos os clientes cuja última positivação está entre 91 dias e 180 dias; esses clientes são atendidos a cada 28 dias.

E, por fim, todo o resto dos clientes do time televendas que não se enquadrou em nenhuma das condições anteriores fica com atendimento a cada 45 dias.
