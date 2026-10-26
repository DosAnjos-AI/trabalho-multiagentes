---
id: regra_167
origem: simulacao/regra_167/entrada.md
gobr: simulacao/regra_167/regra_167.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 7
procedencia: corpus_sintetico
---

## Regras

cliente com cadastro baixado na Receita Federal não é agendado
prospect é atendido a cada 7 dias
cliente com uma única compra é atendido a cada 15 dias
cliente com compra nos últimos 30 dias usa o histórico, entre 7 e 21 dias
cliente com compra entre 31 e 90 dias é atendido a cada 28 dias
cliente com compra entre 91 e 120 dias é atendido a cada 45 dias
cliente sem venda da empresa em 120 dias é atendido a cada 60 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Não agendar baixados na Receita Federal
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: baixado na Receita Federal}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Primeira compra
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Primeiro pedido
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única}
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Ativos pelo histórico
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Aumentar a regularidade
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [31, 90], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 28 dias}
  - nome: Caminhando para a inatividade
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [91, 120], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 45 dias}
  - nome: Resgate de inativos
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 120, unidade: dias, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 60 dias}
termos_fora_vocabulario:
  - baixado na Receita Federal
  - frequência pelo histórico com mínimo e máximo
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| baixado na Receita | jargao | cadastro encerrado no órgão fiscal |
| prospect | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não informa a empresa nem se o televendas trabalha sobre carteira fixa.

## Ambiguidades

- Os limites de 7 e 21 dias da frequência pelo histórico não têm campo próprio e foram registrados apenas na descrição.
