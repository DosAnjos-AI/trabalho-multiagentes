---
id: regra_003
origem: simulacao/regra_003/entrada.md
gobr: simulacao/regra_003/regra_003.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 12
procedencia: corpus_sintetico
---

## Regras

cliente filial não entra na agenda
cliente visitado pelo representante externo na semana anterior não entra na agenda
cliente com rota programada com o representante externo nos próximos 7 dias não entra na agenda
cliente que comprou nos últimos 7 dias com qualquer vendedor não entra na agenda
prospect que nunca fez pedido é atendido a cada 14 dias
cliente cadastrado há mais de 60 dias com uma única compra com o vendedor é atendido a cada 14 dias
cliente com pedido entre 7 e 30 dias atrás é atendido a cada 14 dias
cliente com último pedido entre 31 e 60 dias atrás é atendido a cada 7 dias
cliente com último pedido entre 61 e 90 dias atrás é prioridade máxima e é atendido a cada 3 dias
cliente que comprou nos últimos 14 dias sem ter comprado entre 15 e 90 dias atrás é atendido a cada 14 dias
cliente sem compra há mais de 90 dias é atendido a cada 14 dias
cliente que não se enquadrou nas regras anteriores é atendido a cada 21 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Não agendar filiais
    se:
      - {tipo: segmento, op: igual_a, valor: filial}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar clientes visitados pelo externo na semana anterior
    se:
      - {tipo: tempo_sem_visita, op: igual_a, valor: semana anterior, unidade: periodo_nomeado, alcance: outro_vendedor}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar clientes com rota do externo nos próximos 7 dias
    se:
      - {tipo: agenda_rota, op: dentro_de, valor: 7, unidade: dias, alcance: outro_vendedor}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar clientes com compra nos últimos 7 dias
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 7, unidade: dias, alcance: empresa}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Ativar prospect que nunca fez pedido
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Prospect ativado com compra única
    se:
      - {tipo: situacao_cadastro, op: maior_que, valor: 60, unidade: dias}
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Manter regularidade de quem comprou entre 7 e 30 dias
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [7, 30], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Garantir relacionamento de quem comprou entre 31 e 60 dias
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [31, 60], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Cliente prestes a inativar
    se:
      - {tipo: tempo_sem_comprar, op: entre, valor: [61, 90], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 3 dias}
  - nome: Cliente reativado
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 14, unidade: dias}
      - {tipo: tempo_sem_comprar, op: fora_de, valor: [15, 90], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Ativar cliente inativo
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 90, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Regra genérica
    se: []
    entao: {acao: agendar, frequencia: fixa 21 dias}
termos_fora_vocabulario:
  - filial
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Govendas | jargao | plataforma de vendas |
| televendas | jargao | atendimento por telefone |
| representante externo | jargao | vendedor de campo |
| prospect | jargao | cliente que nunca comprou |
| filial | jargao | unidade filial de um cliente |
| rota | jargao | roteiro de visitas programado |

## Lacunas

- A entrada não informa se as janelas de compra das frequências (7 a 30, 31 a 60, 61 a 90, reativado e inativo) consideram compras com o vendedor ou com qualquer vendedor da empresa; só a exclusão de 7 dias declara "qualquer vendedor".

## Ambiguidades

- "Prospect que foi ativado" é descrito como cadastrado há mais de 60 dias, o que pode ser lido como tempo mínimo ou como referência aproximada de cadastro.
- A faixa "entre 7 e 30 dias" se sobrepõe ao limite de 7 dias da exclusão de compra recente.
