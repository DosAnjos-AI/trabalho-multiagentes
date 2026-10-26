---
id: regra_169
origem: simulacao/regra_169/entrada.md
gobr: simulacao/regra_169/regra_169.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 9
procedencia: corpus_sintetico
---

## Regras

prospect do grupo de ruptura do fornecedor ou da carteira de consumidor é atendido a cada 14 dias
cliente do grupo ou da carteira com compra em até 30 dias é atendido a cada 14 dias
cliente do grupo ou da carteira com compra em até 60 dias é atendido a cada 14 dias
cliente do grupo ou da carteira com compra em até 90 dias é atendido a cada 14 dias
cliente do grupo ou da carteira com compra entre 90 e 180 dias é atendido a cada 14 dias
cliente com compra nos últimos 7 dias não é agendado
cliente inadimplente não é agendado
os clientes restantes do televendas não são agendados, para evitar choque de agendas
os clientes restantes do televendas 2 são atendidos a cada 14 dias

## Estrutura

```yaml
publico: time de televendas e time de televendas 2
comuns: []
regras:
  - nome: Prospects do grupo de ruptura e da carteira de consumidor
    publico: televendas, VENDEDOR_02 a VENDEDOR_05
    se:
      - {tipo: carteira, op: igual_a, valor: [grupo de ruptura do fornecedor, carteira de consumidor do televendas], alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Compra em até 30 dias
    publico: televendas, VENDEDOR_02 a VENDEDOR_05
    se:
      - {tipo: carteira, op: igual_a, valor: [grupo de ruptura do fornecedor, carteira de consumidor do televendas], alcance: grupo}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Compra em até 60 dias
    publico: televendas, VENDEDOR_02 a VENDEDOR_05
    se:
      - {tipo: carteira, op: igual_a, valor: [grupo de ruptura do fornecedor, carteira de consumidor do televendas], alcance: grupo}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 60, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Compra em até 90 dias
    publico: televendas, VENDEDOR_02 a VENDEDOR_05
    se:
      - {tipo: carteira, op: igual_a, valor: [grupo de ruptura do fornecedor, carteira de consumidor do televendas], alcance: grupo}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 90, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Inativos entre 90 e 180 dias
    publico: televendas, VENDEDOR_02 a VENDEDOR_05
    se:
      - {tipo: carteira, op: igual_a, valor: [grupo de ruptura do fornecedor, carteira de consumidor do televendas], alcance: grupo}
      - {tipo: tempo_sem_comprar, op: entre, valor: [90, 180], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Não agendar quem comprou nos últimos 7 dias
    publico: televendas e televendas 2
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 7, unidade: dias}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar inadimplentes
    publico: televendas e televendas 2
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar restantes do televendas
    publico: televendas, VENDEDOR_02 a VENDEDOR_05
    se: []
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Restantes do televendas 2
    publico: televendas 2, VENDEDOR_06 a VENDEDOR_08
    se: []
    entao: {acao: agendar, frequencia: fixa 14 dias}
termos_fora_vocabulario:
  - grupo de ruptura de outro time
  - carteira composta por condições
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Motor Diesel | empresa_foco | EMPRESA_FOCO |
| vendedor 341 | vendedor | VENDEDOR_01 |
| vendedor 203 | vendedor | VENDEDOR_02 |
| vendedor 466 | vendedor | VENDEDOR_03 |
| vendedor 314 | vendedor | VENDEDOR_04 |
| vendedor 291 | vendedor | VENDEDOR_05 |
| vendedor 132 | vendedor | VENDEDOR_06 |
| vendedor 232 | vendedor | VENDEDOR_07 |
| vendedor 145 | vendedor | VENDEDOR_08 |
| ruptura de fornecedor | jargao | repasse de clientes sem compra recente do time fornecedor |
| grupo auxiliar | jargao | conjunto de clientes definido para uso em regras |
| choque de agendas | jargao | conflito de agendamento entre times |

## Lacunas

- A entrada não diz quem executa as cinco primeiras regras; foram atribuídas ao televendas por serem da carteira de consumidor do televendas.

## Ambiguidades

- As faixas "até 30", "até 60" e "até 90 dias" se sobrepõem; a ordem de avaliação define qual se aplica.
- Prospects estão incluídos no grupo de ruptura, mas a regra de prospects também cobre a carteira de consumidor.
