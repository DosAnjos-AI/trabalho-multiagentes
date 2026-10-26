---
id: regra_162
origem: simulacao/regra_162/entrada.md
gobr: simulacao/regra_162/regra_162.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 6
procedencia: corpus_sintetico
---

## Regras

cliente pessoa física não é agendado
cliente inadimplente não é agendado
cliente sem histórico de compra, prospect, é atendido a cada 14 dias
cliente inativo é atendido a cada 14 dias
cliente com mais de 45 dias sem compra é atendido a cada 30 dias
os demais usam a frequência do histórico, entre 14 e 45 dias

## Estrutura

```yaml
publico: todos os vendedores ativos
comuns: []
regras:
  - nome: Não agendar pessoa física
    se:
      - {tipo: segmento, op: igual_a, valor: pessoa física}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar inadimplentes
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Sem histórico de compra
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Inativos
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Mais de 45 dias sem compra
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 45, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Demais clientes pelo histórico
    se: []
    entao: {acao: agendar, frequencia: calculada}
termos_fora_vocabulario:
  - pessoa física
  - frequência pelo histórico com mínimo e máximo
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| prospect | jargao | cliente que nunca comprou |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| frequência do histórico | jargao | frequência calculada pelo histórico de compras |

## Lacunas

- A entrada não diz sobre qual carteira os vendedores trabalham.

## Ambiguidades

- Os limites de 14 e 45 dias da frequência pelo histórico não têm campo próprio e foram registrados apenas na descrição.
