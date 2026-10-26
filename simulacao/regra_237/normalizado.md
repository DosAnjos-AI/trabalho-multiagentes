---
id: regra_237
origem: simulacao/regra_237/entrada.md
gobr: simulacao/regra_237/regra_237.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 5
procedencia: corpus_sintetico
---

## Regras

cliente sem venda é atendido a cada 14 dias
cliente com compra nos últimos 30 dias e intervalo histórico menor que 30 dias usa o histórico, com máximo de 30 dias
cliente com compra entre 30 e 60 dias é atendido a cada 14 dias
cliente sem compra há mais de 60 dias e intervalo histórico maior que 30 dias é atendido a cada 14 dias
cliente sem compra há mais de 60 dias é atendido a cada 14 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Clientes ativados
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Compra com regularidade
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
      - {tipo: tempo_sem_comprar, op: menor_que, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Estimular a regularidade
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [30, 60], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Clientes resgatados
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 60, unidade: dias}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Resgatar inativos
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 60, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
termos_fora_vocabulario:
  - frequência histórica de compra
  - frequência pelo histórico com teto
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| frequência histórica | jargao | intervalo médio entre compras |
| resgate | jargao | reativação de cliente inativo |

## Lacunas

- A entrada não traz regra residual para clientes fora das faixas descritas.

## Ambiguidades

- O nome "clientes ativados" é aplicado a clientes sem venda, o que contradiz o sentido usual de ativado.
- As regras de resgatados e de resgatar inativos têm a mesma frequência; a segunda engloba a primeira.
- O teto de 30 dias da frequência pelo histórico foi registrado apenas na descrição.
