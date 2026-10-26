---
id: regra_089
origem: simulacao/regra_089/entrada.md
gobr: simulacao/regra_089/regra_089.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 5
procedencia: corpus_sintetico
---

## Regras

prospect é atendido a cada 7 dias
cliente ativo e adimplente é atendido a cada 7 dias
cliente ativo e inadimplente é atendido a cada 14 dias
cliente inativo e adimplente é atendido a cada 7 dias
cliente inativo e inadimplente é atendido a cada 14 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Prospects
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Ativos adimplentes
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Ativos inadimplentes
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Inativos adimplentes
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos inadimplentes
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: agendar, frequencia: fixa 14 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| MSJ | empresa_foco | EMPRESA_FOCO |
| televendas | jargao | atendimento por telefone |
| prospect | jargao | cliente que nunca comprou |
| inadimplente | jargao | cliente com pendência financeira em aberto |

## Lacunas

- A entrada não define o prazo que separa ativo de inativo.
- A entrada não diz se o televendas trabalha sobre carteira fixa.

## Ambiguidades

- nenhuma
