---
id: regra_065
origem: simulacao/regra_065/entrada.md
gobr: simulacao/regra_065/regra_065.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 3
procedencia: corpus_sintetico
---

## Regras

cliente que comprou nos últimos 30 dias é atendido a cada 14 dias, preferindo dias úteis
cliente sem compra há mais de 30 dias é atendido a cada 28 dias, preferindo dias úteis
cliente que nunca comprou é atendido a cada 28 dias, preferindo dias úteis

## Estrutura

```yaml
publico: time de televendas
comuns:
  - {tipo: carteira, op: igual_a, valor: carteira fixa do televendas, alcance: grupo}
  - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
regras:
  - nome: Compradores dos últimos 30 dias
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Sem compra há mais de 30 dias
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 28 dias}
  - nome: Nunca comprou
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 28 dias}
termos_fora_vocabulario:
  - preferência por dias úteis
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Evermax | empresa_foco | EMPRESA_FOCO |
| televendas | jargao | atendimento por telefone |
| carteira fixa | jargao | clientes vinculados a um vendedor ou time |

## Lacunas

- A entrada não informa se a última compra considera o vendedor ou qualquer vendedor da empresa.

## Ambiguidades

- "Preferência por dias úteis" é preferência de agendamento, não condição; registrada como critério de período por falta de campo próprio.
