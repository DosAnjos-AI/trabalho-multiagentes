---
id: regra_093
origem: simulacao/regra_093/entrada.md
gobr: simulacao/regra_093/regra_093.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 11
procedencia: corpus_sintetico
---

## Regras

cliente ativo e adimplente do televendas é atendido semanalmente, preferindo dia útil
cliente ativo e inadimplente do televendas é atendido a cada 14 dias, preferindo dia útil
cliente inativo do televendas é atendido a cada 30 dias, preferindo dia útil
cliente sem vendas do televendas é atendido a cada 30 dias, preferindo dia útil
cliente ativo e adimplente da capital é atendido semanalmente, preferindo dia útil
cliente ativo e inadimplente da capital é atendido a cada 14 dias, preferindo dia útil
cliente inativo da capital é atendido a cada 30 dias, preferindo dia útil
cliente sem vendas da capital é atendido a cada 30 dias, preferindo dia útil
cliente ativo do interior é atendido a cada 14 dias, preferindo dia útil
cliente inativo do interior é atendido a cada 30 dias, preferindo dia útil
cliente sem vendas do interior é atendido a cada 30 dias, preferindo dia útil

## Estrutura

```yaml
publico: time de campo do interior, time de campo da capital e time de televendas
comuns:
  - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
regras:
  - nome: Ativos adimplentes do televendas
    publico: todos os vendedores de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Ativos inadimplentes do televendas
    publico: todos os vendedores de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Inativos do televendas
    publico: todos os vendedores de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Sem vendas do televendas
    publico: todos os vendedores de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Ativos adimplentes da capital
    publico: time de campo da capital, todos os vendedores de campo exceto VENDEDOR_01 a VENDEDOR_14
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Ativos inadimplentes da capital
    publico: time de campo da capital, todos os vendedores de campo exceto VENDEDOR_01 a VENDEDOR_14
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Inativos da capital
    publico: time de campo da capital, todos os vendedores de campo exceto VENDEDOR_01 a VENDEDOR_14
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Sem vendas da capital
    publico: time de campo da capital, todos os vendedores de campo exceto VENDEDOR_01 a VENDEDOR_14
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Ativos do interior
    publico: time de campo do interior, VENDEDOR_01 a VENDEDOR_14
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Inativos do interior
    publico: time de campo do interior, VENDEDOR_01 a VENDEDOR_14
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Sem vendas do interior
    publico: time de campo do interior, VENDEDOR_01 a VENDEDOR_14
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 30 dias}
termos_fora_vocabulario:
  - preferência por dia útil
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| vendedor de ID 18 | vendedor | VENDEDOR_01 |
| vendedor de ID 212 | vendedor | VENDEDOR_02 |
| vendedor de ID 300 | vendedor | VENDEDOR_03 |
| vendedor de ID 376 | vendedor | VENDEDOR_04 |
| vendedor de ID 395 | vendedor | VENDEDOR_05 |
| vendedor de ID 421 | vendedor | VENDEDOR_06 |
| vendedor de ID 43 | vendedor | VENDEDOR_07 |
| vendedor de ID 449 | vendedor | VENDEDOR_08 |
| vendedor de ID 486 | vendedor | VENDEDOR_09 |
| vendedor de ID 488 | vendedor | VENDEDOR_10 |
| vendedor de ID 489 | vendedor | VENDEDOR_11 |
| vendedor de ID 490 | vendedor | VENDEDOR_12 |
| vendedor de ID 6 | vendedor | VENDEDOR_13 |
| vendedor de ID 68 | vendedor | VENDEDOR_14 |
| televendas | jargao | atendimento por telefone |
| campo | jargao | atendimento presencial |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| sem vendas | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não diz se os times trabalham sobre carteira fixa.
- A entrada não define o prazo que separa ativo de inativo.

## Ambiguidades

- "Semanal" foi registrado como 7 dias pela convenção de periodicidade; a entrada não dá o número.
- "Preferindo dia útil" é preferência de agendamento, não condição; registrada como critério de período por falta de campo próprio.
