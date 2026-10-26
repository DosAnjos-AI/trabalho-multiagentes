---
id: regra_249
origem: simulacao/regra_249/entrada.md
gobr: simulacao/regra_249/regra_249.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 5
procedencia: corpus_real
---

## Regras

cliente com cadastro baixado na Receita Federal não é agendado
prospect que nunca fez pedido com a empresa é atendido a cada 7 dias
cliente com último pedido nos últimos 60 dias, com qualquer vendedor da empresa, é atendido a cada 14 dias
cliente com pedido nos últimos 90 dias é atendido a cada 7 dias
todo o resto, considerado inativo, é atendido a cada 28 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Não agendar baixados na Receita Federal
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: baixado na Receita Federal}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Prospects
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Ativos
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 60, unidade: dias, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Risco de inatividade
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 90, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos
    se: []
    entao: {acao: agendar, frequencia: fixa 28 dias}
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
- A entrada não informa se a regra de 90 dias considera pedidos com o vendedor ou com a empresa.

## Ambiguidades

- As faixas de 60 e 90 dias se sobrepõem; entende-se que a de 90 dias vale para quem não caiu na de 60.
