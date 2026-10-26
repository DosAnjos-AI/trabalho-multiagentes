---
id: regra_142
origem: simulacao/regra_142/entrada.md
gobr: simulacao/regra_142/regra_142.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 19
procedencia: corpus_sintetico
---

## Regras

cliente de curva A é atendido a cada 3 dias
cliente de curva B é atendido a cada 7 dias
cliente de curva C é atendido a cada 14 dias
cliente sem classificação de curva é atendido a cada 14 dias
cliente de curva A é atendido a cada 2 dias
cliente de curva B é atendido a cada 7 dias
cliente de curva C é atendido a cada 14 dias
cliente sem classificação de curva é atendido a cada 7 dias
cliente de curva A é atendido a cada 4 dias
cliente de curva B é atendido a cada 7 dias
cliente de curva C é atendido a cada 9 dias
cliente sem classificação de curva é atendido a cada 14 dias
cliente inadimplente não é contatado
cliente dos ramos 1 e 2, hospitais e clínicas, é atendido a cada 14 dias
cliente do ramo 3, distribuidora, é atendido a cada 7 dias
cliente do ramo 4, farmácia, é atendido a cada 21 dias
cliente dos ramos 5, 6 e 100 não é contatado
cliente ativo é atendido semanalmente
os demais clientes são atendidos a cada 15 dias

## Estrutura

```yaml
publico: todos os vendedores ativos, com três vendedores em times individuais
comuns: []
regras:
  - nome: Curva A de VENDEDOR_01
    publico: VENDEDOR_01
    se:
      - {tipo: valor_cliente, op: igual_a, valor: curva A}
    entao: {acao: agendar, frequencia: fixa 3 dias}
  - nome: Curva B de VENDEDOR_01
    publico: VENDEDOR_01
    se:
      - {tipo: valor_cliente, op: igual_a, valor: curva B}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Curva C de VENDEDOR_01
    publico: VENDEDOR_01
    se:
      - {tipo: valor_cliente, op: igual_a, valor: curva C}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Sem classificação de VENDEDOR_01
    publico: VENDEDOR_01
    se: []
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Curva A de VENDEDOR_02
    publico: VENDEDOR_02
    se:
      - {tipo: valor_cliente, op: igual_a, valor: curva A}
    entao: {acao: agendar, frequencia: fixa 2 dias}
  - nome: Curva B de VENDEDOR_02
    publico: VENDEDOR_02
    se:
      - {tipo: valor_cliente, op: igual_a, valor: curva B}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Curva C de VENDEDOR_02
    publico: VENDEDOR_02
    se:
      - {tipo: valor_cliente, op: igual_a, valor: curva C}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Sem classificação de VENDEDOR_02
    publico: VENDEDOR_02
    se: []
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Curva A de VENDEDOR_03
    publico: VENDEDOR_03
    se:
      - {tipo: valor_cliente, op: igual_a, valor: curva A}
    entao: {acao: agendar, frequencia: fixa 4 dias}
  - nome: Curva B de VENDEDOR_03
    publico: VENDEDOR_03
    se:
      - {tipo: valor_cliente, op: igual_a, valor: curva B}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Curva C de VENDEDOR_03
    publico: VENDEDOR_03
    se:
      - {tipo: valor_cliente, op: igual_a, valor: curva C}
    entao: {acao: agendar, frequencia: fixa 9 dias}
  - nome: Sem classificação de VENDEDOR_03
    publico: VENDEDOR_03
    se: []
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Não contatar inadimplentes
    publico: todos os vendedores ativos exceto VENDEDOR_01, VENDEDOR_02 e VENDEDOR_03
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Hospitais e clínicas
    publico: todos os vendedores ativos exceto VENDEDOR_01, VENDEDOR_02 e VENDEDOR_03
    se:
      - {tipo: segmento, op: igual_a, valor: ['1', '2']}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Distribuidoras
    publico: todos os vendedores ativos exceto VENDEDOR_01, VENDEDOR_02 e VENDEDOR_03
    se:
      - {tipo: segmento, op: igual_a, valor: ['3']}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Farmácias
    publico: todos os vendedores ativos exceto VENDEDOR_01, VENDEDOR_02 e VENDEDOR_03
    se:
      - {tipo: segmento, op: igual_a, valor: ['4']}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Não contatar órgão público, representantes e fornecedores
    publico: todos os vendedores ativos exceto VENDEDOR_01, VENDEDOR_02 e VENDEDOR_03
    se:
      - {tipo: segmento, op: igual_a, valor: ['5', '6', '100']}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Ativos semanal
    publico: todos os vendedores ativos exceto VENDEDOR_01, VENDEDOR_02 e VENDEDOR_03
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Demais clientes quinzenal
    publico: todos os vendedores ativos exceto VENDEDOR_01, VENDEDOR_02 e VENDEDOR_03
    se: []
    entao: {acao: agendar, frequencia: fixa 15 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Dispomed | empresa_foco | EMPRESA_FOCO |
| Yara, vendedor 10 | vendedor | VENDEDOR_01 |
| Lúcia, vendedor 5 | vendedor | VENDEDOR_02 |
| Wanderson, vendedor 3 | vendedor | VENDEDOR_03 |
| curva A, B e C | jargao | faixas de cliente por faturamento |
| ramo de atividade | jargao | segmento do cliente |
| inadimplente | jargao | cliente com pendência financeira em aberto |

## Lacunas

- A entrada não define os critérios das curvas A, B e C.
- A entrada não diz sobre qual carteira os vendedores trabalham.

## Ambiguidades

- "Semanal" para clientes ativos foi registrado como 7 dias pela convenção de periodicidade; a entrada não dá o número.
