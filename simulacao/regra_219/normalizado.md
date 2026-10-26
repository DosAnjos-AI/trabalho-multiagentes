---
id: regra_219
origem: simulacao/regra_219/entrada.md
gobr: simulacao/regra_219/regra_219.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 6
procedencia: corpus_sintetico
---

## Regras

cliente com cadastro baixado na Receita Federal não é agendado
cliente que comprou com a empresa nos últimos 25 dias não é agendado
prospect com o vendedor é atendido a cada 21 dias
cliente com pedido com a empresa entre 26 e 60 dias é atendido a cada 14 dias
cliente com pedido com a empresa entre 61 e 90 dias é atendido a cada 7 dias
inativo há mais de 90 dias é atendido a cada 21 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Não agendar baixados na Receita Federal
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: baixado na Receita Federal}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar compra nos últimos 25 dias
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 25, unidade: dias, alcance: empresa}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Prospects do vendedor
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Pedido entre 26 e 60 dias
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [26, 60], unidade: dias, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Pedido entre 61 e 90 dias
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [61, 90], unidade: dias, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos há mais de 90 dias
    se: []
    entao: {acao: agendar, frequencia: fixa 21 dias}
termos_fora_vocabulario:
  - baixado na Receita Federal
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| baixado na Receita | jargao | cadastro encerrado no órgão fiscal |
| prospect | jargao | cliente que nunca comprou |

## Lacunas

- nenhuma

## Ambiguidades

- A regra de inativos não tem critério próprio e funciona como regra residual.
