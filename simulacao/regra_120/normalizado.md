---
id: regra_120
origem: simulacao/regra_120/entrada.md
gobr: simulacao/regra_120/regra_120.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 14
procedencia: corpus_sintetico
---

## Regras

os clientes de carteira própria de VENDEDOR_01 não são agendados
cliente ativo do televendas é atendido a cada 14 dias, em dia útil
cliente inativo do televendas é atendido a cada 30 dias, em dia útil
cliente sem venda do televendas é atendido a cada 7 dias, em dia útil
cliente ativo e adimplente da capital é atendido a cada 20 dias, em dia útil
cliente ativo e inadimplente da capital é atendido a cada 20 dias, em dia útil
cliente inativo e adimplente da capital é atendido a cada 30 dias, em dia útil
cliente sem venda da capital é atendido a cada 30 dias, em dia útil
cliente inativo e inadimplente da capital não é agendado
cliente ativo do interior é atendido a cada 21 dias, em dia útil
cliente inativo e adimplente do interior é atendido a cada 21 dias, em dia útil
cliente inativo e inadimplente do interior é atendido a cada 42 dias, em dia útil
cliente sem venda do interior é atendido a cada 38 dias, em dia útil
por último, no interior, cliente inativo e inadimplente não é agendado

## Estrutura

```yaml
publico: VENDEDOR_01, time de televendas, time do interior e time da capital
comuns: []
regras:
  - nome: Não agendar carteira própria de VENDEDOR_01
    publico: VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: carteira própria, alcance: vendedor}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Ativos do televendas
    publico: televendas, exceto VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: carteira do televendas, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Inativos do televendas
    publico: televendas, exceto VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: carteira do televendas, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Sem venda do televendas
    publico: televendas, exceto VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: carteira do televendas, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Ativos adimplentes da capital
    publico: time da capital, VENDEDOR_04, VENDEDOR_05 e VENDEDOR_06
    se:
      - {tipo: carteira, op: igual_a, valor: carteira da capital, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 20 dias}
  - nome: Ativos inadimplentes da capital
    publico: time da capital, VENDEDOR_04, VENDEDOR_05 e VENDEDOR_06
    se:
      - {tipo: carteira, op: igual_a, valor: carteira da capital, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 20 dias}
  - nome: Inativos adimplentes da capital
    publico: time da capital, VENDEDOR_04, VENDEDOR_05 e VENDEDOR_06
    se:
      - {tipo: carteira, op: igual_a, valor: carteira da capital, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Sem venda da capital
    publico: time da capital, VENDEDOR_04, VENDEDOR_05 e VENDEDOR_06
    se:
      - {tipo: carteira, op: igual_a, valor: carteira da capital, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Não agendar inativos inadimplentes da capital
    publico: time da capital, VENDEDOR_04, VENDEDOR_05 e VENDEDOR_06
    se:
      - {tipo: carteira, op: igual_a, valor: carteira da capital, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Ativos do interior
    publico: time do interior, VENDEDOR_02, VENDEDOR_03 e VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: carteira do interior, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Inativos adimplentes do interior
    publico: time do interior, VENDEDOR_02, VENDEDOR_03 e VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: carteira do interior, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Inativos inadimplentes do interior
    publico: time do interior, VENDEDOR_02, VENDEDOR_03 e VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: carteira do interior, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 42 dias}
  - nome: Sem venda do interior
    publico: time do interior, VENDEDOR_02, VENDEDOR_03 e VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: carteira do interior, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 38 dias}
  - nome: Não agendar inativos inadimplentes do interior
    publico: time do interior, VENDEDOR_02, VENDEDOR_03 e VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: carteira do interior, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
termos_fora_vocabulario:
  - preferência por dia útil
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| IdealPet | empresa_foco | EMPRESA_FOCO |
| Yasmim, ID 12 | vendedor | VENDEDOR_01 |
| vendedor 2 | vendedor | VENDEDOR_02 |
| vendedor 3 | vendedor | VENDEDOR_03 |
| vendedor 5 | vendedor | VENDEDOR_04 |
| vendedor 17 | vendedor | VENDEDOR_05 |
| vendedor 18 | vendedor | VENDEDOR_06 |
| televendas | jargao | atendimento por telefone |
| carteira própria | jargao | clientes vinculados ao próprio vendedor |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| sem venda | jargao | cliente que nunca comprou |

## Lacunas

- nenhuma

## Ambiguidades

- VENDEDOR_01 aparece no time exclusivo (com carteira própria não agendada) e também no time do interior.
- No interior, a regra de 42 dias para inativos inadimplentes vem antes da regra que manda não agendá-los; a ordem de avaliação define qual prevalece.
- "Dia útil" é preferência de agendamento, não condição; registrada como critério de período por falta de campo próprio.
