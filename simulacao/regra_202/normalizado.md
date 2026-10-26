---
id: regra_202
origem: simulacao/regra_202/entrada.md
gobr: simulacao/regra_202/regra_202.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 5
procedencia: corpus_sintetico
---

## Regras

cliente sem compra nos últimos 60 dias é atendido a cada 7 dias
cliente sem venda com o vendedor é atendido a cada 7 dias
cliente com uma única compra com o vendedor e sem compra nos últimos 7 dias é atendido a cada 7 dias
cliente com compra nos últimos 30 dias usa o histórico, com máximo de 30 dias
cliente sem pedido entre 31 e 60 dias é atendido a cada 7 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Sem compra nos últimos 60 dias
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 60, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Ativar novo cliente
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Estabelecer relacionamento
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única, alcance: vendedor}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 7, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Alta frequência de compra
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Estimular regularidade
    se:
      - {tipo: tempo_sem_comprar, op: fora_de, valor: [31, 60], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
termos_fora_vocabulario:
  - frequência pelo histórico com teto
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| alta frequência de compra | jargao | cliente que compra com intervalo curto |

## Lacunas

- A entrada não traz regra residual; clientes fora das faixas descritas não têm tratamento declarado.

## Ambiguidades

- "Sem pedido entre 31 e 60 dias" foi registrado como ausência de compra na janela (fora_de).
- O teto de 30 dias da frequência pelo histórico não tem campo próprio e foi registrado apenas na descrição.
