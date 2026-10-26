---
id: regra_171
origem: simulacao/regra_171/entrada.md
gobr: simulacao/regra_171/regra_171.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 11
procedencia: corpus_sintetico
---

## Regras

cliente inadimplente não é agendado
cliente bloqueado não é agendado
cliente filial não é agendado
cliente com cadastro baixado na Receita Federal não é agendado
prospect é atendido a cada 14 dias
cliente com uma única compra com a empresa e cadastrado há 30 dias é atendido a cada 10 dias
cliente com compra nos últimos 30 dias e intervalo histórico menor que 14 dias é atendido a cada 14 dias
cliente com compra nos últimos 30 dias e intervalo histórico menor que 30 dias usa o histórico, entre 14 e 28 dias
cliente com compra entre 21 e 60 dias é atendido a cada 14 dias
cliente com compra entre 61 e 90 dias é atendido a cada 7 dias
cliente sem compra entre 90 e 180 dias é atendido a cada 21 dias

## Estrutura

```yaml
publico: time de televendas
comuns: []
regras:
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
  - nome: Não agendar baixados na Receita Federal
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: baixado na Receita Federal}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Prospects
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Cliente ativado
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única, alcance: empresa}
      - {tipo: situacao_cadastro, op: maior_que, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 10 dias}
  - nome: Alta frequência de compra
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
      - {tipo: tempo_sem_comprar, op: menor_que, valor: 14, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Compra regularmente
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
      - {tipo: tempo_sem_comprar, op: menor_que, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Estimular regularidade
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [21, 60], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Em ruptura
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [61, 90], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos
    se:
      - {tipo: tempo_sem_comprar, op: fora_de, valor: [90, 180], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 21 dias}
termos_fora_vocabulario:
  - bloqueado
  - filial
  - baixado na Receita Federal
  - frequência histórica de compra
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| bloqueado | jargao | cliente com cadastro bloqueado |
| filial | jargao | unidade filial de um cliente |
| baixado na Receita | jargao | cadastro encerrado no órgão fiscal |
| frequência histórica | jargao | intervalo médio entre compras |
| ruptura | jargao | cliente que parou de comprar |

## Lacunas

- A entrada não diz se o televendas trabalha sobre carteira fixa.

## Ambiguidades

- "Cadastrado há 30 dias" foi registrado como tempo mínimo de cadastro (maior_que 30).
- Os limites de 14 e 28 dias da frequência pelo histórico não têm campo próprio e foram registrados apenas na descrição.
- "Sem compra entre 90 e 180 dias" foi registrado como ausência de compra na janela (fora_de).
