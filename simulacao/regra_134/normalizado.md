---
id: regra_134
origem: simulacao/regra_134/entrada.md
gobr: simulacao/regra_134/regra_134.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 1
procedencia: corpus_sintetico
---

## Regras

todos os clientes são atendidos a cada 15 dias

## Estrutura

```yaml
publico: todos os vendedores ativos
comuns: []
regras:
  - nome: Todos os clientes a cada 15 dias
    se: []
    entao: {acao: agendar, frequencia: fixa 15 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Linavet | empresa_foco | EMPRESA_FOCO |

## Lacunas

- A entrada não diz sobre qual carteira os vendedores trabalham.

## Ambiguidades

- nenhuma
