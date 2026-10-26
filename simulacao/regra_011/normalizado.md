---
id: regra_011
origem: simulacao/regra_011/entrada.md
gobr: simulacao/regra_011/regra_011.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 7
procedencia: corpus_sintetico
---

## Regras

cliente ativo para o vendedor na carteira do televendas não é agendado
cliente inativo na carteira do televendas é atendido a cada 14 dias, preferindo dias úteis
cliente sem venda na carteira do televendas é atendido a cada 14 dias, preferindo dias úteis
cliente inativo e inadimplente na carteira do campo não é agendado
cliente ativo na carteira do campo é visitado a cada 14 dias, preferindo dias úteis
cliente inativo adimplente na carteira do campo é visitado a cada 14 dias, em dias úteis
cliente sem venda na carteira do campo é visitado a cada 14 dias, em dias úteis

## Estrutura

```yaml
publico: time de televendas e time de campo
comuns: []
regras:
  - nome: Não agendar ativos do televendas
    publico: time de televendas
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa do televendas, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo, alcance: vendedor}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Inativos do televendas a cada 14 dias
    publico: time de televendas
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa do televendas, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Sem venda do televendas a cada 14 dias
    publico: time de televendas
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa do televendas, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Não agendar inativos inadimplentes do campo
    publico: time de campo
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa do campo, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Ativos do campo a cada 14 dias
    publico: time de campo
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa do campo, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Inativos adimplentes do campo a cada 14 dias
    publico: time de campo
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa do campo, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Sem venda do campo a cada 14 dias
    publico: time de campo
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa do campo, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 14 dias}
termos_fora_vocabulario:
  - preferência por dias úteis
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| VetVida | empresa_foco | EMPRESA_FOCO |
| televendas | jargao | atendimento por telefone |
| campo | jargao | atendimento presencial |
| carteira fixa | jargao | clientes vinculados a um vendedor ou time |
| sem venda | jargao | cliente que nunca comprou |
| inadimplente | jargao | cliente com pendência financeira em aberto |

## Lacunas

- A entrada não define o prazo que separa cliente ativo de inativo.
- A entrada não diz o que acontece com o cliente ativo inadimplente do campo além da frequência de ativo.

## Ambiguidades

- "Preferindo os dias úteis" é preferência de agendamento, não condição de entrada na regra; foi registrada como critério de período por falta de campo próprio.
