---
id: regra_222
origem: simulacao/regra_222/entrada.md
gobr: simulacao/regra_222/regra_222.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 7
procedencia: corpus_sintetico
---

## Regras

cliente adimplente dos ramos listados sem venda há mais de 30 dias é atendido a cada 14 dias
cliente adimplente dos demais ramos listados sem compra há mais de 45 dias é atendido a cada 14 dias
cliente de curva A com compra em 90 dias é atendido a cada 14 dias
cliente de curva B com compra em 90 dias é atendido a cada 21 dias
cliente de curva C com compra em 90 dias é atendido a cada 28 dias
cliente sem classificação de curva e com compra em 90 dias é atendido a cada 21 dias
cliente sem compra há mais de 90 dias é atendido a cada 21 dias

## Estrutura

```yaml
publico: time de ruptura global e time de carteira
comuns: []
regras:
  - nome: Ruptura global, sem venda há mais de 30 dias
    publico: ruptura global, VENDEDOR_01 a VENDEDOR_05
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 30, unidade: dias}
      - {tipo: segmento, op: igual_a, valor: ['6', '7', '8', '10', '28', '32', '33', '37', '38', '40', '41', '42']}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Ruptura global, sem compra há mais de 45 dias
    publico: ruptura global, VENDEDOR_01 a VENDEDOR_05
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 45, unidade: dias}
      - {tipo: segmento, op: igual_a, valor: ['1', '2', '3', '4', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '29', '30', '31', '34', '35', '36', '39', '50', '99']}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Carteira, curva A com compra em 90 dias
    publico: carteira, VENDEDOR_06 a VENDEDOR_08
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 90, unidade: dias}
      - {tipo: valor_cliente, op: igual_a, valor: curva A}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Carteira, curva B com compra em 90 dias
    publico: carteira, VENDEDOR_06 a VENDEDOR_08
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 90, unidade: dias}
      - {tipo: valor_cliente, op: igual_a, valor: curva B}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Carteira, curva C com compra em 90 dias
    publico: carteira, VENDEDOR_06 a VENDEDOR_08
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 90, unidade: dias}
      - {tipo: valor_cliente, op: igual_a, valor: curva C}
    entao: {acao: agendar, frequencia: fixa 28 dias}
  - nome: Carteira, sem classificação com compra em 90 dias
    publico: carteira, VENDEDOR_06 a VENDEDOR_08
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 90, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Carteira, sem compra há mais de 90 dias
    publico: carteira, VENDEDOR_06 a VENDEDOR_08
    se: []
    entao: {acao: agendar, frequencia: fixa 21 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| vendedor 8506 | vendedor | VENDEDOR_01 |
| vendedor 8507 | vendedor | VENDEDOR_02 |
| vendedor 8508 | vendedor | VENDEDOR_03 |
| vendedor 8509 | vendedor | VENDEDOR_04 |
| vendedor 8512 | vendedor | VENDEDOR_05 |
| vendedor 602 | vendedor | VENDEDOR_06 |
| vendedor 607 | vendedor | VENDEDOR_07 |
| vendedor 8406 | vendedor | VENDEDOR_08 |
| ruptura global | jargao | clientes sem compra recente com a empresa |
| curva A, B e C | jargao | faixas de cliente por faturamento |

## Lacunas

- A entrada não define os critérios das curvas A, B e C nem o significado dos códigos de ramo.
- Clientes da ruptura global fora das duas listas de ramos não têm regra declarada.

## Ambiguidades

- nenhuma
