---
id: regra_182
origem: simulacao/regra_182/entrada.md
gobr: simulacao/regra_182/regra_182.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 35
procedencia: corpus_sintetico
---

## Regras

cliente pessoa física não é agendado
cliente inadimplente não é agendado
cliente com cadastro baixado na Receita Federal não é agendado
cliente com pedido nos últimos 7 dias não é agendado
prospect dos ramos 89 a 103 é atendido a cada 7 dias
cliente do ramo 89 com pedido em 45 dias é atendido a cada 14 dias
cliente do ramo 89 com pedido acima de 45 dias é atendido a cada 7 dias
cliente do ramo 90 com pedido em 60 dias é atendido a cada 21 dias
cliente do ramo 90 com pedido acima de 60 dias é atendido a cada 10 dias
cliente do ramo 91 com pedido em 45 dias é atendido a cada 14 dias
cliente do ramo 91 com pedido acima de 45 dias é atendido a cada 7 dias
cliente do ramo 92 com pedido em 90 dias é atendido a cada 28 dias
cliente do ramo 92 com pedido acima de 90 dias é atendido a cada 14 dias
cliente do ramo 93 com pedido em 45 dias é atendido a cada 14 dias
cliente do ramo 93 com pedido acima de 45 dias é atendido a cada 7 dias
cliente do ramo 94 com pedido em 90 dias é atendido a cada 28 dias
cliente do ramo 94 com pedido acima de 90 dias é atendido a cada 14 dias
cliente do ramo 95 com pedido em 75 dias é atendido a cada 21 dias
cliente do ramo 95 com pedido acima de 75 dias é atendido a cada 14 dias
cliente do ramo 96 com pedido em 75 dias é atendido a cada 28 dias
cliente do ramo 96 com pedido acima de 75 dias é atendido a cada 14 dias
cliente do ramo 97 com pedido em 60 dias é atendido a cada 21 dias
cliente do ramo 97 com pedido acima de 60 dias é atendido a cada 10 dias
cliente do ramo 98 com pedido em 60 dias é atendido a cada 21 dias
cliente do ramo 98 com pedido acima de 60 dias é atendido a cada 10 dias
cliente do ramo 99 com pedido em 45 dias é atendido a cada 14 dias
cliente do ramo 99 com pedido acima de 45 dias é atendido a cada 7 dias
cliente do ramo 100 com pedido em 75 dias é atendido a cada 28 dias
cliente do ramo 100 com pedido acima de 75 dias é atendido a cada 7 dias
cliente do ramo 101 com pedido em 90 dias é atendido a cada 28 dias
cliente do ramo 101 com pedido acima de 90 dias é atendido a cada 14 dias
cliente do ramo 102 com pedido em 45 dias é atendido a cada 14 dias
cliente do ramo 102 com pedido acima de 45 dias é atendido a cada 7 dias
cliente do ramo 103 com pedido em 90 dias é atendido a cada 28 dias
cliente do ramo 103 com pedido acima de 90 dias é atendido a cada 14 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Não agendar pessoa física
    se:
      - {tipo: segmento, op: igual_a, valor: pessoa física}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar inadimplentes
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar baixados na Receita Federal
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: baixado na Receita Federal}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar pedido nos últimos 7 dias
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 7, unidade: dias}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Prospects dos ramos 89 a 103
    se:
      - {tipo: segmento, op: igual_a, valor: ['89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103']}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Mangueiras com pedido em 45 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['89']}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 45, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Mangueiras com pedido acima de 45 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['89']}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 45, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Materiais de limpeza com pedido em 60 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['90']}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 60, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Materiais de limpeza com pedido acima de 60 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['90']}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 60, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 10 dias}
  - nome: Revenda de equipamentos de proteção com pedido em 45 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['91']}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 45, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Revenda de equipamentos de proteção com pedido acima de 45 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['91']}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 45, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Materiais de construção com pedido em 90 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['92']}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 90, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 28 dias}
  - nome: Materiais de construção com pedido acima de 90 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['92']}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 90, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Ferragem e ferramentas com pedido em 45 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['93']}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 45, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Ferragem e ferramentas com pedido acima de 45 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['93']}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 45, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Agropecuária com pedido em 90 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['94']}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 90, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 28 dias}
  - nome: Agropecuária com pedido acima de 90 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['94']}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 90, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Prestador de serviço com pedido em 75 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['95']}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 75, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Prestador de serviço com pedido acima de 75 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['95']}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 75, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Indústria com pedido em 75 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['96']}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 75, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 28 dias}
  - nome: Indústria com pedido acima de 75 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['96']}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 75, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Cooperativa com pedido em 60 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['97']}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 60, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Cooperativa com pedido acima de 60 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['97']}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 60, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 10 dias}
  - nome: Home center com pedido em 60 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['98']}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 60, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Home center com pedido acima de 60 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['98']}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 60, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 10 dias}
  - nome: Atacado com pedido em 45 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['99']}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 45, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Atacado com pedido acima de 45 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['99']}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 45, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Construtora com pedido em 75 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['100']}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 75, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 28 dias}
  - nome: Construtora com pedido acima de 75 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['100']}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 75, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Órgão público com pedido em 90 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['101']}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 90, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 28 dias}
  - nome: Órgão público com pedido acima de 90 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['101']}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 90, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Comércio eletrônico com pedido em 45 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['102']}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 45, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Comércio eletrônico com pedido acima de 45 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['102']}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 45, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Produtor rural com pedido em 90 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['103']}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 90, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 28 dias}
  - nome: Produtor rural com pedido acima de 90 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['103']}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 90, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
termos_fora_vocabulario:
  - pessoa física
  - baixado na Receita Federal
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| ramo de atividade | jargao | segmento do cliente |
| EPI | jargao | equipamento de proteção individual |
| e-commerce | jargao | comércio eletrônico |
| baixado na Receita | jargao | cadastro encerrado no órgão fiscal |

## Lacunas

- A entrada não informa se os pedidos consideram o vendedor ou a empresa.

## Ambiguidades

- Em cada ramo, a regra "acima do prazo" pode funcionar como regra residual do ramo, sem critério explícito de tempo.
