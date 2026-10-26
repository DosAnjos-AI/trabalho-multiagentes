---
id: regra_229
origem: simulacao/regra_229/entrada.md
gobr: simulacao/regra_229/regra_229.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 5
procedencia: corpus_sintetico
---

## Regras

cliente com compra nos últimos 30 dias não é agendado
prospect que nunca comprou é atendido a cada 14 dias, com avaliação do vendedor sobre mantê-lo na carteira
cliente entre 31 e 60 dias sem compra é atendido a cada 14 dias
cliente entre 61 e 90 dias sem compra é atendido a cada 21 dias
os clientes com mais de 90 dias sem compra são atendidos a cada 28 dias

## Estrutura

```yaml
publico: time de venda na base, VENDEDOR_01 a VENDEDOR_07
comuns: []
regras:
  - nome: Não agendar compra nos últimos 30 dias
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Prospects
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Cobertura mensal, entre 31 e 60 dias sem compra
    se:
      - {tipo: tempo_sem_comprar, op: fora_de, valor: [31, 60], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Caminhando para inatividade
    se:
      - {tipo: tempo_sem_comprar, op: fora_de, valor: [61, 90], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Mais de 90 dias sem compra
    se: []
    entao: {acao: agendar, frequencia: fixa 28 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| vendedor 3 | vendedor | VENDEDOR_01 |
| vendedor 4 | vendedor | VENDEDOR_02 |
| vendedor 8 | vendedor | VENDEDOR_03 |
| vendedor 9 | vendedor | VENDEDOR_04 |
| vendedor 10 | vendedor | VENDEDOR_05 |
| vendedor 12 | vendedor | VENDEDOR_06 |
| vendedor 16 | vendedor | VENDEDOR_07 |
| farm | jargao | time dedicado à base de clientes existentes |
| positivação | jargao | compra registrada do cliente |

## Lacunas

- A entrada não informa se as compras consideram o vendedor ou a empresa.

## Ambiguidades

- "Entre X e Y dias sem compra" foi registrado como ausência de compra na janela (fora_de).
- A avaliação do vendedor sobre manter o prospect na carteira é orientação, não critério.
