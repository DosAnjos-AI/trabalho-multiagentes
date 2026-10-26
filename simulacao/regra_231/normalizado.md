---
id: regra_231
origem: simulacao/regra_231/entrada.md
gobr: simulacao/regra_231/regra_231.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 7
procedencia: corpus_sintetico
---

## Regras

cliente com cadastro baixado na Receita Federal não é agendado
cliente com compra com qualquer vendedor nos últimos 30 dias não é agendado
cliente com compra entre 30 e 150 dias é atendido a cada 7 dias
cliente com compra nos últimos 150 dias não é agendado
cliente sem compra, prospect, é atendido a cada 14 dias
cliente sem compra com a empresa há mais de 149 dias é atendido a cada 14 dias
todos os clientes são atendidos a cada 7 dias

## Estrutura

```yaml
publico: carteira regional, carteira de reativação e carteira direta
comuns: []
regras:
  - nome: Não agendar baixados na Receita Federal
    publico: os três times
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: baixado na Receita Federal}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Regional, não agendar compra nos últimos 30 dias
    publico: carteira regional, VENDEDOR_01 a VENDEDOR_07
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias, alcance: empresa}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Regional, compra entre 30 e 150 dias
    publico: carteira regional, VENDEDOR_01 a VENDEDOR_07
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [30, 150], unidade: dias, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Reativação, não agendar compra nos últimos 150 dias
    publico: carteira de reativação, VENDEDOR_08 e VENDEDOR_09
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 150, unidade: dias, alcance: empresa}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Reativação, prospects
    publico: carteira de reativação, VENDEDOR_08 e VENDEDOR_09
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Reativação, sem compra há mais de 149 dias
    publico: carteira de reativação, VENDEDOR_08 e VENDEDOR_09
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 149, unidade: dias, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Direta, todos os clientes
    publico: carteira direta, VENDEDOR_10 a VENDEDOR_13
    se: []
    entao: {acao: agendar, frequencia: fixa 7 dias}
termos_fora_vocabulario:
  - baixado na Receita Federal
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| vendedor 200 | vendedor | VENDEDOR_01 |
| vendedor 382 | vendedor | VENDEDOR_02 |
| vendedor 677 | vendedor | VENDEDOR_03 |
| vendedor 631 | vendedor | VENDEDOR_04 |
| vendedor 686 | vendedor | VENDEDOR_05 |
| vendedor 731 | vendedor | VENDEDOR_06 |
| vendedor 789 | vendedor | VENDEDOR_07 |
| vendedor 706 | vendedor | VENDEDOR_08 |
| vendedor 763 | vendedor | VENDEDOR_09 |
| vendedor 708 | vendedor | VENDEDOR_10 |
| vendedor 736 | vendedor | VENDEDOR_11 |
| vendedor 737 | vendedor | VENDEDOR_12 |
| vendedor 755 | vendedor | VENDEDOR_13 |
| baixado na Receita | jargao | cadastro encerrado no órgão fiscal |
| reativação | jargao | retomada de clientes sem compra |

## Lacunas

- A entrada não informa a empresa dona das regras nem a origem do pedido.
- Clientes da regional sem compra há mais de 150 dias não têm regra declarada.

## Ambiguidades

- Os times são chamados de carteiras, mas definidos por vendedores; não fica claro se trabalham sobre carteira fixa.
