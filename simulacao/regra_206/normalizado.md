---
id: regra_206
origem: simulacao/regra_206/entrada.md
gobr: simulacao/regra_206/regra_206.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 12
procedencia: corpus_sintetico
---

## Regras

cliente filial não é agendado
cliente inadimplente não é agendado
prospect não é agendado
cliente dos ramos 1, 2, 4 e 12 com compra nos últimos 90 dias é atendido a cada 7 dias
transportadora com compra nos últimos 90 dias é atendida a cada 15 dias
cliente de segmento não especificado com compra nos últimos 90 dias é atendido a cada 28 dias
cliente dos ramos 1, 2, 4 e 12 com compra entre 91 e 180 dias é atendido a cada 7 dias
transportadora com compra entre 91 e 180 dias é atendida a cada 15 dias
cliente de segmento não especificado com compra entre 91 e 180 dias é atendido a cada 28 dias
contato ou prospect dos ramos 1, 2, 4 e 12 é atendido a cada 7 dias
contato ou prospect de transportadora é atendido a cada 15 dias
contato ou prospect de segmento não especificado é atendido a cada 28 dias

## Estrutura

```yaml
publico: time de ativo e inativo e time de prospecção
comuns: []
regras:
  - nome: Não agendar filiais
    publico: os dois times
    se:
      - {tipo: segmento, op: igual_a, valor: filial}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar inadimplentes
    publico: os dois times
    se:
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar prospects no time de ativo e inativo
    publico: time de ativo e inativo, televendas ativos exceto VENDEDOR_01
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Compra em 90 dias, ramos 1, 2, 4 e 12
    publico: time de ativo e inativo, televendas ativos exceto VENDEDOR_01
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 90, unidade: dias, alcance: empresa}
      - {tipo: segmento, op: igual_a, valor: ['1', '2', '4', '12']}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Compra em 90 dias, transportadora
    publico: time de ativo e inativo, televendas ativos exceto VENDEDOR_01
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 90, unidade: dias, alcance: empresa}
      - {tipo: segmento, op: igual_a, valor: ['3']}
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Compra em 90 dias, segmentos não especificados
    publico: time de ativo e inativo, televendas ativos exceto VENDEDOR_01
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 90, unidade: dias, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 28 dias}
  - nome: Clientes em risco, ramos 1, 2, 4 e 12
    publico: time de ativo e inativo, televendas ativos exceto VENDEDOR_01
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [91, 180], unidade: dias, alcance: empresa}
      - {tipo: segmento, op: igual_a, valor: ['1', '2', '4', '12']}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Clientes em risco, transportadora
    publico: time de ativo e inativo, televendas ativos exceto VENDEDOR_01
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [91, 180], unidade: dias, alcance: empresa}
      - {tipo: segmento, op: igual_a, valor: ['3']}
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Clientes em risco, segmentos não especificados
    publico: time de ativo e inativo, televendas ativos exceto VENDEDOR_01
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [91, 180], unidade: dias, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 28 dias}
  - nome: Prospecção, ramos 1, 2, 4 e 12
    publico: time de prospecção, VENDEDOR_01
    se:
      - {tipo: segmento, op: igual_a, valor: ['1', '2', '4', '12']}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Prospecção, transportadora
    publico: time de prospecção, VENDEDOR_01
    se:
      - {tipo: segmento, op: igual_a, valor: ['3']}
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Prospecção, segmentos não especificados
    publico: time de prospecção, VENDEDOR_01
    se: []
    entao: {acao: agendar, frequencia: fixa 28 dias}
termos_fora_vocabulario:
  - filial
  - carteira livre por faixa de compra
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| vendedor 135 | vendedor | VENDEDOR_01 |
| televendas | jargao | atendimento por telefone |
| carteira livre | jargao | conjunto de clientes compartilhado |
| lead | jargao | contato comercial potencial |
| filial | jargao | unidade filial de um cliente |
| ramo de atividade | jargao | segmento do cliente |

## Lacunas

- Clientes sem compra há mais de 180 dias não têm regra declarada no time de ativo e inativo.

## Ambiguidades

- O time de prospecção atende contatos e prospects, mas as regras desse time não trazem critério explícito de estágio de relacionamento.
