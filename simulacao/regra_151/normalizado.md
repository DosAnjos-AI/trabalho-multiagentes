---
id: regra_151
origem: simulacao/regra_151/entrada.md
gobr: simulacao/regra_151/regra_151.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 1
procedencia: corpus_sintetico
---

## Regras

na última semana do mês, clientes do grupo auxiliar de ativos do campo com venda em 60 dias não são agendados para o televendas

## Estrutura

```yaml
publico: televendas, VENDEDOR_03
comuns: []
regras:
  - nome: Não agendar ativos do campo na última semana do mês
    se:
      - {tipo: carteira, op: igual_a, valor: carteira fixa do televendas com ruptura do campo, alcance: vendedor}
      - {tipo: carteira, op: igual_a, valor: grupo auxiliar de clientes de ruptura, alcance: outro_vendedor}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 60, unidade: dias, alcance: outro_vendedor}
      - {tipo: periodo_vigencia, op: igual_a, valor: última semana do mês, unidade: periodo_nomeado}
    entao: {acao: nao_agendar, frequencia: nao_informada}
termos_fora_vocabulario:
  - grupo auxiliar de clientes
  - carteira composta com ruptura
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| vendedor 283 | vendedor | VENDEDOR_01 |
| vendedor 279 | vendedor | VENDEDOR_02 |
| vendedor 291 | vendedor | VENDEDOR_03 |
| ruptura | jargao | repasse de clientes sem compra recente para outro vendedor |
| grupo auxiliar | jargao | conjunto de clientes definido para uso em regras |
| carteira fixa | jargao | clientes vinculados a um vendedor |

## Lacunas

- A entrada não informa nenhuma regra de agendamento com frequência para o televendas; só a exclusão.

## Ambiguidades

- O grupo auxiliar (venda nos últimos 60 dias) e a ruptura (entre 7 e 60 dias sem comprar) se sobrepõem; o efeito prático da exclusão depende de como os dois conjuntos se cruzam.
