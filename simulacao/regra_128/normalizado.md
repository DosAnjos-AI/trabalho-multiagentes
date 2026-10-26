---
id: regra_128
origem: simulacao/regra_128/entrada.md
gobr: simulacao/regra_128/regra_128.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 30
procedencia: corpus_sintetico
---

## Regras

cliente com cadastro baixado na Receita Federal não é agendado
prospect do grupo da dupla ROTA_01 e ROTA_02 é atendido a cada 7 dias
cliente do grupo com compra nos últimos 60 dias é atendido a cada 5 dias, a partir do dia 16 de cada mês
cliente do grupo com compra em até 90 dias é atendido a cada 7 dias
o restante do grupo é atendido a cada 7 dias
prospect do grupo da dupla ROTA_03 e ROTA_04 é atendido a cada 7 dias
cliente do grupo com compra nos últimos 60 dias é atendido a cada 5 dias, a partir do dia 16 de cada mês
cliente do grupo com compra em até 90 dias é atendido a cada 7 dias
o restante do grupo é atendido a cada 7 dias
prospect do grupo da dupla ROTA_05 e ROTA_06 é atendido a cada 7 dias
cliente do grupo com compra nos últimos 60 dias é atendido a cada 5 dias, a partir do dia 16 de cada mês
cliente do grupo com compra em até 90 dias é atendido a cada 7 dias
o restante do grupo é atendido a cada 7 dias
prospect do grupo da dupla ROTA_07 e ROTA_08 é atendido a cada 7 dias
cliente do grupo com compra nos últimos 60 dias é atendido a cada 5 dias, a partir do dia 16 de cada mês
cliente do grupo com compra em até 90 dias é atendido a cada 7 dias
o restante do grupo é atendido a cada 7 dias
prospect do grupo da dupla ROTA_09 e ROTA_10 é atendido a cada 7 dias
cliente do grupo com compra nos últimos 60 dias é atendido a cada 5 dias, a partir do dia 16 de cada mês
cliente do grupo com compra em até 90 dias é atendido a cada 7 dias
o restante do grupo é atendido a cada 7 dias
prospect do grupo da dupla ROTA_11 e ROTA_12 é atendido a cada 7 dias
cliente do grupo com compra nos últimos 60 dias é atendido a cada 5 dias, a partir do dia 16 de cada mês
cliente do grupo com compra em até 90 dias é atendido a cada 7 dias
o restante do grupo é atendido a cada 7 dias
prospect exclusivo do televendas é atendido a cada 7 dias
cliente com compra nos últimos 60 dias é atendido a cada 7 dias
cliente com compra em até 90 dias é atendido a cada 7 dias
cliente que não está em nenhum dos seis grupos dos externos é atendido a cada 7 dias
quem não se enquadrou em nenhuma regra não é agendado

## Estrutura

