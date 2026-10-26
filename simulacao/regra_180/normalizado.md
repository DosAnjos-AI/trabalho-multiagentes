---
id: regra_180
origem: simulacao/regra_180/entrada.md
gobr: simulacao/regra_180/regra_180.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 6
procedencia: corpus_sintetico
---

## Regras

cliente filial não é agendado
cliente com cadastro suspenso na Receita Federal não é agendado
cliente com cadastro inapto na Receita Federal não é agendado
cliente com cadastro baixado na Receita Federal não é agendado
clientes dos ramos 84, 73, 69, 85 e 22 são atendidos a cada 7 dias
todos os demais clientes são atendidos a cada 30 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Não agendar filiais
    se:
      - {tipo: segmento, op: igual_a, valor: filial}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar suspensos na Receita Federal
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: suspenso na Receita Federal}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar inaptos na Receita Federal
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: inapto na Receita Federal}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar baixados na Receita Federal
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: baixado na Receita Federal}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Ramos 84, 73, 69, 85 e 22
    se:
      - {tipo: segmento, op: igual_a, valor: ['84', '73', '69', '85', '22']}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Demais clientes
    se: []
    entao: {acao: agendar, frequencia: fixa 30 dias}
termos_fora_vocabulario:
  - filial
  - situação na Receita Federal
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| filial | jargao | unidade filial de um cliente |
| suspenso, inapto ou baixado na Receita | jargao | cadastro irregular no órgão fiscal |
| ramo de atividade | jargao | segmento do cliente |

## Lacunas

- A entrada não informa o significado dos códigos de ramo de atividade.

## Ambiguidades

- A exclusão por situação na Receita Federal é descrita numa única frase; foi desdobrada em três regras, uma por situação.
