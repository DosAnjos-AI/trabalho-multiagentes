---
id: regra_136
origem: simulacao/regra_136/entrada.md
gobr: simulacao/regra_136/regra_136.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 5
procedencia: corpus_sintetico
---

## Regras

cliente do ramo 19, funcionários, não é agendado
cliente ativo da capital é atendido a cada 7 dias
cliente inativo da capital não é agendado
cliente ativo do interior é atendido a cada 14 dias
cliente inativo do interior não é agendado

## Estrutura

```yaml
publico: todos os vendedores ativos, com times de campo da capital e do interior
comuns: []
regras:
  - nome: Não agendar ramo 19
    publico: todos os vendedores ativos
    se:
      - {tipo: segmento, op: igual_a, valor: ['19']}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Ativos da capital
    publico: time da capital, vendedores de campo exceto VENDEDOR_01 a VENDEDOR_07
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Não agendar inativos da capital
    publico: time da capital, vendedores de campo exceto VENDEDOR_01 a VENDEDOR_07
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Ativos do interior
    publico: time do interior, VENDEDOR_01 a VENDEDOR_07
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Não agendar inativos do interior
    publico: time do interior, VENDEDOR_01 a VENDEDOR_07
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
    entao: {acao: nao_agendar, frequencia: nao_informada}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Multisul | empresa_foco | EMPRESA_FOCO |
| vendedor 5 | vendedor | VENDEDOR_01 |
| vendedor 9 | vendedor | VENDEDOR_02 |
| vendedor 15 | vendedor | VENDEDOR_03 |
| vendedor 16 | vendedor | VENDEDOR_04 |
| vendedor 21 | vendedor | VENDEDOR_05 |
| vendedor 31 | vendedor | VENDEDOR_06 |
| vendedor 33 | vendedor | VENDEDOR_07 |
| ramo de atividade | jargao | segmento do cliente |
| campo | jargao | atendimento presencial |

## Lacunas

- A entrada não define o prazo que separa ativo de inativo.
- A entrada não diz se capital e interior trabalham sobre carteira fixa.

## Ambiguidades

- nenhuma
