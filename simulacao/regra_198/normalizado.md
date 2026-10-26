---
id: regra_198
origem: simulacao/regra_198/entrada.md
gobr: simulacao/regra_198/regra_198.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 5
procedencia: corpus_sintetico
---

## Regras

prospect é atendido a cada 25 dias
cliente com uma única compra com a empresa e sem compra com o vendedor nos últimos 30 dias é atendido a cada 14 dias
cliente com compra com o vendedor nos últimos 30 dias usa o histórico, entre 7 e 30 dias
cliente ativo com a empresa é atendido a cada 14 dias
inativos são atendidos a cada 21 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Prospects
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 25 dias}
  - nome: Ativado, boas-vindas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única, alcance: empresa}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 30, unidade: dias, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Alta frequência de compra
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias, alcance: vendedor}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Ativos com a empresa
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Inativos
    se: []
    entao: {acao: agendar, frequencia: fixa 21 dias}
termos_fora_vocabulario:
  - frequência pelo histórico com mínimo e máximo
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| prospect | jargao | cliente que nunca comprou |
| ativado | jargao | cliente que fez a primeira compra |

## Lacunas

- A entrada não diz se o televendas trabalha sobre carteira fixa.

## Ambiguidades

- Os limites de 7 e 30 dias da frequência pelo histórico não têm campo próprio e foram registrados apenas na descrição.
