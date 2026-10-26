---
id: regra_183
origem: simulacao/regra_183/entrada.md
gobr: simulacao/regra_183/regra_183.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 6
procedencia: corpus_sintetico
---

## Regras

cliente inadimplente não é agendado
prospect é atendido a cada 21 dias
cliente ativo com intervalo histórico menor que 30 dias usa o histórico, entre 5 e 30 dias
cliente ativo com intervalo histórico maior que 30 dias e sem pedido nos últimos 30 dias é atendido a cada 14 dias
cliente ativo com intervalo histórico maior que 30 dias e pedido nos últimos 30 dias é atendido a cada 14 dias
cliente inativo com a empresa é atendido a cada 21 dias

## Estrutura

```yaml
publico: time de televendas, VENDEDOR_01 a VENDEDOR_05
comuns: []
regras:
  - nome: Não agendar inadimplentes
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Prospects
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Alta frequência de compra
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: tempo_sem_comprar, op: menor_que, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Compra regular sem pedido em 30 dias
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 30, unidade: dias}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Compra regular com pedido em 30 dias
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 30, unidade: dias}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Inativos com a empresa
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 21 dias}
termos_fora_vocabulario:
  - frequência histórica de compra
  - frequência pelo histórico com mínimo e máximo
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| vendedor 522 | vendedor | VENDEDOR_01 |
| vendedor 353 | vendedor | VENDEDOR_02 |
| vendedor 519 | vendedor | VENDEDOR_03 |
| vendedor 520 | vendedor | VENDEDOR_04 |
| vendedor 523 | vendedor | VENDEDOR_05 |
| televendas | jargao | atendimento por telefone |
| frequência histórica | jargao | intervalo médio entre compras |
| prospect | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não diz se o televendas trabalha sobre carteira fixa.

## Ambiguidades

- As duas regras de compra regular têm a mesma frequência de 14 dias; a distinção por pedido nos últimos 30 dias não altera o atendimento.
- Os limites de 5 e 30 dias da frequência pelo histórico não têm campo próprio e foram registrados apenas na descrição.
