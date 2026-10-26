---
id: regra_243
origem: simulacao/regra_243/entrada.md
gobr: simulacao/regra_243/regra_243.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 5
procedencia: corpus_sintetico
---

## Regras

cliente pessoa jurídica sem venda é atendido a cada 21 dias, preferindo dia útil e sábado
cliente pessoa jurídica com compra nos últimos 20 dias é atendido a cada 3 dias, preferindo dia útil e sábado
cliente pessoa jurídica com compra entre 20 e 33 dias usa o histórico acrescido de 2 dias, entre 20 e 33 dias, preferindo dia útil e sábado
cliente pessoa jurídica sem compra em 33 dias não é agendado
cliente que não é pessoa jurídica não é agendado

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Ativar cliente
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
      - {tipo: situacao_cadastro, op: igual_a, valor: pessoa jurídica}
      - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Pós-venda
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 20, unidade: dias}
      - {tipo: situacao_cadastro, op: igual_a, valor: pessoa jurídica}
      - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 3 dias}
  - nome: Manter o cliente engajado
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [20, 33], unidade: dias}
      - {tipo: situacao_cadastro, op: igual_a, valor: pessoa jurídica}
      - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Não agendar sem compra em 33 dias
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: pessoa jurídica}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar quem não é pessoa jurídica
    se: []
    entao: {acao: nao_agendar, frequencia: nao_informada}
termos_fora_vocabulario:
  - frequência pelo histórico com acréscimo
  - preferência por dia útil e sábado
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| pessoa jurídica | jargao | cliente com cadastro de empresa |
| pós-venda | jargao | contato logo após a compra |

## Lacunas

- A entrada não informa se as compras consideram o vendedor ou a empresa.

## Ambiguidades

- O acréscimo de 2 dias e os limites de 20 e 33 dias da frequência pelo histórico foram registrados apenas na descrição.
- A regra de não agendar pessoa jurídica sem compra em 33 dias não traz critério explícito de tempo; funciona como residual dos clientes pessoa jurídica.
