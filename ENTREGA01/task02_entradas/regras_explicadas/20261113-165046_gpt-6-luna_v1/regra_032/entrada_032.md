---
regra_id: 032
arquivo_regra: regra_032.gobr
hash_regra_sha256: 599e19af41a7c2972337a19e241d6dfa32c699957f0c6c348af47062e138cd44
arquivo_prompt: prompt_v1.md
hash_prompt_sha256: 40b5974705636c81d4d57c25c412ca473605bb769027303c4200113603a52462
modelo: gpt-6-luna
fornecedor: openai
temperatura: 1.0 (padrao fixo do modelo)
tokens_entrada: 7548
tokens_saida: 3211
custo_usd: 0.002360
tempo_segundos: 27.22
timestamp: 2026-11-13T16:51:34-03:00
---

A equipe é o televendas, com todos os vendedores ativos. Os clientes fixos dessa equipe são separados pela UF: Paraná, Santa Catarina, Rio Grande do Sul, São Paulo, Rio de Janeiro, Minas Gerais, Espírito Santo, Goiás, Mato Grosso, Mato Grosso do Sul e Distrito Federal ficam no grupo Sul, Sudeste e Centro-Oeste; Acre, Amapá, Amazonas, Pará, Rondônia, Roraima, Tocantins, Alagoas, Bahia, Ceará, Maranhão, Paraíba, Pernambuco, Piauí, Rio Grande do Norte e Sergipe ficam no grupo Norte e Nordeste.

Antes de definir as visitas, não agendamos clientes cuja situação na Receita Federal esteja como baixada. Prospect, em qualquer uma dessas regiões, recebe contato a cada 14 dias. Para os demais clientes, a frequência depende da região, do ramo, do tempo desde a última positivação e da média faturada no ano com a empresa. Quando houver sobreposição entre as curvas, consideramos primeiro os limites de faturamento mais altos; a curva seguinte atende quem supera seu limite, mas não o limite mais alto, e a curva C atende os demais dentro daquela classificação.

No Sul, Sudeste e Centro-Oeste, Matcon, Ferragista, Agropecuária e Home Center seguem estas frequências: clientes ativos, com positivação global nos últimos 120 dias, são visitados a cada 14 dias na curva A, quando a média anual faturada supera R$ 25000; a cada 21 dias na curva B, quando supera R$ 10000; e a cada 28 dias na curva C, sem limite de faturamento. Os pré-inativos, com positivação global em 150 dias, são visitados a cada 14 dias nas três curvas: A acima de R$ 25000, B acima de R$ 10000 e C sem limite de faturamento. Para os inativos desses ramos, a visita também é a cada 14 dias nas três curvas, sem condição de recência: A acima de R$ 25000, B acima de R$ 10000 e C sem limite de faturamento. Na curva C dos pré-inativos, a condição de recência é de positivação em 150 dias, sem a indicação de que seja global.

EPI e Licitação no Sul, Sudeste e Centro-Oeste têm os mesmos critérios e intervalos: ativos com positivação global em 120 dias recebem visita a cada 14 dias na curva A, acima de R$ 25000; a cada 21 dias na curva B, acima de R$ 10000; e a cada 28 dias na curva C, sem limite de faturamento. Pré-inativos com positivação global em 150 dias recebem visita a cada 14 dias: curva A acima de R$ 25000, curva B acima de R$ 10000 e curva C sem limite de faturamento. Inativos, sem condição de recência, também recebem visita a cada 14 dias: curva A acima de R$ 25000, curva B acima de R$ 10000 e curva C sem limite de faturamento.

Para Atacado no Sul, Sudeste e Centro-Oeste, os ativos com positivação global em 120 dias são visitados a cada 10 dias na curva A, com média anual acima de R$ 50000; a cada 14 dias na curva B, acima de R$ 25000; e a cada 21 dias na curva C, sem limite de faturamento. Os pré-inativos com positivação global em 150 dias recebem visita a cada 7 dias na curva A, acima de R$ 50000; a cada 10 dias na curva B, acima de R$ 25000; e a cada 14 dias na curva C, sem limite de faturamento. Para os inativos, sem condição de recência, a visita é a cada 10 dias nas curvas A, acima de R$ 50000, e B, acima de R$ 25000; na curva C, sem limite de faturamento, é a cada 21 dias.

