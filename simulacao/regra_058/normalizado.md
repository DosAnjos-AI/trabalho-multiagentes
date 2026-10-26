---
id: regra_058
origem: simulacao/regra_058/entrada.md
gobr: simulacao/regra_058/regra_058.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 6
procedencia: corpus_sintetico
---

## Regras

cliente inadimplente do televendas é atendido a cada 14 dias
os demais clientes do televendas usam a frequência calculada pelo histórico de vendas, com máximo de 14 dias
cliente adimplente do campo é atendido a cada 7 dias
cliente ativo e inadimplente do campo é atendido a cada 14 dias
cliente inativo e inadimplente do campo é atendido a cada 60 dias
cliente sem venda do campo é atendido a cada 14 dias

## Estrutura

```yaml
publico: time de televendas e time de campo
comuns: []
regras:
  - nome: Inadimplentes do televendas
    publico: time de televendas
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa do televendas, alcance: grupo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Demais clientes do televendas pelo histórico
    publico: time de televendas
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa do televendas, alcance: grupo}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Adimplentes do campo
    publico: time de campo
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa do campo, alcance: grupo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Ativos inadimplentes do campo
    publico: time de campo
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa do campo, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Inativos inadimplentes do campo
    publico: time de campo
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa do campo, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: agendar, frequencia: fixa 60 dias}
  - nome: Sem venda do campo
    publico: time de campo
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa do campo, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 14 dias}
termos_fora_vocabulario:
  - frequência pelo histórico com teto de 14 dias
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Ótima Atacado | empresa_foco | EMPRESA_FOCO |
| televendas | jargao | atendimento por telefone |
| campo | jargao | atendimento presencial |
| carteira fixa | jargao | clientes vinculados a um vendedor ou time |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| sem venda | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não diz o que acontece com o cliente inativo adimplente do campo além da regra de adimplentes.
- A entrada não explica como a frequência é calculada a partir do histórico de vendas.

## Ambiguidades

- A frequência dos demais clientes do televendas é calculada, mas com teto de 14 dias; o teto não tem campo próprio e foi registrado apenas na descrição.
