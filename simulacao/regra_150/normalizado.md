---
id: regra_150
origem: simulacao/regra_150/entrada.md
gobr: simulacao/regra_150/regra_150.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 4
procedencia: corpus_sintetico
---

## Regras

cliente com compra com a empresa nos últimos 45 dias não é agendado
prospect é atendido a cada 28 dias
cliente com compra entre 46 e 89 dias é atendido a cada 14 dias
cliente inativo é atendido a cada 21 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Não agendar quem comprou nos últimos 45 dias
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 45, unidade: dias, alcance: empresa}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Prospects
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 28 dias}
  - nome: Caminhando para a inatividade
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [46, 89], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Resgate de inativos
    se: []
    entao: {acao: agendar, frequencia: fixa 21 dias}
termos_fora_vocabulario: []
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| prospect | jargao | cliente que nunca comprou |
| resgate | jargao | reativação de cliente inativo |

## Lacunas

- A entrada não informa se a faixa de 46 a 89 dias considera compras com a empresa ou com o vendedor.

## Ambiguidades

- A regra de inativos não tem critério próprio e funciona como regra residual.
