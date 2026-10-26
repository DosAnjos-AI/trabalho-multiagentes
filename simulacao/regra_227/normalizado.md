---
id: regra_227
origem: simulacao/regra_227/entrada.md
gobr: simulacao/regra_227/regra_227.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 6
procedencia: corpus_sintetico
---

## Regras

cliente com rota há 7 dias é atendido a cada 1 dia, com frequência fixa
cliente com compra nos últimos 30 dias não é agendado
prospect é atendido a cada 60 dias
cliente com compra entre 30 e 90 dias é atendido a cada 15 dias
cliente sem compra há mais de 90 dias é atendido a cada 10 dias
quem não foi coberto por nenhuma regra não é agendado

## Estrutura

```yaml
publico: time de SUPERVISOR_A, televendas ativos exceto VENDEDOR_01 a VENDEDOR_07
comuns: []
regras:
  - nome: Cobertura de rota 7 dias depois
    publico: time de SUPERVISOR_A
    se:
      - {tipo: agenda_rota, op: igual_a, valor: 7, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 1 dias}
  - nome: Não agendar compra nos últimos 30 dias
    publico: time de SUPERVISOR_A
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Prospects
    publico: time de SUPERVISOR_A
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 60 dias}
  - nome: Compra entre 30 e 90 dias
    publico: time de SUPERVISOR_A
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [30, 90], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Sem compra há mais de 90 dias
    publico: time de SUPERVISOR_A
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 90, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 10 dias}
  - nome: Não agendar não cobertos
    publico: time de SUPERVISOR_A
    se: []
    entao: {acao: nao_agendar, frequencia: nao_informada}
termos_fora_vocabulario:
  - rota realizada há dias
  - frequência fixa rígida
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| SIM Lubrificantes | empresa_cliente | EMPRESA_CLIENTE |
| Felipe | supervisor | SUPERVISOR_A |
| vendedor 518 | vendedor | VENDEDOR_01 |
| vendedor 519 | vendedor | VENDEDOR_02 |
| vendedor 521 | vendedor | VENDEDOR_03 |
| vendedor 626 | vendedor | VENDEDOR_04 |
| vendedor 503 | vendedor | VENDEDOR_05 |
| vendedor 624 | vendedor | VENDEDOR_06 |
| vendedor 623 | vendedor | VENDEDOR_07 |
| televendas | jargao | atendimento por telefone |
| cobertura de rota | jargao | contato após a visita de rota |

## Lacunas

- A entrada não informa a empresa dona das regras; menciona apenas a conta de origem da cópia.
- A entrada não informa o papel da pessoa que dá nome ao time.

## Ambiguidades

- A empresa da qual a regra foi copiada foi classificada como empresa cliente, por não ser a dona das regras.
- A pessoa que dá nome ao time foi classificada como supervisor por suposição de papel; pode ser outro cargo.
