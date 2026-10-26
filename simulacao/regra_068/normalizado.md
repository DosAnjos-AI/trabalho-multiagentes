---
id: regra_068
origem: simulacao/regra_068/entrada.md
gobr: simulacao/regra_068/regra_068.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 9
procedencia: corpus_sintetico
---

## Regras

cliente do ramo 17, plano veterinário, não é agendado
cliente pessoa física não é agendado
cliente ativo e adimplente do campo é atendido a cada 30 dias
cliente sem venda do campo é atendido a cada 21 dias
todo o restante do campo, inadimplentes ou inativos, não é agendado
cliente inadimplente do televendas não é agendado
cliente ativo e adimplente do televendas é atendido a cada 14 dias
cliente inativo e adimplente do televendas é atendido a cada 30 dias
cliente sem venda do televendas é atendido a cada 14 dias

## Estrutura

```yaml
publico: time de campo e time de televendas
comuns: []
regras:
  - nome: Não agendar ramo 17 no campo
    publico: time de campo
    se:
      - {tipo: segmento, op: igual_a, valor: ['17']}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar pessoa física no campo
    publico: time de campo
    se:
      - {tipo: segmento, op: igual_a, valor: pessoa física}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Ativos adimplentes do campo
    publico: time de campo
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Sem venda do campo
    publico: time de campo
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Não agendar o restante do campo
    publico: time de campo
    se: []
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar inadimplentes do televendas
    publico: time de televendas
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Ativos adimplentes do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Inativos adimplentes do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Sem venda do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 14 dias}
termos_fora_vocabulario:
  - pessoa física
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Playpet | empresa_foco | EMPRESA_FOCO |
| campo | jargao | atendimento presencial |
| televendas | jargao | atendimento por telefone |
| ramo de atividade | jargao | segmento do cliente |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| sem venda | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não diz se os times trabalham sobre carteira fixa.

## Ambiguidades

- nenhuma
