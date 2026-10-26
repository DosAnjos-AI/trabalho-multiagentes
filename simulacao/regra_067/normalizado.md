---
id: regra_067
origem: simulacao/regra_067/entrada.md
gobr: simulacao/regra_067/regra_067.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 13
procedencia: corpus_sintetico
---

## Regras

cliente ativo é atendido a cada 14 dias, preferindo dias úteis
cliente inativo é atendido a cada 30 dias, preferindo dias úteis
cliente sem venda é atendido a cada 7 dias, preferindo dias úteis
cliente ativo e adimplente da capital é atendido a cada 20 dias, preferindo dias úteis
cliente ativo e inadimplente da capital é atendido a cada 20 dias, preferindo dias úteis
cliente inativo e adimplente da capital é atendido a cada 30 dias, preferindo dias úteis
cliente inativo e inadimplente da capital não é agendado
cliente sem venda da capital é atendido a cada 30 dias, preferindo dias úteis
cliente ativo do interior é atendido a cada 21 dias, preferindo dias úteis
cliente inativo e adimplente do interior é atendido a cada 21 dias, preferindo dias úteis
cliente inativo e inadimplente do interior é atendido a cada 42 dias, preferindo dias úteis
cliente sem venda do interior é atendido a cada 14 dias, preferindo dias úteis
regra adicional que também manda não agendar inativos inadimplentes, aplicada sobre a carteira da capital

## Estrutura

```yaml
publico: time de televendas, time do interior e time da capital
comuns: []
regras:
  - nome: Ativos do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Inativos do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Sem venda do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Ativos adimplentes da capital
    publico: time da capital, VENDEDOR_05, VENDEDOR_06, VENDEDOR_07 e VENDEDOR_08
    se:
      - {tipo: carteira, op: igual_a, valor: carteira da capital, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 20 dias}
  - nome: Ativos inadimplentes da capital
    publico: time da capital, VENDEDOR_05, VENDEDOR_06, VENDEDOR_07 e VENDEDOR_08
    se:
      - {tipo: carteira, op: igual_a, valor: carteira da capital, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 20 dias}
  - nome: Inativos adimplentes da capital
    publico: time da capital, VENDEDOR_05, VENDEDOR_06, VENDEDOR_07 e VENDEDOR_08
    se:
      - {tipo: carteira, op: igual_a, valor: carteira da capital, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Não agendar inativos inadimplentes da capital
    publico: time da capital, VENDEDOR_05, VENDEDOR_06, VENDEDOR_07 e VENDEDOR_08
    se:
      - {tipo: carteira, op: igual_a, valor: carteira da capital, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Sem venda da capital
    publico: time da capital, VENDEDOR_05, VENDEDOR_06, VENDEDOR_07 e VENDEDOR_08
    se:
      - {tipo: carteira, op: igual_a, valor: carteira da capital, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Ativos do interior
    publico: time do interior, VENDEDOR_01, VENDEDOR_02, VENDEDOR_03 e VENDEDOR_04
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Inativos adimplentes do interior
    publico: time do interior, VENDEDOR_01, VENDEDOR_02, VENDEDOR_03 e VENDEDOR_04
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Inativos inadimplentes do interior
    publico: time do interior, VENDEDOR_01, VENDEDOR_02, VENDEDOR_03 e VENDEDOR_04
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 42 dias}
  - nome: Sem venda do interior
    publico: time do interior, VENDEDOR_01, VENDEDOR_02, VENDEDOR_03 e VENDEDOR_04
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Regra adicional de não agendar inativos inadimplentes na carteira da capital
    publico: time da capital, VENDEDOR_05, VENDEDOR_06, VENDEDOR_07 e VENDEDOR_08
    se:
      - {tipo: carteira, op: igual_a, valor: carteira da capital, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
termos_fora_vocabulario:
  - preferência por dias úteis
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| NutriPet | empresa_foco | EMPRESA_FOCO |
| vendedor 11 | vendedor | VENDEDOR_01 |
| vendedor 3 | vendedor | VENDEDOR_02 |
| vendedor 12 | vendedor | VENDEDOR_03 |
| vendedor 21 | vendedor | VENDEDOR_04 |
| vendedor 2 | vendedor | VENDEDOR_05 |
| vendedor 4 | vendedor | VENDEDOR_06 |
| vendedor 5 | vendedor | VENDEDOR_07 |
| vendedor 6 | vendedor | VENDEDOR_08 |
| televendas | jargao | atendimento por telefone |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| sem venda | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não diz se televendas e interior trabalham sobre carteira fixa.

## Ambiguidades

- A regra adicional de não agendar inativos inadimplentes repete, sobre a carteira da capital, uma regra que a capital já tem; não fica claro se a intenção era aplicá-la ao interior, cuja regra para inativos inadimplentes é de 42 dias.
- "Preferência por dias úteis" é preferência de agendamento, não condição; registrada como critério de período por falta de campo próprio.
