---
id: regra_087
origem: simulacao/regra_087/entrada.md
gobr: simulacao/regra_087/regra_087.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 8
procedencia: corpus_sintetico
---

## Regras

cliente ativo e adimplente do televendas é atendido a cada 14 dias, preferindo dia útil
cliente ativo e inadimplente do televendas é atendido a cada 30 dias, preferindo dia útil
cliente inativo e adimplente do televendas é atendido a cada 30 dias, preferindo dia útil
cliente inativo e inadimplente do televendas é atendido a cada 60 dias, preferindo dia útil
cliente sem venda do televendas é atendido a cada 30 dias, preferindo dia útil
cliente adimplente do campo é atendido a cada 14 dias, preferindo dia útil
cliente inadimplente do campo é atendido a cada 30 dias, preferindo dia útil
cliente sem venda do campo é atendido a cada 30 dias, preferindo dia útil

## Estrutura

```yaml
publico: time de televendas e time de campo
comuns:
  - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
regras:
  - nome: Ativos adimplentes do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Ativos inadimplentes do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Inativos adimplentes do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Inativos inadimplentes do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: agendar, frequencia: fixa 60 dias}
  - nome: Sem venda do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Adimplentes do campo
    publico: time de campo
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Inadimplentes do campo
    publico: time de campo
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Sem venda do campo
    publico: time de campo
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 30 dias}
termos_fora_vocabulario:
  - preferência por dia útil
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| campo | jargao | atendimento presencial |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| sem venda | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não diz se os times trabalham sobre carteira fixa.
- A entrada não define o prazo que separa ativo de inativo.

## Ambiguidades

- No campo, a regra de adimplentes vem antes da de sem venda; um cliente sem venda e adimplente pode cair na primeira, dependendo da ordem de avaliação.
- "Preferindo dia útil" é preferência de agendamento, não condição; registrada como critério de período por falta de campo próprio.
