---
id: regra_060
origem: simulacao/regra_060/entrada.md
gobr: simulacao/regra_060/regra_060.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 4
procedencia: corpus_sintetico
---

## Regras

cliente ativo para o vendedor é atendido a cada 7 dias
todos os demais clientes, os inativos, são atendidos a cada 15 dias
cliente ativo é atendido a cada 7 dias, com frequência fixa e rígida para o gerador de agenda
os demais clientes são atendidos a cada 15 dias, com frequência fixa e rígida para o gerador de agenda

## Estrutura

```yaml
publico: time de televendas e time de campo
comuns: []
regras:
  - nome: Ativos do televendas semanal
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Demais clientes do televendas quinzenal
    publico: time de televendas
    se: []
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Ativos do campo
    publico: time de campo
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Demais clientes do campo
    publico: time de campo
    se: []
    entao: {acao: agendar, frequencia: fixa 15 dias}
termos_fora_vocabulario:
  - frequência fixa rígida para o gerador de agenda
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| goVendas | jargao | plataforma de vendas |
| televendas | jargao | atendimento por telefone |
| campo | jargao | atendimento presencial |
| gerador de agenda | jargao | rotina que monta a agenda de atendimentos |
| parametrização fixa | jargao | frequência travada, sem ajuste automático |

## Lacunas

- A entrada não define o prazo que separa ativo de inativo.
- A entrada não diz se os times trabalham sobre carteira fixa.

## Ambiguidades

- nenhuma
