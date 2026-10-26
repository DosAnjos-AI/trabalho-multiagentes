---
id: regra_056
origem: simulacao/regra_056/entrada.md
gobr: simulacao/regra_056/regra_056.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 7
procedencia: corpus_sintetico
---

## Regras

cliente sem venda da carteira de prospecção é atendido a cada 30 dias, com a preferência de dia do vendedor
qualquer outro cliente da carteira de prospecção, quem já comprou, não é agendado
cliente ativo e adimplente é atendido a cada 14 dias, com a preferência de dia do vendedor
cliente inativo e adimplente é atendido a cada 30 dias, com a preferência de dia do vendedor
cliente ativo e inadimplente é atendido a cada 30 dias, com a preferência de dia do vendedor
cliente inativo e inadimplente não é agendado
cliente sem vendas é atendido a cada 30 dias, com a preferência de dia do vendedor

## Estrutura

```yaml
publico: time de prospecção e demais vendedores da empresa
comuns: []
regras:
  - nome: Sem venda da prospecção
    publico: time de prospecção, VENDEDOR_01 e VENDEDOR_02
    se:
      - {tipo: carteira, op: igual_a, valor: carteira do time de prospecção, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
      - {tipo: periodo_vigencia, op: igual_a, valor: preferência do vendedor, unidade: periodo_nomeado, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Não agendar quem já comprou na prospecção
    publico: time de prospecção, VENDEDOR_01 e VENDEDOR_02
    se:
      - {tipo: carteira, op: igual_a, valor: carteira do time de prospecção, alcance: grupo}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Ativos adimplentes
    publico: todos os vendedores exceto VENDEDOR_01 e VENDEDOR_02
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
      - {tipo: periodo_vigencia, op: igual_a, valor: preferência do vendedor, unidade: periodo_nomeado, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Inativos adimplentes
    publico: todos os vendedores exceto VENDEDOR_01 e VENDEDOR_02
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
      - {tipo: periodo_vigencia, op: igual_a, valor: preferência do vendedor, unidade: periodo_nomeado, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Ativos inadimplentes
    publico: todos os vendedores exceto VENDEDOR_01 e VENDEDOR_02
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
      - {tipo: periodo_vigencia, op: igual_a, valor: preferência do vendedor, unidade: periodo_nomeado, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Não agendar inativos inadimplentes
    publico: todos os vendedores exceto VENDEDOR_01 e VENDEDOR_02
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Sem vendas
    publico: todos os vendedores exceto VENDEDOR_01 e VENDEDOR_02
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
      - {tipo: periodo_vigencia, op: igual_a, valor: preferência do vendedor, unidade: periodo_nomeado, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 30 dias}
termos_fora_vocabulario:
  - preferência de dia do vendedor
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Destra | empresa_foco | EMPRESA_FOCO |
| vendedor de ID 50 | vendedor | VENDEDOR_01 |
| vendedor de ID 53 | vendedor | VENDEDOR_02 |
| prospecção | jargao | busca de clientes novos |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| sem venda | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não diz se o restante da empresa trabalha sobre carteira fixa.

## Ambiguidades

- A preferência de dia do vendedor é preferência de agendamento, não condição; registrada como critério de período por falta de campo próprio.
