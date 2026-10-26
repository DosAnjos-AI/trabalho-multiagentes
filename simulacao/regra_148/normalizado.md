---
id: regra_148
origem: simulacao/regra_148/entrada.md
gobr: simulacao/regra_148/regra_148.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 4
procedencia: corpus_sintetico
---

## Regras

cliente inadimplente não é agendado
cliente ativo é atendido semanalmente
cliente inativo é atendido quinzenalmente
cliente sem vendas é atendido quinzenalmente, a cada 14 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Não agendar inadimplentes
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Ativos semanal
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos quinzenal
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Sem vendas quinzenal
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 14 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Jumori | empresa_foco | EMPRESA_FOCO |
| televendas | jargao | atendimento por telefone |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| sem vendas | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não define o prazo que separa ativo de inativo.

## Ambiguidades

- "Semanal" e o "quinzenal" dos inativos foram registrados como 7 e 15 dias pela convenção de periodicidade; para os sem vendas, a entrada explicita 14 dias para "quinzenal", o que indica que o quinzenal dos inativos também pode ser 14.
