---
id: regra_244
origem: simulacao/regra_244/entrada.md
gobr: simulacao/regra_244/regra_244.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 8
procedencia: corpus_sintetico
---

## Regras

cliente filial não é agendado
cliente inadimplente não é agendado
prospect com o vendedor é atendido a cada 14 dias
cliente com uma única compra com o vendedor é atendido a cada 7 dias
cliente ativo para o vendedor com intervalo histórico menor que 8 dias usa o histórico, entre 5 e 7 dias
cliente com compra com o vendedor entre 8 e 30 dias é atendido a cada 14 dias
cliente com compra entre 31 e 60 dias é atendido a cada 7 dias
cliente sem compra há mais de 60 dias é atendido a cada 14 dias

## Estrutura

```yaml
publico: todos os vendedores ativos
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
  - nome: Prospects do vendedor
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Cliente ativado
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Compra regularmente
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo, alcance: vendedor}
      - {tipo: tempo_sem_comprar, op: menor_que, valor: 8, unidade: dias}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Estimular regularidade
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [8, 30], unidade: dias, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Em ruptura
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [31, 60], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 60, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
termos_fora_vocabulario:
  - filial
  - frequência histórica de compra
  - frequência pelo histórico com mínimo e máximo
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| filial | jargao | unidade filial de um cliente |
| prospect | jargao | cliente que nunca comprou |
| frequência histórica | jargao | intervalo médio entre compras |
| ruptura | jargao | cliente que parou de comprar |

## Lacunas

- A entrada não informa se as faixas de ruptura e inativo consideram compras com o vendedor ou com a empresa.

## Ambiguidades

- Os limites de 5 e 7 dias da frequência pelo histórico foram registrados apenas na descrição.
