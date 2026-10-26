---
id: regra_211
origem: simulacao/regra_211/entrada.md
gobr: simulacao/regra_211/regra_211.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 2
procedencia: corpus_sintetico
---

## Regras

cliente com pedido nos últimos 30 dias é atendido a cada 21 dias
cliente sem pedido nos últimos 30 dias é atendido a cada 15 dias

## Estrutura

```yaml
publico: time de ativação, VENDEDOR_01 e VENDEDOR_02
comuns: []
regras:
  - nome: Com pedido nos últimos 30 dias
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Sem pedido nos últimos 30 dias
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 15 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| vendedor 965 | vendedor | VENDEDOR_01 |
| vendedor 945 | vendedor | VENDEDOR_02 |
| time de ativação | jargao | time dedicado a ativar clientes |

## Lacunas

- A entrada não diz sobre qual carteira o time trabalha.

## Ambiguidades

- nenhuma
