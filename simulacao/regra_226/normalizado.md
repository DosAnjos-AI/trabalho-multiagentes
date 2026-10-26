---
id: regra_226
origem: simulacao/regra_226/entrada.md
gobr: simulacao/regra_226/regra_226.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 6
procedencia: corpus_sintetico
---

## Regras

cliente sem venda com a empresa é atendido a cada 7 dias
cliente com uma única compra com a empresa e compra nos últimos 30 dias é atendido a cada 14 dias
cliente com intervalo histórico de 30 dias e compra nos últimos 120 dias é atendido a cada 28 dias
cliente com última compra com o vendedor entre 20 e 30 dias usa o histórico, com máximo de 60 dias
cliente sem compra com a empresa há mais de 120 dias é atendido a cada 14 dias
cliente sem compra há mais de 180 dias é atendido a cada 28 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Ativar oportunidade
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Cliente ativado
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única, alcance: empresa}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Compra mensal
    se:
      - {tipo: tempo_sem_comprar, op: igual_a, valor: 30, unidade: dias}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 120, unidade: dias, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 28 dias}
  - nome: Compra mês sim, mês não
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [20, 30], unidade: dias, alcance: vendedor}
    entao: {acao: agendar, frequencia: calculada}
  - nome: Manter cliente ativo
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 120, unidade: dias, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Resgate de inativo
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 180, unidade: dias, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 28 dias}
termos_fora_vocabulario:
  - frequência histórica de compra
  - frequência pelo histórico com teto
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| ativado | jargao | cliente que fez a primeira compra |
| frequência histórica | jargao | intervalo médio entre compras |
| resgate | jargao | reativação de cliente inativo |

## Lacunas

- A entrada não traz regra residual para clientes fora das faixas descritas.

## Ambiguidades

- A regra de mais de 120 dias sem compra vem antes da de mais de 180 dias e abrange os mesmos clientes; a regra de 180 dias pode nunca ser alcançada, dependendo da ordem de avaliação.
- O teto de 60 dias da frequência pelo histórico não tem campo próprio e foi registrado apenas na descrição.
