---
id: regra_090
origem: simulacao/regra_090/entrada.md
gobr: simulacao/regra_090/regra_090.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 3
procedencia: corpus_sintetico
---

## Regras

cliente ativo é atendido semanalmente, de segunda a sábado
cliente inativo é atendido a cada 14 dias, de segunda a sábado
cliente sem venda é atendido a cada 14 dias, de segunda a sábado

## Estrutura

```yaml
publico: todos os vendedores da empresa
comuns:
  - {tipo: carteira, op: igual_a, valor: carteira fixa, alcance: vendedor}
  - {tipo: periodo_vigencia, op: igual_a, valor: [segunda, terça, quarta, quinta, sexta, sábado], unidade: periodo_nomeado}
regras:
  - nome: Ativos semanal
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos a cada 14 dias
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Sem venda a cada 14 dias
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 14 dias}
termos_fora_vocabulario:
  - dias da semana permitidos
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Fribel | empresa_foco | EMPRESA_FOCO |
| carteira fixa | jargao | clientes vinculados a um vendedor |
| sem venda | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não define o prazo que separa ativo de inativo.

## Ambiguidades

- "Semanal" foi registrado como 7 dias pela convenção de periodicidade; a entrada não dá o número.
