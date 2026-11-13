---
regra_id: 032
arquivo_regra: regra_032.gobr
hash_regra_sha256: 599e19af41a7c2972337a19e241d6dfa32c699957f0c6c348af47062e138cd44
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-5-mini
fornecedor: openai
temperatura: 1.0 (padrao fixo do modelo)
tokens_entrada: 8542
tokens_saida: 6917
custo_usd: 0.015970
tempo_segundos: 65.33
timestamp: 2026-11-13T18:14:18-03:00
---

A gente atende com a equipe de televendas — todos os vendedores de televendas que estão ativados no cadastro — e trabalha só com os clientes fixos de televendas agrupados em duas carteiras chamadas exatamente sul_sudeste_centrooeste e norte_nordeste, onde a divisão por estado é: sul_sudeste_centrooeste = PR, SC, RS, SP, RJ, MG, ES, GO, MT, MS, DF; norte_nordeste = AC, AP, AM, PA, RO, RR, TO, AL, BA, CE, MA, PB, PE, PI, RN, SE. Primeiro aplicamos as exceções que não devem ser agendadas e depois as demais regras; quem já ficou alocado numa regra não passa para as regras seguintes.

Antes de tudo não agendamos clientes cujo status na Receita Federal esteja definido como baixada; essa regra vale para os vendedores do televendas. Em seguida, os clientes que estão no ciclo de vida prospect com a empresa e que pertencem às carteiras sul_sudeste_centrooeste ou norte_nordeste são visitados a cada 14 dias.

Para o resto seguimos por região e por segmento, com as condições e frequências abaixo (dizemos ramo de atividade pelos códigos do cadastro e os valores de faturamento e dias exatamente como estão):

Região sul_sudeste_centrooeste — segmento MATCON, FERRAGISTA, AGROPECUARIA e HOME CENTER:
- Ativos Curva A: ramo igual MATCON,FERRAGISTA,AGROPECUARIA,HOME CENTER e recência de positivação global em 120 dias e média faturada no ano com a empresa maior que R$ 25000 → visitar a cada 14 dias.
- Ativos Curva B: mesmo ramo e recência de positivação global em 120 dias e média faturada no ano com a empresa maior que R$ 10000 → visitar a cada 21 dias.
- Ativos Curva C: mesmo ramo e recência de positivação global em 120 dias → visitar a cada 28 dias.
- Pré-inativos Curva A: mesmo ramo e recência de positivação global em 150 dias e média faturada no ano com a empresa maior que R$ 25000 → visitar a cada 14 dias.
- Pré-inativos Curva B: mesmo ramo e recência de positivação global em 150 days e média faturada no ano com a empresa maior que R$ 10000 → visitar a cada 14 dias.
- Pré-inativos Curva C: mesmo ramo e recência de positivação em 150 dias (observe que aqui a condição usa “recência de positivação” sem o termo global) → visitar a cada 14 dias.
- Inativos Curva A: mesmo ramo e média faturada no ano com a empresa maior que R$ 25000 → visitar a cada 14 dias.
- Inativos Curva B: mesmo ramo e média faturada no ano com a empresa maior que R$ 10000 → visitar a cada 14 dias.
- Inativos Curva C: mesmo ramo → visitar a cada 14 dias.

Região sul_sudeste_centrooeste — segmento EPI e LICITACAO:
- Ativos Curva A: ramo igual EPI,LICITACAO e recência de positivação global em 120 dias e média faturada no ano com a empresa maior que R$ 25000 → 14 dias.
- Ativos Curva B: mesmo ramo e recência de positivação global em 120 dias e média faturada no ano com a empresa maior que R$ 10000 → 21 dias.
- Ativos Curva C: mesmo ramo e recência de positivação global em 120 dias → 28 dias.
- Pré-inativos Curva A: mesmo ramo e recência de positivação global em 150 dias e média faturada no ano com a empresa maior que R$ 25000 → 14 dias.
- Pré-inativos Curva B: mesmo ramo e recência de positivação global em 150 dias e média faturada no ano com a empresa maior que R$ 10000 → 14 dias.
- Pré-inativos Curva C: mesmo ramo e recência de positivação global em 150 dias → 14 dias.
- Inativos Curva A: mesmo ramo e média faturada no ano com a empresa maior que R$ 25000 → 14 dias.
- Inativos Curva B: mesmo ramo e média faturada no ano com a empresa maior que R$ 10000 → 14 dias.
- Inativos Curva C: mesmo ramo → 14 dias.

