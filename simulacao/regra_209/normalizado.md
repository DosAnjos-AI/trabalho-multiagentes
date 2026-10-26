---
id: regra_209
origem: simulacao/regra_209/entrada.md
gobr: simulacao/regra_209/regra_209.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 6
procedencia: corpus_sintetico
---

## Regras

cliente inadimplente não é agendado
cliente filial não é agendado
cliente sem compra com o vendedor nos últimos 90 dias não é agendado
prospect com o vendedor é atendido a cada 7 dias
cliente com intervalo histórico entre 0 e 30 dias e compra com o vendedor nos últimos 30 dias é atendido a cada 7 dias
cliente sem compra com o vendedor entre 31 e 90 dias é atendido a cada 17 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Não agendar inadimplentes
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar filiais
    se:
      - {tipo: segmento, op: igual_a, valor: filial}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar sem compra com o vendedor em 90 dias
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 90, unidade: dias, alcance: vendedor}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Prospects do vendedor
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Compra com regularidade
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [0, 30], unidade: dias}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Precisa de acompanhamento
    se:
      - {tipo: tempo_sem_comprar, op: fora_de, valor: [31, 90], unidade: dias, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 17 dias}
termos_fora_vocabulario:
  - filial
  - frequência histórica de compra
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| filial | jargao | unidade filial de um cliente |
| recência | jargao | tempo desde a última compra |
| frequência histórica | jargao | intervalo médio entre compras |

## Lacunas

- A entrada não traz regra residual para clientes que não se enquadram nas regras de agendamento.

## Ambiguidades

- "Sem compra com o vendedor entre 31 e 90 dias" foi registrado como ausência de compra na janela (fora_de).
