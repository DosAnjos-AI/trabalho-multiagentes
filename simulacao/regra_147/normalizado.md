---
id: regra_147
origem: simulacao/regra_147/entrada.md
gobr: simulacao/regra_147/regra_147.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 10
procedencia: corpus_sintetico
---

## Regras

cliente cadastrado a partir de 18 de julho de 2023 e sem visita nos últimos 60 dias é atendido a cada 1 dia
cliente novo, cadastrado a partir de 18 de julho de 2023, é atendido a cada 7 dias
cliente ativo é atendido a cada 5 dias
cliente inativo é atendido a cada 10 dias
cliente sem venda é atendido a cada 20 dias
cliente de curva A do vendedor é atendido a cada 2 dias
cliente de curva B do vendedor é atendido a cada 4 dias
cliente de curva C do vendedor é atendido a cada 7 dias
cliente sem classificação de curva é atendido a cada 15 dias
todos os clientes são atendidos a cada 7 dias

## Estrutura

```yaml
publico: times de carteira, distribuidor, veterinário, portal e pré-venda
comuns: []
regras:
  - nome: Clientes novos sem visita
    publico: times de carteira, veterinário e portal
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: a partir de 18 de julho de 2023, unidade: periodo_nomeado}
      - {tipo: tempo_sem_visita, op: maior_que, valor: 60, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 1 dias}
  - nome: Clientes novos
    publico: times de carteira, veterinário e portal
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: a partir de 18 de julho de 2023, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Ativos
    publico: times de carteira, veterinário e portal
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
    entao: {acao: agendar, frequencia: fixa 5 dias}
  - nome: Inativos
    publico: times de carteira, veterinário e portal
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
    entao: {acao: agendar, frequencia: fixa 10 dias}
  - nome: Sem venda
    publico: times de carteira, veterinário e portal
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 20 dias}
  - nome: Curva A do distribuidor
    publico: time distribuidor, VENDEDOR_03 a VENDEDOR_06
    se:
      - {tipo: valor_cliente, op: igual_a, valor: curva A, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 2 dias}
  - nome: Curva B do distribuidor
    publico: time distribuidor, VENDEDOR_03 a VENDEDOR_06
    se:
      - {tipo: valor_cliente, op: igual_a, valor: curva B, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 4 dias}
  - nome: Curva C do distribuidor
    publico: time distribuidor, VENDEDOR_03 a VENDEDOR_06
    se:
      - {tipo: valor_cliente, op: igual_a, valor: curva C, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Sem classificação do distribuidor
    publico: time distribuidor, VENDEDOR_03 a VENDEDOR_06
    se: []
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Todos os clientes da pré-venda
    publico: time de pré-venda, VENDEDOR_10, VENDEDOR_11 e VENDEDOR_12
    se: []
    entao: {acao: agendar, frequencia: fixa 7 dias}
termos_fora_vocabulario:
  - data de cadastro a partir de dia específico
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| HospDrogas | empresa_foco | EMPRESA_FOCO |
| vendedor 3597 | vendedor | VENDEDOR_01 |
| vendedor 3568 | vendedor | VENDEDOR_02 |
| vendedor 3516 | vendedor | VENDEDOR_03 |
| vendedor 3556 | vendedor | VENDEDOR_04 |
| vendedor 3531 | vendedor | VENDEDOR_05 |
| vendedor 3519 | vendedor | VENDEDOR_06 |
| vendedor 3559 | vendedor | VENDEDOR_07 |
| vendedor 3594 | vendedor | VENDEDOR_08 |
| vendedor 3580 | vendedor | VENDEDOR_09 |
| vendedor 3621 | vendedor | VENDEDOR_10 |
| vendedor 3622 | vendedor | VENDEDOR_11 |
| vendedor 3623 | vendedor | VENDEDOR_12 |
| petvet | jargao | time de atendimento veterinário |
| portal | jargao | time de vendas por portal |
| pré-venda | jargao | time que prepara o pedido antes da venda |
| curva A, B e C | jargao | faixas de cliente por faturamento |

## Lacunas

- A entrada não lista todos os 17 vendedores do time de carteira nem os 20 do portal; dá apenas o primeiro e o último código de cada lista.
- A entrada não define os critérios das curvas A, B e C.

## Ambiguidades

- "De ID 3597 a 3568" pode ser lido como faixa numérica de códigos, mas os códigos não estão em ordem crescente; trata-se do primeiro e do último de uma lista.
