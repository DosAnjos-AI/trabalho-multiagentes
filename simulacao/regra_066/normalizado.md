---
id: regra_066
origem: simulacao/regra_066/entrada.md
gobr: simulacao/regra_066/regra_066.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 9
procedencia: corpus_sintetico
---

## Regras

cliente ativo e adimplente do televendas é atendido a cada 7 dias, preferindo dias úteis
cliente ativo e inadimplente do televendas é atendido a cada 14 dias, preferindo dias úteis
cliente inativo e adimplente do televendas é atendido a cada 30 dias, preferindo dias úteis
cliente inativo e inadimplente do televendas não é agendado
cliente sem venda do televendas não é agendado
cliente ativo do campo é atendido a cada 7 dias, preferindo dias úteis
cliente inativo e adimplente do campo é atendido a cada 30 dias, preferindo dias úteis
cliente inativo e inadimplente do campo não é agendado
cliente sem venda do campo não é agendado

## Estrutura

```yaml
publico: time de televendas (internos) e time de campo (externos)
comuns: []
regras:
  - nome: Ativos adimplentes do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Ativos inadimplentes do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Inativos adimplentes do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Não agendar inativos inadimplentes do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar sem venda do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Ativos do campo
    publico: time de campo
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos adimplentes do campo
    publico: time de campo
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Não agendar inativos inadimplentes do campo
    publico: time de campo
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar sem venda do campo
    publico: time de campo
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: nao_agendar, frequencia: nao_informada}
termos_fora_vocabulario:
  - preferência por dias úteis
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Sul Frios | empresa_foco | EMPRESA_FOCO |
| televendas, internos | jargao | atendimento por telefone |
| campo, externos | jargao | atendimento presencial |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| sem venda | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não diz se os times trabalham sobre carteira fixa.
- A entrada não diz o que acontece com o cliente ativo inadimplente do campo além da regra de ativos.

## Ambiguidades

- "Prefere dia útil" é preferência de agendamento, não condição; registrada como critério de período por falta de campo próprio.