Para Consumidor Final, chamado de Corporativo/Consumidor, no Sul, Sudeste e Centro-Oeste, os ativos com positivação global em 120 dias recebem visita a cada 28 dias nas três curvas: A acima de R$ 15000, B acima de R$ 10000 e C sem limite de faturamento. Os pré-inativos com positivação global em 150 dias recebem visita a cada 14 dias nas três curvas, com os mesmos limites: A acima de R$ 15000, B acima de R$ 10000 e C sem limite. Os inativos, sem condição de recência, recebem visita a cada 28 dias: curva A acima de R$ 15000, curva B acima de R$ 10000 e curva C sem limite de faturamento.

No Norte e Nordeste, Matcon, Ferragista, Agropecuária e Home Center têm os mesmos intervalos por curva, mas os prazos de positivação são diferentes dos do Sul, Sudeste e Centro-Oeste. Os ativos com positivação global em 150 dias recebem visita a cada 14 dias na curva A, acima de R$ 25000; a cada 21 dias na curva B, acima de R$ 10000; e a cada 28 dias na curva C, sem limite de faturamento. Os pré-inativos com positivação global em 180 dias recebem visita a cada 14 dias nas três curvas: A acima de R$ 25000, B acima de R$ 10000 e C sem limite. Para os inativos, sem condição de recência, a visita é a cada 14 dias nas três curvas, com os mesmos limites de faturamento.

EPI e Licitação no Norte e Nordeste também seguem os prazos de positivação de 150 dias para ativos e 180 dias para pré-inativos. Os ativos com positivação global em 150 dias recebem visita a cada 14 dias na curva A, acima de R$ 25000; a cada 21 dias na curva B, acima de R$ 10000; e a cada 28 dias na curva C, sem limite. Os pré-inativos com positivação global em 180 dias recebem visita a cada 14 dias: A acima de R$ 25000, B acima de R$ 10000 e C sem limite. Os inativos, sem condição de recência, recebem visita a cada 14 dias nas três curvas, com A acima de R$ 25000, B acima de R$ 10000 e C sem limite de faturamento.

Para Atacado no Norte e Nordeste, os ativos com positivação global em 150 dias recebem visita a cada 10 dias na curva A, acima de R$ 50000; a cada 14 dias na curva B, acima de R$ 25000; e a cada 21 dias na curva C, sem limite. Os pré-inativos com positivação global em 180 dias recebem visita a cada 7 dias na curva A, acima de R$ 50000; a cada 10 dias na curva B, acima de R$ 25000; e a cada 14 dias na curva C, sem limite. Os inativos, sem condição de recência, recebem visita a cada 10 dias nas curvas A, acima de R$ 50000, e B, acima de R$ 25000; na curva C, sem limite de faturamento, a visita é a cada 21 dias.

No Norte e Nordeste, Consumidor Final tem para os ativos com positivação global em 150 dias visitas a cada 28 dias: curva A acima de R$ 15000, curva B acima de R$ 10000 e curva C sem limite de faturamento. Para os pré-inativos com positivação global em 180 dias, a visita é a cada 14 dias nas três curvas, com os mesmos limites: A acima de R$ 15000, B acima de R$ 10000 e C sem limite. Para os inativos, a curva A, acima de R$ 15000, e a curva B, acima de R$ 10000, têm visita a cada 28 dias, sem condição de recência. Há também uma classificação de inativos curva C para esse ramo, sem condição de recência ou faturamento, mas ela não especifica intervalo de visita.

Por fim, para os clientes atendidos pelo televendas que não se enquadrarem nas situações padrão, não agendamos atendimento.
