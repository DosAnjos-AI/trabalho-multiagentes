---
id: regra_018
origem: simulacao/regra_018/entrada.md
gobr: simulacao/regra_018/regra_018.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 3
procedencia: corpus_sintetico
---

## Regras

clientes da carteira fixa inativos para o vendedor recebem a frequência típica dos inativos da empresa
clientes da carteira fixa ativos para o vendedor recebem a frequência típica dos ativos da empresa
clientes da carteira fixa sem nenhuma venda registrada seguem a frequência típica dos inativos da empresa

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
| Govendas | jargao | plataforma de vendas |
| carteira fixa | jargao | clientes vinculados a um vendedor |
| sem venda | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não informa o valor em dias das frequências típicas de ativos e de inativos da empresa.

## Ambiguidades

- Não fica claro se "nenhuma venda registrada" se refere à empresa toda ou ao vendedor.
