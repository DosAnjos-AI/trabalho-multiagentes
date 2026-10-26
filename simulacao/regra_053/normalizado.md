---
id: regra_053
origem: simulacao/regra_053/entrada.md
gobr: simulacao/regra_053/regra_053.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 8
procedencia: corpus_sintetico
---

## Regras

cliente ativo e adimplente do televendas é atendido a cada 14 dias
cliente ativo e inadimplente do televendas é atendido a cada 30 dias
cliente inativo e adimplente do televendas é atendido a cada 7 dias
cliente inativo e inadimplente do televendas não é agendado
cliente sem vendas do televendas é atendido a cada 7 dias
cliente inativo do campo recebe a frequência média dos inativos da empresa, com a preferência de dia do vendedor
cliente ativo do campo recebe a frequência média dos ativos da empresa, com a preferência de dia do vendedor
cliente sem venda do campo segue a frequência média dos inativos da empresa, com a preferência de dia do vendedor

## Estrutura

```yaml
publico: time de televendas e time de campo
comuns: []
regras:
  - nome: Ativos adimplentes do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Ativos inadimplentes do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Inativos adimplentes do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Não agendar inativos inadimplentes do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Sem vendas do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Configuração padrão de inativos do campo
    publico: time de campo
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: periodo_vigencia, op: igual_a, valor: preferência do vendedor, unidade: periodo_nomeado, alcance: vendedor}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Configuração padrão de ativos do campo
    publico: time de campo
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: periodo_vigencia, op: igual_a, valor: preferência do vendedor, unidade: periodo_nomeado, alcance: vendedor}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Configuração padrão de sem venda do campo
    publico: time de campo
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
      - {tipo: periodo_vigencia, op: igual_a, valor: preferência do vendedor, unidade: periodo_nomeado, alcance: vendedor}
    entao: {acao: agendar, frequencia: calculada}
termos_fora_vocabulario:
  - preferência de dia do vendedor
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| campo | jargao | atendimento presencial |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| sem vendas | jargao | cliente que nunca comprou |
| configuração padrão | jargao | frequências calculadas pela média da empresa |

## Lacunas

- A entrada não diz se os times trabalham sobre carteira fixa.
- A entrada não informa o valor em dias das médias de ativos e inativos da empresa.

## Ambiguidades

- A preferência de dia do vendedor é preferência de agendamento, não condição; registrada como critério de período por falta de campo próprio.
