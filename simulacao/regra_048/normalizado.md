---
id: regra_048
origem: simulacao/regra_048/entrada.md
gobr: simulacao/regra_048/regra_048.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 12
procedencia: corpus_sintetico
---

## Regras

cliente ativo e adimplente do televendas é atendido a cada 14 dias
cliente ativo e inadimplente do televendas é atendido a cada 7 dias
cliente inativo e adimplente do televendas é atendido a cada 30 dias
cliente inativo e inadimplente do televendas é atendido a cada 60 dias
cliente sem venda do televendas é atendido a cada 30 dias
o que sobrar na carteira do televendas, os prospects, é atendido a cada 30 dias
cliente ativo e adimplente do campo é atendido a cada 7 dias
cliente ativo e inadimplente do campo é atendido a cada 14 dias
cliente inativo e adimplente do campo é atendido a cada 14 dias
cliente inativo e inadimplente do campo é atendido a cada 30 dias
cliente sem venda do campo é atendido a cada 14 dias
os prospects da carteira do campo são atendidos a cada 14 dias

## Estrutura

```yaml
publico: time de televendas e time de campo
comuns: []
regras:
  - nome: Ativos adimplentes do televendas
    publico: time de televendas
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa do televendas, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Ativos inadimplentes do televendas
    publico: time de televendas
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa do televendas, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos adimplentes do televendas
    publico: time de televendas
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa do televendas, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Inativos inadimplentes do televendas
    publico: time de televendas
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa do televendas, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: agendar, frequencia: fixa 60 dias}
  - nome: Sem venda do televendas
    publico: time de televendas
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa do televendas, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Restante do televendas, prospects
    publico: time de televendas
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa do televendas, alcance: grupo}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Ativos adimplentes do campo
    publico: time de campo
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa do campo, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Ativos inadimplentes do campo
    publico: time de campo
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa do campo, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Inativos adimplentes do campo
    publico: time de campo
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa do campo, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Inativos inadimplentes do campo
    publico: time de campo
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa do campo, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Sem venda do campo
    publico: time de campo
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa do campo, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Restante do campo, prospects
    publico: time de campo
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa do campo, alcance: grupo}
    entao: {acao: agendar, frequencia: fixa 14 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| campo | jargao | atendimento presencial |
| carteira fixa | jargao | clientes vinculados a um vendedor ou time |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| sem venda | jargao | cliente que nunca comprou |
| prospect | jargao | cliente potencial ainda não convertido |

## Lacunas

- A entrada não define o prazo que separa ativo de inativo.

## Ambiguidades

- No televendas, a última regra vale para "o que sobrar", identificado como os prospects; no campo, a regra de prospects aparece sem a palavra "sobrar". Ambas foram tratadas como regra residual da carteira, sem critério próprio de prospect.
