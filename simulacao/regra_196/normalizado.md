---
id: regra_196
origem: simulacao/regra_196/entrada.md
gobr: simulacao/regra_196/regra_196.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 5
procedencia: corpus_sintetico
---

## Regras

cliente inadimplente não é agendado
cliente de Fortaleza com compra nos últimos 60 dias não é agendado
prospect é atendido a cada 40 dias
cliente ativo e adimplente é atendido a cada 15 dias
cliente inativo e adimplente é atendido a cada 20 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Não agendar inadimplentes
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar Fortaleza com compra recente
    se:
      - {tipo: localizacao, op: igual_a, valor: [Fortaleza]}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 60, unidade: dias}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Prospects
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 40 dias}
  - nome: Ativos adimplentes
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Inativos adimplentes
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 20 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| prospect | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não define o prazo que separa ativo de inativo.

## Ambiguidades

- O critério de adimplência das duas últimas regras decorre da exclusão anterior dos inadimplentes.
