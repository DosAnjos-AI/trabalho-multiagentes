---
id: regra_155
origem: simulacao/regra_155/entrada.md
gobr: simulacao/regra_155/regra_155.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 14
procedencia: corpus_sintetico
---

## Regras

cliente pessoa física não é agendado
cliente filial não é agendado
cliente com cadastro baixado na Receita Federal não é agendado
cliente inadimplente não é agendado
cliente que comprou nos últimos 30 dias não é agendado
prospect cadastrado há mais de 30 dias é atendido a cada 7 dias
prospect em geral, que nunca pediu orçamento ou não pede há mais de um ano, é atendido a cada 21 dias
cliente com uma única compra com o vendedor é atendido a cada 7 dias
cliente de curva A sem compra com a empresa entre 30 e 45 dias é atendido a cada 14 dias
cliente de curva B sem compra com a empresa entre 30 e 45 dias é atendido a cada 28 dias
os demais clientes sem compra com a empresa entre 30 e 45 dias são atendidos a cada 45 dias
cliente sem orçamento entre 46 e 60 dias é atendido a cada 28 dias
cliente sem orçamento entre 61 e 90 dias é atendido a cada 21 dias
cliente há mais de 90 dias sem orçamento é atendido a cada 14 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Não agendar pessoa física
    se:
      - {tipo: segmento, op: igual_a, valor: pessoa física}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar filiais
    se:
      - {tipo: segmento, op: igual_a, valor: filial}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar baixados na Receita Federal
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: baixado na Receita Federal}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar inadimplentes
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar quem comprou nos últimos 30 dias
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Ativação de novo cliente em potencial
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
      - {tipo: situacao_cadastro, op: maior_que, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Requalificar contato
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Boas-vindas ao cliente ativado
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Bom histórico, curva A
    se:
      - {tipo: tempo_sem_comprar, op: fora_de, valor: [30, 45], unidade: dias, alcance: empresa}
      - {tipo: valor_cliente, op: igual_a, valor: curva A}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Bom histórico, curva B
    se:
      - {tipo: tempo_sem_comprar, op: fora_de, valor: [30, 45], unidade: dias, alcance: empresa}
      - {tipo: valor_cliente, op: igual_a, valor: curva B}
    entao: {acao: agendar, frequencia: fixa 28 dias}
  - nome: Bom histórico, demais
    se:
      - {tipo: tempo_sem_comprar, op: fora_de, valor: [30, 45], unidade: dias, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 45 dias}
  - nome: Estimular regularidade
    se:
      - {tipo: tempo_sem_comprar, op: fora_de, valor: [46, 60], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 28 dias}
  - nome: Risco de ficar inativo
    se:
      - {tipo: tempo_sem_comprar, op: fora_de, valor: [61, 90], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Risco de ativação por outro vendedor
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 90, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
termos_fora_vocabulario:
  - pessoa física
  - filial
  - baixado na Receita Federal
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| filial | jargao | unidade filial de um cliente |
| baixado na Receita Federal | jargao | cadastro encerrado no órgão fiscal |
| prospect | jargao | cliente que nunca comprou |
| lead | jargao | contato comercial potencial |
| orçamento | jargao | pedido ou cotação do cliente |
| curva A, B | jargao | faixas de cliente por faturamento |

## Lacunas

- A entrada não define os critérios das curvas A e B.
- A regra de requalificação menciona "não pede há mais de um ano", mas não traz esse prazo como critério.

## Ambiguidades

- "Entre 30 e 45 dias sem compra" foi registrado como ausência de compra na janela (fora_de); pode também ser lido como última compra ocorrida nessa faixa. O mesmo vale para as faixas de 46 a 60 e 61 a 90 dias.
- A regra de risco de ativação por outro vendedor (mais de 90 dias) não tem critério próprio na estrutura original e pode funcionar como regra residual.
