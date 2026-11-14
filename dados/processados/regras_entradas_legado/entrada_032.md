---
regra_id: 032
arquivo_regra: regra_032.gobr
hash_regra_sha256: 599e19af41a7c2972337a19e241d6dfa32c699957f0c6c348af47062e138cd44
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 8542
tokens_saida: 897
custo_usd: 0.013027
tempo_segundos: 11.17
timestamp: 2026-11-13T19:50:43-03:00
---

Os vendedores de televendas habilitados atendem os clientes fixos de cada um. Separamos esses clientes em dois grupos: um com os de PR, SC, RS, SP, RJ, MG, ES, GO, MT, MS e DF, e outro com os de AC, AP, AM, PA, RO, RR, TO, AL, BA, CE, MA, PB, PE, PI, RN e SE. Pela divisão por estado, o mesmo cliente não aparece nos dois grupos.

Primeiro, não agendamos nenhum cliente da equipe que esteja com situação baixada na Receita Federal. Depois, nos dois grupos regionais, atendemos a cada 14 dias os prospects que nunca compraram com a empresa. Nas demais situações, seguimos a ordem abaixo: quem se encaixar em mais de uma recebe o atendimento da primeira situação em que entrar.

Para as situações por ramo, consideramos as compras com qualquer vendedor da empresa e o faturamento médio anual com a empresa. No primeiro grupo de estados, olhamos primeiro quem comprou nos últimos 120 dias e depois quem comprou nos últimos 150 dias. No segundo grupo, os períodos são, respectivamente, 150 e 180 dias. Em cada período, verificamos primeiro o faturamento acima do limite maior, depois acima do limite menor e, por fim, sem exigir limite de faturamento. Depois desses períodos, fazemos a mesma sequência de faturamento sem exigir compra recente.

Para MATCON, FERRAGISTA, AGROPECUARIA e HOME CENTER, assim como para EPI e LICITACAO, os limites são R$ 25000 e R$ 10000. No primeiro período de compra de cada região, atendemos a cada 14 dias acima de R$ 25000, a cada 21 dias acima de R$ 10000 e a cada 28 dias sem limite de faturamento. No segundo período, as três situações são atendidas a cada 14 dias. A exceção é que, no primeiro grupo de estados, para MATCON, FERRAGISTA, AGROPECUARIA e HOME CENTER, a situação do segundo período sem limite de faturamento considera a compra nos últimos 150 dias somente com o próprio vendedor do cliente. Sem exigir compra recente, as três situações desses ramos são atendidas a cada 14 dias.

Para ATACADO, os limites são R$ 50000 e R$ 25000. No primeiro período de compra, atendemos a cada 10 dias acima de R$ 50000, a cada 14 dias acima de R$ 25000 e a cada 21 dias sem limite de faturamento. No segundo período, os respectivos intervalos são 7, 10 e 14 dias. Sem exigir compra recente, atendemos a cada 10 dias acima de R$ 50000, a cada 10 dias acima de R$ 25000 e a cada 21 dias sem limite de faturamento.

Para CONS. FINAL, os limites são R$ 15000 e R$ 10000. No primeiro período de compra, as três situações são atendidas a cada 28 dias; no segundo período, a cada 14 dias. Sem exigir compra recente, atendemos a cada 28 dias tanto acima de R$ 15000 quanto acima de R$ 10000. No primeiro grupo de estados, também atendemos a cada 28 dias sem exigir limite de faturamento. No segundo grupo, para essa última situação sem limite de faturamento, ainda não definimos de quanto em quanto tempo atender.

Por fim, os demais clientes da equipe que não se enquadrarem nas situações anteriores não são agendados.
