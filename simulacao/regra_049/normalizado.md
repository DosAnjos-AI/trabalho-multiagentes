---
id: regra_049
origem: simulacao/regra_049/entrada.md
gobr: simulacao/regra_049/regra_049.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 5
procedencia: corpus_sintetico
---

## Regras

cliente baixado na Receita Federal não é agendado
cliente que comprou nos últimos 30 dias é atendido a cada 14 dias
cliente que comprou nos últimos 45 dias mas não nos últimos 30 é atendido a cada 7 dias
cliente sem compra há mais de 45 dias é atendido a cada 14 dias
prospect que nunca comprou é atendido a cada 7 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Bloqueio de baixados na Receita Federal
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: baixado na Receita Federal}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Clientes ativos
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
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 7 dias}
termos_fora_vocabulario:
  - baixado na Receita Federal
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| baixado na Receita Federal | jargao | cadastro encerrado no órgão fiscal |
| prospect | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não informa se a última compra considera o vendedor ou qualquer vendedor da empresa.

## Ambiguidades

- O prospect aparece depois das faixas de compra; como nunca comprou, pode cair antes na regra de inativos, dependendo da ordem de avaliação.
