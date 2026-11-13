---
regra_id: 032
arquivo_regra: regra_032.gobr
hash_regra_sha256: 599e19af41a7c2972337a19e241d6dfa32c699957f0c6c348af47062e138cd44
arquivo_prompt: prompt_v2.md
hash_prompt_sha256: d7c1517e7309120a292faa10f14a10a8a33e6456183253cbf924817242d80d73
modelo: gpt-5-mini-2025-08-07
fornecedor: openai
temperatura: 1.0 (padrao fixo do modelo)
tokens_entrada: 8542
tokens_saida: 6047
custo_usd: 0.014230
tempo_segundos: 57.38
timestamp: 2026-11-13T18:15:16-03:00
---

A gente trabalha com a equipe de televendas: todos os vendedores do televendas que estão ativados no sistema atendem essa carteira e cada regra vale sobre os clientes fixos de televendas. Para organizar por região criamos duas carteiras geográficas: a carteira sul_sudeste_centrooeste são os clientes fixos de televendas cujos estados são PR, SC, RS, SP, RJ, MG, ES, GO, MT, MS e DF; a carteira norte_nordeste são os clientes fixos de televendas cujos estados são AC, AP, AM, PA, RO, RR, TO, AL, BA, CE, MA, PB, PE, PI, RN e SE.

Na hora de gerar visitas a gente aplica algumas exceções antes de qualquer frequência: todos os clientes da equipe de televendas com o status na Receita Federal igual a baixada não são agendados. Depois disso tratamos prospects: clientes que estão no ciclo de vida prospect com a empresa e que pertencem a qualquer uma das duas carteiras (sul_sudeste_centrooeste ou norte_nordeste) devem ser visitados a cada 14 dias.

Em seguida aplicamos as regras por região, por segmento e por curva. Se um cliente se enquadrar em mais de uma condição, a prioridade segue essa sequência (exceção de baixados e prospects já mencionados); o que não entrar em nenhuma das regras padrão fica sem agendamento. Abaixo está o que fazemos em cada região e segmento, com todas as condições e os prazos exatos.

Para Sul, Sudeste e Centro-Oeste, por segmentos:

- Para os ramos MATCON, FERRAGISTA, AGROPECUARIA e HOME CENTER:
  - cliente que comprou com qualquer vendedor da empresa nos últimos 120 dias e cuja média faturada no ano com a empresa é maior que R$ 25000: visitar a cada 14 dias.
  - cliente que comprou com qualquer vendedor da empresa nos últimos 120 dias e cuja média faturada no ano com a empresa é maior que R$ 10000: visitar a cada 21 dias.
  - cliente que comprou com qualquer vendedor da empresa nos últimos 120 dias (sem critério de média): visitar a cada 28 dias.
  - cliente que comprou com qualquer vendedor da empresa nos últimos 150 dias e cuja média faturada no ano com a empresa é maior que R$ 25000 (pré-inativo): visitar a cada 14 dias.
  - cliente que comprou com qualquer vendedor da empresa nos últimos 150 days e cuja média faturada no ano com a empresa é maior que R$ 10000 (pré-inativo): visitar a cada 14 days.
  - cliente que comprou com qualquer vendedor da empresa nos últimos 150 dias (pré-inativo, sem critério de média): visitar a cada 14 dias.
  - cliente com média faturada no ano com a empresa maior que R$ 25000 e classificado como inativo: visitar a cada 14 dias.
  - cliente com média faturada no ano com a empresa maior que R$ 10000 e classificado como inativo: visitar a cada 14 dias.
  - clientes inativos desse ramo sem as condições de média acima: visitar a cada 14 dias.

- Para os ramos EPI e LICITACAO:
  - quem comprou com qualquer vendedor da empresa nos últimos 120 dias e média anual > R$ 25000: visitar a cada 14 dias.
  - quem comprou com qualquer vendedor da empresa nos últimos 120 dias e média anual > R$ 10000: visitar a cada 21 dias.
  - quem comprou com qualquer vendedor da empresa nos últimos 120 days: visitar a cada 28 days.
  - pré-inativos (compra nos últimos 150 days) com média anual > R$ 25000: visitar a cada 14 days.
  - pré-inativos com média anual > R$ 10000: visitar a cada 14 days.
  - pré-inativos com recência de compra de 150 dias (sem critério de média): visitar a cada 14 days.
  - inativos com média anual > R$ 25000: visitar a cada 14 days.
  - inativos com média anual > R$ 10000: visitar a cada 14 days.
  - inativos sem critério de média: visitar a cada 14 days.

- Para o ramo ATACADO (Atacado/ Distribuidores):
  - quem comprou com qualquer vendedor da empresa nos últimos 120 days e média anual > R$ 50000: visitar a cada 10 dias.
  - quem comprou com qualquer vendedor da empresa nos últimos 120 days e média anual > R$ 25000: visitar a cada 14 days.
  - quem comprou com qualquer vendedor da empresa nos últimos 120 days (sem critério de média): visitar a cada 21 days.
  - pré-inativos (compra nos últimos 150 days) com média anual > R$ 50000: visitar a cada 7 days.
  - pré-inativos com média anual > R$ 25000: visitar a cada 10 days.
  - pré-inativos com recência de compra de 150 days (sem critério de média): visitar a cada 14 days.
  - inativos com média anual > R$ 50000: visitar a cada 10 days.
  - inativos com média anual > R$ 25000: visitar a cada 10 days.
  - inativos sem critério de média: visitar a cada 21 days.

