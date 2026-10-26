---
id: regra_246
origem: simulacao/regra_246/entrada.md
gobr: simulacao/regra_246/regra_246.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 11
procedencia: corpus_sintetico
---

## Regras

cliente com cadastro baixado na Receita Federal não é agendado
prospect é atendido a cada 7 dias
cliente do grupo 1 com compra nos últimos 45 dias é atendido a cada 14 dias
cliente inativo do grupo 1 é atendido a cada 7 dias
cliente do grupo 2 com compra nos últimos 60 dias é atendido a cada 21 dias
cliente inativo do grupo 2 é atendido a cada 10 dias
cliente do grupo 3 com compra nos últimos 75 dias é atendido a cada 28 dias
cliente inativo do grupo 3 é atendido a cada 14 dias
cliente do grupo 4 com compra nos últimos 90 dias é atendido a cada 28 dias
cliente inativo do grupo 4 é atendido a cada 14 dias
quem não se enquadrou em nenhuma regra não é agendado

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
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Grupo 1, ativos
    publico: vendedores de televendas ativos, carteira do grupo 1
    se:
      - {tipo: segmento, op: igual_a, valor: ['101009', '101016', '101025', '101101', '101102', '101103', '101104', '101105', '201008', '201009', '201018', '201099']}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 45, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Grupo 1, inativos
    publico: vendedores de televendas ativos, carteira do grupo 1
    se:
      - {tipo: segmento, op: igual_a, valor: ['101009', '101016', '101025', '101101', '101102', '101103', '101104', '101105', '201008', '201009', '201018', '201099']}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Grupo 2, ativos
    publico: vendedores de televendas ativos, carteira do grupo 2
    se:
      - {tipo: segmento, op: igual_a, valor: ['101001', '101002', '101003', '101004', '101005', '101006', '101007', '101011', '101012', '101014', '101015', '101027', '101028', '101029', '101032', '101035', '101037', '101039', '101106', '101107', '201012', '201016', '301001', '301004', '301007', '301015']}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 60, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Grupo 2, inativos
    publico: vendedores de televendas ativos, carteira do grupo 2
    se:
      - {tipo: segmento, op: igual_a, valor: ['101001', '101002', '101003', '101004', '101005', '101006', '101007', '101011', '101012', '101014', '101015', '101027', '101028', '101029', '101032', '101035', '101037', '101039', '101106', '101107', '201012', '201016', '301001', '301004', '301007', '301015']}
    entao: {acao: agendar, frequencia: fixa 10 dias}
  - nome: Grupo 3, ativos
    publico: vendedores de televendas ativos, carteira do grupo 3
    se:
      - {tipo: segmento, op: igual_a, valor: ['101008', '101010', '101017', '101018', '101019', '101020', '101021', '101022', '101023', '101024', '101026', '101031', '101033', '101034', '101036', '101038', '201003', '201004', '201010', '201013', '201014', '201015', '201019', '201022', '201023', '301002', '301005', '301006', '301009', '301010', '301011', '301012', '301013', '301014']}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 75, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 28 dias}
  - nome: Grupo 3, inativos
    publico: vendedores de televendas ativos, carteira do grupo 3
    se:
      - {tipo: segmento, op: igual_a, valor: ['101008', '101010', '101017', '101018', '101019', '101020', '101021', '101022', '101023', '101024', '101026', '101031', '101033', '101034', '101036', '101038', '201003', '201004', '201010', '201013', '201014', '201015', '201019', '201022', '201023', '301002', '301005', '301006', '301009', '301010', '301011', '301012', '301013', '301014']}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Grupo 4, ativos
    publico: vendedores de televendas ativos, carteira do grupo 4
    se:
      - {tipo: segmento, op: igual_a, valor: ['101013', '101040', '102001', '102002', '201011', '201021', '201025', '999999']}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 90, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 28 dias}
  - nome: Grupo 4, inativos
    publico: vendedores de televendas ativos, carteira do grupo 4
    se:
      - {tipo: segmento, op: igual_a, valor: ['101013', '101040', '102001', '102002', '201011', '201021', '201025', '999999']}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Não agendar não enquadrados
    se: []
    entao: {acao: nao_agendar, frequencia: nao_informada}
termos_fora_vocabulario:
  - baixado na Receita Federal
  - carteira livre
  - código de ramo de atividade
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| carteira livre | jargao | agrupamento de clientes por filtro, sem vínculo fixo |
| ramo de atividade | jargao | código de segmento do cliente |
| baixado na Receita | jargao | cadastro encerrado no órgão fiscal |
| prospect | jargao | cliente que nunca comprou |
| VDO | jargao | sigla de tipo de posto de serviço |

## Lacunas

- A entrada não informa se as compras consideram o vendedor ou a empresa.
- A entrada não traz a correspondência entre cada código de ramo e cada atividade nomeada.

## Ambiguidades

- As faixas de códigos indicadas com "a" na entrada (101001 a 101007, 101017 a 101024, 301009 a 301014) foram expandidas código a código na representação estruturada.
- As regras de inativos não trazem critério de tempo; funcionam como residuais de cada grupo.
