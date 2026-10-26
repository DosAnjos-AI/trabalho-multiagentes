---
id: regra_130
origem: simulacao/regra_130/entrada.md
gobr: simulacao/regra_130/regra_130.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 8
procedencia: corpus_sintetico
---

## Regras

cliente pessoa física não é agendado
cliente ativo é atendido a cada 7 dias
cliente inativo e adimplente é atendido a cada 15 dias
cliente inativo e inadimplente não é agendado
cliente sem compra e pessoa física não é agendado
cliente sem compra e pessoa jurídica é atendido a cada 20 dias
cliente ativo é atendido a cada 7 dias, com frequência fixa
cliente inativo é atendido a cada 15 dias, com frequência fixa

## Estrutura

```yaml
publico: time interno (televendas) e time externo (campo)
comuns: []
regras:
  - nome: Não agendar pessoa física no interno
    publico: time interno
    se:
      - {tipo: segmento, op: igual_a, valor: pessoa física}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Ativos do interno
    publico: time interno
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos adimplentes do interno
    publico: time interno
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Não agendar inativos inadimplentes do interno
    publico: time interno
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar sem compra pessoa física
    publico: time interno
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
      - {tipo: segmento, op: igual_a, valor: pessoa física}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Sem compra pessoa jurídica
    publico: time interno
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
      - {tipo: segmento, op: igual_a, valor: pessoa jurídica}
    entao: {acao: agendar, frequencia: fixa 20 dias}
  - nome: Ativos do externo
    publico: time externo
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos do externo
    publico: time externo
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
    entao: {acao: agendar, frequencia: fixa 15 dias}
termos_fora_vocabulario:
  - pessoa física
  - pessoa jurídica
  - frequência fixa rígida
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Macropac | empresa_foco | EMPRESA_FOCO |
| time interno | jargao | atendimento por telefone |
| time externo | jargao | atendimento presencial |
| CPF | jargao | cliente pessoa física |
| CNPJ | jargao | cliente pessoa jurídica |
| inadimplente | jargao | cliente com pendência financeira em aberto |

## Lacunas

- A entrada não diz se os times trabalham sobre carteira fixa.

## Ambiguidades

- A regra de não agendar sem compra e pessoa física repete parte da regra inicial de não agendar pessoa física.