Região sul_sudeste_centrooeste — segmento ATACADO (Atacado/Distribuidores):
- Ativos Curva A: ramo igual ATACADO e recência de positivação global em 120 dias e média faturada no ano com a empresa maior que R$ 50000 → 10 dias.
- Ativos Curva B: mesmo ramo e recência de positivação global em 120 dias e média faturada no ano com a empresa maior que R$ 25000 → 14 dias.
- Ativos Curva C: mesmo ramo e recência de positivação global em 120 dias → 21 dias.
- Pré-inativos Curva A: mesmo ramo e recência de positivação global em 150 days e média faturada no ano com a empresa maior que R$ 50000 → 7 dias.
- Pré-inativos Curva B: mesmo ramo e recência de positivação global em 150 dias e média faturada no ano com a empresa maior que R$ 25000 → 10 dias.
- Pré-inativos Curva C: mesmo ramo e recência de positivação global em 150 dias → 14 dias.
- Inativos Curva A: mesmo ramo e média faturada no ano com a empresa maior que R$ 50000 → 10 dias.
- Inativos Curva B: mesmo ramo e média faturada no ano com a empresa maior que R$ 25000 → 10 dias.
- Inativos Curva C: mesmo ramo → 21 dias.

Região sul_sudeste_centrooeste — segmento CONS. FINAL (Corporativo/Consumidor):
- Ativos Curva A: ramo igual CONS. FINAL e recência de positivação global em 120 dias e média faturada no ano com a empresa maior que R$ 15000 → 28 dias.
- Ativos Curva B: mesmo ramo e recência de positivação global em 120 dias e média faturada no ano com a empresa maior que R$ 10000 → 28 dias.
- Ativos Curva C: mesmo ramo e recência de positivação global em 120 dias → 28 dias.
- Pré-inativos Curva A: mesmo ramo e recência de positivação global em 150 dias e média faturada no ano com a empresa maior que R$ 15000 → 14 dias.
- Pré-inativos Curva B: mesmo ramo e recência de positivação global em 150 dias e média faturada no ano com a empresa maior que R$ 10000 → 14 dias.
- Pré-inativos Curva C: mesmo ramo e recência de positivação global em 150 dias → 14 dias.
- Inativos Curva A: mesmo ramo e média faturada no ano com a empresa maior que R$ 15000 → 28 dias.
- Inativos Curva B: mesmo ramo e média faturada no ano com a empresa maior que R$ 10000 → 28 dias.
- Inativos Curva C: mesmo ramo → 28 dias.

Região norte_nordeste — segmentos MATCON, FERRAGISTA, AGROPECUARIA e HOME CENTER:
- Ativos Curva A: ramo igual MATCON,FERRAGISTA,AGROPECUARIA,HOME CENTER e recência de positivação global em 150 days e média faturada no ano com a empresa maior que R$ 25000 → 14 dias.
- Ativos Curva B: mesmo ramo e recência de positivação global em 150 dias e média faturada no ano com a empresa maior que R$ 10000 → 21 dias.
- Ativos Curva C: mesmo ramo e recência de positivação global em 150 dias → 28 dias.
- Pré-inativos Curva A: mesmo ramo e recência de positivação global em 180 days e média faturada no ano com a empresa maior que R$ 25000 → 14 dias.
- Pré-inativos Curva B: mesmo ramo e recência de positivação global em 180 days e média faturada no ano com a empresa maior que R$ 10000 → 14 dias.
- Pré-inativos Curva C: mesmo ramo e recência de positivação global em 180 days → 14 dias.
- Inativos Curva A: mesmo ramo e média faturada no ano com a empresa maior que R$ 25000 → 14 dias.
- Inativos Curva B: mesmo ramo e média faturada no ano com a empresa maior que R$ 10000 → 14 dias.
- Inativos Curva C: mesmo ramo → 14 dias.

