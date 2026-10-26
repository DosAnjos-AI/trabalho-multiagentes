---
id: regra_200
origem: simulacao/regra_200/entrada.md
gobr: simulacao/regra_200/regra_200.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 7
procedencia: corpus_sintetico
---

## Regras

prospect é atendido a cada 21 dias
cliente com uma única compra é atendido a cada 10 dias
cliente com compra nos últimos 30 dias usa o histórico acrescido de 5 dias, com máximo de 30 dias
cliente com compra com o vendedor nos últimos 30 dias é atendido a cada 14 dias
cliente com compra entre 31 e 60 dias é atendido a cada 7 dias
cliente com compra entre 61 e 90 dias é atendido a cada 7 dias
clientes sem compra, inativos, são atendidos a cada 21 dias

## Estrutura

```yaml
publico: televendas, exceto VENDEDOR_01
comuns: []
regras:
  - nome: Prospects
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Ativado, boas-vindas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única}
    entao: {acao: agendar, frequencia: fixa 10 dias}
  - nome: Alta frequência de compra
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Compra regular
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Estimular regularidade
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [31, 60], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Risco de inatividade
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [61, 90], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Resgate de inativos
    se: []
    entao: {acao: agendar, frequencia: fixa 21 dias}
termos_fora_vocabulario:
  - frequência pelo histórico com acréscimo e teto
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| vendedor 1 | vendedor | VENDEDOR_01 |
| televendas | jargao | atendimento por telefone |
| prospect | jargao | cliente que nunca comprou |
| boas-vindas | jargao | contato após a primeira compra |

## Lacunas

- A entrada não diz se o televendas trabalha sobre carteira fixa.

## Ambiguidades

- A regra de compra regular (com o vendedor nos últimos 30 dias) vem depois da de alta frequência (compra nos últimos 30 dias) e pode nunca ser alcançada, dependendo da ordem de avaliação.
- O acréscimo de 5 dias e o teto de 30 dias da frequência pelo histórico não têm campo próprio e foram registrados apenas na descrição.
