---
id: regra_124
origem: simulacao/regra_124/entrada.md
gobr: simulacao/regra_124/regra_124.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 5
procedencia: corpus_sintetico
---

## Regras

todos os clientes do campo são atendidos a cada 30 dias
cliente ativo do televendas é atendido a cada 25 dias, em dia útil, sem coincidir com o campo
cliente inativo e adimplente do televendas é atendido a cada 25 dias, em dia útil, sem coincidir com o campo
cliente inativo e inadimplente do televendas é atendido a cada 25 dias, em dia útil, sem coincidir com o campo
cliente sem vendas do televendas é atendido a cada 25 dias, em dia útil, sem coincidir com o campo

## Estrutura

```yaml
publico: time de campo e time de televendas
comuns: []
regras:
  - nome: Todos os clientes do campo
    publico: time de campo
    se: []
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Ativos do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
      - {tipo: agenda_rota, op: igual_a, valor: sem conflito com visita do campo, alcance: grupo}
    entao: {acao: agendar, frequencia: fixa 25 dias}
  - nome: Inativos adimplentes do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
      - {tipo: agenda_rota, op: igual_a, valor: sem conflito com visita do campo, alcance: grupo}
    entao: {acao: agendar, frequencia: fixa 25 dias}
  - nome: Inativos inadimplentes do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
      - {tipo: agenda_rota, op: igual_a, valor: sem conflito com visita do campo, alcance: grupo}
    entao: {acao: agendar, frequencia: fixa 25 dias}
  - nome: Sem vendas do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
      - {tipo: agenda_rota, op: igual_a, valor: sem conflito com visita do campo, alcance: grupo}
    entao: {acao: agendar, frequencia: fixa 25 dias}
termos_fora_vocabulario:
  - preferência por dia útil
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Roda Viva | empresa_foco | EMPRESA_FOCO |
| televendas | jargao | atendimento por telefone |
| campo | jargao | atendimento presencial |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| sem vendas | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não diz se os times trabalham sobre carteira fixa.

## Ambiguidades

- "Dia útil" é preferência de agendamento, não condição; registrada como critério de período por falta de campo próprio.
