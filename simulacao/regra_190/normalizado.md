---
id: regra_190
origem: simulacao/regra_190/entrada.md
gobr: simulacao/regra_190/regra_190.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 10
procedencia: corpus_sintetico
---

## Regras

prospect é atendido a cada 21 dias
cliente com uma única compra e cadastrado há mais de 30 dias é atendido a cada 10 dias
cliente adimplente com compra entre 61 e 90 dias é atendido a cada 7 dias
cliente adimplente e inativo com a empresa é atendido a cada 14 dias
cliente de curva A com compra no mês usa o histórico, com máximo de 30 dias
cliente de curva A sem compra no mês é atendido a cada 7 dias
cliente de curva B com compra no mês usa o histórico, com máximo de 30 dias
cliente de curva B sem compra no mês é atendido a cada 14 dias
demais clientes com compra no mês usam o histórico, com máximo de 30 dias
demais clientes sem compra no mês são atendidos a cada 21 dias

## Estrutura

```yaml
publico: todos os vendedores ativos, tratados como televendas
comuns: []
regras:
  - nome: Prospects
    publico: todos os vendedores ativos
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Ativado, boas-vindas
    publico: todos os vendedores ativos
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única}
      - {tipo: situacao_cadastro, op: maior_que, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 10 dias}
  - nome: Em ruptura
    publico: todos os vendedores ativos
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
      - {tipo: tempo_sem_comprar, op: entre, valor: [61, 90], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos, resgate
    publico: todos os vendedores ativos
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Curva A com compra no mês
    publico: todos os vendedores ativos
    se:
      - {tipo: valor_cliente, op: igual_a, valor: curva A}
      - {tipo: tempo_sem_comprar, op: igual_a, valor: mês atual, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Curva A sem compra no mês
    publico: todos os vendedores ativos
    se:
      - {tipo: valor_cliente, op: igual_a, valor: curva A}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Curva B com compra no mês
    publico: todos os vendedores ativos
    se:
      - {tipo: valor_cliente, op: igual_a, valor: curva B}
      - {tipo: tempo_sem_comprar, op: igual_a, valor: mês atual, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Curva B sem compra no mês
    publico: todos os vendedores ativos
    se:
      - {tipo: valor_cliente, op: igual_a, valor: curva B}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Curva C ou demais com compra no mês
    publico: todos os vendedores ativos
    se:
      - {tipo: tempo_sem_comprar, op: igual_a, valor: mês atual, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Curva C ou demais sem compra no mês
    publico: todos os vendedores ativos
    se: []
    entao: {acao: agendar, frequencia: fixa 21 dias}
termos_fora_vocabulario:
  - compra no mês corrente
  - frequência pelo histórico com teto
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Ases | empresa_foco | EMPRESA_FOCO |
| televendas | jargao | atendimento por telefone |
| prospect | jargao | cliente que nunca comprou |
| curva A, B e C | jargao | faixas de cliente por faturamento |
| ruptura | jargao | cliente que parou de comprar |

## Lacunas

- A entrada não define os critérios das curvas A, B e C.

## Ambiguidades

- As regras "sem compra no mês" não trazem critério explícito de ausência de compra; funcionam como residuais de cada curva.
- O teto de 30 dias da frequência pelo histórico não tem campo próprio e foi registrado apenas na descrição.
