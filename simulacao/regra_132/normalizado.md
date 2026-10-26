---
id: regra_132
origem: simulacao/regra_132/entrada.md
gobr: simulacao/regra_132/regra_132.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 7
procedencia: corpus_sintetico
---

## Regras

cliente inadimplente não é agendado
cliente que nunca fez pedido com o vendedor é atendido a cada 7 dias
cliente que fez um pedido e não comprou mais é atendido a cada 7 dias
cliente com intervalo histórico de compra menor que 11 dias é atendido a cada 14 dias
cliente com último pedido com o vendedor entre 11 e 59 dias é atendido a cada 10 dias
cliente com último pedido entre 60 e 89 dias é atendido a cada 7 dias
cliente inativo, sem compra, é atendido a cada 10 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Não agendar inadimplentes
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Prospect do vendedor
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Cliente ativado
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Compra regularmente
    se:
      - {tipo: tempo_sem_comprar, op: menor_que, valor: 11, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Estimular regularidade
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [11, 59], unidade: dias, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 10 dias}
  - nome: Em ruptura
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [60, 89], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos sem compra
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
    entao: {acao: agendar, frequencia: fixa 10 dias}
termos_fora_vocabulario:
  - frequência histórica de compra
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| prospect | jargao | cliente que nunca comprou |
| ruptura | jargao | cliente que parou de comprar |
| frequência histórica | jargao | intervalo médio entre compras |

## Lacunas

- A entrada não define o prazo que caracteriza o cliente inativo da última regra.

## Ambiguidades

- A última regra é descrita como "cliente inativo, sem compra", mas não traz critério de prazo; pode funcionar como regra residual.
