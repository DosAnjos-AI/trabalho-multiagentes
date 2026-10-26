---
id: regra_046
origem: simulacao/regra_046/entrada.md
gobr: simulacao/regra_046/regra_046.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 4
procedencia: corpus_sintetico
---

## Regras

cliente ativo para o vendedor é atendido a cada 7 dias
cliente inativo e adimplente é atendido a cada 14 dias
cliente inativo e inadimplente é atendido a cada 30 dias
o restante da carteira, os sem venda, é atendido a cada 7 dias

## Estrutura

```yaml
publico: todos os vendedores da empresa
comuns:
  - {tipo: carteira, op: igual_a, valor: carteira fixa, alcance: vendedor}
regras:
  - nome: Ativos a cada 7 dias
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos adimplentes a cada 14 dias
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Inativos inadimplentes a cada 30 dias
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Restante a cada 7 dias
    se: []
    entao: {acao: agendar, frequencia: fixa 7 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| carteira fixa | jargao | clientes vinculados a um vendedor |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| sem venda | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não define o prazo que separa ativo de inativo.

## Ambiguidades

- A última regra vale para "o restante", identificado como os sem venda, mas sem critério explícito que a restrinja a eles.
