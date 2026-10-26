---
id: regra_194
origem: simulacao/regra_194/entrada.md
gobr: simulacao/regra_194/regra_194.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 5
procedencia: corpus_sintetico
---

## Regras

cliente com cadastro baixado na Receita Federal não é agendado
prospect é atendido a cada 7 dias
cliente com último pedido em até 60 dias é atendido a cada 14 dias
cliente com pedido entre 60 e 90 dias é atendido a cada 7 dias
cliente com último pedido há mais de 90 dias é atendido a cada 28 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Não agendar baixados na Receita Federal
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: baixado na Receita Federal}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Prospects
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Ativos
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 60, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Risco de inatividade
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [60, 90], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 90, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 28 dias}
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

- A entrada não informa se os pedidos consideram o vendedor ou a empresa.

## Ambiguidades

- A regra de inativos pode funcionar como regra residual, sem critério próprio de tempo.
