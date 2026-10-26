---
id: regra_023
origem: simulacao/regra_023/entrada.md
gobr: simulacao/regra_023/regra_023.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 8
procedencia: corpus_sintetico
---

## Regras

cliente sem venda da carteira do televendas de Goiânia é atendido a cada 7 dias
os demais clientes da carteira do televendas de Goiânia são atendidos a cada 14 dias
cliente adimplente da carteira do televendas do Distrito Federal é atendido a cada 7 dias
cliente ativo e inadimplente da carteira do televendas do Distrito Federal é atendido a cada 14 dias
cliente inativo e inadimplente da carteira do televendas do Distrito Federal não é agendado
cliente sem venda da carteira do televendas do Distrito Federal é atendido a cada 7 dias
cliente ativo é visitado a cada 7 dias, com frequência fixa que o gerador de agenda não altera
os demais clientes, os inativos, são visitados a cada 15 dias, com frequência fixa que o gerador de agenda não altera

## Estrutura

```yaml
publico: times de televendas de Goiânia e do Distrito Federal e time de campo do Distrito Federal
comuns: []
regras:
  - nome: Sem venda do televendas de Goiânia
    publico: vendedores de televendas do SUPERVISOR_A
    se:
      - {tipo: carteira, op: igual_a, valor: carteira do televendas de Goiânia, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Demais clientes do televendas de Goiânia
    publico: vendedores de televendas do SUPERVISOR_A
    se:
      - {tipo: carteira, op: igual_a, valor: carteira do televendas de Goiânia, alcance: grupo}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Adimplentes do televendas do Distrito Federal
    publico: todos os vendedores de televendas
    se:
      - {tipo: carteira, op: igual_a, valor: carteira do televendas do Distrito Federal, alcance: grupo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Ativos inadimplentes do televendas do Distrito Federal
    publico: todos os vendedores de televendas
    se:
      - {tipo: carteira, op: igual_a, valor: carteira do televendas do Distrito Federal, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Não agendar inativos inadimplentes do televendas do Distrito Federal
    publico: todos os vendedores de televendas
    se:
      - {tipo: carteira, op: igual_a, valor: carteira do televendas do Distrito Federal, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Sem venda do televendas do Distrito Federal
    publico: todos os vendedores de televendas
    se:
      - {tipo: carteira, op: igual_a, valor: carteira do televendas do Distrito Federal, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Ativos do campo do Distrito Federal
    publico: todos os vendedores de campo
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Demais clientes do campo do Distrito Federal
    publico: todos os vendedores de campo
    se: []
    entao: {acao: agendar, frequencia: fixa 15 dias}
termos_fora_vocabulario:
  - frequência fixa não alterável pelo gerador de agenda
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| BSB Vet | empresa_foco | EMPRESA_FOCO |
| supervisor 5178 | supervisor | SUPERVISOR_A |
| televendas | jargao | atendimento por telefone |
| campo | jargao | atendimento presencial |
| sem venda | jargao | cliente que nunca comprou |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| gerador de agenda | jargao | rotina que monta a agenda de atendimentos |

## Lacunas

- A entrada não informa como os clientes são separados entre Goiânia e Distrito Federal além da composição dos times.

## Ambiguidades

- O time de televendas do Distrito Federal reúne todos os vendedores de televendas, o que inclui os do SUPERVISOR_A, também presentes no time de Goiânia.
- A regra dos demais clientes do campo é descrita como "o resto, ou seja, inativos": pode valer para todo cliente não ativo ou apenas para os inativos.
