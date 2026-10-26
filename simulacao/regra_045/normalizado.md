---
id: regra_045
origem: simulacao/regra_045/entrada.md
gobr: simulacao/regra_045/regra_045.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 4
procedencia: corpus_sintetico
---

## Regras

os clientes da carteira de VENDEDOR_01 são atendidos semanalmente, preferindo dias úteis
cliente inativo e inadimplente é atendido a cada 30 dias, preferindo dias úteis
os inativos restantes, os adimplentes, são atendidos a cada 7 dias, preferindo dias úteis
todos os outros clientes, ativos e sem venda, são atendidos a cada 14 dias, preferindo dias úteis

## Estrutura

```yaml
publico: todos os vendedores da empresa, com VENDEDOR_01 em time separado
comuns:
  - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
regras:
  - nome: Carteira de VENDEDOR_01 semanal
    publico: VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: carteira de VENDEDOR_01, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos inadimplentes a cada 30 dias
    publico: todos os vendedores exceto VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa, alcance: vendedor}
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Demais inativos a cada 7 dias
    publico: todos os vendedores exceto VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa, alcance: vendedor}
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Demais clientes a cada 14 dias
    publico: todos os vendedores exceto VENDEDOR_01
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 14 dias}
termos_fora_vocabulario:
  - preferência por dias úteis
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Milenium | empresa_foco | EMPRESA_FOCO |
| Sandra, ID 945 | vendedor | VENDEDOR_01 |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| sem venda | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não diz se o restante da empresa trabalha sobre carteira fixa; isso é assumido pela menção à carteira de VENDEDOR_01.

## Ambiguidades

- "Frequência semanal" foi registrada como 7 dias pela convenção de periodicidade; a entrada não dá o número.
- "Preferindo dias úteis" é preferência de agendamento, não condição; registrada como critério de período por falta de campo próprio.
