---
id: regra_144
origem: simulacao/regra_144/entrada.md
gobr: simulacao/regra_144/regra_144.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 8
procedencia: corpus_sintetico
---

## Regras

prospect é atendido a cada 14 dias
cliente inadimplente é atendido a cada 21 dias
cliente com uma única compra e cadastrado há mais de 30 dias é atendido a cada 28 dias
cliente com compra entre 31 e 60 dias é atendido a cada 30 dias
cliente com compra entre 61 e 90 dias, em risco de inatividade, é atendido a cada 10 dias
cliente inativo é atendido a cada 21 dias
cliente que compra regularmente, nos últimos 30 dias, é atendido a cada 21 dias
cliente que compra regularmente, nos últimos 30 dias, é atendido a cada 28 dias

## Estrutura

```yaml
publico: todos os vendedores ativos e times por tipo de cliente
comuns: []
regras:
  - nome: Prospects
    publico: todos os vendedores ativos
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Inadimplentes
    publico: todos os vendedores ativos
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Boas-vindas
    publico: todos os vendedores ativos
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única}
      - {tipo: situacao_cadastro, op: maior_que, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 28 dias}
  - nome: Compra entre 31 e 60 dias
    publico: todos os vendedores ativos
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [31, 60], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Em ruptura
    publico: todos os vendedores ativos
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [61, 90], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 10 dias}
  - nome: Resgate de inativos
    publico: todos os vendedores ativos
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Compra regular para fabricantes e revendas
    publico: times de fabricantes e de revendas, VENDEDOR_01 a VENDEDOR_04
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Compra regular para consumidor final e compra esporádica
    publico: times de consumidor final recorrente, compra esporádica e grande porte, VENDEDOR_05 e VENDEDOR_03
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 28 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| vendedor F | vendedor | VENDEDOR_01 |
| vendedor L | vendedor | VENDEDOR_02 |
| vendedor A | vendedor | VENDEDOR_03 |
| vendedor J | vendedor | VENDEDOR_04 |
| vendedor LC | vendedor | VENDEDOR_05 |
| prospect | jargao | cliente que nunca comprou |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| ruptura | jargao | cliente que parou de comprar |

## Lacunas

- A entrada não informa se as faixas de compra consideram o vendedor ou a empresa.

## Ambiguidades

- O mesmo código de vendedor aparece em mais de um time (VENDEDOR_03 em fabricantes e grande porte; VENDEDOR_05 em consumidor final recorrente e compra esporádica).
- As regras específicas dos times vêm depois das regras de todos; a ordem de avaliação define se chegam a ser aplicadas.
