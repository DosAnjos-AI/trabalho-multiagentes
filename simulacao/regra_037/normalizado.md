---
id: regra_037
origem: simulacao/regra_037/entrada.md
gobr: simulacao/regra_037/regra_037.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 1
procedencia: corpus_sintetico
---

## Regras

todo cliente da carteira fixa é atendido a cada 30 dias, preferindo dias úteis

## Estrutura

```yaml
publico: todos os vendedores da empresa
comuns: []
regras:
  - nome: Todos os clientes a cada 30 dias
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa, alcance: vendedor}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 30 dias}
termos_fora_vocabulario:
  - preferência por dias úteis
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Magnavet | empresa_foco | EMPRESA_FOCO |
| carteira fixa | jargao | clientes vinculados a um vendedor |

## Lacunas

- nenhuma

## Ambiguidades

- "Prefere que caia em dia útil" é preferência de agendamento, não condição; registrada como critério de período por falta de campo próprio.
