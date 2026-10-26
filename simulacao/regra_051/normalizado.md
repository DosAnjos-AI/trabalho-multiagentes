---
id: regra_051
origem: simulacao/regra_051/entrada.md
gobr: simulacao/regra_051/regra_051.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 5
procedencia: corpus_sintetico
---

## Regras

cliente ativo e adimplente é atendido semanalmente, preferindo dias úteis e sábado
cliente ativo e inadimplente é atendido a cada 14 dias, preferindo dias úteis e sábado
cliente inativo e adimplente é atendido a cada 14 dias, preferindo dias úteis e sábado
cliente inativo e inadimplente não é agendado
cliente sem venda é atendido a cada 14 dias, preferindo dias úteis e sábado

## Estrutura

```yaml
publico: todos os vendedores ativos
comuns:
  - {tipo: carteira, op: igual_a, valor: carteira fixa, alcance: vendedor}
regras:
  - nome: Ativos adimplentes semanal
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
      - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Ativos inadimplentes a cada 14 dias
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
      - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Inativos adimplentes a cada 14 dias
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
      - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Não agendar inativos inadimplentes
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Sem venda a cada 14 dias
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
      - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 14 dias}
termos_fora_vocabulario:
  - preferência por dias úteis e sábado
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Armazém Santa Maria | empresa_foco | EMPRESA_FOCO |
| carteira fixa | jargao | clientes vinculados a um vendedor |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| sem venda | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não define o prazo que separa ativo de inativo.

## Ambiguidades

- "Semanal" foi registrado como 7 dias pela convenção de periodicidade; a entrada não dá o número.
- A preferência por dias úteis e sábado é preferência de agendamento, não condição; registrada como critério de período por falta de campo próprio.
