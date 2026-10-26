---
id: regra_175
origem: simulacao/regra_175/entrada.md
gobr: simulacao/regra_175/regra_175.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 8
procedencia: corpus_sintetico
---

## Regras

filial da carteira dos ramos selecionados não é agendada
inadimplente da carteira dos ramos selecionados não é agendado
cliente da carteira com compra nos últimos 30 dias não é agendado
cliente da carteira ativo na empresa é atendido a cada 14 dias
cliente da carteira inativo na empresa é atendido a cada 21 dias
cliente da carteira que comprou no ano anterior e está sem venda neste ano é atendido a cada 21 dias
cliente da carteira que comprou em 2023 e não comprou mais é atendido a cada 30 dias
quem estiver fora das regras, em todo o televendas, não é agendado

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Não agendar filiais
    se:
      - {tipo: segmento, op: igual_a, valor: ['1', '2', '3', '4', '8', '18', '23']}
      - {tipo: segmento, op: igual_a, valor: filial}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar inadimplentes
    se:
      - {tipo: segmento, op: igual_a, valor: ['1', '2', '3', '4', '8', '18', '23']}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar quem comprou nos últimos 30 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['1', '2', '3', '4', '8', '18', '23']}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Ativos na empresa
    se:
      - {tipo: segmento, op: igual_a, valor: ['1', '2', '3', '4', '8', '18', '23']}
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Inativos na empresa
    se:
      - {tipo: segmento, op: igual_a, valor: ['1', '2', '3', '4', '8', '18', '23']}
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Compraram no ano anterior e não neste ano
    se:
      - {tipo: segmento, op: igual_a, valor: ['1', '2', '3', '4', '8', '18', '23']}
      - {tipo: estagio_relacionamento, op: igual_a, valor: parou de comprar, alcance: empresa}
      - {tipo: periodo_vigencia, op: igual_a, valor: ano anterior sem compra no ano atual, unidade: periodo_nomeado, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Compraram em 2023 e não compraram mais
    se:
      - {tipo: segmento, op: igual_a, valor: ['1', '2', '3', '4', '8', '18', '23']}
      - {tipo: tempo_sem_comprar, op: igual_a, valor: ano de 2023, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Não agendar fora das regras
    se: []
    entao: {acao: nao_agendar, frequencia: nao_informada}
termos_fora_vocabulario:
  - filial
  - compra por ano civil
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| carteira livre | jargao | conjunto de clientes compartilhado |
| ramo de atividade | jargao | segmento do cliente |
| filial | jargao | unidade filial de um cliente |
| inadimplente | jargao | cliente com pendência financeira em aberto |

## Lacunas

- A entrada não informa o significado dos códigos de ramo de atividade.

## Ambiguidades

- "Ano anterior" e "este ano" dependem da data de execução da regra.
