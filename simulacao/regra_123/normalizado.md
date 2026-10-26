---
id: regra_123
origem: simulacao/regra_123/entrada.md
gobr: simulacao/regra_123/regra_123.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 7
procedencia: corpus_sintetico
---

## Regras

cliente ativo do televendas é atendido a cada 7 dias
os demais clientes do televendas são atendidos a cada 15 dias
cliente ativo do ramo 1 é atendido a cada 7 dias
os demais clientes do ramo 1 são atendidos a cada 15 dias
qualquer cliente que não seja do ramo de saúde não é agendado
cliente ativo do campo é atendido a cada 7 dias, com frequência fixa
os demais clientes do campo são atendidos a cada 15 dias, com frequência fixa

## Estrutura

```yaml
publico: time de televendas, time de saúde e time de campo
comuns: []
regras:
  - nome: Ativos do televendas
    publico: televendas, exceto VENDEDOR_01
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Demais clientes do televendas
    publico: televendas, exceto VENDEDOR_01
    se: []
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Ativos do ramo 1 no time de saúde
    publico: time de saúde, VENDEDOR_01
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: segmento, op: igual_a, valor: ['1']}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Demais clientes do ramo 1 no time de saúde
    publico: time de saúde, VENDEDOR_01
    se:
      - {tipo: segmento, op: igual_a, valor: ['1']}
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Não agendar fora do ramo de saúde
    publico: time de saúde, VENDEDOR_01
    se: []
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Ativos do campo
    publico: time de campo
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Demais clientes do campo
    publico: time de campo
    se: []
    entao: {acao: agendar, frequencia: fixa 15 dias}
termos_fora_vocabulario:
  - frequência fixa rígida
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| goVendas | jargao | plataforma de vendas |
| vendedor 7027 | vendedor | VENDEDOR_01 |
| televendas | jargao | atendimento por telefone |
| campo | jargao | atendimento presencial |
| ramo 1 | jargao | segmento de saúde |
| parametrização fixa | jargao | frequência travada, sem ajuste automático |

## Lacunas

- A entrada não diz se os times trabalham sobre carteira fixa.
- A entrada não define o prazo que caracteriza o cliente ativo.

## Ambiguidades

- nenhuma
