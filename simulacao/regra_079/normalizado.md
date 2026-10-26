---
id: regra_079
origem: simulacao/regra_079/entrada.md
gobr: simulacao/regra_079/regra_079.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 3
procedencia: corpus_sintetico
---

## Regras

cliente com ramo de atividade fora de 12 a 19 não é agendado
cliente do ramo 12 é atendido a cada 7 dias
os demais clientes, ramos 13 a 19, são atendidos a cada 14 dias

## Estrutura

```yaml
publico: todos os vendedores ativos, tratados como televendas
comuns: []
regras:
  - nome: Não agendar ramos fora da lista
    se:
      - {tipo: segmento, op: fora_de, valor: ['12', '13', '14', '15', '16', '17', '18', '19']}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Ramo 12 a cada 7 dias
    se:
      - {tipo: segmento, op: igual_a, valor: ['12']}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Demais ramos a cada 14 dias
    se: []
    entao: {acao: agendar, frequencia: fixa 14 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Girardi | empresa_foco | EMPRESA_FOCO |
| televendas | jargao | atendimento por telefone |
| ramo de atividade | jargao | segmento do cliente |

## Lacunas

- A entrada não informa o significado dos códigos de ramo de atividade.

## Ambiguidades

- nenhuma
