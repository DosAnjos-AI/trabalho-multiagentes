---
id: regra_215
origem: simulacao/regra_215/entrada.md
gobr: simulacao/regra_215/regra_215.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 6
procedencia: corpus_sintetico
---

## Regras

prospect com o vendedor é atendido a cada 7 dias
cliente com uma única compra e sem compra nos últimos 20 dias é atendido a cada 7 dias
cliente com compra nos últimos 30 dias é atendido a cada 7 dias
cliente com compra entre 31 e 60 dias é atendido a cada 7 dias
cliente com compra entre 60 e 90 dias é atendido a cada 7 dias
cliente sem compra há mais de 90 dias é atendido a cada 7 dias

## Estrutura

```yaml
publico: time de televendas
comuns: []
regras:
  - nome: Primeira compra
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Prospect ativado
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única, alcance: vendedor}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 20, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Compra regularmente
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Estimular regularidade
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [31, 60], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Risco de inatividade
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [60, 90], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Resgate
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 90, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| prospect | jargao | cliente que nunca comprou |
| resgate | jargao | reativação de cliente inativo |

## Lacunas

- A entrada não informa se as compras consideram o vendedor ou a empresa.

## Ambiguidades

- Todas as regras têm a mesma frequência de 7 dias, o que torna a distinção entre perfis irrelevante para a frequência.
