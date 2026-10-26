---
id: regra_235
origem: simulacao/regra_235/entrada.md
gobr: simulacao/regra_235/regra_235.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 14
procedencia: corpus_sintetico
---

## Regras

cliente com cadastro baixado na Receita Federal não é agendado
cliente com rota nos próximos 7 dias não é agendado
cliente com compra nos últimos 7 dias não é agendado
cliente com compra nos últimos 30 dias não é agendado
cliente com rota há 14 dias e 5% de crédito é atendido a cada 1 dia, preferindo dia útil e sábado
cliente com compra entre 30 e 90 dias é atendido a cada 15 dias, preferindo dia útil e sábado
cliente sem compra em 90 dias é atendido a cada 10 dias, preferindo dia útil e sábado
cliente com rota há 7 dias ou mais e 5% de crédito é atendido a cada 14 dias, preferindo dia útil e sábado
cliente com compra entre 7 e 30 dias e 5% de crédito é atendido a cada 14 dias, preferindo dia útil e sábado
cliente com compra entre 31 e 60 dias e 5% de crédito é atendido a cada 14 dias, preferindo dia útil e sábado
cliente com compra entre 61 e 89 dias e 5% de crédito é atendido a cada 7 dias, preferindo dia útil e sábado
cliente com compra entre 90 e 179 dias e 5% de crédito é atendido a cada 14 dias, preferindo dia útil e sábado
cliente sem compra em 180 dias e com 5% de crédito é atendido a cada 21 dias, preferindo dia útil e sábado
quem não se enquadrou em nenhuma regra não é agendado

## Estrutura

```yaml
publico: times de SUPERVISOR_A, SUPERVISOR_B 1, SUPERVISOR_B 2 e temporário de 2 meses
comuns: []
regras:
  - nome: Não agendar baixados na Receita Federal
    publico: os quatro times
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: baixado na Receita Federal}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar rota nos próximos 7 dias
    publico: times SUPERVISOR_B 1 e SUPERVISOR_B 2
    se:
      - {tipo: agenda_rota, op: dentro_de, valor: 7, unidade: dias}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar compra nos últimos 7 dias
    publico: times SUPERVISOR_B 1 e SUPERVISOR_B 2
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 7, unidade: dias}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar compra nos últimos 30 dias
    publico: time de SUPERVISOR_A
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Cobertura de rota 14 dias depois
    publico: time temporário de 2 meses, VENDEDOR_04 a VENDEDOR_06
    se:
      - {tipo: agenda_rota, op: igual_a, valor: 14, unidade: dias}
      - {tipo: situacao_financeira, op: igual_a, valor: 5, unidade: percentual}
      - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 1 dias}
  - nome: Compra entre 30 e 90 dias
    publico: time de SUPERVISOR_A
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [30, 90], unidade: dias}
      - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Sem compra em 90 dias
    publico: time de SUPERVISOR_A
    se:
      - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 10 dias}
  - nome: Rota há 7 dias ou mais
    publico: times SUPERVISOR_B 1 e SUPERVISOR_B 2
    se:
      - {tipo: agenda_rota, op: maior_que, valor: 7, unidade: dias}
      - {tipo: situacao_financeira, op: igual_a, valor: 5, unidade: percentual}
      - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Compra entre 7 e 30 dias
    publico: times SUPERVISOR_B 1 e SUPERVISOR_B 2
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [7, 30], unidade: dias}
      - {tipo: situacao_financeira, op: igual_a, valor: 5, unidade: percentual}
      - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Compra entre 31 e 60 dias
    publico: times SUPERVISOR_B 1 e SUPERVISOR_B 2
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [31, 60], unidade: dias}
      - {tipo: situacao_financeira, op: igual_a, valor: 5, unidade: percentual}
      - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Compra entre 61 e 89 dias
    publico: times SUPERVISOR_B 1 e SUPERVISOR_B 2
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [61, 89], unidade: dias}
      - {tipo: situacao_financeira, op: igual_a, valor: 5, unidade: percentual}
      - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Compra entre 90 e 179 dias
    publico: times SUPERVISOR_B 1 e SUPERVISOR_B 2
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [90, 179], unidade: dias}
      - {tipo: situacao_financeira, op: igual_a, valor: 5, unidade: percentual}
      - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Sem compra em 180 dias
    publico: times SUPERVISOR_B 1 e SUPERVISOR_B 2
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: 5, unidade: percentual}
      - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Não agendar não enquadrados
    publico: os quatro times
    se: []
    entao: {acao: nao_agendar, frequencia: nao_informada}
termos_fora_vocabulario:
  - baixado na Receita Federal
  - percentual de crédito
  - rota realizada há dias
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Felipe | supervisor | SUPERVISOR_A |
| Paola | supervisor | SUPERVISOR_B |
| vendedor 503 | vendedor | VENDEDOR_01 |
| vendedor 518 | vendedor | VENDEDOR_02 |
| vendedor 519 | vendedor | VENDEDOR_03 |
| vendedor 521 | vendedor | VENDEDOR_04 |
| vendedor 623 | vendedor | VENDEDOR_05 |
| vendedor 624 | vendedor | VENDEDOR_06 |
| vendedor 626 | vendedor | VENDEDOR_07 |
| televendas | jargao | atendimento por telefone |
| baixado na Receita | jargao | cadastro encerrado no órgão fiscal |
| cobertura de rota | jargao | contato após a visita de rota |

## Lacunas

- A entrada não explica o que significa "5 por cento de crédito".
- A entrada não informa o papel das pessoas que dão nome aos times.
- A entrada não informa se as compras consideram o vendedor ou a empresa.

## Ambiguidades

- As pessoas que dão nome aos times foram classificadas como supervisores por suposição de papel.
- VENDEDOR_04 a VENDEDOR_06 pertencem ao mesmo tempo ao time SUPERVISOR_B 2 e ao time temporário.
- No time de SUPERVISOR_A, a preferência por dia útil e sábado aparece só após a regra de 90 dias; foi aplicada às duas regras do time.
- "Rota há 7 dias ou mais" foi registrado como maior_que 7, por falta de operador "maior ou igual".
- As regras "sem compra em 90 dias" e "sem compra em 180 dias" funcionam como residuais e não receberam critério de tempo.
