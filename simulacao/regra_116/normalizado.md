---
id: regra_116
origem: simulacao/regra_116/entrada.md
gobr: simulacao/regra_116/regra_116.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 7
procedencia: corpus_sintetico
---

## Regras

cliente filial não é agendado por nenhum dos times
todos os clientes do televendas são atendidos a cada 7 dias, em dias úteis e sábado, sem coincidir com visita do campo
cliente ativo e adimplente do campo é atendido a cada 7 dias
cliente ativo e inadimplente do campo é atendido a cada 14 dias
cliente inativo e adimplente do campo é atendido a cada 30 dias
cliente inativo e inadimplente do campo é atendido a cada 60 dias
cliente sem venda do campo é atendido a cada 7 dias

## Estrutura

```yaml
publico: time de televendas e time de campo
comuns: []
regras:
  - nome: Não agendar filiais
    se:
      - {tipo: segmento, op: igual_a, valor: filial}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Todos os clientes do televendas
    publico: time de televendas
    se:
      - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado], unidade: periodo_nomeado}
      - {tipo: agenda_rota, op: igual_a, valor: sem conflito com visita do campo, alcance: grupo}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Ativos adimplentes do campo
    publico: time de campo
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Ativos inadimplentes do campo
    publico: time de campo
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Inativos adimplentes do campo
    publico: time de campo
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Inativos inadimplentes do campo
    publico: time de campo
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: agendar, frequencia: fixa 60 dias}
  - nome: Sem venda do campo
    publico: time de campo
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 7 dias}
termos_fora_vocabulario:
  - filial
  - preferência por dias úteis e sábado
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| campo | jargao | atendimento presencial |
| filial | jargao | unidade filial de um cliente |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| sem venda | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não diz se os times trabalham sobre carteira fixa.
- A entrada não define o prazo que separa ativo de inativo.

## Ambiguidades

- "Em dias úteis e sábado" é preferência de agendamento, não condição; registrada como critério de período por falta de campo próprio.
