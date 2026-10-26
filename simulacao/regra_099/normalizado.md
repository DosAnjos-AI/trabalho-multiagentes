---
id: regra_099
origem: simulacao/regra_099/entrada.md
gobr: simulacao/regra_099/regra_099.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 5
procedencia: corpus_sintetico
---

## Regras

cliente sem vendas do televendas é atendido a cada 7 dias
cliente ativo e inadimplente do televendas é atendido a cada 30 dias
cliente inativo e inadimplente do televendas não é agendado
cliente adimplente do televendas é atendido a cada 7 dias
todos os clientes do campo são atendidos a cada 30 dias

## Estrutura

```yaml
publico: time de televendas e time de campo
comuns: []
regras:
  - nome: Sem vendas do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Ativos inadimplentes do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Não agendar inativos inadimplentes do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Adimplentes do televendas
    publico: time de televendas
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Todos os clientes do campo
    publico: time de campo
    se: []
    entao: {acao: agendar, frequencia: fixa 30 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Elluc | empresa_foco | EMPRESA_FOCO |
| televendas | jargao | atendimento por telefone |
| campo | jargao | atendimento presencial |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| sem vendas | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não diz se os times trabalham sobre carteira fixa.

## Ambiguidades

- nenhuma
