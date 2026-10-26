---
id: regra_071
origem: simulacao/regra_071/entrada.md
gobr: simulacao/regra_071/regra_071.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 11
procedencia: corpus_sintetico
---

## Regras

cliente inativo e inadimplente das carteiras de Piauí e Paraíba é atendido a cada 14 dias, em dia útil, sem coincidir com a rota do campo
o restante da carteira do Piauí é atendido pela frequência do histórico, no máximo semanal, em dias úteis e sábado, sem coincidir com a rota do campo
o restante da carteira da Paraíba é atendido pela frequência do histórico, no máximo semanal, só em dias úteis, sem coincidir com a rota do campo
cliente inativo e inadimplente do Tocantins é atendido a cada 14 dias, em dia útil, sem coincidir com a rota do campo
o restante da carteira do Tocantins é atendido pelo histórico, no máximo semanal, em dias úteis e sábado, sem coincidir com a rota do campo
cliente ativo e adimplente é atendido pelo histórico, no máximo semanal, em dia útil
cliente ativo e inadimplente é atendido a cada 14 dias, em dia útil
cliente inativo e adimplente é atendido pelo histórico, no máximo semanal, de segunda a sexta
cliente inativo e inadimplente é atendido a cada 30 dias, de segunda a sexta
o restante é atendido pelo histórico, no máximo semanal, de segunda a sexta
todos os clientes do campo são atendidos semanalmente, a cada 7 dias

## Estrutura

```yaml
publico: televendas do Piauí, televendas da Paraíba, time do Tocantins, televendas geral e campo
comuns: []
regras:
  - nome: Inativos inadimplentes de Piauí e Paraíba
    publico: televendas do Piauí (SUPERVISOR_A) e televendas da Paraíba (SUPERVISOR_B)
    se:
      - {tipo: carteira, op: igual_a, valor: [carteira do televendas do Piauí, carteira do televendas da Paraíba], alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
      - {tipo: agenda_rota, op: igual_a, valor: sem conflito com a rota do campo, alcance: grupo}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Restante do Piauí pelo histórico
    publico: televendas do Piauí (SUPERVISOR_A)
    se:
      - {tipo: carteira, op: igual_a, valor: carteira do televendas do Piauí, alcance: grupo}
      - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado], unidade: periodo_nomeado}
      - {tipo: agenda_rota, op: igual_a, valor: sem conflito com a rota do campo, alcance: grupo}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Restante da Paraíba pelo histórico
    publico: televendas da Paraíba (SUPERVISOR_B)
    se:
      - {tipo: carteira, op: igual_a, valor: carteira do televendas da Paraíba, alcance: grupo}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
      - {tipo: agenda_rota, op: igual_a, valor: sem conflito com a rota do campo, alcance: grupo}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Inativos inadimplentes do Tocantins
    publico: time do Tocantins, VENDEDOR_01 a VENDEDOR_07
    se:
      - {tipo: carteira, op: igual_a, valor: carteira do time do Tocantins, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
      - {tipo: agenda_rota, op: igual_a, valor: sem conflito com a rota do campo, alcance: grupo}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Restante do Tocantins pelo histórico
    publico: time do Tocantins, VENDEDOR_01 a VENDEDOR_07
    se:
      - {tipo: carteira, op: igual_a, valor: carteira do time do Tocantins, alcance: grupo}
      - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado], unidade: periodo_nomeado}
      - {tipo: agenda_rota, op: igual_a, valor: sem conflito com a rota do campo, alcance: grupo}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Ativos adimplentes do televendas geral
    publico: televendas geral
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Ativos inadimplentes do televendas geral
    publico: televendas geral
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Inativos adimplentes do televendas geral
    publico: televendas geral
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
      - {tipo: periodo_vigencia, op: igual_a, valor: [segunda, terça, quarta, quinta, sexta], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Inativos inadimplentes do televendas geral
    publico: televendas geral
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
      - {tipo: periodo_vigencia, op: igual_a, valor: [segunda, terça, quarta, quinta, sexta], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Restante do televendas geral
    publico: televendas geral
    se:
      - {tipo: periodo_vigencia, op: igual_a, valor: [segunda, terça, quarta, quinta, sexta], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Todos os clientes do campo
    publico: time de campo
    se: []
    entao: {acao: agendar, frequencia: fixa 7 dias}
termos_fora_vocabulario:
  - frequência pelo histórico com teto semanal
  - preferência de dias da semana
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Palmed | empresa_foco | EMPRESA_FOCO |
| supervisor 2736 | supervisor | SUPERVISOR_A |
| supervisor 2731 | supervisor | SUPERVISOR_B |
| vendedor 435 | vendedor | VENDEDOR_01 |
| vendedor 261 | vendedor | VENDEDOR_02 |
| vendedor 385 | vendedor | VENDEDOR_03 |
| vendedor 276 | vendedor | VENDEDOR_04 |
| vendedor 438 | vendedor | VENDEDOR_05 |
| vendedor 63 | vendedor | VENDEDOR_06 |
| vendedor 164 | vendedor | VENDEDOR_07 |
| televendas | jargao | atendimento por telefone |
| campo | jargao | atendimento presencial |
| frequência do histórico | jargao | frequência calculada pelo histórico de compras |
| rota | jargao | roteiro de visitas programado |

## Lacunas

- A entrada não explica como é calculada a frequência pelo histórico.
- A entrada não diz se o televendas geral e o campo trabalham sobre carteira fixa.

## Ambiguidades

- O teto "no máximo semanal" da frequência pelo histórico não tem campo próprio e foi registrado apenas na descrição.
- O televendas geral inclui todos os vendedores de televendas, o que pode sobrepor os times do Piauí e da Paraíba.
- As preferências de dia são preferências de agendamento, não condições; registradas como critério de período por falta de campo próprio.
