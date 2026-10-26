---
id: regra_111
origem: simulacao/regra_111/entrada.md
gobr: simulacao/regra_111/regra_111.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 3
procedencia: corpus_sintetico
---

## Regras

clientes da carteira fixa inativos para o vendedor são atendidos na frequência média dos inativos da empresa
clientes da carteira fixa ativos para o vendedor são atendidos na frequência média dos ativos da empresa
clientes da carteira fixa que nunca compraram ficam com a frequência média dos inativos da empresa

## Estrutura

```yaml
publico: todos os vendedores da empresa
comuns:
  - {tipo: carteira, op: igual_a, valor: carteira fixa, alcance: vendedor}
regras:
  - nome: Frequência de inativos
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo, alcance: vendedor}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Frequência de ativos
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo, alcance: vendedor}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Frequência de clientes sem venda
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: calculada}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| goVendas | jargao | plataforma de vendas |
| carteira fixa | jargao | clientes vinculados a um vendedor |
| sem venda | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não informa o valor em dias das frequências médias de ativos e de inativos da empresa, nem o método de cálculo da média.

## Ambiguidades

- Não fica claro se "nunca compraram" se refere à empresa toda ou ao vendedor.
