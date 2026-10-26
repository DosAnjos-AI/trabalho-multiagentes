---
id: regra_248
origem: simulacao/regra_248/entrada.md
gobr: simulacao/regra_248/regra_248.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 10
procedencia: corpus_real
---

## Regras

cliente com cadastro baixado na Receita Federal não é agendado
cliente inadimplente não é agendado
cliente com data de rota marcada na semana não é agendado
prospect que nunca fez pedido com a empresa é atendido a cada 14 dias
cliente com compra nos últimos 60 dias é atendido a cada 14 dias
cliente com compra em até 90 dias é atendido a cada 7 dias
cliente com compra em até 120 dias é atendido a cada 14 dias
cliente com compra em até 150 dias é atendido a cada 21 dias
cliente com compra em até 180 dias é atendido a cada 28 dias
cliente que não se enquadrou em nenhuma regra não é agendado

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Não agendar baixados na Receita Federal
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: baixado na Receita Federal}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar inadimplentes
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar com rota na semana
    se:
      - {tipo: agenda_rota, op: igual_a, valor: semana atual, unidade: periodo_nomeado}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Prospects
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Ativos
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 60, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Risco de inatividade
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 90, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Inativos, compra nos últimos 120 dias
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 120, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Inativos, compra nos últimos 150 dias
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 150, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Inativos, compra nos últimos 180 dias
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 180, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 28 dias}
  - nome: Não agendar os demais
    se: []
    entao: {acao: nao_agendar, frequencia: nao_informada}
termos_fora_vocabulario:
  - baixado na Receita Federal
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| baixado na Receita | jargao | cadastro encerrado no órgão fiscal |
| rota | jargao | roteiro de visitas programado |
| prospect | jargao | cliente que nunca comprou |
| Govendas | jargao | plataforma de vendas |

## Lacunas

- A entrada não informa se as compras consideram o vendedor ou a empresa.
- A entrada não informa a origem do pedido.

## Ambiguidades

- As faixas de 90, 120, 150 e 180 dias se sobrepõem; entende-se que cada uma vale para quem não caiu na anterior.
