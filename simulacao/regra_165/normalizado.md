---
id: regra_165
origem: simulacao/regra_165/entrada.md
gobr: simulacao/regra_165/regra_165.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 7
procedencia: corpus_sintetico
---

## Regras

cliente inativo com a empresa e inadimplente não é agendado
cliente sem compra há mais de 90 dias é atendido a cada 7 dias
cliente do grupo com intervalo histórico de 1 a 7 dias e sem compra entre 8 e 15 dias é atendido a cada 14 dias
cliente do grupo com intervalo histórico de 16 a 30 dias e sem compra entre 31 e 45 dias é atendido a cada 28 dias
cliente do grupo com intervalo histórico de 31 a 45 dias e sem compra entre 46 e 60 dias é atendido a cada 21 dias
cliente do grupo com intervalo histórico de 61 a 90 dias e sem compra há 90 dias é atendido a cada 15 dias
cliente que não se encaixe em nenhuma regra não é agendado

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Não agendar inativos inadimplentes
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: inativo, alcance: empresa}
      - {tipo: situacao_financeira, op: igual_a, valor: inadimplente}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Sem compra há mais de 90 dias
    se:
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 90, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Grupo de 1 a 7 dias
    se:
      - {tipo: carteira, op: igual_a, valor: grupo de 1 a 7 dias, alcance: outro_vendedor}
      - {tipo: tempo_sem_comprar, op: fora_de, valor: [8, 15], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Grupo de 16 a 30 dias
    se:
      - {tipo: carteira, op: igual_a, valor: grupo de 16 a 30 dias, alcance: outro_vendedor}
      - {tipo: tempo_sem_comprar, op: fora_de, valor: [31, 45], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 28 dias}
  - nome: Grupo de 31 a 45 dias
    se:
      - {tipo: carteira, op: igual_a, valor: grupo de 31 a 45 dias, alcance: outro_vendedor}
      - {tipo: tempo_sem_comprar, op: fora_de, valor: [46, 60], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Grupo de 61 a 90 dias
    se:
      - {tipo: carteira, op: igual_a, valor: grupo de 61 a 90 dias, alcance: outro_vendedor}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 90, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 15 dias}
  - nome: Não agendar os demais
    se: []
    entao: {acao: nao_agendar, frequencia: nao_informada}
termos_fora_vocabulario:
  - grupo auxiliar por intervalo histórico de compra
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Chegatto | empresa_foco | EMPRESA_FOCO |
| televendas | jargao | atendimento por telefone |
| campo | jargao | atendimento presencial |
| grupo auxiliar | jargao | conjunto de clientes definido para uso em regras |
| frequência histórica | jargao | intervalo médio entre pedidos |
| inadimplente | jargao | cliente com pendência financeira em aberto |

## Lacunas

- A entrada não traz regras para o time de campo; ele só fornece os grupos auxiliares.
- Não há grupo para intervalo histórico entre 8 e 15 dias nem entre 46 e 60 dias.

## Ambiguidades

- "Sem compra entre X e Y dias" foi registrado como ausência de compra na janela (fora_de); pode ser lido como última compra nessa faixa.
