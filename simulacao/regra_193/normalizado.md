---
id: regra_193
origem: simulacao/regra_193/entrada.md
gobr: simulacao/regra_193/regra_193.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 6
procedencia: corpus_sintetico
---

## Regras

cliente filial não é agendado
cliente com cadastro baixado na Receita Federal não é agendado
cliente com rota do vendedor nos próximos 21 dias e compra nos últimos 60 dias não é agendado
cliente dos ramos da primeira lista com venda nos últimos 60 dias é atendido a cada 14 dias
cliente dos demais ramos com venda nos últimos 60 dias é atendido a cada 21 dias
cliente de qualquer ramo sem venda em 60 dias é atendido a cada 7 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Não agendar filiais
    se:
      - {tipo: segmento, op: igual_a, valor: filial}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar baixados na Receita Federal
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: baixado na Receita Federal}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar fora da semana de cobertura
    se:
      - {tipo: agenda_rota, op: dentro_de, valor: 21, unidade: dias, alcance: vendedor}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 60, unidade: dias}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Primeira lista de ramos com venda em 60 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['30', '583', '33', '26', '42', '34', '7', '21', '2', '29', '43', '4', '40', '52', '20', '584', '110', '124', '39', '120', '75', '57', '240', '366', '470', '237', '58', '69', '242', '46', '298', '56']}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 60, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Demais ramos com venda em 60 dias
    se:
      - {tipo: segmento, op: fora_de, valor: ['30', '583', '33', '26', '42', '34', '7', '21', '2', '29', '43', '4', '40', '52', '20', '584', '110', '124', '39', '120', '75', '57', '240', '366', '470', '237', '58', '69', '242', '46', '298', '56']}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 60, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Todos os ramos sem venda em 60 dias
    se: []
    entao: {acao: agendar, frequencia: fixa 7 dias}
termos_fora_vocabulario:
  - filial
  - baixado na Receita Federal
  - semana de cobertura
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| ramo de atividade | jargao | segmento do cliente |
| filial | jargao | unidade filial de um cliente |
| baixado na Receita | jargao | cadastro encerrado no órgão fiscal |
| semana de cobertura | jargao | período em que a rota do vendedor atende o cliente |

## Lacunas

- A entrada não informa o significado dos códigos de ramo de atividade.

## Ambiguidades

- A regra de 7 dias para "todos os ramos sem venda em 60 dias" não tem critério explícito e funciona como regra residual.
