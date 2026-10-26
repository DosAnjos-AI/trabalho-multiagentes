---
id: regra_241
origem: simulacao/regra_241/entrada.md
gobr: simulacao/regra_241/regra_241.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 8
procedencia: corpus_sintetico
---

## Regras

cliente com cadastro baixado na Receita Federal não é agendado
clientes de revenda dos ramos 106, 139, 109, 143, 141 e 142 são atendidos a cada 7 dias
clientes de revenda dos ramos 140, 146 e 148 são atendidos a cada 14 dias
clientes de revenda do ramo 138 são atendidos a cada 28 dias
clientes de consumo dos ramos 144, 147 e 108 são atendidos a cada 7 dias
clientes de consumo dos ramos 111, 100, 110, 112, 145, 107 e 113 são atendidos a cada 14 dias
clientes de consumo do ramo 114 são atendidos a cada 28 dias
clientes fora dos ramos mapeados não são agendados

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Não agendar baixados na Receita Federal
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: baixado na Receita Federal}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Revenda, 7 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['106', '139', '109', '143', '141', '142']}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Revenda, 14 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['140', '146', '148']}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Revenda, 28 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['138']}
    entao: {acao: agendar, frequencia: fixa 28 dias}
  - nome: Consumo, 7 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['144', '147', '108']}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Consumo, 14 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['111', '100', '110', '112', '145', '107', '113']}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Consumo, 28 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['114']}
    entao: {acao: agendar, frequencia: fixa 28 dias}
  - nome: Não agendar fora dos ramos mapeados
    se: []
    entao: {acao: nao_agendar, frequencia: nao_informada}
termos_fora_vocabulario:
  - baixado na Receita Federal
  - código de ramo de atividade
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| baixado na Receita | jargao | cadastro encerrado no órgão fiscal |
| ramo de atividade | jargao | código de segmento do cliente |
| revenda | jargao | cliente que revende os produtos |
| consumo | jargao | cliente que consome os produtos |

## Lacunas

- A entrada não informa o significado de cada código de ramo de atividade.

## Ambiguidades

- Os códigos de ramo foram mantidos como valores de segmento, por não identificarem pessoas nem empresas.
