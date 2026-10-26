---
id: regra_141
origem: simulacao/regra_141/entrada.md
gobr: simulacao/regra_141/regra_141.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 7
procedencia: corpus_sintetico
---

## Regras

cliente ativo de curva A é atendido a cada 15 dias
cliente inativo de curva A é atendido a cada 7 dias
cliente ativo de curva B é atendido a cada 21 dias
cliente inativo de curva B é atendido a cada 14 dias
cliente ativo de curva C é atendido a cada 30 dias
cliente inativo de curva C é atendido a cada 21 dias
quem não tem curva, o prospect, é atendido a cada 21 dias

## Estrutura

```yaml
publico: todos os vendedores ativos
comuns: []
regras:
  - nome: Curva A ativos
    se:
      - {tipo: valor_cliente, op: igual_a, valor: curva A}
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Curva A inativos
    se:
      - {tipo: valor_cliente, op: igual_a, valor: curva A}
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Curva B ativos
    se:
      - {tipo: valor_cliente, op: igual_a, valor: curva B}
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Curva B inativos
    se:
      - {tipo: valor_cliente, op: igual_a, valor: curva B}
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Curva C ativos
    se:
      - {tipo: valor_cliente, op: igual_a, valor: curva C}
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Curva C inativos
    se:
      - {tipo: valor_cliente, op: igual_a, valor: curva C}
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Sem curva, prospects
    se: []
    entao: {acao: agendar, frequencia: fixa 21 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Ever Limp | empresa_foco | EMPRESA_FOCO |
| curva ABC | jargao | faixas de cliente por faturamento |
| prospect | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não define os critérios das curvas A, B e C nem o prazo que separa ativo de inativo.

## Ambiguidades

- nenhuma
