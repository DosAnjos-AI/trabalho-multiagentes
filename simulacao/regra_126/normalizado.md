---
id: regra_126
origem: simulacao/regra_126/entrada.md
gobr: simulacao/regra_126/regra_126.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 9
procedencia: corpus_sintetico
---

## Regras

cliente sem compra com a empresa há mais de 31 dias é atendido a cada 14 dias, em dia útil
os demais clientes, que compraram há menos de 31 dias, não são agendados
cliente ativo e adimplente do televendas é atendido a cada 14 dias, em dia útil
cliente ativo e inadimplente do televendas é atendido a cada 21 dias, em dia útil
cliente inativo e adimplente do televendas é atendido a cada 30 dias, em dia útil
cliente inativo e inadimplente do televendas não é agendado
cliente sem venda do televendas é atendido a cada 30 dias, em dia útil
cliente ativo do campo é atendido a cada 7 dias, com frequência fixa
cliente inativo do campo é atendido a cada 15 dias, com frequência fixa

## Estrutura

```yaml
publico: time de ruptura global, time de televendas ativo e time de campo ativo
comuns: []
regras:
  - nome: Ruptura global, sem compra há mais de 31 dias
    publico: time de ruptura global, VENDEDOR_01 a VENDEDOR_04
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 31, unidade: dias, alcance: empresa}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Ruptura global, demais clientes
    publico: time de ruptura global, VENDEDOR_01 a VENDEDOR_04
    se: []
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Ativos adimplentes do televendas
    publico: televendas ativo, exceto VENDEDOR_01 a VENDEDOR_04
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Ativos inadimplentes do televendas
    publico: televendas ativo, exceto VENDEDOR_01 a VENDEDOR_04
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Inativos adimplentes do televendas
    publico: televendas ativo, exceto VENDEDOR_01 a VENDEDOR_04
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Não agendar inativos inadimplentes do televendas
    publico: televendas ativo, exceto VENDEDOR_01 a VENDEDOR_04
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Sem venda do televendas
    publico: televendas ativo, exceto VENDEDOR_01 a VENDEDOR_04
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Ativos do campo
    publico: time de campo ativo
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos do campo
    publico: time de campo ativo
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
    entao: {acao: agendar, frequencia: fixa 15 dias}
termos_fora_vocabulario:
  - preferência por dia útil
  - frequência fixa rígida
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Femac | empresa_foco | EMPRESA_FOCO |
| vendedor 73 | vendedor | VENDEDOR_01 |
| vendedor 196 | vendedor | VENDEDOR_02 |
| vendedor 254 | vendedor | VENDEDOR_03 |
| vendedor 313 | vendedor | VENDEDOR_04 |
| ruptura global | jargao | clientes sem compra recente com a empresa |
| televendas | jargao | atendimento por telefone |
| campo | jargao | atendimento presencial |
| inadimplente | jargao | cliente com pendência financeira em aberto |

## Lacunas

- A entrada não diz se os times trabalham sobre carteira fixa.

## Ambiguidades

- "Dia útil" é preferência de agendamento, não condição; registrada como critério de período por falta de campo próprio.
