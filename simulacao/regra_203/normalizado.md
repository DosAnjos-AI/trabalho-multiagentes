---
id: regra_203
origem: simulacao/regra_203/entrada.md
gobr: simulacao/regra_203/regra_203.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 13
procedencia: corpus_sintetico
---

## Regras

cliente com cadastro baixado na Receita Federal não é agendado
filial não é agendada, exceto as filiais do cliente principal de código 36979
cliente inadimplente não é agendado
prospect sem venda não é agendado
cliente sem compra há mais de 95 dias não é agendado
cliente com uma única compra é atendido a cada 28 dias
cliente com intervalo histórico médio de 0 a 7 dias é atendido a cada 6 dias
cliente com intervalo histórico médio de 8 a 14 dias é atendido a cada 9 dias
cliente com intervalo histórico médio de 15 a 21 dias é atendido a cada 16 dias
cliente com intervalo histórico médio de 22 a 28 dias é atendido a cada 23 dias
cliente com intervalo histórico médio de 29 a 38 dias é atendido a cada 29 dias
cliente com intervalo histórico médio de 39 a 60 dias é atendido a cada 35 dias
cliente com intervalo histórico médio de 61 a 95 dias é atendido a cada 55 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Não agendar baixados na Receita Federal
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: baixado na Receita Federal}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar filiais, exceto as do cliente principal 36979
    se:
      - {tipo: segmento, op: igual_a, valor: filial}
      - {tipo: identificacao, op: fora_de, valor: ['36979']}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar inadimplentes
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar prospects
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar sem compra há mais de 95 dias
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 95, unidade: dias}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Compra única
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 28 dias}
  - nome: Intervalo histórico de 0 a 7 dias
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [0, 7], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 6 dias}
  - nome: Intervalo histórico de 8 a 14 dias
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [8, 14], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 9 dias}
  - nome: Intervalo histórico de 15 a 21 dias
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [15, 21], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 16 dias}
  - nome: Intervalo histórico de 22 a 28 dias
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [22, 28], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 23 dias}
  - nome: Intervalo histórico de 29 a 38 dias
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [29, 38], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 29 dias}
  - nome: Intervalo histórico de 39 a 60 dias
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [39, 60], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 35 dias}
  - nome: Intervalo histórico de 61 a 95 dias
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [61, 95], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 55 dias}
termos_fora_vocabulario:
  - baixado na Receita Federal
  - filial
  - frequência histórica de compra
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| baixado na Receita | jargao | cadastro encerrado no órgão fiscal |
| filial | jargao | unidade filial de um cliente |
| cliente principal | jargao | matriz de um grupo de filiais |
| frequência histórica | jargao | intervalo médio entre pedidos |

## Lacunas

- A entrada não informa a que empresa pertence o cliente principal 36979.

## Ambiguidades

- A faixa de 61 a 95 dias é a última e pode funcionar como regra residual.
