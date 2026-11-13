---
regra_id: 032
arquivo_regra: regra_032.gobr
hash_regra_sha256: 599e19af41a7c2972337a19e241d6dfa32c699957f0c6c348af47062e138cd44
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gemini-3.8-flash
fornecedor: gemini
temperatura: 0.3
tokens_entrada: 9380
tokens_saida: 7569
custo_usd: 0.035419
tempo_segundos: 49.89
timestamp: 2026-11-13T18:36:12-03:00
---

A nossa equipe de televendas, considerando apenas os vendedores ativos no sistema, cuida dos clientes fixos de cada um deles. Para organizar o atendimento, dividimos esses clientes fixos em dois grupos regionais conforme o estado cadastrado: um reunindo Sul, Sudeste e Centro-Oeste com PR, SC, RS, SP, RJ, MG, ES, GO, MT, MS e DF; e outro reunindo Norte e Nordeste com AC, AP, AM, PA, RO, RR, TO, AL, BA, CE, MA, PB, PE, PI, RN e SE.

A prioridade começa com duas situações gerais. Antes de qualquer coisa, se o cliente da equipe de televendas estiver com a situação cadastrada como baixada na Receita Federal, nós não agendamos atendimento. Em seguida, os clientes pertencentes a qualquer um dos dois grupos regionais que estiverem no ciclo de vida como prospect com a empresa devem ser atendidos a cada 14 dias.

Para os demais clientes, o atendimento é definido pela região e pelo ramo de atividade, avaliando primeiro quem comprou mais recentemente, depois quem comprou há mais tempo e, por fim, quem já não compra nesses prazos.

No grupo de Sul, Sudeste e Centro-Oeste, tratamos os ramos da seguinte forma:

Para os clientes dos ramos MATCON, FERRAGISTA, AGROPECUARIA e HOME CENTER, quem comprou com qualquer vendedor da empresa nos últimos 120 dias e tem faturamento médio no ano com a empresa maior que R$ 25000 é atendido a cada 14 dias; se a média faturada no ano for maior que R$ 10000, o atendimento é a cada 21 dias; e os demais que compraram nesses últimos 120 dias são atendidos a cada 28 dias. Em seguida, avaliamos quem comprou nos últimos 150 dias: se comprou com qualquer vendedor da empresa e tem média faturada no ano acima de R$ 25000, o atendimento é a cada 14 dias; com compra com qualquer vendedor e faturamento médio acima de R$ 10000, também a cada 14 dias; e para quem comprou nos últimos 150 dias só com o próprio vendedor dele, o atendimento também é a cada 14 dias. Para os clientes desses ramos que não compraram nesses prazos, quem tem faturamento médio no ano com a empresa maior que R$ 25000 é atendido a cada 14 dias; com faturamento médio maior que R$ 10000, a cada 14 dias; e todos os demais que sobraram desses ramos recebem atendimento a cada 14 dias.

Para os ramos EPI e LICITACAO, quem comprou com qualquer vendedor da empresa nos últimos 120 dias e tem faturamento médio no ano com a empresa maior que R$ 25000 é atendido a cada 14 dias; se a média faturada for maior que R$ 10000, a cada 21 dias; e os outros que compraram no período, a cada 28 dias. Depois, quem comprou com qualquer vendedor da empresa nos últimos 150 dias com faturamento médio acima de R$ 25000 é atendido a cada 14 dias; com faturamento médio acima de R$ 10000, a cada 14 dias; e os demais que compraram com qualquer vendedor nesses 150 dias, a cada 14 dias. Dos clientes restantes desses ramos, quem tem faturamento médio no ano maior que R$ 25000 é atendido a cada 14 dias; maior que R$ 10000, a cada 14 dias; e todo o restante desses ramos, a cada 14 dias.

Para o ramo ATACADO, quem comprou com qualquer vendedor da empresa nos últimos 120 dias e tem faturamento médio no ano com a empresa maior que R$ 50000 é atendido a cada 10 dias; se o faturamento médio for maior que R$ 25000, a cada 14 dias; e os demais que compraram no período, a cada 21 dias. Em seguida, quem comprou com qualquer vendedor da empresa nos últimos 150 dias com faturamento médio maior que R$ 50000 é atendido a cada 7 dias; com média maior que R$ 25000, a cada 10 dias; e os outros que compraram nesses 150 dias, a cada 14 dias. Entre os que não compraram nesses prazos, quem tem faturamento médio maior que R$ 50000 é atendido a cada 10 dias; maior que R$ 25000, a cada 10 dias; e os demais desse ramo, a cada 21 dias.

