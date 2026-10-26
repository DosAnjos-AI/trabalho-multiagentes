---
id: regra_020
origem: simulacao/regra_020/entrada.md
gobr: simulacao/regra_020/regra_020.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 1
procedencia: corpus_sintetico
---

## Regras

todo cliente da carteira fixa é atendido a cada 7 dias

## Estrutura

```yaml
publico: todos os vendedores da empresa
comuns: []
regras:
  - nome: Todos os clientes a cada 7 dias
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 7 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Trenas | empresa_foco | EMPRESA_FOCO |
| carteira fixa | jargao | clientes vinculados a um vendedor |

## Lacunas

- nenhuma

## Ambiguidades

- nenhuma
