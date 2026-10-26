---
id: regra_081
origem: simulacao/regra_081/entrada.md
gobr: simulacao/regra_081/regra_081.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 5
procedencia: corpus_sintetico
---

## Regras

cliente ativo é atendido semanalmente, preferindo dia útil
cliente ativo e inadimplente é atendido a cada 21 dias, preferindo dia útil
cliente inativo é atendido a cada 30 dias, preferindo dia útil
cliente inativo e inadimplente não é agendado
cliente sem vendas é atendido a cada 30 dias, preferindo dia útil

## Estrutura

```yaml
publico: todos os vendedores da empresa
comuns:
  - {tipo: carteira, op: igual_a, valor: carteira fixa, alcance: vendedor}
regras:
  - nome: Ativos semanal
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Ativos inadimplentes a cada 21 dias
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Inativos a cada 30 dias
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Não agendar inativos inadimplentes
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Sem vendas a cada 30 dias
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 30 dias}
termos_fora_vocabulario:
  - preferência por dia útil
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Recife Doces | empresa_foco | EMPRESA_FOCO |
| carteira fixa | jargao | clientes vinculados a um vendedor |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| sem vendas | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não define o prazo que separa ativo de inativo.

## Ambiguidades

- "Semanal" foi registrado como 7 dias pela convenção de periodicidade; a entrada não dá o número.
- A regra de ativos vem antes da de ativos inadimplentes e não exclui os inadimplentes; dependendo da ordem de avaliação, a regra de 21 dias pode nunca ser alcançada. O mesmo vale para inativos antes de inativos inadimplentes.
- "Preferindo dia útil" é preferência de agendamento, não condição; registrada como critério de período por falta de campo próprio.
