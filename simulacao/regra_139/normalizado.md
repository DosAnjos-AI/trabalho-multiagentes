---
id: regra_139
origem: simulacao/regra_139/entrada.md
gobr: simulacao/regra_139/regra_139.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 10
procedencia: corpus_sintetico
---

## Regras

cliente prospect não é agendado
cliente inadimplente não é agendado
cliente bloqueado não é agendado
cliente com intervalo histórico menor que 31 dias usa a frequência do histórico, com máximo de 30 dias
cliente com padrão de compra entre 31 e 90 dias é atendido a cada 21 dias
cliente com padrão de compra acima de 90 dias é atendido a cada 30 dias
cliente com última compra com o vendedor entre 45 e 90 dias é atendido a cada 30 dias
cliente com última compra com o vendedor entre 91 e 180 dias é atendido a cada 25 dias
cliente inativo para o vendedor é atendido a cada 21 dias
cliente com intervalo histórico menor que 45 dias usa a frequência do histórico, entre 40 e 45 dias

## Estrutura

```yaml
publico: time de ativação de novos clientes e time de venda na base
comuns: []
regras:
  - nome: Não agendar prospects na venda na base
    publico: time de venda na base, VENDEDOR_01 e VENDEDOR_02
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar inadimplentes
    publico: os dois times
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar bloqueados
    publico: os dois times
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: bloqueado}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Padrão de compra em até 30 dias
    publico: time de ativação, televendas ativos exceto VENDEDOR_01 e VENDEDOR_02
    se:
      - {tipo: tempo_sem_comprar, op: menor_que, valor: 31, unidade: dias}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Padrão de compra entre 31 e 90 dias
    publico: time de ativação, televendas ativos exceto VENDEDOR_01 e VENDEDOR_02
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [31, 90], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Padrão de compra acima de 90 dias
    publico: time de ativação, televendas ativos exceto VENDEDOR_01 e VENDEDOR_02
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 90, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Estimular regularidade na venda na base
    publico: time de venda na base, VENDEDOR_01 e VENDEDOR_02
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [45, 90], unidade: dias, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Risco de inatividade na venda na base
    publico: time de venda na base, VENDEDOR_01 e VENDEDOR_02
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [91, 180], unidade: dias, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 25 dias}
  - nome: Resgate de inativos na venda na base
    publico: time de venda na base, VENDEDOR_01 e VENDEDOR_02
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Alta frequência de compra na venda na base
    publico: time de venda na base, VENDEDOR_01 e VENDEDOR_02
    se:
      - {tipo: tempo_sem_comprar, op: menor_que, valor: 45, unidade: dias}
    entao: {acao: agendar, frequencia: calculada}
termos_fora_vocabulario:
  - bloqueado
  - frequência histórica de compra
  - frequência pelo histórico com mínimo e máximo
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| vendedor 10185 | vendedor | VENDEDOR_01 |
| vendedor 1824 | vendedor | VENDEDOR_02 |
| hunter | jargao | vendedor dedicado a ativar clientes novos |
| farm | jargao | vendedor dedicado à base de clientes existentes |
| televendas | jargao | atendimento por telefone |
| bloqueado | jargao | cliente com cadastro bloqueado |
| frequência histórica | jargao | intervalo médio entre compras |

## Lacunas

- A entrada não informa se o padrão de compra do time de ativação considera o vendedor ou a empresa.

## Ambiguidades

- Os limites da frequência pelo histórico (máximo de 30 dias; mínimo de 40 e máximo de 45 dias) não têm campo próprio e foram registrados apenas na descrição.
- No time de venda na base, a regra de alta frequência vem por último e pode ser alcançada só por quem não caiu nas regras anteriores.
