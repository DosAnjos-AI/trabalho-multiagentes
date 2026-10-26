---
id: regra_214
origem: simulacao/regra_214/entrada.md
gobr: simulacao/regra_214/regra_214.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 10
procedencia: corpus_sintetico
---

## Regras

cliente inadimplente não é agendado
cliente com uma única compra com o vendedor é atendido a cada 14 dias, preferindo dia útil e sábado
cliente do ramo 29 com uma única compra e compra nos últimos 30 dias é atendido a cada 21 dias
cliente dos demais ramos com uma única compra e compra nos últimos 30 dias é atendido a cada 14 dias
cliente ativo com intervalo histórico menor que 14 dias é atendido a cada 10 dias
cliente do ramo 29 com compra com o vendedor entre 21 e 59 dias é atendido a cada 30 dias
cliente dos demais ramos com compra com o vendedor entre 21 e 59 dias é atendido a cada 14 dias
cliente do ramo 29 com compra entre 60 e 89 dias é atendido a cada 14 dias
cliente dos demais ramos com compra entre 60 e 89 dias é atendido a cada 14 dias
cliente sem compra com o vendedor há mais de 90 dias é atendido a cada 10 dias

## Estrutura

```yaml
publico: time de televendas
comuns: []
regras:
  - nome: Não agendar inadimplentes
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Compra única com o vendedor
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única, alcance: vendedor}
      - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Ativado, ramo 29
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única, alcance: vendedor}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
      - {tipo: segmento, op: igual_a, valor: ['29']}
      - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Ativado, demais ramos
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única, alcance: vendedor}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
      - {tipo: segmento, op: fora_de, valor: ['29']}
      - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Compra regularmente
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo, alcance: vendedor}
      - {tipo: tempo_sem_comprar, op: menor_que, valor: 14, unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 10 dias}
  - nome: Estimular regularidade, ramo 29
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [21, 59], unidade: dias, alcance: vendedor}
      - {tipo: segmento, op: igual_a, valor: ['29']}
      - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Estimular regularidade, demais ramos
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [21, 59], unidade: dias, alcance: vendedor}
      - {tipo: segmento, op: fora_de, valor: ['29']}
      - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Em ruptura, ramo 29
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [60, 89], unidade: dias, alcance: vendedor}
      - {tipo: segmento, op: igual_a, valor: ['29']}
      - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Em ruptura, demais ramos
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [60, 89], unidade: dias, alcance: vendedor}
      - {tipo: segmento, op: fora_de, valor: ['29']}
      - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Resgate de cliente sem compra
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 90, unidade: dias, alcance: vendedor}
      - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 10 dias}
termos_fora_vocabulario:
  - preferência por dia útil e sábado
  - frequência histórica de compra
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| ramo de atividade | jargao | segmento do cliente |
| frequência histórica | jargao | intervalo médio entre compras |
| ruptura | jargao | cliente que parou de comprar |

## Lacunas

- A entrada não diz se o televendas trabalha sobre carteira fixa.

## Ambiguidades

- A regra de compra única com o vendedor (14 dias) vem antes das regras de ativado, que também exigem compra única; dependendo da ordem de avaliação, estas podem não ser alcançadas.
