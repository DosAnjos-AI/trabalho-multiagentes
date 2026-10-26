---
id: regra_225
origem: simulacao/regra_225/entrada.md
gobr: simulacao/regra_225/regra_225.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 5
procedencia: corpus_sintetico
---

## Regras

prospect é atendido a cada 10 dias, preferindo dia útil e sábado
cliente ativo e adimplente é atendido a cada 21 dias, preferindo dia útil e sábado
o restante dos ativos, inadimplentes, é atendido a cada 10 dias, preferindo dia útil e sábado
cliente inativo e adimplente é atendido a cada 14 dias, preferindo dia útil e sábado
o restante, inativos inadimplentes, é atendido a cada 21 dias, preferindo dia útil e sábado

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns:
  - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado], unidade: periodo_nomeado}
regras:
  - nome: Prospects
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 10 dias}
  - nome: Ativos adimplentes
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Ativos inadimplentes
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
    entao: {acao: agendar, frequencia: fixa 10 dias}
  - nome: Inativos adimplentes
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Inativos inadimplentes
    se: []
    entao: {acao: agendar, frequencia: fixa 21 dias}
termos_fora_vocabulario:
  - preferência por dia útil e sábado
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| prospect | jargao | cliente que nunca comprou |
| inadimplente | jargao | cliente com pendência financeira em aberto |

## Lacunas

- A entrada não define o prazo que separa ativo de inativo.

## Ambiguidades

- As regras de inadimplentes são descritas como "o restante" e dependem da ordem de avaliação para separar adimplentes de inadimplentes.
