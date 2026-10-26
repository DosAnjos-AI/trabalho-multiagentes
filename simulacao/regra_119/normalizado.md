---
id: regra_119
origem: simulacao/regra_119/entrada.md
gobr: simulacao/regra_119/regra_119.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 5
procedencia: corpus_sintetico
---

## Regras

cliente ativo e adimplente é atendido a cada 15 dias
cliente ativo e inadimplente é atendido a cada 30 dias
cliente inativo e adimplente é atendido a cada 7 dias
cliente inativo e inadimplente não é agendado
cliente sem compra é atendido a cada 15 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Ativos adimplentes
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Ativos inadimplentes
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Inativos adimplentes
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Não agendar inativos inadimplentes
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Sem compra
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 15 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Ultrax | empresa_foco | EMPRESA_FOCO |
| televendas | jargao | atendimento por telefone |
| inadimplente | jargao | cliente com pendência financeira em aberto |

## Lacunas

- A entrada não diz se o televendas trabalha sobre carteira fixa.
- A entrada não define o prazo que separa ativo de inativo.

## Ambiguidades

- nenhuma
