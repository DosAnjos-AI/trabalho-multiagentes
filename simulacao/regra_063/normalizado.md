---
id: regra_063
origem: simulacao/regra_063/entrada.md
gobr: simulacao/regra_063/regra_063.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 6
procedencia: corpus_sintetico
---

## Regras

cliente ativo da carteira do campo é atendido a cada 30 dias, preferindo dias úteis
cliente inativo da carteira do campo é atendido a cada 30 dias, preferindo dias úteis
cliente sem venda da carteira do campo é atendido a cada 30 dias, preferindo dias úteis
cliente ativo da carteira do televendas é atendido a cada 30 dias, preferindo dias úteis e sem coincidir com visita do campo
cliente inativo da carteira do televendas é atendido a cada 30 dias, preferindo dias úteis e sem coincidir com visita do campo
cliente sem venda da carteira do televendas é atendido a cada 30 dias, preferindo dias úteis e sem coincidir com visita do campo

## Estrutura

```yaml
publico: time de campo e time de televendas
comuns:
  - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
regras:
  - nome: Ativos do campo
    publico: time de campo
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa do campo, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Inativos do campo
    publico: time de campo
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa do campo, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Sem venda do campo
    publico: time de campo
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa do campo, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Ativos do televendas
    publico: time de televendas
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa do televendas, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: agenda_rota, op: igual_a, valor: sem conflito com visita do campo, alcance: grupo}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Inativos do televendas
    publico: time de televendas
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa do televendas, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: agenda_rota, op: igual_a, valor: sem conflito com visita do campo, alcance: grupo}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Sem venda do televendas
    publico: time de televendas
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa do televendas, alcance: grupo}
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
      - {tipo: agenda_rota, op: igual_a, valor: sem conflito com visita do campo, alcance: grupo}
    entao: {acao: agendar, frequencia: fixa 30 dias}
termos_fora_vocabulario:
  - preferência por dias úteis
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Verteiler | empresa_foco | EMPRESA_FOCO |
| televendas | jargao | atendimento por telefone |
| campo | jargao | atendimento presencial |
| carteira fixa | jargao | clientes vinculados a um vendedor ou time |
| sem venda | jargao | cliente que nunca comprou |

## Lacunas

- nenhuma

## Ambiguidades

- A entrada agrupa ativo, inativo e sem venda numa única frase para os dois times; o conjunto foi desdobrado em seis regras, três por time.
- "Preferindo dias úteis" é preferência de agendamento, não condição; registrada como critério de período por falta de campo próprio.
