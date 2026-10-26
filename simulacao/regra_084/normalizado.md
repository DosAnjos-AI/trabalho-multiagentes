---
id: regra_084
origem: simulacao/regra_084/entrada.md
gobr: simulacao/regra_084/regra_084.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 3
procedencia: corpus_sintetico
---

## Regras

clientes da carteira fixa inativos para o vendedor são atendidos na frequência média de inativos da empresa
clientes da carteira fixa ativos para o vendedor são atendidos na frequência média de ativos da empresa
clientes da carteira fixa que nunca tiveram venda são atendidos na frequência média de inativos da empresa

## Estrutura

```yaml
publico: todos os vendedores da empresa, campo e televendas
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
| televendas | jargao | atendimento por telefone |
| campo | jargao | atendimento presencial |

## Lacunas

- A entrada não informa o valor em dias das frequências médias de ativos e de inativos da empresa, nem como essa média é calculada.

## Ambiguidades

- Não fica claro se "nunca tiveram venda" se refere à empresa toda ou ao vendedor.
