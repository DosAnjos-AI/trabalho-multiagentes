---
id: regra_022
origem: simulacao/regra_022/entrada.md
gobr: simulacao/regra_022/regra_022.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 3
procedencia: corpus_sintetico
---

## Regras

todos os clientes do time de televendas são atendidos a cada 14 dias, preferindo dias úteis
cliente sem venda da carteira do campo não é agendado
todos os demais clientes da carteira do campo, ativos ou inativos, são visitados a cada 14 dias, preferindo dias úteis

## Estrutura

```yaml
publico: time de campo e time de televendas
comuns: []
regras:
  - nome: Todos os clientes do televendas a cada 14 dias
    publico: time de televendas
    se:
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Não agendar sem venda do campo
    publico: time de campo
    se:
      - {tipo: carteira, op: igual_a, valor: carteira do time de campo, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Demais clientes do campo a cada 14 dias
    publico: time de campo
    se:
      - {tipo: carteira, op: igual_a, valor: carteira do time de campo, alcance: grupo}
      - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 14 dias}
termos_fora_vocabulario:
  - preferência por dias úteis
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Supergiro | empresa_foco | EMPRESA_FOCO |
| televendas | jargao | atendimento por telefone |
| campo | jargao | atendimento presencial |
| sem venda | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não diz se o televendas trabalha sobre uma carteira fixa ou sobre todos os clientes da empresa.

## Ambiguidades

- "Preferência pelos dias úteis" é preferência de agendamento, não condição; registrada como critério de período por falta de campo próprio.
