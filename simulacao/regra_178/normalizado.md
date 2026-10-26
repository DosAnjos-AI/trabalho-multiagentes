---
id: regra_178
origem: simulacao/regra_178/entrada.md
gobr: simulacao/regra_178/regra_178.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 11
procedencia: corpus_sintetico
---

## Regras

cliente com cadastro baixado na Receita Federal não é agendado
cliente cadastrado há mais de 7 dias não é agendado
cliente que comprou nos últimos 39 dias não é agendado
cliente cadastrado há 60 dias é atendido a cada 30 dias
cliente cadastrado há 30 dias é atendido a cada 20 dias
cliente cadastrado há 15 dias é atendido a cada 15 dias
cliente cadastrado há 8 dias é atendido a cada 15 dias
cliente com compra entre 40 e 89 dias é atendido a cada 15 dias
cliente com compra entre 90 e 119 dias é atendido a cada 7 dias
cliente com compra entre 120 e 359 dias é atendido a cada 7 dias
cliente sem compra há mais de 359 dias é atendido a cada 7 dias

## Estrutura

```yaml
publico: primeiro time de televendas e segundo time de televendas (VENDEDOR_01)
comuns: []
regras:
  - nome: Não agendar baixados na Receita Federal
    publico: primeiro time, televendas ativos
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: baixado na Receita Federal}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar cadastrados há mais de 7 dias
    publico: segundo time, VENDEDOR_01
    se:
      - {tipo: situacao_cadastro, op: maior_que, valor: 7, unidade: dias}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar compra recente
    publico: primeiro time, televendas ativos
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 39, unidade: dias}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Tentativa final
    publico: segundo time, VENDEDOR_01
    se:
      - {tipo: situacao_cadastro, op: maior_que, valor: 60, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Contato frio
    publico: segundo time, VENDEDOR_01
    se:
      - {tipo: situacao_cadastro, op: maior_que, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 20 dias}
  - nome: Contato morno
    publico: segundo time, VENDEDOR_01
    se:
      - {tipo: situacao_cadastro, op: maior_que, valor: 15, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Acompanhamento
    publico: segundo time, VENDEDOR_01
    se:
      - {tipo: situacao_cadastro, op: maior_que, valor: 8, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Estimular recompra
    publico: primeiro time, televendas ativos
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [40, 89], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Reativação moderada
    publico: primeiro time, televendas ativos
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [90, 119], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Reativação intensa
    publico: primeiro time, televendas ativos
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [120, 359], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Resgate crítico
    publico: primeiro time, televendas ativos
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 359, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
termos_fora_vocabulario:
  - baixado na Receita Federal
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| vendedor 48 | vendedor | VENDEDOR_01 |
| televendas | jargao | atendimento por telefone |
| lead | jargao | contato comercial potencial |
| follow-up | jargao | acompanhamento de contato |
| baixado na Receita | jargao | cadastro encerrado no órgão fiscal |

## Lacunas

- A entrada não diz se os times trabalham sobre carteira fixa.

## Ambiguidades

- O bloqueio de cadastrados há mais de 7 dias no segundo time contradiz as regras seguintes do mesmo time, que agendam cadastrados há 8, 15, 30 e 60 dias; a ordem de avaliação define se essas regras chegam a valer.
- VENDEDOR_01 também está no primeiro time, que reúne todos os televendas ativos.
