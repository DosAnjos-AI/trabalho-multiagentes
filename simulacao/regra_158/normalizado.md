---
id: regra_158
origem: simulacao/regra_158/entrada.md
gobr: simulacao/regra_158/regra_158.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 9
procedencia: corpus_sintetico
---

## Regras

cliente inadimplente não é agendado
cliente com cadastro baixado na Receita Federal não é agendado
prospect, cliente potencial, é atendido a cada 30 dias
cliente com uma única compra, compra nos últimos 45 dias e cadastrado há mais de 120 dias é atendido a cada 21 dias
cliente com compra nos últimos 45 dias e intervalo histórico menor que 30 dias é atendido a cada 14 dias
cliente com compra nos últimos 120 dias e intervalo histórico menor que 120 dias é atendido a cada 30 dias
cliente com compra entre 45 e 70 dias é atendido a cada 30 dias
cliente com compra entre 71 e 120 dias é atendido a cada 21 dias
cliente sem compra há mais de 120 dias é atendido a cada 30 dias

## Estrutura

```yaml
publico: time de televendas
comuns: []
regras:
  - nome: Não agendar inadimplentes
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar baixados na Receita Federal
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: baixado na Receita Federal}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Prospects
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Cliente ativado
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 45, unidade: dias}
      - {tipo: situacao_cadastro, op: maior_que, valor: 120, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Ativo de alta frequência
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 45, unidade: dias}
      - {tipo: tempo_sem_comprar, op: menor_que, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Ativo que compra regularmente
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 120, unidade: dias}
      - {tipo: tempo_sem_comprar, op: menor_que, valor: 120, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Estimular regularidade
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [45, 70], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Em ruptura
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [71, 120], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Inativos
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 120, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 30 dias}
termos_fora_vocabulario:
  - baixado na Receita Federal
  - frequência histórica de compra
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| baixado na Receita | jargao | cadastro encerrado no órgão fiscal |
| prospect | jargao | cliente que nunca comprou |
| frequência histórica | jargao | intervalo médio entre compras |
| ruptura | jargao | cliente que parou de comprar |

## Lacunas

- A entrada não diz se o televendas trabalha sobre carteira fixa.

## Ambiguidades

- As faixas de compra se sobrepõem (45 dias, 120 dias); a ordem de avaliação define qual regra se aplica.
