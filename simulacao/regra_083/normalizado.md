---
id: regra_083
origem: simulacao/regra_083/entrada.md
gobr: simulacao/regra_083/regra_083.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 3
procedencia: corpus_sintetico
---

## Regras

cliente inativo recebe a frequência média dos inativos da empresa
cliente ativo recebe a frequência média dos ativos da empresa
cliente sem venda segue a frequência média dos inativos da empresa

## Estrutura

```yaml
publico: todos os vendedores da empresa
comuns:
  - {tipo: carteira, op: igual_a, valor: carteira fixa, alcance: vendedor}
regras:
  - nome: Frequência de inativos
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Frequência de ativos
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
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
| Brida | empresa_foco | EMPRESA_FOCO |
| goVendas | jargao | plataforma de vendas |
| carteira fixa | jargao | clientes vinculados a um vendedor |
| sem venda | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não informa o valor em dias das médias de ativos e inativos da empresa.

## Ambiguidades

- nenhuma
