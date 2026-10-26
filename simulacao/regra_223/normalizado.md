---
id: regra_223
origem: simulacao/regra_223/entrada.md
gobr: simulacao/regra_223/regra_223.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 5
procedencia: corpus_sintetico
---

## Regras

cliente com pedido nos últimos 30 dias é atendido a cada 21 dias
cliente sem pedido nos últimos 30 dias é atendido a cada 15 dias
cliente com compra na semana corrente, de segunda a sexta, não é agendado
os demais clientes são atendidos semanalmente, a cada 7 dias
todos os clientes são atendidos a cada 14 dias

## Estrutura

```yaml
publico: times de ativação, generalista e construtora
comuns: []
regras:
  - nome: Ativação, com pedido nos últimos 30 dias
    publico: time de ativação, VENDEDOR_01 a VENDEDOR_04
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Ativação, sem pedido
    publico: time de ativação, VENDEDOR_01 a VENDEDOR_04
    se: []
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Generalista, não agendar compra na semana
    publico: time generalista, VENDEDOR_05 a VENDEDOR_18
    se:
      - {tipo: tempo_sem_comprar, op: igual_a, valor: semana atual, unidade: periodo_nomeado}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Generalista, demais clientes
    publico: time generalista, VENDEDOR_05 a VENDEDOR_18
    se: []
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Construtora, todos os clientes
    publico: time de construtora, VENDEDOR_19 a VENDEDOR_23
    se: []
    entao: {acao: agendar, frequencia: fixa 14 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| vendedor 970 | vendedor | VENDEDOR_01 |
| vendedor 967 | vendedor | VENDEDOR_02 |
| vendedor 973 | vendedor | VENDEDOR_03 |
| vendedor 974 | vendedor | VENDEDOR_04 |
| vendedor 511 | vendedor | VENDEDOR_05 |
| vendedor 803 | vendedor | VENDEDOR_06 |
| vendedor 510 | vendedor | VENDEDOR_07 |
| vendedor 906 | vendedor | VENDEDOR_08 |
| vendedor 507 | vendedor | VENDEDOR_09 |
| vendedor 506 | vendedor | VENDEDOR_10 |
| vendedor 606 | vendedor | VENDEDOR_11 |
| vendedor 925 | vendedor | VENDEDOR_12 |
| vendedor 904 | vendedor | VENDEDOR_13 |
| vendedor 907 | vendedor | VENDEDOR_14 |
| vendedor 536 | vendedor | VENDEDOR_15 |
| vendedor 927 | vendedor | VENDEDOR_16 |
| vendedor 964 | vendedor | VENDEDOR_17 |
| vendedor 521 | vendedor | VENDEDOR_18 |
| vendedor 956 | vendedor | VENDEDOR_19 |
| vendedor 954 | vendedor | VENDEDOR_20 |
| vendedor 958 | vendedor | VENDEDOR_21 |
| vendedor 971 | vendedor | VENDEDOR_22 |
| vendedor 520 | vendedor | VENDEDOR_23 |
| time de ativação | jargao | time dedicado a ativar clientes |
| generalista | jargao | time que atende clientes de qualquer segmento |

## Lacunas

- A entrada não diz sobre qual carteira os times trabalham.

## Ambiguidades

- O nome do time de construtora sugere segmento, mas a regra vale para todos os clientes do time.
