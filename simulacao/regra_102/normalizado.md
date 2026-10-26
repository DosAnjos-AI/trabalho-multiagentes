---
id: regra_102
origem: simulacao/regra_102/entrada.md
gobr: simulacao/regra_102/regra_102.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 3
procedencia: corpus_sintetico
---

## Regras

cliente inativo e inadimplente do televendas é atendido a cada 30 dias, preferindo dia útil
todo o restante do televendas é atendido a cada 14 dias, preferindo dia útil
todos os clientes do campo são atendidos a cada 30 dias, preferindo dia útil

## Estrutura

```yaml
publico: time de campo e time de televendas
comuns:
  - {tipo: periodo_vigencia, op: igual_a, valor: dias úteis, unidade: periodo_nomeado}
regras:
  - nome: Inativos inadimplentes do televendas
    publico: time de televendas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Restante do televendas
    publico: time de televendas
    se: []
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Todos os clientes do campo
    publico: time de campo
    se: []
    entao: {acao: agendar, frequencia: fixa 30 dias}
termos_fora_vocabulario:
  - preferência por dia útil
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Aliança Distribuidora | empresa_foco | EMPRESA_FOCO |
| televendas | jargao | atendimento por telefone |
| campo | jargao | atendimento presencial |
| inadimplente | jargao | cliente com pendência financeira em aberto |

## Lacunas

- A entrada não diz se os times trabalham sobre carteira fixa.

## Ambiguidades

- "Preferindo dia útil" é preferência de agendamento, não condição; registrada como critério de período por falta de campo próprio.
