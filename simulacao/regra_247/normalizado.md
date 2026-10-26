---
id: regra_247
origem: simulacao/regra_247/entrada.md
gobr: simulacao/regra_247/regra_247.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 5
procedencia: corpus_sintetico
---

## Regras

cliente com cadastro baixado na Receita Federal não é agendado
cliente com compra nos últimos 30 dias é atendido a cada 14 dias
cliente com compra em até 45 dias mas não nos últimos 30 é atendido semanalmente, a cada 7 dias
cliente sem compra há mais de 45 dias é atendido a cada 14 dias
prospect que nunca comprou com a empresa é atendido a cada 7 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Não agendar baixados na Receita Federal
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: baixado na Receita Federal}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Ativos
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Risco de inatividade
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 45, unidade: dias}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 45, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Prospects
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 7 dias}
termos_fora_vocabulario:
  - baixado na Receita Federal
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Govendas | jargao | plataforma de vendas |
| televendas | jargao | atendimento por telefone |
| baixado na Receita | jargao | cadastro encerrado no órgão fiscal |
| prospect | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não informa a origem do pedido.
- A entrada não informa se as compras consideram o vendedor ou a empresa nas faixas de tempo.

## Ambiguidades

- A regra de prospects vem depois da de inativos; dependendo da ordem de avaliação, prospects podem ser classificados como inativos antes.
