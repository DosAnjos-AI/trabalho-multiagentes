---
id: regra_059
origem: simulacao/regra_059/entrada.md
gobr: simulacao/regra_059/regra_059.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 11
procedencia: corpus_sintetico
---

## Regras

cliente com ramo de atividade fora da lista permitida não é agendado
prospect dos ramos 2, 7, 11, 12, 14 e 19 é atendido a cada 30 dias
cliente ativo dos ramos 3, 4, 6, 8, 15 e 18 é atendido a cada 30 dias
cliente ativo dos ramos 7 e 17 é atendido a cada 15 dias
cliente ativo dos ramos 10, 11, 14 e 19 é atendido a cada 7 dias
cliente ativo dos ramos 2 e 12 é atendido a cada 5 dias
demais clientes, inativos, dos ramos 3, 4, 6, 8, 15 e 18 são atendidos a cada 30 dias
demais clientes, inativos, do ramo 17 são atendidos a cada 20 dias
demais clientes, inativos, do ramo 10 são atendidos a cada 15 dias
demais clientes, inativos, dos ramos 11 e 19 são atendidos a cada 10 dias
o que sobrar, os ramos 2, 7, 12 e 14, é atendido a cada 5 dias

## Estrutura

```yaml
publico: time de televendas
comuns: []
regras:
  - nome: Não agendar ramos fora da lista
    se:
      - {tipo: segmento, op: fora_de, valor: ['2', '3', '4', '5', '6', '7', '8', '10', '11', '12', '14', '15', '17', '18', '19']}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Prospects dos ramos 2, 7, 11, 12, 14 e 19
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
      - {tipo: segmento, op: igual_a, valor: ['2', '7', '11', '12', '14', '19']}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Ativos dos ramos 3, 4, 6, 8, 15 e 18
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: segmento, op: igual_a, valor: ['3', '4', '6', '8', '15', '18']}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Ativos dos ramos 7 e 17
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: segmento, op: igual_a, valor: ['7', '17']}
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Ativos dos ramos 10, 11, 14 e 19
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: segmento, op: igual_a, valor: ['10', '11', '14', '19']}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Ativos dos ramos 2 e 12
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: segmento, op: igual_a, valor: ['2', '12']}
    entao: {acao: agendar, frequencia: fixa 5 dias}
  - nome: Inativos dos ramos 3, 4, 6, 8, 15 e 18
    se:
      - {tipo: segmento, op: igual_a, valor: ['3', '4', '6', '8', '15', '18']}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Inativos do ramo 17
    se:
      - {tipo: segmento, op: igual_a, valor: ['17']}
    entao: {acao: agendar, frequencia: fixa 20 dias}
  - nome: Inativos do ramo 10
    se:
      - {tipo: segmento, op: igual_a, valor: ['10']}
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Inativos dos ramos 11 e 19
    se:
      - {tipo: segmento, op: igual_a, valor: ['11', '19']}
    entao: {acao: agendar, frequencia: fixa 10 dias}
  - nome: Restante, ramos 2, 7, 12 e 14
    se: []
    entao: {acao: agendar, frequencia: fixa 5 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Hospidrogas | empresa_foco | EMPRESA_FOCO |
| televendas | jargao | atendimento por telefone |
| ramo de atividade | jargao | segmento do cliente |
| prospect | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não informa o significado de cada código de ramo de atividade.
- A entrada não diz se o televendas trabalha sobre carteira fixa.

## Ambiguidades

- As regras de inativos são descritas como "para os demais", sem critério explícito de inatividade; dependem da ordem de avaliação após as regras de ativos.
