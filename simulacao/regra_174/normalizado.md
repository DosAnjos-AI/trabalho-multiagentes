---
id: regra_174
origem: simulacao/regra_174/entrada.md
gobr: simulacao/regra_174/regra_174.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 12
procedencia: corpus_sintetico
---

## Regras

cliente inadimplente não é agendado
cliente com cadastro baixado na Receita Federal não é agendado
prospect com o vendedor é atendido a cada 14 dias
cliente com uma única compra com o vendedor e cadastrado há mais de 60 dias é atendido a cada 21 dias
cliente com compra com o vendedor nos últimos 30 dias e intervalo histórico menor que 14 dias usa o histórico, entre 10 e 14 dias
cliente dos ramos 9 e 18 com compra nos últimos 60 dias e intervalo histórico menor que 30 dias usa o histórico, entre 14 e 21 dias
cliente dos demais ramos com compra nos últimos 60 dias e intervalo histórico menor que 30 dias é atendido a cada 28 dias
cliente dos ramos 9 e 18 com compra entre 21 e 60 dias é atendido a cada 14 dias
cliente dos demais ramos com compra entre 21 e 60 dias é atendido a cada 21 dias
cliente dos ramos 9 e 18 com compra entre 61 e 90 dias é atendido a cada 14 dias
cliente dos demais ramos com compra entre 61 e 90 dias é atendido a cada 14 dias
cliente sem compra há mais de 90 dias é atendido a cada 21 dias

## Estrutura

```yaml
publico: time de televendas
comuns: []
regras:
  - nome: Não agendar inadimplentes
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar baixados na Receita Federal
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: baixado na Receita Federal}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Prospects do vendedor
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Cliente ativado
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única, alcance: vendedor}
      - {tipo: situacao_cadastro, op: maior_que, valor: 60, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Alta frequência de compra
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias, alcance: vendedor}
      - {tipo: tempo_sem_comprar, op: menor_que, valor: 14, unidade: dias}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Compra regular, ramos 9 e 18
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 60, unidade: dias}
      - {tipo: tempo_sem_comprar, op: menor_que, valor: 30, unidade: dias}
      - {tipo: segmento, op: igual_a, valor: ['9', '18']}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Compra regular, demais ramos
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 60, unidade: dias}
      - {tipo: tempo_sem_comprar, op: menor_que, valor: 30, unidade: dias}
      - {tipo: segmento, op: fora_de, valor: ['9', '18']}
    entao: {acao: agendar, frequencia: fixa 28 dias}
  - nome: Estimular regularidade, ramos 9 e 18
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [21, 60], unidade: dias}
      - {tipo: segmento, op: igual_a, valor: ['9', '18']}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Estimular regularidade, demais ramos
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [21, 60], unidade: dias}
      - {tipo: segmento, op: fora_de, valor: ['9', '18']}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Em ruptura, ramos 9 e 18
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [61, 90], unidade: dias}
      - {tipo: segmento, op: igual_a, valor: ['9', '18']}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Em ruptura, demais ramos
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [61, 90], unidade: dias}
      - {tipo: segmento, op: fora_de, valor: ['9', '18']}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Inativos
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 90, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 21 dias}
termos_fora_vocabulario:
  - baixado na Receita Federal
  - frequência histórica de compra
  - frequência pelo histórico com mínimo e máximo
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| baixado na Receita | jargao | cadastro encerrado no órgão fiscal |
| prospect | jargao | cliente que nunca comprou |
| frequência histórica | jargao | intervalo médio entre compras |
| ramo de atividade | jargao | segmento do cliente |
| ruptura | jargao | cliente que parou de comprar |

## Lacunas

- A entrada não diz se o televendas trabalha sobre carteira fixa.

## Ambiguidades

- Os limites das frequências pelo histórico (10 a 14 dias; 14 a 21 dias) não têm campo próprio e foram registrados apenas na descrição.
