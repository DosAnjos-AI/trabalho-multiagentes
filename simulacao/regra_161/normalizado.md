---
id: regra_161
origem: simulacao/regra_161/entrada.md
gobr: simulacao/regra_161/regra_161.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 4
procedencia: corpus_sintetico
---

## Regras

ativo de curva A é atendido a cada 15 dias
ativo de curva B é atendido a cada 7 dias
ativo de curva C é atendido a cada 15 dias
os inativos são atendidos a cada 7 dias

## Estrutura

```yaml
publico: todos os vendedores ativos
comuns: []
regras:
  - nome: Ativos curva A
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: valor_cliente, op: igual_a, valor: curva A}
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Ativos curva B
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: valor_cliente, op: igual_a, valor: curva B}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Ativos curva C
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: valor_cliente, op: igual_a, valor: curva C}
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Inativos
    se: []
    entao: {acao: agendar, frequencia: fixa 7 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| curva ABC | jargao | faixas de cliente por faturamento |

## Lacunas

- A entrada não define os critérios das curvas A, B e C.

## Ambiguidades

- A regra de inativos não tem critério próprio e funciona como regra residual.
