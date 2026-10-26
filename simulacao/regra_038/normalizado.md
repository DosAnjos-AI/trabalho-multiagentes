---
id: regra_038
origem: simulacao/regra_038/entrada.md
gobr: simulacao/regra_038/regra_038.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 4
procedencia: corpus_sintetico
---

## Regras

cliente ativo para o vendedor é atendido a cada 7 dias
cliente inativo e adimplente é atendido a cada 14 dias
cliente inativo e inadimplente é atendido a cada 30 dias
todos os demais clientes da carteira fixa, na prática os sem venda, são atendidos a cada 14 dias

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
  - nome: Demais clientes a cada 14 dias
    se: []
    entao: {acao: agendar, frequencia: fixa 14 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Gomes | empresa_foco | EMPRESA_FOCO |
| carteira fixa | jargao | clientes vinculados a um vendedor |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| sem venda | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não define o prazo que separa ativo de inativo.

## Ambiguidades

- A última regra vale para "todo o resto"; a entrada diz que na prática são os clientes sem venda, mas não restringe a regra a eles.
