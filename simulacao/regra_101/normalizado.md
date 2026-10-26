---
id: regra_101
origem: simulacao/regra_101/entrada.md
gobr: simulacao/regra_101/regra_101.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 11
procedencia: corpus_sintetico
---

## Regras

cliente ativo do televendas é atendido a cada 7 dias
cliente inativo do televendas é atendido a cada 30 dias
cliente sem venda do televendas é atendido a cada 7 dias
cliente ativo da capital é atendido a cada 7 dias
cliente inativo e adimplente da capital é atendido a cada 14 dias
cliente inativo e inadimplente da capital não é agendado
cliente sem venda da capital é atendido a cada 14 dias
cliente ativo do interior é atendido a cada 14 dias
cliente inativo e adimplente do interior é atendido a cada 30 dias
cliente inativo e inadimplente do interior não é agendado
cliente sem venda do interior é atendido a cada 30 dias

## Estrutura

```yaml
publico: time de televendas, time da capital e time do interior
comuns: []
regras:
  - nome: Ativos do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Sem venda do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Ativos da capital
    publico: time da capital, todos os vendedores de campo exceto VENDEDOR_01, VENDEDOR_02 e VENDEDOR_03
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos adimplentes da capital
    publico: time da capital, todos os vendedores de campo exceto VENDEDOR_01, VENDEDOR_02 e VENDEDOR_03
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Não agendar inativos inadimplentes da capital
    publico: time da capital, todos os vendedores de campo exceto VENDEDOR_01, VENDEDOR_02 e VENDEDOR_03
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Sem venda da capital
    publico: time da capital, todos os vendedores de campo exceto VENDEDOR_01, VENDEDOR_02 e VENDEDOR_03
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Ativos do interior
    publico: time do interior, VENDEDOR_01, VENDEDOR_02 e VENDEDOR_03
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Inativos adimplentes do interior
    publico: time do interior, VENDEDOR_01, VENDEDOR_02 e VENDEDOR_03
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Não agendar inativos inadimplentes do interior
    publico: time do interior, VENDEDOR_01, VENDEDOR_02 e VENDEDOR_03
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Sem venda do interior
    publico: time do interior, VENDEDOR_01, VENDEDOR_02 e VENDEDOR_03
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 30 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Propec | empresa_foco | EMPRESA_FOCO |
| vendedor 17 | vendedor | VENDEDOR_01 |
| vendedor 18 | vendedor | VENDEDOR_02 |
| vendedor 13 | vendedor | VENDEDOR_03 |
| televendas | jargao | atendimento por telefone |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| sem venda | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não diz se os times trabalham sobre carteira fixa.
- A entrada não define o prazo que separa ativo de inativo.

## Ambiguidades

- nenhuma
