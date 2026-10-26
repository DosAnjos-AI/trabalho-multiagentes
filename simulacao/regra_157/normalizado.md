---
id: regra_157
origem: simulacao/regra_157/entrada.md
gobr: simulacao/regra_157/regra_157.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 3
procedencia: corpus_sintetico
---

## Regras

cliente sem compra há mais de 120 dias é atendido a cada 14 dias, preferindo dia útil
cliente sem compra há mais de 30 dias é atendido a cada 7 dias, preferindo dia útil
os demais clientes usam a frequência do histórico, entre 5 e 30 dias, preferindo dia útil

## Estrutura

```yaml
publico: todos os vendedores ativos
comuns:
  - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
regras:
  - nome: Sem compra há mais de 120 dias
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 120, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Sem compra há mais de 30 dias
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Demais clientes pelo histórico
    se: []
    entao: {acao: agendar, frequencia: calculada}
termos_fora_vocabulario:
  - preferência por dia útil
  - frequência pelo histórico com mínimo e máximo
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Lubrilages | empresa_foco | EMPRESA_FOCO |
| frequência do histórico | jargao | frequência calculada pelo histórico de compras |

## Lacunas

- A entrada não diz sobre qual carteira os vendedores trabalham.

## Ambiguidades

- Os limites de 5 e 30 dias da frequência pelo histórico não têm campo próprio e foram registrados apenas na descrição.
