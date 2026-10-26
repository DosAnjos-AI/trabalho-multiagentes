---
id: regra_208
origem: simulacao/regra_208/entrada.md
gobr: simulacao/regra_208/regra_208.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 11
procedencia: corpus_sintetico
---

## Regras

cliente com cadastro baixado na Receita Federal não é agendado
cliente inadimplente não é agendado
cliente bloqueado não é agendado
cliente filial não é agendado
prospect com o vendedor é atendido a cada 7 dias
cliente com uma única compra com o vendedor é atendido a cada 14 dias
cliente que comprou no mês e tem intervalo histórico entre 90 e 120 dias é atendido a cada 14 dias
cliente com compra nos últimos 30 dias é atendido a cada 14 dias
cliente com compra nos últimos 89 dias é atendido a cada 7 dias
cliente com compra em até 120 dias é atendido a cada 3 dias
clientes não mapeados nas regras não são agendados

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
  - nome: Não agendar bloqueados
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: bloqueado}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar filiais
    se:
      - {tipo: segmento, op: igual_a, valor: filial}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Ativação de novos
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Relacionamento com compra única
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Contato com quem comprou no mês
    se:
      - {tipo: tempo_sem_comprar, op: igual_a, valor: mês atual, unidade: periodo_nomeado}
      - {tipo: tempo_sem_comprar, op: entre, valor: [90, 120], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Manter regularidade
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Evitar inatividade
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 89, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Resgatar inativo
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 120, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 3 dias}
  - nome: Não agendar os não mapeados
    se: []
    entao: {acao: nao_agendar, frequencia: nao_informada}
termos_fora_vocabulario:
  - baixado na Receita Federal
  - bloqueado
  - filial
  - frequência histórica de compra
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| baixado na Receita | jargao | cadastro encerrado no órgão fiscal |
| bloqueado | jargao | cliente com cadastro bloqueado |
| filial | jargao | unidade filial de um cliente |
| frequência histórica | jargao | intervalo médio entre compras |

## Lacunas

- A entrada não informa se as compras consideram o vendedor ou a empresa.

## Ambiguidades

- As faixas "nos últimos 30", "89" e "até 120 dias" se sobrepõem; cada uma vale para quem não caiu na anterior.
- O resgate de inativos tem a frequência mais curta (3 dias), mantida como declarada.
