---
id: regra_184
origem: simulacao/regra_184/entrada.md
gobr: simulacao/regra_184/regra_184.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 13
procedencia: corpus_sintetico
---

## Regras

cliente com uma única compra feita neste mês é atendido a cada 5 dias
cliente com compra entre 1 e 7 dias usa o histórico, entre 1 e 5 dias, preferindo segunda e terça
cliente com compra entre 7 e 14 dias usa o histórico, entre 7 e 12 dias
cliente com compra entre 14 e 30 dias usa o histórico, entre 14 e 28 dias
cliente com compra entre 31 e 90 dias é atendido a cada 14 dias
cliente com compra entre 91 e 180 dias é atendido a cada 14 dias
cliente sem compra há mais de 360 dias é atendido a cada 21 dias
cliente com intervalo histórico de 7 dias é atendido a cada 7 dias, preferindo segunda, com frequência fixa
cliente com intervalo histórico de 14 dias é atendido a cada 14 dias, preferindo segunda, com frequência fixa
cliente com intervalo histórico de 28 dias é atendido a cada 28 dias, preferindo segunda, com frequência fixa
cliente com intervalo histórico de 56 dias é atendido a cada 56 dias, preferindo segunda, com frequência fixa
cliente com intervalo histórico de 84 dias é atendido a cada 84 dias, preferindo segunda, com frequência fixa
quem não se enquadrou nas regras é atendido a cada 30 dias

## Estrutura

```yaml
publico: time de televendas e time de São Paulo
comuns: []
regras:
  - nome: Garantir recorrência
    publico: televendas, exceto VENDEDOR_01 a VENDEDOR_08
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única}
      - {tipo: tempo_sem_comprar, op: igual_a, valor: mês atual, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 5 dias}
  - nome: Alta frequência de compra
    publico: televendas, exceto VENDEDOR_01 a VENDEDOR_08
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [1, 7], unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: [segunda, terça], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Manter regularidade
    publico: televendas, exceto VENDEDOR_01 a VENDEDOR_08
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [7, 14], unidade: dias}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Estimular compra no mês
    publico: televendas, exceto VENDEDOR_01 a VENDEDOR_08
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [14, 30], unidade: dias}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Gerar relacionamento
    publico: televendas, exceto VENDEDOR_01 a VENDEDOR_08
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [31, 90], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Resgate de inativos
    publico: televendas, exceto VENDEDOR_01 a VENDEDOR_08
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [91, 180], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Requalificar perfil
    publico: televendas, exceto VENDEDOR_01 a VENDEDOR_08
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 360, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: São Paulo, intervalo histórico de 7 dias
    publico: time de São Paulo, VENDEDOR_01 a VENDEDOR_08
    se:
      - {tipo: tempo_sem_comprar, op: igual_a, valor: 7, unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: segunda, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: São Paulo, intervalo histórico de 14 dias
    publico: time de São Paulo, VENDEDOR_01 a VENDEDOR_08
    se:
      - {tipo: tempo_sem_comprar, op: igual_a, valor: 14, unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: segunda, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: São Paulo, intervalo histórico de 28 dias
    publico: time de São Paulo, VENDEDOR_01 a VENDEDOR_08
    se:
      - {tipo: tempo_sem_comprar, op: igual_a, valor: 28, unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: segunda, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 28 dias}
  - nome: São Paulo, intervalo histórico de 56 dias
    publico: time de São Paulo, VENDEDOR_01 a VENDEDOR_08
    se:
      - {tipo: tempo_sem_comprar, op: igual_a, valor: 56, unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: segunda, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 56 dias}
  - nome: São Paulo, intervalo histórico de 84 dias
    publico: time de São Paulo, VENDEDOR_01 a VENDEDOR_08
    se:
      - {tipo: tempo_sem_comprar, op: igual_a, valor: 84, unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: segunda, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 84 dias}
  - nome: Demais clientes dos dois times
    publico: os dois times
    se: []
    entao: {acao: agendar, frequencia: fixa 30 dias}
termos_fora_vocabulario:
  - frequência histórica de compra
  - frequência pelo histórico com mínimo e máximo
  - preferência de dias da semana
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| vendedor 39 | vendedor | VENDEDOR_01 |
| vendedor 11 | vendedor | VENDEDOR_02 |
| vendedor 63 | vendedor | VENDEDOR_03 |
| vendedor 8 | vendedor | VENDEDOR_04 |
| vendedor 49 | vendedor | VENDEDOR_05 |
| vendedor 31 | vendedor | VENDEDOR_06 |
| vendedor 29 | vendedor | VENDEDOR_07 |
| vendedor 10 | vendedor | VENDEDOR_08 |
| televendas | jargao | atendimento por telefone |
| frequência histórica | jargao | intervalo médio entre compras |
| fallback | jargao | regra para quem não se enquadrou nas demais |

## Lacunas

- Não há regra para clientes com compra entre 181 e 360 dias no televendas além da regra residual de 30 dias.

## Ambiguidades

- As faixas de compra compartilham os limites 7, 14 e 30 dias.
- Os limites das frequências pelo histórico não têm campo próprio e foram registrados apenas na descrição.
