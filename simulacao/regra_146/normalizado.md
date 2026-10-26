---
id: regra_146
origem: simulacao/regra_146/entrada.md
gobr: simulacao/regra_146/regra_146.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 8
procedencia: corpus_sintetico
---

## Regras

cliente inadimplente não é agendado
cliente dos ramos 37, 43 e 15 é atendido a cada 7 dias
cliente dos ramos 41, 4 e 25 com intervalo histórico de compra de 7 dias é atendido a cada 7 dias
cliente sem venda com o vendedor é atendido a cada 30 dias
cliente com uma única compra com o vendedor e compra nos últimos 30 dias é atendido a cada 30 dias
cliente com intervalo histórico menor que 21 dias é atendido a cada 21 dias
cliente com última compra entre 30 e 45 dias é atendido a cada 21 dias
cliente sem compra há mais de 46 dias é atendido a cada 45 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Não agendar inadimplentes
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Segmento saúde
    se:
      - {tipo: segmento, op: igual_a, valor: ['37', '43', '15']}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Segmento de alimentação
    se:
      - {tipo: segmento, op: igual_a, valor: ['41', '4', '25']}
      - {tipo: tempo_sem_comprar, op: igual_a, valor: 7, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Cliente potencial
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Cliente ativado
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única, alcance: vendedor}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Compra regularmente
    se:
      - {tipo: tempo_sem_comprar, op: menor_que, valor: 21, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Em ruptura
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [30, 45], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Inativos
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 46, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 45 dias}
termos_fora_vocabulario:
  - frequência histórica de compra
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| food | jargao | segmento de alimentação |
| ramo de atividade | jargao | segmento do cliente |
| frequência histórica | jargao | intervalo médio entre compras |
| ruptura | jargao | cliente que parou de comprar |

## Lacunas

- A entrada não informa se as compras de 30 dias, 30 a 45 dias e 46 dias consideram o vendedor ou a empresa.

## Ambiguidades

- O cliente sem compra entre 45 e 46 dias não se enquadra explicitamente nem na regra de ruptura nem na de inativos.
