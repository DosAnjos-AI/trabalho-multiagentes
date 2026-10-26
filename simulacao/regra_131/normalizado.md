---
id: regra_131
origem: simulacao/regra_131/entrada.md
gobr: simulacao/regra_131/regra_131.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 13
procedencia: corpus_sintetico
---

## Regras

cliente inadimplente não é agendado
cliente com código de atividade econômica de administração pública ou segurança e ordem pública não é agendado
cliente sem crédito é atendido a cada 7 dias
cliente ativo do modelo 1 é atendido a cada 7 dias
cliente inativo do modelo 1 é atendido a cada 14 dias
cliente ativo do modelo 2 é atendido a cada 21 dias
cliente inativo do modelo 2 é atendido a cada 30 dias
todo o restante do televendas é atendido a cada 30 dias
cliente ativo do modelo 1 é atendido a cada 7 dias, preferindo segunda, quarta e sexta
cliente inativo do modelo 1 é atendido a cada 14 dias, preferindo segunda, quarta e sexta
cliente ativo do modelo 2 é atendido a cada 21 dias, preferindo segunda, quarta e sexta
cliente inativo do modelo 2 é atendido a cada 30 dias, preferindo segunda, quarta e sexta
todo o restante do campo é atendido a cada 30 dias, preferindo segunda, quarta e sexta

## Estrutura

```yaml
publico: vendedores ativos de televendas e de campo
comuns: []
regras:
  - nome: Não agendar inadimplentes
    publico: televendas e campo
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar administração pública e segurança
    publico: televendas e campo
    se:
      - {tipo: segmento, op: igual_a, valor: ['8411600', '8424800']}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Sem crédito a cada 7 dias
    publico: televendas e campo
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: sem crédito}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Modelo 1, ativos do televendas
    publico: televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: segmento, op: igual_a, valor: ['8630501', '8610101', '8630502', '7500100', '8610102', '8630503', '8640201', '8690901']}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Modelo 1, inativos do televendas
    publico: televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: segmento, op: igual_a, valor: ['8630501', '8610101', '8630502', '7500100', '8610102', '8630503', '8640201', '8690901']}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Modelo 2, ativos do televendas
    publico: televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: segmento, op: igual_a, valor: ['8533300', '8532500', '4645101', '3250705', '4773300']}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Modelo 2, inativos do televendas
    publico: televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: segmento, op: igual_a, valor: ['8533300', '8532500', '4645101', '3250705', '4773300']}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Modelo 3, restante do televendas
    publico: televendas
    se: []
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Modelo 1, ativos do campo
    publico: campo
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: segmento, op: igual_a, valor: ['8630501', '8610101', '8630502', '7500100', '8610102', '8630503', '8640201', '8690901']}
      - {tipo: periodo_vigencia, op: igual_a, valor: [segunda, quarta, sexta], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Modelo 1, inativos do campo
    publico: campo
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: segmento, op: igual_a, valor: ['8630501', '8610101', '8630502', '7500100', '8610102', '8630503', '8640201', '8690901']}
      - {tipo: periodo_vigencia, op: igual_a, valor: [segunda, quarta, sexta], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Modelo 2, ativos do campo
    publico: campo
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: segmento, op: igual_a, valor: ['8533300', '8532500', '4645101', '3250705', '4773300']}
      - {tipo: periodo_vigencia, op: igual_a, valor: [segunda, quarta, sexta], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Modelo 2, inativos do campo
    publico: campo
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: segmento, op: igual_a, valor: ['8533300', '8532500', '4645101', '3250705', '4773300']}
      - {tipo: periodo_vigencia, op: igual_a, valor: [segunda, quarta, sexta], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Modelo 3, restante do campo
    publico: campo
    se:
      - {tipo: periodo_vigencia, op: igual_a, valor: [segunda, quarta, sexta], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 30 dias}
termos_fora_vocabulario:
  - código de atividade econômica
  - preferência de dias da semana
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Labtech | empresa_foco | EMPRESA_FOCO |
| CNAE | jargao | código de atividade econômica |
| televendas | jargao | atendimento por telefone |
| campo | jargao | atendimento presencial |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| sem crédito | jargao | cliente sem limite de crédito disponível |

## Lacunas

- A entrada não diz se os times trabalham sobre carteira fixa.
- A entrada não define o prazo que separa ativo de inativo.

## Ambiguidades

- A preferência de segunda, quarta e sexta é preferência de agendamento, não condição; registrada como critério de período por falta de campo próprio.
