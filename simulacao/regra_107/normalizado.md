---
id: regra_107
origem: simulacao/regra_107/entrada.md
gobr: simulacao/regra_107/regra_107.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 3
procedencia: corpus_sintetico
---

## Regras

cliente inativo é atendido quinzenalmente, com a preferência de dia do vendedor
cliente ativo é atendido quinzenalmente, com a preferência de dia do vendedor
cliente sem vendas é atendido quinzenalmente, sem preferência de dia definida

## Estrutura

```yaml
publico: todos os vendedores da empresa
comuns:
  - {tipo: carteira, op: igual_a, valor: carteira fixa, alcance: vendedor}
regras:
  - nome: Inativos quinzenal
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: periodo_vigencia, op: igual_a, valor: preferência do vendedor, unidade: periodo_nomeado, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Ativos quinzenal
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: periodo_vigencia, op: igual_a, valor: preferência do vendedor, unidade: periodo_nomeado, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Sem vendas quinzenal
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 15 dias}
termos_fora_vocabulario:
  - preferência de dia do vendedor
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Higicop | empresa_foco | EMPRESA_FOCO |
| carteira fixa | jargao | clientes vinculados a um vendedor |
| sem vendas | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não define o prazo que separa ativo de inativo.

## Ambiguidades

- "Quinzenal" foi registrado como 15 dias pela convenção de periodicidade; a entrada não dá o número.
- A preferência de dia do vendedor é preferência de agendamento, não condição; registrada como critério de período por falta de campo próprio.
