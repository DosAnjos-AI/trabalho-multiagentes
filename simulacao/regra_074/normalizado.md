---
id: regra_074
origem: simulacao/regra_074/entrada.md
gobr: simulacao/regra_074/regra_074.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 3
procedencia: corpus_sintetico
---

## Regras

cliente inativo é atendido a cada 45 dias, com a preferência de dia do vendedor
cliente ativo é atendido a cada 21 dias, com a preferência de dia do vendedor
cliente sem vendas é atendido a cada 45 dias, com a preferência de dia do vendedor

## Estrutura

```yaml
publico: todos os vendedores da empresa
comuns:
  - {tipo: carteira, op: igual_a, valor: carteira fixa, alcance: vendedor}
  - {tipo: periodo_vigencia, op: igual_a, valor: preferência do vendedor, unidade: periodo_nomeado, alcance: vendedor}
regras:
  - nome: Inativos a cada 45 dias
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
    entao: {acao: agendar, frequencia: fixa 45 dias}
  - nome: Ativos a cada 21 dias
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Sem vendas a cada 45 dias
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 45 dias}
termos_fora_vocabulario:
  - preferência de dia do vendedor
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Bela Forma | empresa_foco | EMPRESA_FOCO |
| carteira fixa | jargao | clientes vinculados a um vendedor |
| sem vendas | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não define o prazo que separa ativo de inativo.

## Ambiguidades

- A preferência de dia do vendedor é preferência de agendamento, não condição; registrada como critério de período por falta de campo próprio.
