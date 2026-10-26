---
id: regra_201
origem: simulacao/regra_201/entrada.md
gobr: simulacao/regra_201/regra_201.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 12
procedencia: corpus_sintetico
---

## Regras

cliente com cadastro baixado na Receita Federal não é agendado
cliente inadimplente não é agendado
cliente bloqueado não é agendado
cliente filial não é agendado
prospect com o vendedor é atendido a cada 7 dias
cliente sem compra há mais de 90 dias é atendido a cada 28 dias
cliente cadastrado há mais de 60 dias e com uma única compra com o vendedor é atendido a cada 30 dias
cliente com compra nos últimos 30 dias e intervalo histórico menor que 30 dias é atendido a cada 30 dias
cliente com compra nos últimos 30 dias e intervalo histórico menor que 90 dias é atendido a cada 30 dias
cliente com compra entre 30 e 60 dias é atendido a cada 10 dias
cliente com compra entre 61 e 90 dias é atendido a cada 14 dias
o restante, que não se enquadrou em nenhuma regra, não é agendado

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Não agendar baixados na Receita Federal
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: baixado na Receita Federal}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar inadimplentes
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar bloqueados
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: bloqueado}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar filiais
    se:
      - {tipo: segmento, op: igual_a, valor: filial}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Prospect do vendedor
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 90, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 28 dias}
  - nome: Cliente ativado
    se:
      - {tipo: situacao_cadastro, op: maior_que, valor: 60, unidade: dias}
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Alta frequência de compra
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
      - {tipo: tempo_sem_comprar, op: menor_que, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Compra regular
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
      - {tipo: tempo_sem_comprar, op: menor_que, valor: 90, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Estimular regularidade
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [30, 60], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 10 dias}
  - nome: Em ruptura
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [61, 90], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Não agendar os demais
    se: []
    entao: {acao: nao_agendar, frequencia: nao_informada}
termos_fora_vocabulario:
  - baixado na Receita Federal
  - bloqueado
  - filial
  - frequência histórica de compra
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| baixado na Receita | jargao | cadastro encerrado no órgão fiscal |
| bloqueado | jargao | cliente com cadastro bloqueado |
| filial | jargao | unidade filial de um cliente |
| frequência histórica | jargao | intervalo médio entre compras |
| ruptura | jargao | cliente que parou de comprar |

## Lacunas

- A entrada não informa se as compras consideram o vendedor ou a empresa.

## Ambiguidades

- A ordem das regras é declarada como intencional (inativos antes das demais), o que torna a precedência parte do significado do conjunto.
