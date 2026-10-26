---
id: regra_133
origem: simulacao/regra_133/entrada.md
gobr: simulacao/regra_133/regra_133.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 5
procedencia: corpus_sintetico
---

## Regras

cliente inadimplente do televendas não é agendado
cliente ativo do televendas é atendido a cada 7 dias
cliente inativo do televendas é atendido a cada 14 dias
cliente ativo do campo é atendido a cada 7 dias, com frequência fixa
cliente inativo do campo é atendido a cada 15 dias, com frequência fixa

## Estrutura

```yaml
publico: time de televendas e time de campo
comuns: []
regras:
  - nome: Não agendar inadimplentes do televendas
    publico: time de televendas
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Ativos do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Ativos do campo
    publico: time de campo
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos do campo
    publico: time de campo
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
    entao: {acao: agendar, frequencia: fixa 15 dias}
termos_fora_vocabulario:
  - frequência fixa rígida
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Casa Cardão | empresa_foco | EMPRESA_FOCO |
| televendas | jargao | atendimento por telefone |
| campo | jargao | atendimento presencial |
| inadimplente | jargao | cliente com pendência financeira em aberto |

## Lacunas

- A entrada não diz se os times trabalham sobre carteira fixa.
- A entrada não define o prazo que separa ativo de inativo.

## Ambiguidades

- nenhuma
