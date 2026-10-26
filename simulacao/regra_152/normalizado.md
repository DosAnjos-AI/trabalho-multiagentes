---
id: regra_152
origem: simulacao/regra_152/entrada.md
gobr: simulacao/regra_152/regra_152.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 7
procedencia: corpus_sintetico
---

## Regras

prospect que nunca fez pedido com o vendedor é atendido a cada 7 dias
cliente que fez o primeiro pedido é atendido a cada 7 dias
cliente com pedido entre 0 e 7 dias é atendido a cada 14 dias
cliente com pedido entre 7 e 30 dias é atendido a cada 14 dias
cliente com pedido entre 30 e 60 dias é atendido a cada 14 dias
cliente com pedido entre 60 e 90 dias é atendido a cada 7 dias
cliente com pedido há 90 dias ou mais é atendido a cada 7 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Prospects do vendedor
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Primeiro pedido
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Pedido entre 0 e 7 dias
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [0, 7], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Pedido entre 7 e 30 dias
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [7, 30], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Pedido entre 30 e 60 dias
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [30, 60], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Pedido entre 60 e 90 dias
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [60, 90], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Pedido há 90 dias ou mais
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 90, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Br Distribuidora | empresa_foco | EMPRESA_FOCO |
| televendas | jargao | atendimento por telefone |
| prospect | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não informa se os pedidos das faixas consideram o vendedor ou a empresa.

## Ambiguidades

- As faixas compartilham os limites 7, 30, 60 e 90 dias.
- "Há 90 dias ou mais" inclui o próprio 90, registrado como maior_que 90 por falta de operador "maior ou igual".