Para o ramo CONS. FINAL, quem comprou com qualquer vendedor da empresa nos últimos 120 dias com faturamento médio no ano maior que R$ 15000, maior que R$ 10000 ou qualquer outro valor que tenha comprado nesse período é atendido a cada 28 dias. Depois, quem comprou com qualquer vendedor da empresa nos últimos 150 dias com faturamento médio maior que R$ 15000, maior que R$ 10000 ou qualquer outro valor é atendido a cada 14 dias. Dos que restaram no ramo, quem tem faturamento médio anual maior que R$ 15000 é atendido a cada 28 dias; maior que R$ 10000, a cada 28 dias; e todos os demais de CONS. FINAL, a cada 28 dias.

No grupo de Norte e Nordeste, seguimos uma lógica semelhante, porém os prazos de compra mudam para 150 e 180 dias:

Para MATCON, FERRAGISTA, AGROPECUARIA e HOME CENTER, quem comprou com qualquer vendedor da empresa nos últimos 150 dias e tem faturamento médio no ano com a empresa maior que R$ 25000 é atendido a cada 14 dias; com faturamento médio maior que R$ 10000, a cada 21 dias; e os demais com compra no período, a cada 28 dias. Em seguida, quem comprou com qualquer vendedor da empresa nos últimos 180 dias com faturamento médio maior que R$ 25000 é atendido a cada 14 dias; com faturamento maior que R$ 10000, a cada 14 dias; e os demais que compraram com qualquer vendedor nesses 180 dias, a cada 14 dias. Para os clientes que não compraram nesses prazos, quem tem faturamento médio anual maior que R$ 25000 é atendido a cada 14 dias; maior que R$ 10000, a cada 14 dias; e o restante desses ramos, a cada 14 dias.

Para EPI e LICITACAO, quem comprou com qualquer vendedor da empresa nos últimos 150 dias e tem faturamento médio no ano maior que R$ 25000 é atendido a cada 14 dias; com faturamento maior que R$ 10000, a cada 21 dias; e os demais com compra no período, a cada 28 dias. Depois, quem comprou com qualquer vendedor nos últimos 180 dias com faturamento médio maior que R$ 25000 é atendido a cada 14 dias; com faturamento maior que R$ 10000, a cada 14 dias; e os demais que compraram nesses 180 dias, a cada 14 dias. Para quem não comprou nesses períodos, faturamento médio anual maior que R$ 25000 fica com frequência de 14 dias; maior que R$ 10000, com 14 dias; e todos os que sobrarem desses ramos, a cada 14 dias.

Para ATACADO, quem comprou com qualquer vendedor da empresa nos últimos 150 dias e fatura em média no ano mais de R$ 50000 é atendido a cada 10 dias; com faturamento médio maior que R$ 25000, a cada 14 dias; e os demais que compraram no período, a cada 21 dias. Em seguida, quem comprou com qualquer vendedor nos últimos 180 dias com faturamento médio maior que R$ 50000 é atendido a cada 7 dias; com faturamento maior que R$ 25000, a cada 10 dias; e os outros com compra nesses 180 dias, a cada 14 dias. Entre os clientes que não compraram nesses prazos, faturamento médio acima de R$ 50000 fica com frequência de 10 dias; acima de R$ 25000, a cada 10 dias; e o restante do ramo, a cada 21 dias.

Para CONS. FINAL, quem comprou com qualquer vendedor da empresa nos últimos 150 dias com faturamento médio anual maior que R$ 15000, maior que R$ 10000 ou qualquer outro valor é atendido a cada 28 dias. Depois, quem comprou com qualquer vendedor nos últimos 180 dias com faturamento médio maior que R$ 15000, maior que R$ 10000 ou qualquer outro valor é atendido a cada 14 dias. Dos clientes que não compraram nesses períodos, quem tem faturamento médio anual maior que R$ 15000 é atendido a cada 28 dias; e com faturamento maior que R$ 10000, a cada 28 dias. Para os clientes que sobrarem no ramo CONS. FINAL nessa região, ainda não definimos de quanto em quanto tempo atender.

Por fim, todo o restante dos clientes da equipe de televendas que não tiver entrado em nenhuma dessas condições não deve ser agendado.
