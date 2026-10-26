---
id: regra_160
origem: simulacao/regra_160/entrada.md
gobr: simulacao/regra_160/regra_160.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 14
procedencia: corpus_sintetico
---

## Regras

pessoa jurídica com rota amanhã, sem visita há mais de 3 dias e sem venda com o vendedor é atendida a cada 1 dia
pessoa jurídica com rota amanhã, sem visita há mais de 3 dias e última compra entre 31 e 60 dias é atendida a cada 1 dia
pessoa jurídica com rota amanhã, sem visita há mais de 3 dias e última compra entre 61 e 90 dias é atendida a cada 1 dia
pessoa jurídica com rota amanhã, sem visita há mais de 3 dias e atividade do vendedor nos últimos 30 dias é atendida a cada 1 dia
pessoa jurídica com rota amanhã, sem visita há mais de 3 dias e inativa para o vendedor é atendida a cada 1 dia
pessoa jurídica com rota amanhã e sem visita há mais de 3 dias é atendida a cada 1 dia
pessoa jurídica sem venda com o vendedor é atendida a cada 7 dias
pessoa jurídica sem venda com o vendedor é atendida a cada 14 dias
pessoa jurídica com última compra entre 61 e 90 dias é atendida a cada 7 dias
pessoa jurídica com última compra entre 31 e 60 dias é atendida a cada 14 dias
pessoa jurídica que compra regularmente é atendida a cada 14 dias
pessoa jurídica inativa para o vendedor é atendida a cada 21 dias
cliente pessoa física é atendido a cada 14 dias
o restante, com tipo de pessoa indefinido, é atendido a cada 14 dias

## Estrutura

```yaml
publico: time de vendedores de ativos e time de vendedores de prospects
comuns: []
regras:
  - nome: Fechamento de rota, primeira compra
    publico: os dois times
    se:
      - {tipo: segmento, op: igual_a, valor: pessoa jurídica}
      - {tipo: agenda_rota, op: dentro_de, valor: 1, unidade: dias}
      - {tipo: tempo_sem_visita, op: maior_que, valor: 3, unidade: dias}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 1 dias}
  - nome: Fechamento de rota, estimular regularidade
    publico: os dois times
    se:
      - {tipo: segmento, op: igual_a, valor: pessoa jurídica}
      - {tipo: agenda_rota, op: dentro_de, valor: 1, unidade: dias}
      - {tipo: tempo_sem_visita, op: maior_que, valor: 3, unidade: dias}
      - {tipo: tempo_sem_comprar, op: entre, valor: [31, 60], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 1 dias}
  - nome: Fechamento de rota, risco de inatividade
    publico: os dois times
    se:
      - {tipo: segmento, op: igual_a, valor: pessoa jurídica}
      - {tipo: agenda_rota, op: dentro_de, valor: 1, unidade: dias}
      - {tipo: tempo_sem_visita, op: maior_que, valor: 3, unidade: dias}
      - {tipo: tempo_sem_comprar, op: entre, valor: [61, 90], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 1 dias}
  - nome: Fechamento de rota, compra regular
    publico: os dois times
    se:
      - {tipo: segmento, op: igual_a, valor: pessoa jurídica}
      - {tipo: agenda_rota, op: dentro_de, valor: 1, unidade: dias}
      - {tipo: tempo_sem_visita, op: maior_que, valor: 3, unidade: dias}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 1 dias}
  - nome: Fechamento de rota, resgate
    publico: os dois times
    se:
      - {tipo: segmento, op: igual_a, valor: pessoa jurídica}
      - {tipo: agenda_rota, op: dentro_de, valor: 1, unidade: dias}
      - {tipo: tempo_sem_visita, op: maior_que, valor: 3, unidade: dias}
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 1 dias}
  - nome: Fechamento de rota, caso geral
    publico: os dois times
    se:
      - {tipo: segmento, op: igual_a, valor: pessoa jurídica}
      - {tipo: agenda_rota, op: dentro_de, valor: 1, unidade: dias}
      - {tipo: tempo_sem_visita, op: maior_que, valor: 3, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 1 dias}
  - nome: Primeira compra, time de prospects
    publico: time de prospects, VENDEDOR_01 a VENDEDOR_04
    se:
      - {tipo: segmento, op: igual_a, valor: pessoa jurídica}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Primeira compra, time de ativos
    publico: time de ativos, televendas ativos exceto VENDEDOR_01 a VENDEDOR_04
    se:
      - {tipo: segmento, op: igual_a, valor: pessoa jurídica}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Risco de inatividade
    publico: os dois times
    se:
      - {tipo: segmento, op: igual_a, valor: pessoa jurídica}
      - {tipo: tempo_sem_comprar, op: entre, valor: [61, 90], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Estimular regularidade
    publico: os dois times
    se:
      - {tipo: segmento, op: igual_a, valor: pessoa jurídica}
      - {tipo: tempo_sem_comprar, op: entre, valor: [31, 60], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Compra regularmente
    publico: os dois times
    se:
      - {tipo: segmento, op: igual_a, valor: pessoa jurídica}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Resgate de inativos
    publico: os dois times
    se:
      - {tipo: segmento, op: igual_a, valor: pessoa jurídica}
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Pessoa física
    publico: os dois times
    se:
      - {tipo: segmento, op: igual_a, valor: pessoa física}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Pessoa física ou jurídica indefinida
    publico: os dois times
    se: []
    entao: {acao: agendar, frequencia: fixa 14 dias}
termos_fora_vocabulario:
  - pessoa jurídica
  - pessoa física
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| vendedor 2136 | vendedor | VENDEDOR_01 |
| vendedor 2179 | vendedor | VENDEDOR_02 |
| vendedor 2134 | vendedor | VENDEDOR_03 |
| vendedor 1865 | vendedor | VENDEDOR_04 |
| televendas | jargao | atendimento por telefone |
| fechamento de rota | jargao | contato na véspera da visita de rota |
| pessoa jurídica | jargao | cliente empresa |
| resgate | jargao | reativação de cliente inativo |

## Lacunas

- A entrada não informa se as faixas de última compra consideram o vendedor ou a empresa.

## Ambiguidades

- "Rota nos próximos dias, ou seja, rota marcada para amanhã" foi registrada como dentro de 1 dia.
