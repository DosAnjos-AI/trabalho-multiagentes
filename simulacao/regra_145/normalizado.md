---
id: regra_145
origem: simulacao/regra_145/entrada.md
gobr: simulacao/regra_145/regra_145.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 8
procedencia: corpus_sintetico
---

## Regras

cliente filial não é agendado
prospect pessoa jurídica sem pedido com o vendedor é atendido a cada 10 dias
pessoa jurídica do ramo 2, indústria, sem venda com o vendedor, é atendida a cada 14 dias
pessoa jurídica do ramo 1, revenda, sem venda com o vendedor, é atendida a cada 7 dias
pessoa jurídica adimplente com última compra com o vendedor entre 31 e 60 dias é atendida a cada 14 dias
pessoa jurídica adimplente com atividade do vendedor nos últimos 30 dias é atendida a cada 21 dias
pessoa jurídica adimplente com última compra entre 61 e 90 dias é atendida a cada 7 dias
pessoa jurídica restante, sem compra, é atendida a cada 21 dias

## Estrutura

```yaml
publico: todos os vendedores ativos
comuns: []
regras:
  - nome: Não agendar filiais
    se:
      - {tipo: segmento, op: igual_a, valor: filial}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Ativação de prospects
    se:
      - {tipo: segmento, op: igual_a, valor: pessoa jurídica}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 10 dias}
  - nome: Primeira compra, indústria
    se:
      - {tipo: segmento, op: igual_a, valor: pessoa jurídica}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: vendedor}
      - {tipo: segmento, op: igual_a, valor: ['2']}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Primeira compra, revenda
    se:
      - {tipo: segmento, op: igual_a, valor: pessoa jurídica}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: vendedor}
      - {tipo: segmento, op: igual_a, valor: ['1']}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Estimular regularidade
    se:
      - {tipo: segmento, op: igual_a, valor: pessoa jurídica}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
      - {tipo: tempo_sem_comprar, op: entre, valor: [31, 60], unidade: dias, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Compra regularmente
    se:
      - {tipo: segmento, op: igual_a, valor: pessoa jurídica}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Risco de inatividade
    se:
      - {tipo: segmento, op: igual_a, valor: pessoa jurídica}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
      - {tipo: tempo_sem_comprar, op: entre, valor: [61, 90], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Resgate de clientes sem compra
    se:
      - {tipo: segmento, op: igual_a, valor: pessoa jurídica}
    entao: {acao: agendar, frequencia: fixa 21 dias}
termos_fora_vocabulario:
  - filial
  - pessoa jurídica
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| filial | jargao | unidade filial de um cliente |
| prospect | jargao | cliente que nunca comprou |
| pessoa jurídica | jargao | cliente empresa |
| ramo de atividade | jargao | segmento do cliente |

## Lacunas

- A entrada não diz sobre qual carteira os vendedores trabalham.
- Clientes pessoa física não têm regra declarada além da exclusão implícita das regras de agendamento.

## Ambiguidades

- A regra de resgate não tem critério de tempo sem compra; funciona como regra residual para pessoa jurídica.
