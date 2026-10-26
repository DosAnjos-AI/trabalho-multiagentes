---
id: regra_094
origem: simulacao/regra_094/entrada.md
gobr: simulacao/regra_094/regra_094.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 4
procedencia: corpus_sintetico
---

## Regras

cliente adimplente do televendas é atendido a cada 30 dias
cliente inadimplente do televendas é atendido a cada 60 dias
cliente sem venda do televendas é atendido a cada 30 dias
todos os clientes do campo são atendidos a cada 30 dias

## Estrutura

```yaml
publico: time de televendas e time de campo
comuns: []
regras:
  - nome: Adimplentes do televendas
    publico: time de televendas
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Inadimplentes do televendas
    publico: time de televendas
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: agendar, frequencia: fixa 60 dias}
  - nome: Sem venda do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Todos os clientes do campo
    publico: time de campo
    se: []
    entao: {acao: agendar, frequencia: fixa 30 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| AHL | empresa_foco | EMPRESA_FOCO |
| televendas | jargao | atendimento por telefone |
| campo | jargao | atendimento presencial |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| sem venda | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não diz se os times trabalham sobre carteira fixa.

## Ambiguidades

- No televendas, as regras de adimplente e inadimplente vêm antes da de sem venda; um cliente sem venda pode cair nas primeiras, dependendo da ordem de avaliação.
