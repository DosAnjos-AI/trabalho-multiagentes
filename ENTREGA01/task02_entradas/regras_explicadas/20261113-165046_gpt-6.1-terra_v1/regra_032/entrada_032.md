---
regra_id: 032
arquivo_regra: regra_032.gobr
hash_regra_sha256: 599e19af41a7c2972337a19e241d6dfa32c699957f0c6c348af47062e138cd44
arquivo_prompt: prompt_v1.md
hash_prompt_sha256: 40b5974705636c81d4d57c25c412ca473605bb769027303c4200113603a52462
modelo: gpt-6.1-terra
fornecedor: openai
temperatura: 1.0 (padrao fixo do modelo)
tokens_entrada: 7548
tokens_saida: 895
custo_usd: 0.012023
tempo_segundos: 11.91
timestamp: 2026-11-13T16:51:46-03:00
---

Os vendedores ativos do televendas cuidam dos seus clientes fixos. Separamos esses clientes em dois grupos: um com PR, SC, RS, SP, RJ, MG, ES, GO, MT, MS e DF; outro com AC, AP, AM, PA, RO, RR, TO, AL, BA, CE, MA, PB, PE, PI, RN e SE.

Antes de qualquer outra coisa, não agendamos clientes com situação baixada na Receita Federal. Em seguida, os prospects desses dois grupos devem ser atendidos a cada 14 dias. Para os demais, olhamos o ramo, a última compra e a média faturada no ano com a empresa. Primeiro consideramos os ativos, depois os pré-inativos e, por último, os demais clientes daquele ramo, que chamamos de inativos. Dentro de cada situação, olhamos primeiro a curva A, depois a B e, por fim, a C.

No Sul, Sudeste e Centro-Oeste, consideramos ativos os que compraram nos últimos 120 dias e pré-inativos os que compraram nos últimos 150 dias. No Norte e Nordeste, esses prazos são de 150 e 180 dias, respectivamente. Nessas avaliações, consideramos as compras com todos os vendedores, com uma exceção: para a curva C de pré-inativos de material de construção, ferragista, agropecuária e home center no Sul, Sudeste e Centro-Oeste, consideramos a compra vinculada ao vendedor nos últimos 150 dias.

Para material de construção, ferragista, agropecuária, home center, EPI e licitação, em ambas as regiões, a curva A tem média anual acima de R$ 25.000; a B, acima de R$ 10.000; e a C reúne os demais. Atendemos os ativos A a cada 14 dias, os B a cada 21 dias e os C a cada 28 dias. Os pré-inativos e os inativos desses ramos são atendidos a cada 14 dias, em todas as curvas.

Para atacado e distribuidores, a curva A tem média anual acima de R$ 50.000; a B, acima de R$ 25.000; e a C reúne os demais. Em ambas as regiões, atendemos os ativos A, B e C a cada 10, 14 e 21 dias, respectivamente; os pré-inativos A, B e C a cada 7, 10 e 14 dias; e os inativos A e B a cada 10 dias e os C a cada 21 dias.

Para corporativo e consumidor final, a curva A tem média anual acima de R$ 15.000; a B, acima de R$ 10.000; e a C reúne os demais. Em ambas as regiões, atendemos os ativos de todas as curvas a cada 28 dias e os pré-inativos de todas as curvas a cada 14 dias. No Sul, Sudeste e Centro-Oeste, os inativos de todas as curvas são atendidos a cada 28 dias. No Norte e Nordeste, esse prazo é de 28 dias para os inativos A e B; para os inativos C não há intervalo de atendimento definido.

Os clientes do televendas que não se enquadrarem nas situações de atendimento ficam sem agendamento.
