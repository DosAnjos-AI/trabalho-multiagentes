---
id: regra_192
origem: simulacao/regra_192/entrada.md
gobr: simulacao/regra_192/regra_192.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 5
procedencia: corpus_sintetico
---

## Regras

cliente com cadastro baixado na Receita Federal não é agendado
prospect é atendido a cada 14 dias
cliente com compra nos últimos 15 dias é atendido a cada 7 dias
cliente com compra em até 30 dias é atendido a cada 3 dias
o restante é atendido a cada 5 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Não agendar baixados na Receita Federal
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: baixado na Receita Federal}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Prospects
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Ativos
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 15, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Risco de inatividade
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 3 dias}
  - nome: Inativos de 30 dias
    se: []
    entao: {acao: agendar, frequencia: fixa 5 dias}
termos_fora_vocabulario:
  - baixado na Receita Federal
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| baixado na Receita | jargao | cadastro encerrado no órgão fiscal |
| prospect | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não informa se as compras consideram o vendedor ou a empresa.

## Ambiguidades

- A faixa "até 30 dias" se sobrepõe à de 15 dias; vale para quem não caiu na anterior.
