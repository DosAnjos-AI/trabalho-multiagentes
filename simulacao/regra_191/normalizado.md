---
id: regra_191
origem: simulacao/regra_191/entrada.md
gobr: simulacao/regra_191/regra_191.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 8
procedencia: corpus_sintetico
---

## Regras

cliente com cadastro baixado na Receita Federal não é agendado
cliente inadimplente não é agendado
prospect é atendido a cada 21 dias
cliente com compra nos últimos 7 dias é atendido a cada 21 dias
cliente com compra nos últimos 30 dias usa o histórico acrescido de 3 dias, entre 14 e 30 dias
cliente com compra em até 45 dias é atendido a cada 7 dias
cliente com compra em até 60 dias é atendido a cada 7 dias
inativos são atendidos a cada 7 dias

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
  - nome: Prospects
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Pós-venda
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 7, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Alta regularidade
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Estimular regularidade
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 45, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Risco de inatividade
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 60, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos
    se: []
    entao: {acao: agendar, frequencia: fixa 7 dias}
termos_fora_vocabulario:
  - baixado na Receita Federal
  - frequência pelo histórico com acréscimo e limites
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| baixado na Receita | jargao | cadastro encerrado no órgão fiscal |
| prospect | jargao | cliente que nunca comprou |
| pós-venda | jargao | contato após compra recente |

## Lacunas

- A entrada não informa se as compras consideram o vendedor ou a empresa.

## Ambiguidades

- O acréscimo de 3 dias e os limites de 14 e 30 dias da frequência pelo histórico não têm campo próprio e foram registrados apenas na descrição.
- As faixas "nos últimos 7", "30", "até 45" e "até 60 dias" se sobrepõem; cada uma vale para quem não caiu na anterior.
