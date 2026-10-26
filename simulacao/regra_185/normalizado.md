---
id: regra_185
origem: simulacao/regra_185/entrada.md
gobr: simulacao/regra_185/regra_185.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 5
procedencia: corpus_sintetico
---

## Regras

cliente pessoa física não é agendado
cliente com cadastro baixado na Receita Federal não é agendado
prospect é atendido a cada 14 dias
cliente ativo com a empresa é atendido a cada 7 dias
inativos são atendidos a cada 14 dias

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
  - nome: Prospects
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Ativos com a empresa
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos
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

## Lacunas

- A entrada não diz se o televendas trabalha sobre carteira fixa.

## Ambiguidades

- A regra de inativos não tem critério próprio e funciona como regra residual.
