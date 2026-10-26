---
id: regra_232
origem: simulacao/regra_232/entrada.md
gobr: simulacao/regra_232/regra_232.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 7
procedencia: corpus_sintetico
---

## Regras

cliente filial não é agendado
cliente inadimplente não é agendado
prospect é atendido a cada 21 dias
cliente com compra entre 1 e 29 dias usa o histórico, entre 14 e 30 dias
cliente com compra entre 30 e 59 dias é atendido a cada 21 dias
cliente com compra entre 60 e 89 dias é atendido a cada 21 dias
cliente sem compra em 90 dias é atendido a cada 21 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Não agendar filiais
    se:
      - {tipo: segmento, op: igual_a, valor: filial}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar inadimplentes
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Prospects
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Compra entre 1 e 29 dias
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [1, 29], unidade: dias}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Compra entre 30 e 59 dias
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [30, 59], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Compra entre 60 e 89 dias
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [60, 89], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Sem compra em 90 dias
    se: []
    entao: {acao: agendar, frequencia: fixa 21 dias}
termos_fora_vocabulario:
  - filial
  - frequência pelo histórico com mínimo e máximo
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| filial | jargao | unidade filial de um cliente |
| prospect | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não informa se as compras consideram o vendedor ou a empresa.

## Ambiguidades

- Os limites de 14 e 30 dias da frequência pelo histórico não têm campo próprio e foram registrados apenas na descrição.
