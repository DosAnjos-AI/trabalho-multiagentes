---
id: regra_218
origem: simulacao/regra_218/entrada.md
gobr: simulacao/regra_218/regra_218.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 6
procedencia: corpus_sintetico
---

## Regras

cliente sem compra há mais de 7 dias é atendido a cada 5 dias
cliente com compra nos últimos 14 dias usa o histórico, com máximo de 14 dias
os demais clientes são atendidos a cada 14 dias
prospect com o vendedor é atendido a cada 14 dias
cliente com compra nos últimos 30 dias é atendido a cada 14 dias
cliente sem compra em 30 dias é atendido a cada 7 dias

## Estrutura

```yaml
publico: primeiro time de televendas e segundo time (VENDEDOR_01)
comuns: []
regras:
  - nome: Sem compra há mais de 7 dias
    publico: primeiro time, televendas ativos exceto VENDEDOR_01
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 7, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 5 dias}
  - nome: Compra nos últimos 14 dias
    publico: primeiro time, televendas ativos exceto VENDEDOR_01
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 14, unidade: dias}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Demais clientes do primeiro time
    publico: primeiro time, televendas ativos exceto VENDEDOR_01
    se: []
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Prospects do vendedor no segundo time
    publico: segundo time, VENDEDOR_01
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Compra nos últimos 30 dias no segundo time
    publico: segundo time, VENDEDOR_01
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Sem compra em 30 dias no segundo time
    publico: segundo time, VENDEDOR_01
    se: []
    entao: {acao: agendar, frequencia: fixa 7 dias}
termos_fora_vocabulario:
  - frequência pelo histórico com teto
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| vendedor 4504 | vendedor | VENDEDOR_01 |
| televendas | jargao | atendimento por telefone |
| prospect | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não informa se as compras consideram o vendedor ou a empresa.

## Ambiguidades

- No primeiro time, a regra de quem está sem compra há mais de 7 dias vem antes da de compra nos últimos 14 dias; clientes entre 8 e 14 dias caem na primeira, dependendo da ordem de avaliação.
- O teto de 14 dias da frequência pelo histórico não tem campo próprio e foi registrado apenas na descrição.