- Para o ramo CONS. FINAL (Corporativo/ Consumidor):
  - quem comprou com qualquer vendedor da empresa nos últimos 120 days e média anual > R$ 15000: visitar a cada 28 days.
  - quem comprou com qualquer vendedor da empresa nos últimos 120 days e média anual > R$ 10000: visitar a cada 28 days.
  - quem comprou com qualquer vendedor da empresa nos últimos 120 days (sem critério de média): visitar a cada 28 days.
  - pré-inativos (compra nos últimos 150 days) com média anual > R$ 15000: visitar a cada 14 days.
  - pré-inativos com média anual > R$ 10000: visitar a cada 14 days.
  - pré-inativos com recência de compra de 150 days (sem critério de média): visitar a cada 14 days.
  - inativos com média anual > R$ 15000: visitar a cada 28 days.
  - inativos com média anual > R$ 10000: visitar a cada 28 days.
  - inativos sem critério de média: visitar a cada 28 days.

Para Norte e Nordeste, as regras são parecidas por segmento, mas com recência e alguns prazos diferentes:

- Para os ramos MATCON, FERRAGISTA, AGROPECUARIA e HOME CENTER:
  - ativos: compra com qualquer vendedor nos últimos 150 days e média anual > R$ 25000: visitar a cada 14 days.
  - ativos: compra nos últimos 150 days e média anual > R$ 10000: visitar a cada 21 days.
  - ativos: compra nos últimos 150 days (sem média): visitar a cada 28 days.
  - pré-inativos: compra nos últimos 180 days e média anual > R$ 25000: visitar a cada 14 days.
  - pré-inativos: compra nos últimos 180 days e média anual > R$ 10000: visitar a cada 14 days.
  - pré-inativos: compra nos últimos 180 days (sem média): visitar a cada 14 days.
  - inativos com média anual > R$ 25000: visitar a cada 14 days.
  - inativos com média anual > R$ 10000: visitar a cada 14 days.
  - inativos sem critério de média: visitar a cada 14 days.

- Para os ramos EPI e LICITACAO:
  - ativos: compra com qualquer vendedor nos últimos 150 days e média anual > R$ 25000: visitar a cada 14 days.
  - ativos: compra nos últimos 150 days e média anual > R$ 10000: visitar a cada 21 days.
  - ativos: compra nos últimos 150 days: visitar a cada 28 days.
  - pré-inativos: compra nos últimos 180 days e média anual > R$ 25000: visitar a cada 14 days.
  - pré-inativos: compra nos últimos 180 days e média anual > R$ 10000: visitar a cada 14 days.
  - pré-inativos: compra nos últimos 180 days (sem média): visitar a cada 14 days.
  - inativos com média anual > R$ 25000: visitar a cada 14 days.
  - inativos com média anual > R$ 10000: visitar a cada 14 days.
  - inativos sem critério de média: visitar a cada 14 days.

- Para o ramo ATACADO:
  - ativos: compra com qualquer vendedor nos últimos 150 days e média anual > R$ 50000: visitar a cada 10 days.
  - ativos: compra nos últimos 150 days e média anual > R$ 25000: visitar a cada 14 days.
  - ativos: compra nos últimos 150 days (sem média): visitar a cada 21 days.
  - pré-inativos: compra nos últimos 180 days e média anual > R$ 50000: visitar a cada 7 days.
  - pré-inativos: compra nos últimos 180 days e média anual > R$ 25000: visitar a cada 10 days.
  - pré-inativos: compra nos últimos 180 days (sem média): visitar a cada 14 days.
  - inativos com média anual > R$ 50000: visitar a cada 10 days.
  - inativos com média anual > R$ 25000: visitar a cada 10 days.
  - inativos sem critério de média: visitar a cada 21 days.

- Para o ramo CONS. FINAL (Corporativo/ Consumidor) no Norte/Nordeste:
  - ativos: compra com qualquer vendedor nos últimos 150 days e média anual > R$ 15000: visitar a cada 28 days.
  - ativos: compra nos últimos 150 days e média anual > R$ 10000: visitar a cada 28 days.
  - ativos: compra nos últimos 150 days (sem média): visitar a cada 28 days.
  - pré-inativos: compra nos últimos 180 days e média anual > R$ 15000: visitar a cada 14 days.
  - pré-inativos: compra nos últimos 180 days e média anual > R$ 10000: visitar a cada 14 days.
  - pré-inativos: compra nos últimos 180 days (sem média): visitar a cada 14 days.
  - inativos com média anual > R$ 15000: visitar a cada 28 days.
  - inativos com média anual > R$ 10000: visitar a cada 28 days.
  - para a Curva C de inativos desse segmento na carteira norte_nordeste não há, atualmente, definição de periodicidade de atendimento registrada.

Por fim, qualquer cliente da equipe de televendas que hoje não se enquadrar em nenhuma das regras padrão acima ficará sem agendamento.

Resumo prático: atendem todos os vendedores ativados do televendas, as carteiras são os clientes fixos de televendas divididos por estado conforme as duas listas; primeiro excluímos os baixados na Receita (não agendados), depois prospect a cada 14 dias, depois aplicamos as regras por região, ramo e curva conforme os prazos e limites de média anual e recência descritos item a item; e o que sobrar dos clientes da equipe não é agendado.
