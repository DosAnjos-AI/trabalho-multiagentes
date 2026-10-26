---
id: regra_070
origem: simulacao/regra_070/entrada.md
gobr: simulacao/regra_070/regra_070.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 7
procedencia: corpus_sintetico
---

## Regras

cliente inativo e inadimplente do televendas não é agendado
cliente ativo do televendas é atendido a cada 14 dias, preferindo dia útil
cliente inativo e adimplente do televendas é atendido a cada 30 dias, preferindo dia útil
cliente sem venda do televendas é atendido a cada 30 dias, preferindo dia útil
cliente ativo do campo é atendido a cada 14 dias, preferindo dia útil
cliente inativo do campo é atendido a cada 30 dias, preferindo dia útil
cliente sem venda do campo não é agendado

## Estrutura

```yaml
publico: time de televendas e time de campo
comuns: []
regras:
  - nome: Não agendar inativos inadimplentes do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Ativos do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Inativos adimplentes do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Sem venda do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Ativos do campo
    publico: time de campo
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Inativos do campo
    publico: time de campo
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Não agendar sem venda do campo
    publico: time de campo
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: nao_agendar, frequencia: nao_informada}
termos_fora_vocabulario:
  - preferência por dia útil
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Tripet | empresa_foco | EMPRESA_FOCO |
| televendas | jargao | atendimento por telefone |
| campo | jargao | atendimento presencial |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| sem venda | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não diz se os times trabalham sobre carteira fixa.
- A entrada não define o prazo que separa ativo de inativo.

## Ambiguidades

- "Preferindo dia útil" é preferência de agendamento, não condição; registrada como critério de período por falta de campo próprio.
