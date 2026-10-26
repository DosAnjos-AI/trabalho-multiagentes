---
id: regra_230
origem: simulacao/regra_230/entrada.md
gobr: simulacao/regra_230/regra_230.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 7
procedencia: corpus_sintetico
---

## Regras

cliente inadimplente não é agendado
prospect com o vendedor é atendido a cada 14 dias
cliente com uma única compra com o vendedor é atendido a cada 7 dias
cliente ativo para o vendedor com intervalo histórico menor que 16 dias é atendido a cada 14 dias
cliente com compra entre 16 e 45 dias é atendido a cada 14 dias
cliente com compra entre 60 e 89 dias é atendido a cada 7 dias
cliente sem compra há mais de 60 dias é atendido a cada 21 dias

## Estrutura

```yaml
publico: time de televendas
comuns: []
regras:
  - nome: Não agendar inadimplentes
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Prospects do vendedor
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Cliente ativado
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Compra regularmente
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo, alcance: vendedor}
      - {tipo: tempo_sem_comprar, op: menor_que, valor: 16, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Estimular regularidade
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [16, 45], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Em ruptura
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [60, 89], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 60, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 21 dias}
termos_fora_vocabulario:
  - frequência histórica de compra
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| prospect | jargao | cliente que nunca comprou |
| frequência histórica | jargao | intervalo médio entre compras |
| ruptura | jargao | cliente que parou de comprar |

## Lacunas

- Clientes com compra entre 46 e 59 dias não têm regra explícita além da regra de inativos.

## Ambiguidades

- A regra de inativos (mais de 60 dias) se sobrepõe à de ruptura (60 a 89 dias); a ordem de avaliação define qual prevalece.
