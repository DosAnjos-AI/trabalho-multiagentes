---
id: regra_129
origem: simulacao/regra_129/entrada.md
gobr: simulacao/regra_129/regra_129.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 4
procedencia: corpus_sintetico
---

## Regras

cliente inadimplente não é agendado
cliente filial não é agendado
cliente ativo é atendido a cada 7 dias
os demais clientes, inativos, são atendidos a cada 14 dias

## Estrutura

```yaml
publico: todos os vendedores ativos
comuns: []
regras:
  - nome: Não agendar inadimplentes
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar filiais
    se:
      - {tipo: segmento, op: igual_a, valor: filial}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Ativos a cada 7 dias
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Demais clientes a cada 14 dias
    se: []
    entao: {acao: agendar, frequencia: fixa 14 dias}
termos_fora_vocabulario:
  - filial
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Boa Praça | empresa_foco | EMPRESA_FOCO |
| inadimplente | jargao | cliente com pendência financeira em aberto |
| filial | jargao | unidade filial de um cliente |

## Lacunas

- A entrada não diz sobre qual carteira os vendedores trabalham.
- A entrada não define o prazo que caracteriza o cliente ativo.

## Ambiguidades

- nenhuma
