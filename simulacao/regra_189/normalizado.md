---
id: regra_189
origem: simulacao/regra_189/entrada.md
gobr: simulacao/regra_189/regra_189.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 7
procedencia: corpus_sintetico
---

## Regras

cliente sem venda no ano e com ticket médio acima de 4999 reais é atendido semanalmente, preferindo segunda e sexta, com frequência fixa
cliente sem venda no ano e com ticket médio abaixo de 4999 reais é atendido semanalmente, preferindo terça e sexta, com frequência fixa
cliente sem venda no ano e com venda no ano passado é atendido semanalmente, preferindo quarta e quinta
cliente sem venda com o vendedor é atendido a cada 7 dias
cliente com uma única compra com o vendedor é atendido a cada 7 dias
cliente com intervalo histórico entre 0 e 14 dias usa o histórico, entre 4 e 6 dias
cliente sem compra com o vendedor entre 25 e 30 dias é atendido a cada 7 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Base de valor alto
    se:
      - {tipo: tempo_sem_comprar, op: igual_a, valor: sem venda no ano atual, unidade: periodo_nomeado, alcance: empresa}
      - {tipo: valor_cliente, op: maior_que, valor: 4999, unidade: reais}
      - {tipo: periodo_vigencia, op: igual_a, valor: [segunda, sexta], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Base de valor médio
    se:
      - {tipo: tempo_sem_comprar, op: igual_a, valor: sem venda no ano atual, unidade: periodo_nomeado, alcance: empresa}
      - {tipo: valor_cliente, op: menor_que, valor: 4999, unidade: reais}
      - {tipo: periodo_vigencia, op: igual_a, valor: [terça, sexta], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Última compra em 2024
    se:
      - {tipo: tempo_sem_comprar, op: igual_a, valor: venda no ano anterior e nenhuma no ano atual, unidade: periodo_nomeado, alcance: empresa}
      - {tipo: periodo_vigencia, op: igual_a, valor: [quarta, quinta], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Ativação de novo cliente em potencial
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Boas-vindas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Bom histórico de compra
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [0, 14], unidade: dias}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Risco de ficar inativo
    se:
      - {tipo: tempo_sem_comprar, op: fora_de, valor: [25, 30], unidade: dias, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 7 dias}
termos_fora_vocabulario:
  - compra por ano civil
  - preferência de dias da semana
  - frequência pelo histórico com mínimo e máximo
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| ticket médio | jargao | valor médio por pedido |
| frequência histórica | jargao | intervalo médio entre compras |

## Lacunas

- Ticket médio exatamente igual a 4999 reais não se enquadra em nenhuma das duas bases.

## Ambiguidades

- "Semanal" foi registrado como 7 dias pela convenção de periodicidade.
- "Última compra em 2024" depende do ano corrente; a regra fala em ano passado.
