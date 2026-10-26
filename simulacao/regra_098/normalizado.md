---
id: regra_098
origem: simulacao/regra_098/entrada.md
gobr: simulacao/regra_098/regra_098.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 1
procedencia: corpus_sintetico
---

## Regras

todos os clientes são atendidos a cada 1 dia

## Estrutura

```yaml
publico: todos os vendedores ativos
comuns: []
regras:
  - nome: Todos os clientes diariamente
    se: []
    entao: {acao: agendar, frequencia: fixa 1 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| teste CCN 11 | jargao | identificador de regra de teste |

## Lacunas

- A entrada não diz sobre qual carteira os vendedores trabalham.

## Ambiguidades

- Não fica claro se a sigla do teste designa uma empresa.
