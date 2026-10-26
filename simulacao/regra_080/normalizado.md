---
id: regra_080
origem: simulacao/regra_080/entrada.md
gobr: simulacao/regra_080/regra_080.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 5
procedencia: corpus_sintetico
---

## Regras

cliente inativo com código de atividade econômica iniciado por 03, 47 ou 27 é atendido mensalmente, com a preferência de dia do vendedor
os demais clientes inativos são atendidos quinzenalmente, com a preferência de dia do vendedor
repetição da regra dos inativos quinzenais, com o mesmo conteúdo
cliente ativo é atendido mensalmente, com a preferência de dia do vendedor
cliente sem vendas é atendido mensalmente, com a preferência de dia do vendedor

## Estrutura

```yaml
publico: todos os vendedores da empresa
comuns:
  - {tipo: carteira, op: igual_a, valor: carteira fixa, alcance: vendedor}
  - {tipo: periodo_vigencia, op: igual_a, valor: preferência do vendedor, unidade: periodo_nomeado, alcance: vendedor}
regras:
  - nome: Inativos com atividade econômica 03, 47 ou 27
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: segmento, op: igual_a, valor: ['03', '47', '27']}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Demais inativos quinzenal
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Demais inativos quinzenal, repetição
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Ativos mensal
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Sem vendas mensal
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 30 dias}
termos_fora_vocabulario:
  - CNAE iniciado por código
  - preferência de dia do vendedor
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Makro Services | empresa_foco | EMPRESA_FOCO |
| ERP | sistema_externo | SISTEMA_EXTERNO |
| CNAE | jargao | código de atividade econômica |
| carteira fixa | jargao | clientes vinculados a um vendedor |
| sem vendas | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não define o prazo que separa ativo de inativo.

## Ambiguidades

- "Mensal" e "quinzenal" foram registrados como 30 e 15 dias pela convenção de periodicidade; a entrada não dá os números.
- O critério de atividade econômica é "começa com", não igualdade exata; registrado como igual_a com a lista de prefixos.
- A regra dos inativos quinzenais aparece repetida; a repetição foi mantida como regra própria para preservar a contagem.
