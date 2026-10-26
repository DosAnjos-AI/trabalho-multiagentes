---
id: regra_221
origem: simulacao/regra_221/entrada.md
gobr: simulacao/regra_221/regra_221.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 6
procedencia: corpus_sintetico
---

## Regras

cliente sem venda com o vendedor é atendido a cada 21 dias, preferindo dia útil e sábado
cliente com uma única compra e sem compra nos últimos 30 dias é atendido a cada 14 dias
cliente com compra nos últimos 30 dias e sem compra nos últimos 21 é atendido a cada 14 dias
cliente sem compra entre 31 e 60 dias é atendido a cada 14 dias
cliente sem compra entre 61 e 90 dias é atendido a cada 7 dias
cliente sem compra entre 91 e 360 dias, caso tenha perfil, é atendido a cada 28 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns:
  - {tipo: periodo_vigencia, op: igual_a, valor: [dias úteis, sábado], unidade: periodo_nomeado}
regras:
  - nome: Pré-qualificado sem venda
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou, alcance: vendedor}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Cliente ativado
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única, alcance: vendedor}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 30, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Compra regular e bom histórico
    se:
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 21, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Estimular regularidade
    se:
      - {tipo: tempo_sem_comprar, op: fora_de, valor: [31, 60], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Deixando de comprar
    se:
      - {tipo: tempo_sem_comprar, op: fora_de, valor: [61, 90], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Resgate
    se:
      - {tipo: tempo_sem_comprar, op: fora_de, valor: [91, 360], unidade: dias}
    entao: {acao: agendar, frequencia: fixa 28 dias}
termos_fora_vocabulario:
  - preferência por dia útil e sábado
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| pré-qualificado | jargao | contato avaliado como cliente potencial |
| perfil | jargao | adequação do cliente ao público-alvo |

## Lacunas

- A entrada não define o que é "ter perfil" na regra de resgate.

## Ambiguidades

- "Sem compra entre X e Y dias" foi registrado como ausência de compra na janela (fora_de).
