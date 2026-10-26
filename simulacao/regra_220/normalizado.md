---
id: regra_220
origem: simulacao/regra_220/entrada.md
gobr: simulacao/regra_220/regra_220.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 6
procedencia: corpus_sintetico
---

## Regras

cliente com compra na empresa nos últimos 30 dias não é agendado
o restante, sem compra entre 30 e 150 dias, é atendido a cada 7 dias
cliente sem compra com a empresa há mais de 149 dias é atendido a cada 14 dias
cliente sem compra é atendido a cada 14 dias
quem tem menos de 150 dias sem compra não é agendado
todos os clientes são atendidos a cada 7 dias

## Estrutura

```yaml
publico: carteira regional, carteira de reativação e carteira direta
comuns: []
regras:
  - nome: Regional, não agendar compra nos últimos 30 dias
    publico: carteira regional, VENDEDOR_01 a VENDEDOR_04
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias, alcance: empresa}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Regional, restante
    publico: carteira regional, VENDEDOR_01 a VENDEDOR_04
    se: []
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Reativação, sem compra há mais de 149 dias
    publico: carteira de reativação, VENDEDOR_05 e VENDEDOR_06
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 149, unidade: dias, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Reativação, sem compra
    publico: carteira de reativação, VENDEDOR_05 e VENDEDOR_06
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Reativação, não agendar os demais
    publico: carteira de reativação, VENDEDOR_05 e VENDEDOR_06
    se: []
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Direta, todos os clientes
    publico: carteira direta, VENDEDOR_07 e VENDEDOR_08
    se: []
    entao: {acao: agendar, frequencia: fixa 7 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Girobem | empresa_foco | EMPRESA_FOCO |
| vendedor 99 | vendedor | VENDEDOR_01 |
| vendedor 645 | vendedor | VENDEDOR_02 |
| vendedor 693 | vendedor | VENDEDOR_03 |
| vendedor 729 | vendedor | VENDEDOR_04 |
| vendedor 744 | vendedor | VENDEDOR_05 |
| vendedor 738 | vendedor | VENDEDOR_06 |
| vendedor 568 | vendedor | VENDEDOR_07 |
| vendedor 712 | vendedor | VENDEDOR_08 |
| reativação | jargao | retomada de clientes sem compra |

## Lacunas

- Clientes da regional sem compra há mais de 150 dias são cobertos pela regra residual, mas a entrada descreve o restante como "entre 30 e 150 dias".

## Ambiguidades

- Os times são chamados de carteiras, mas definidos por vendedores; não fica claro se trabalham sobre carteira fixa.
