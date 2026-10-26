---
id: regra_181
origem: simulacao/regra_181/entrada.md
gobr: simulacao/regra_181/regra_181.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 6
procedencia: corpus_sintetico
---

## Regras

cliente filial da carteira fixa não é agendado
cliente ativo e adimplente é atendido semanalmente, com a preferência de dia do vendedor
cliente ativo e inadimplente é atendido a cada 14 dias
cliente inativo e adimplente é atendido a cada 14 dias
cliente inativo e inadimplente é atendido a cada 30 dias, com a preferência de dia do vendedor
cliente sem vendas é atendido a cada 14 dias

## Estrutura

```yaml
publico: todos os vendedores da empresa
comuns:
  - {tipo: carteira, op: igual_a, valor: carteira fixa, alcance: vendedor}
regras:
  - nome: Não agendar filiais
    se:
      - {tipo: segmento, op: igual_a, valor: filial}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Ativos adimplentes semanal
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
      - {tipo: periodo_vigencia, op: igual_a, valor: preferência do vendedor, unidade: periodo_nomeado, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Ativos inadimplentes
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Inativos adimplentes
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Inativos inadimplentes
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
      - {tipo: periodo_vigencia, op: igual_a, valor: preferência do vendedor, unidade: periodo_nomeado, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Sem vendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 14 dias}
termos_fora_vocabulario:
  - filial
  - preferência de dia do vendedor
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Cescom | empresa_foco | EMPRESA_FOCO |
| carteira fixa | jargao | clientes vinculados a um vendedor |
| filial | jargao | unidade filial de um cliente |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| sem vendas | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não define o prazo que separa ativo de inativo.

## Ambiguidades

- A preferência de dia do vendedor é citada para os ativos adimplentes e para os inativos inadimplentes; não fica claro se vale também para as faixas intermediárias.
- "Semanal" foi registrado como 7 dias pela convenção de periodicidade.
