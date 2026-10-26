---
id: regra_217
origem: simulacao/regra_217/entrada.md
gobr: simulacao/regra_217/regra_217.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 2
procedencia: corpus_sintetico
---

## Regras

cliente com uma única compra com o vendedor é atendido a cada 7 dias
cliente com compra entre 7 e 30 dias usa o histórico, entre 14 e 28 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Fazer relacionamento
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Manter regularidade de compra
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [7, 30], unidade: dias}
    entao: {acao: agendar, frequencia: calculada}
termos_fora_vocabulario:
  - frequência pelo histórico com mínimo e máximo
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| histórico | jargao | frequência calculada pelo histórico de compras |

## Lacunas

- A entrada não traz regras para clientes fora dos dois casos descritos.

## Ambiguidades

- Os limites de 14 e 28 dias da frequência pelo histórico não têm campo próprio e foram registrados apenas na descrição.
