---
id: regra_061
origem: simulacao/regra_061/entrada.md
gobr: simulacao/regra_061/regra_061.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 8
procedencia: corpus_sintetico
---

## Regras

cliente inativo da carteira de VENDEDOR_01 é atendido a cada 14 dias
cliente sem venda da carteira de VENDEDOR_01 é atendido a cada 14 dias
cliente ativo da carteira de VENDEDOR_01 é atendido a cada 14 dias
cliente inativo e inadimplente do campo não é agendado
todos os demais clientes do campo são atendidos a cada 14 dias
cliente inativo e inadimplente do televendas não é agendado
cliente sem venda do televendas não é agendado
os demais clientes do televendas são atendidos a cada 14 dias

## Estrutura

```yaml
publico: VENDEDOR_01, time de campo e time de televendas
comuns: []
regras:
  - nome: Inativos de VENDEDOR_01
    publico: VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: carteira de VENDEDOR_01, alcance: vendedor}
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Sem venda de VENDEDOR_01
    publico: VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: carteira de VENDEDOR_01, alcance: vendedor}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Ativos de VENDEDOR_01
    publico: VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: carteira de VENDEDOR_01, alcance: vendedor}
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Não agendar inativos inadimplentes do campo
    publico: time de campo
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Demais clientes do campo
    publico: time de campo
    se: []
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Não agendar inativos inadimplentes do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar sem venda do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Demais clientes do televendas
    publico: time de televendas
    se: []
    entao: {acao: agendar, frequencia: fixa 14 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Gesiane, ID 16 | vendedor | VENDEDOR_01 |
| televendas | jargao | atendimento por telefone |
| campo | jargao | atendimento presencial |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| sem venda | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não diz se campo e televendas trabalham sobre carteira fixa nem se VENDEDOR_01 também integra um desses times.

## Ambiguidades

- A carteira de VENDEDOR_01 é descrita numa única frase ("inativo, sem venda ou ativo"); foi desdobrada em três regras, uma por situação.
