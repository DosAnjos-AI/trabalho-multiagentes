---
id: regra_055
origem: simulacao/regra_055/entrada.md
gobr: simulacao/regra_055/regra_055.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 8
procedencia: corpus_sintetico
---

## Regras

cliente adimplente do televendas é atendido a cada 14 dias
cliente ativo e inadimplente do televendas é atendido a cada 30 dias
cliente sem venda do televendas é atendido a cada 30 dias
cliente inativo e inadimplente do televendas não é agendado
cliente sem venda da capital é atendido a cada 30 dias
cliente inadimplente da capital é atendido a cada 30 dias
o restante dos clientes da capital, os adimplentes, é atendido a cada 14 dias
todos os clientes do interior são atendidos a cada 30 dias

## Estrutura

```yaml
publico: time de televendas, time de campo do interior e time de campo da capital
comuns: []
regras:
  - nome: Adimplentes do televendas
    publico: time de televendas
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Ativos inadimplentes do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Sem venda do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Não agendar inativos inadimplentes do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Sem venda da capital
    publico: time da capital, todos os vendedores de campo exceto VENDEDOR_01, VENDEDOR_02 e VENDEDOR_03
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Inadimplentes da capital
    publico: time da capital, todos os vendedores de campo exceto VENDEDOR_01, VENDEDOR_02 e VENDEDOR_03
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Restante da capital
    publico: time da capital, todos os vendedores de campo exceto VENDEDOR_01, VENDEDOR_02 e VENDEDOR_03
    se: []
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Todos os clientes do interior
    publico: time do interior, VENDEDOR_01, VENDEDOR_02 e VENDEDOR_03
    se: []
    entao: {acao: agendar, frequencia: fixa 30 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| NB Distribuidora | empresa_foco | EMPRESA_FOCO |
| vendedor de ID 27 | vendedor | VENDEDOR_01 |
| vendedor de ID 35 | vendedor | VENDEDOR_02 |
| vendedor de ID 34 | vendedor | VENDEDOR_03 |
| televendas | jargao | atendimento por telefone |
| vendedor de campo | jargao | vendedor que atende presencialmente |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| sem venda | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não informa se os times trabalham sobre carteira fixa.
- A entrada não diz o que acontece com o cliente inativo adimplente do televendas além da regra de adimplentes.

## Ambiguidades

- nenhuma
