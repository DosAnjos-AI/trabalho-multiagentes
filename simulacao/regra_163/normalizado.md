---
id: regra_163
origem: simulacao/regra_163/entrada.md
gobr: simulacao/regra_163/regra_163.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 12
procedencia: corpus_sintetico
---

## Regras

cliente da carteira de construtoras que comprou nos últimos 30 dias não é agendado
construtora sem venda com o vendedor é atendida a cada 30 dias
construtora com uma única compra e sem compra nos últimos 60 dias é atendida a cada 21 dias
construtora sem compra com o vendedor entre 31 e 60 dias é atendida a cada 28 dias
construtora sem compra entre 61 e 90 dias é atendida a cada 14 dias
o restante das construtoras é atendido a cada 21 dias
cliente de material de construção sem venda é atendido a cada 7 dias
cliente com uma única compra e sem compra nos últimos 30 dias é atendido a cada 14 dias
cliente com última compra entre 7 e 30 dias usa a frequência do histórico, entre 7 e 30 dias
cliente sem compra entre 31 e 60 dias é atendido a cada 14 dias
cliente sem compra entre 61 e 90 dias é atendido a cada 7 dias
o restante é atendido a cada 7 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Construtoras, não agendar quem comprou nos últimos 30 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['3', '6', '15', '16']}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Construtoras, sem venda com o vendedor
    se:
      - {tipo: segmento, op: igual_a, valor: ['3', '6', '15', '16']}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Construtoras, compra única
    se:
      - {tipo: segmento, op: igual_a, valor: ['3', '6', '15', '16']}
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 60, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Construtoras, estimular regularidade
    se:
      - {tipo: segmento, op: igual_a, valor: ['3', '6', '15', '16']}
      - {tipo: tempo_sem_comprar, op: fora_de, valor: [31, 60], unidade: dias, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 28 dias}
  - nome: Construtoras, entrando em ruptura
    se:
      - {tipo: segmento, op: igual_a, valor: ['3', '6', '15', '16']}
      - {tipo: tempo_sem_comprar, op: fora_de, valor: [61, 90], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Construtoras, restante
    se:
      - {tipo: segmento, op: igual_a, valor: ['3', '6', '15', '16']}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Material de construção, sem venda
    se:
      - {tipo: segmento, op: fora_de, valor: ['3', '6', '15', '16']}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Material de construção, compra única
    se:
      - {tipo: segmento, op: fora_de, valor: ['3', '6', '15', '16']}
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Material de construção, compra regular
    se:
      - {tipo: segmento, op: fora_de, valor: ['3', '6', '15', '16']}
      - {tipo: tempo_sem_comprar, op: entre, valor: [7, 30], unidade: dias}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Material de construção, estimular regularidade
    se:
      - {tipo: segmento, op: fora_de, valor: ['3', '6', '15', '16']}
      - {tipo: tempo_sem_comprar, op: fora_de, valor: [31, 60], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Material de construção, entrando em ruptura
    se:
      - {tipo: segmento, op: fora_de, valor: ['3', '6', '15', '16']}
      - {tipo: tempo_sem_comprar, op: fora_de, valor: [61, 90], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Material de construção, restante
    se:
      - {tipo: segmento, op: fora_de, valor: ['3', '6', '15', '16']}
    entao: {acao: agendar, frequencia: fixa 7 dias}
termos_fora_vocabulario:
  - carteira livre por ramo
  - frequência pelo histórico com mínimo e máximo
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| carteira livre | jargao | conjunto de clientes compartilhado |
| matcom | jargao | material de construção |
| ramo de atividade | jargao | segmento do cliente |
| ruptura | jargao | cliente que parou de comprar |

## Lacunas

- A entrada não informa se as compras consideram o vendedor ou a empresa em todas as faixas.

## Ambiguidades

- "Sem compra entre 31 e 60 dias" foi registrado como ausência de compra na janela (fora_de); pode ser lido como última compra nessa faixa.
- As carteiras são descritas como livres e com sobreposição possível, mas os ramos que as definem são complementares.
