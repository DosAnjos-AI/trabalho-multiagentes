---
id: regra_047
origem: simulacao/regra_047/entrada.md
gobr: simulacao/regra_047/regra_047.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 6
procedencia: corpus_sintetico
---

## Regras

cliente pessoa física não é agendado
cliente ativo e adimplente é atendido a cada 7 dias
cliente ativo e inadimplente é atendido a cada 14 dias
cliente inativo e adimplente é atendido a cada 14 dias
cliente inativo e inadimplente não é agendado
cliente sem vendas é atendido a cada 14 dias

## Estrutura

```yaml
publico: todos os vendedores ativos
comuns:
  - {tipo: carteira, op: igual_a, valor: carteira fixa, alcance: vendedor}
regras:
  - nome: Não agendar pessoa física
    se:
      - {tipo: segmento, op: igual_a, valor: pessoa física}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Ativos adimplentes a cada 7 dias
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Ativos inadimplentes a cada 14 dias
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Inativos adimplentes a cada 14 dias
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: adimplente}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Não agendar inativos inadimplentes
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Sem vendas a cada 14 dias
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 14 dias}
termos_fora_vocabulario:
  - pessoa física
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| STO | empresa_foco | EMPRESA_FOCO |
| Govendas | jargao | plataforma de vendas |
| CPF | jargao | cliente pessoa física |
| carteira fixa | jargao | clientes vinculados a um vendedor |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| sem vendas | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não define o prazo que separa ativo de inativo.

## Ambiguidades

- nenhuma