```yaml
publico: seis vendedores de televendas, VENDEDOR_01 a VENDEDOR_06
comuns: []
regras:
  - nome: Não agendar baixados na Receita Federal
    publico: os seis televendas, VENDEDOR_01 a VENDEDOR_06
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: baixado na Receita Federal}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Prospects do grupo ROTA_01 e ROTA_02 para o televendas 1
    publico: televendas 1, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: grupo ROTA_01 e ROTA_02, alcance: outro_vendedor}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Ativos do grupo ROTA_01 e ROTA_02 para o televendas 1
    publico: televendas 1, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: grupo ROTA_01 e ROTA_02, alcance: outro_vendedor}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 60, unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: a partir do dia 16 de cada mês, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 5 dias}
  - nome: Retenção do grupo ROTA_01 e ROTA_02 para o televendas 1
    publico: televendas 1, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: grupo ROTA_01 e ROTA_02, alcance: outro_vendedor}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 90, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Recuperação do grupo ROTA_01 e ROTA_02 para o televendas 1
    publico: televendas 1, VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: grupo ROTA_01 e ROTA_02, alcance: outro_vendedor}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Prospects do grupo ROTA_03 e ROTA_04 para o televendas 2
    publico: televendas 2, VENDEDOR_02
    se:
      - {tipo: carteira, op: igual_a, valor: grupo ROTA_03 e ROTA_04, alcance: outro_vendedor}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Ativos do grupo ROTA_03 e ROTA_04 para o televendas 2
    publico: televendas 2, VENDEDOR_02
    se:
      - {tipo: carteira, op: igual_a, valor: grupo ROTA_03 e ROTA_04, alcance: outro_vendedor}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 60, unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: a partir do dia 16 de cada mês, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 5 dias}
  - nome: Retenção do grupo ROTA_03 e ROTA_04 para o televendas 2
    publico: televendas 2, VENDEDOR_02
    se:
      - {tipo: carteira, op: igual_a, valor: grupo ROTA_03 e ROTA_04, alcance: outro_vendedor}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 90, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Recuperação do grupo ROTA_03 e ROTA_04 para o televendas 2
    publico: televendas 2, VENDEDOR_02
    se:
      - {tipo: carteira, op: igual_a, valor: grupo ROTA_03 e ROTA_04, alcance: outro_vendedor}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Prospects do grupo ROTA_05 e ROTA_06 para o televendas 3
    publico: televendas 3, VENDEDOR_03
    se:
      - {tipo: carteira, op: igual_a, valor: grupo ROTA_05 e ROTA_06, alcance: outro_vendedor}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Ativos do grupo ROTA_05 e ROTA_06 para o televendas 3
    publico: televendas 3, VENDEDOR_03
    se:
      - {tipo: carteira, op: igual_a, valor: grupo ROTA_05 e ROTA_06, alcance: outro_vendedor}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 60, unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: a partir do dia 16 de cada mês, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 5 dias}
  - nome: Retenção do grupo ROTA_05 e ROTA_06 para o televendas 3
    publico: televendas 3, VENDEDOR_03
    se:
      - {tipo: carteira, op: igual_a, valor: grupo ROTA_05 e ROTA_06, alcance: outro_vendedor}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 90, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Recuperação do grupo ROTA_05 e ROTA_06 para o televendas 3
    publico: televendas 3, VENDEDOR_03
    se:
      - {tipo: carteira, op: igual_a, valor: grupo ROTA_05 e ROTA_06, alcance: outro_vendedor}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Prospects do grupo ROTA_07 e ROTA_08 para o televendas 5
    publico: televendas 5, VENDEDOR_04
    se:
      - {tipo: carteira, op: igual_a, valor: grupo ROTA_07 e ROTA_08, alcance: outro_vendedor}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Ativos do grupo ROTA_07 e ROTA_08 para o televendas 5
    publico: televendas 5, VENDEDOR_04
    se:
      - {tipo: carteira, op: igual_a, valor: grupo ROTA_07 e ROTA_08, alcance: outro_vendedor}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 60, unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: a partir do dia 16 de cada mês, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 5 dias}
  - nome: Retenção do grupo ROTA_07 e ROTA_08 para o televendas 5
    publico: televendas 5, VENDEDOR_04
    se:
      - {tipo: carteira, op: igual_a, valor: grupo ROTA_07 e ROTA_08, alcance: outro_vendedor}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 90, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Recuperação do grupo ROTA_07 e ROTA_08 para o televendas 5
    publico: televendas 5, VENDEDOR_04
    se:
      - {tipo: carteira, op: igual_a, valor: grupo ROTA_07 e ROTA_08, alcance: outro_vendedor}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Prospects do grupo ROTA_09 e ROTA_10 para o televendas 6
    publico: televendas 6, VENDEDOR_05
    se:
      - {tipo: carteira, op: igual_a, valor: grupo ROTA_09 e ROTA_10, alcance: outro_vendedor}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Ativos do grupo ROTA_09 e ROTA_10 para o televendas 6
    publico: televendas 6, VENDEDOR_05
    se:
      - {tipo: carteira, op: igual_a, valor: grupo ROTA_09 e ROTA_10, alcance: outro_vendedor}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 60, unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: a partir do dia 16 de cada mês, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 5 dias}
  - nome: Retenção do grupo ROTA_09 e ROTA_10 para o televendas 6
    publico: televendas 6, VENDEDOR_05
    se:
      - {tipo: carteira, op: igual_a, valor: grupo ROTA_09 e ROTA_10, alcance: outro_vendedor}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 90, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Recuperação do grupo ROTA_09 e ROTA_10 para o televendas 6
    publico: televendas 6, VENDEDOR_05
    se:
      - {tipo: carteira, op: igual_a, valor: grupo ROTA_09 e ROTA_10, alcance: outro_vendedor}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Prospects do grupo ROTA_11 e ROTA_12 para o televendas 7
    publico: televendas 7, VENDEDOR_06
    se:
      - {tipo: carteira, op: igual_a, valor: grupo ROTA_11 e ROTA_12, alcance: outro_vendedor}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Ativos do grupo ROTA_11 e ROTA_12 para o televendas 7
    publico: televendas 7, VENDEDOR_06
    se:
      - {tipo: carteira, op: igual_a, valor: grupo ROTA_11 e ROTA_12, alcance: outro_vendedor}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 60, unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: a partir do dia 16 de cada mês, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 5 dias}
  - nome: Retenção do grupo ROTA_11 e ROTA_12 para o televendas 7
    publico: televendas 7, VENDEDOR_06
    se:
      - {tipo: carteira, op: igual_a, valor: grupo ROTA_11 e ROTA_12, alcance: outro_vendedor}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 90, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Recuperação do grupo ROTA_11 e ROTA_12 para o televendas 7
    publico: televendas 7, VENDEDOR_06
    se:
      - {tipo: carteira, op: igual_a, valor: grupo ROTA_11 e ROTA_12, alcance: outro_vendedor}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Prospects exclusivos do televendas
    publico: os seis televendas, VENDEDOR_01 a VENDEDOR_06
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Ativos exclusivos do televendas
    publico: os seis televendas, VENDEDOR_01 a VENDEDOR_06
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 60, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Retenção exclusiva do televendas
    publico: os seis televendas, VENDEDOR_01 a VENDEDOR_06
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 90, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Recuperação exclusiva do televendas
    publico: os seis televendas, VENDEDOR_01 a VENDEDOR_06
    se:
      - {tipo: carteira, op: fora_de, valor: [grupo ROTA_01 e ROTA_02, grupo ROTA_03 e ROTA_04, grupo ROTA_05 e ROTA_06, grupo ROTA_07 e ROTA_08, grupo ROTA_09 e ROTA_10, grupo ROTA_11 e ROTA_12], alcance: outro_vendedor}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Clientes que não se enquadraram
    publico: os seis televendas, VENDEDOR_01 a VENDEDOR_06
    se: []
    entao: {acao: nao_agendar, frequencia: nao_informada}
termos_fora_vocabulario:
  - baixado na Receita Federal
  - grupo auxiliar de clientes de outro vendedor
  - a partir de dia do mês
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| vendedor 291 (TMK 1) | vendedor | VENDEDOR_01 |
| vendedor 292 (TMK 2) | vendedor | VENDEDOR_02 |
| vendedor 294 (TMK 3) | vendedor | VENDEDOR_03 |
| vendedor 375 (TMK 5) | vendedor | VENDEDOR_04 |
| vendedor 900 (TMK 6) | vendedor | VENDEDOR_05 |
| vendedor 901 (TMK 7) | vendedor | VENDEDOR_06 |
| vendedor 283 | vendedor | VENDEDOR_07 |
| vendedor 279 | vendedor | VENDEDOR_08 |
| vendedor 286 | vendedor | VENDEDOR_09 |
| vendedor 284 | vendedor | VENDEDOR_10 |
| vendedor 275 | vendedor | VENDEDOR_11 |
| vendedor 277 | vendedor | VENDEDOR_12 |
| vendedor 278 | vendedor | VENDEDOR_13 |
| vendedor 280 | vendedor | VENDEDOR_14 |
| vendedor 273 | vendedor | VENDEDOR_15 |
| vendedor 274 | vendedor | VENDEDOR_16 |
| vendedor 282 | vendedor | VENDEDOR_17 |
| vendedor 276 | vendedor | VENDEDOR_18 |
| Niterói | rota | ROTA_01 |
| Rio 2 | rota | ROTA_02 |
| Lagos | rota | ROTA_03 |
| Norte | rota | ROTA_04 |
| Baixada 1 | rota | ROTA_05 |
| Baixada 3 | rota | ROTA_06 |
| Rio 1 | rota | ROTA_07 |
| Rio 3 | rota | ROTA_08 |
| Sul Fluminense 1 | rota | ROTA_09 |
| Sul Fluminense 2 | rota | ROTA_10 |
| Serrana | rota | ROTA_11 |
| Baixada 2 | rota | ROTA_12 |
| TMK | jargao | televendas |
| ruptura | jargao | repasse de clientes dos externos ao televendas |
| externo | jargao | vendedor de campo |
| grupo auxiliar | jargao | conjunto de clientes repassado a outro vendedor |
| baixado na Receita | jargao | cadastro encerrado no órgão fiscal |

## Lacunas

- A entrada não informa se as compras de 60 e 90 dias consideram o vendedor, o externo ou qualquer vendedor da empresa.
- Não há televendas 4 na numeração dos times; a entrada não explica a ausência.

## Ambiguidades

- A regra de ativos vale a partir do dia 16 de cada mês, mas o nome da regra fala em dia 20.
- As regras de prospects, ativos e retenção exclusivas do televendas não restringem explicitamente os clientes fora dos grupos dos externos; só a recuperação traz essa restrição.
