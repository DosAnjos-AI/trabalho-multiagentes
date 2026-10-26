---
id: regra_188
origem: simulacao/regra_188/entrada.md
gobr: simulacao/regra_188/regra_188.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 8
procedencia: corpus_sintetico
---

## Regras

cliente inadimplente não é agendado
cliente filial não é agendado
cliente com cadastro baixado na Receita Federal não é agendado
cliente sem venda com o vendedor é atendido a cada 21 dias
cliente com compra nos últimos 30 dias usa o histórico, entre 7 e 30 dias
cliente sem compra entre 31 e 45 dias é atendido a cada 14 dias
cliente sem compra entre 46 e 60 dias é atendido a cada 7 dias
os demais clientes, caso tenham perfil, são atendidos a cada 14 dias

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
  - nome: Não agendar baixados na Receita Federal
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: baixado na Receita Federal}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Pré-qualificado sem venda
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Compra regular e bom histórico
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Estimular regularidade
    se:
      - {tipo: tempo_sem_comprar, op: fora_de, valor: [31, 45], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Deixando de comprar
    se:
      - {tipo: tempo_sem_comprar, op: fora_de, valor: [46, 60], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Resgate dos demais
    se: []
    entao: {acao: agendar, frequencia: fixa 14 dias}
termos_fora_vocabulario:
  - filial
  - baixado na Receita Federal
  - frequência pelo histórico com mínimo e máximo
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| filial | jargao | unidade filial de um cliente |
| baixado na Receita | jargao | cadastro encerrado no órgão fiscal |
| pré-qualificado | jargao | contato avaliado como cliente potencial |
| perfil | jargao | adequação do cliente ao público-alvo |

## Lacunas

- A entrada não define o que é "ter perfil" na regra de resgate.

## Ambiguidades

- "Sem compra entre X e Y dias" foi registrado como ausência de compra na janela (fora_de).
- Os limites de 7 e 30 dias da frequência pelo histórico não têm campo próprio e foram registrados apenas na descrição.