Região norte_nordeste — segmento EPI e LICITACAO:
- Ativos Curva A: ramo igual EPI,LICITACAO e recência de positivação global em 150 days e média faturada no ano com a empresa maior que R$ 25000 → 14 dias.
- Ativos Curva B: mesmo ramo e recência de positivação global em 150 days e média faturada no ano com a empresa maior que R$ 10000 → 21 dias.
- Ativos Curva C: mesmo ramo e recência de positivação global em 150 days → 28 dias.
- Pré-inativos Curva A: mesmo ramo e recência de positivação global em 180 days e média faturada no ano com a empresa maior que R$ 25000 → 14 dias.
- Pré-inativos Curva B: mesmo ramo e recência de positivação global em 180 days e média faturada no ano com a empresa maior que R$ 10000 → 14 dias.
- Pré-inativos Curva C: mesmo ramo e recência de positivação global em 180 days → 14 dias.
- Inativos Curva A: mesmo ramo e média faturada no ano com a empresa maior que R$ 25000 → 14 dias.
- Inativos Curva B: mesmo ramo e média faturada no ano com a empresa maior que R$ 10000 → 14 dias.
- Inativos Curva C: mesmo ramo → 14 dias.

Região norte_nordeste — segmento ATACADO:
- Ativos Curva A: ramo igual ATACADO e recência de positivação global em 150 days e média faturada no ano com a empresa maior que R$ 50000 → 10 dias.
- Ativos Curva B: mesmo ramo e recência de positivação global em 150 days e média faturada no ano com a empresa maior que R$ 25000 → 14 dias.
- Ativos Curva C: mesmo ramo e recência de positivação global em 150 days → 21 dias.
- Pré-inativos Curva A: mesmo ramo e recência de positivação global em 180 days e média faturada no ano com a empresa maior que R$ 50000 → 7 dias.
- Pré-inativos Curva B: mesmo ramo e recência de positivação global em 180 days e média faturada no ano com a empresa maior que R$ 25000 → 10 dias.
- Pré-inativos Curva C: mesmo ramo e recência de positivação global em 180 days → 14 dias.
- Inativos Curva A: mesmo ramo e média faturada no ano com a empresa maior que R$ 50000 → 10 dias.
- Inativos Curva B: mesmo ramo e média faturada no ano com a empresa maior que R$ 25000 → 10 dias.
- Inativos Curva C: mesmo ramo → 21 dias.

Região norte_nordeste — segmento CONS. FINAL:
- Ativos Curva A: ramo igual CONS. FINAL e recência de positivação global em 150 days e média faturada no ano com a empresa maior que R$ 15000 → 28 dias.
- Ativos Curva B: mesmo ramo e recência de positivação global em 150 days e média faturada no ano com a empresa maior que R$ 10000 → 28 dias.
- Ativos Curva C: mesmo ramo e recência de positivação global em 150 days → 28 dias.
- Pré-inativos Curva A: mesmo ramo e recência de positivação global em 180 days e média faturada no ano com a empresa maior que R$ 15000 → 14 dias.
- Pré-inativos Curva B: mesmo ramo e recência de positivação global em 180 days e média faturada no ano com a empresa maior que R$ 10000 → 14 dias.
- Pré-inativos Curva C: mesmo ramo e recência de positivação global em 180 days → 14 dias.
- Inativos Curva A: mesmo ramo e média faturada no ano com a empresa maior que R$ 15000 → 28 dias.
- Inativos Curva B: mesmo ramo e média faturada no ano com a empresa maior que R$ 10000 → 28 dias.
- Inativos Curva C (Norte e Nordeste - Corporativo/ Consumidor): existe um grupo definido pelo ramo igual CONS. FINAL, mas não há definição de frequência nesse cadastro — para esse grupo ainda não definimos de quanto em quanto tempo atender.

Por fim, há uma regra final para os vendedores do televendas que cobre “Clientes que hoje não se enquadraram nas regras padrão”: esses clientes não devem ser agendados.
