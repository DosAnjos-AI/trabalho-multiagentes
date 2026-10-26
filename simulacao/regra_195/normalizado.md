---
id: regra_195
origem: simulacao/regra_195/entrada.md
gobr: simulacao/regra_195/regra_195.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 9
procedencia: corpus_sintetico
---

## Regras

cliente pessoa física não é agendado
cliente com cadastro baixado na Receita Federal não é agendado, como paliativo
cliente com pedido nos últimos 7 dias não é agendado
cliente com compra entre 7 e 30 dias é atendido a cada 21 dias
prospect é atendido a cada 14 dias
cliente com uma única compra é atendido a cada 21 dias
cliente com compra com o vendedor entre 31 e 60 dias é atendido a cada 21 dias
cliente com compra entre 61 e 90 dias é atendido a cada 7 dias
os inativos são atendidos a cada 14 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Não agendar pessoa física
    se:
      - {tipo: segmento, op: igual_a, valor: pessoa física}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar baixados na Receita Federal
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: baixado na Receita Federal}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar pedido nos últimos 7 dias
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 7, unidade: dias}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Manter contato com quem comprou no mês
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [7, 30], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Ativação de novos
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Relacionamento com compra única
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Manter regularidade
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [31, 60], unidade: dias, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Evitar inatividade
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [61, 90], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Resgatar inativo
    se: []
    entao: {acao: agendar, frequencia: fixa 14 dias}
termos_fora_vocabulario:
  - pessoa física
  - baixado na Receita Federal
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| baixado na Receita | jargao | cadastro encerrado no órgão fiscal |
| prospect | jargao | cliente que nunca comprou |
| paliativo | jargao | medida provisória |

## Lacunas

- A entrada não explica por que a exclusão de baixados na Receita é paliativa.

## Ambiguidades

- A regra de resgate de inativos não tem critério próprio e funciona como regra residual.
