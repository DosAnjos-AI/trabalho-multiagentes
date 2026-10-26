---
id: regra_057
origem: simulacao/regra_057/entrada.md
gobr: simulacao/regra_057/regra_057.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 3
procedencia: corpus_sintetico
---

## Regras

prospect que nunca comprou é atendido a cada 30 dias
cliente ativo para o vendedor, adimplente ou inadimplente, é atendido a cada 25 dias
todos os demais clientes, os inativos, são atendidos a cada 30 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Prospects a cada 30 dias
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Ativos a cada 25 dias
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 25 dias}
  - nome: Demais clientes a cada 30 dias
    se: []
    entao: {acao: agendar, frequencia: fixa 30 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| prospect | jargao | cliente que nunca comprou |
| inadimplente | jargao | cliente com pendência financeira em aberto |

## Lacunas

- A entrada não define o prazo que caracteriza o cliente ativo.

## Ambiguidades

- nenhuma
