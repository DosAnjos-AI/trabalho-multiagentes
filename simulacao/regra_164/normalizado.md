---
id: regra_164
origem: simulacao/regra_164/entrada.md
gobr: simulacao/regra_164/regra_164.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 17
procedencia: corpus_sintetico
---

## Regras

cliente com rótulo condomínio cadastrado a partir de 3 de outubro de 2024 é atendido a cada 14 dias
cliente com rótulo condomínio e compra com a empresa nos últimos 30 dias é atendido a cada 7 dias
cliente com rótulo condomínio sem compra com a empresa há mais de 90 dias é atendido a cada 30 dias
prospect sem venda cadastrado a partir de 1º de agosto de 2024 é atendido a cada 7 dias
construtora com uma única compra e sem compra há mais de 60 dias é atendida a cada 14 dias
construtora do Rio de Janeiro, curva A, com intervalo histórico menor que 30 dias e sem compra há mais de 14 dias, é atendida a cada 7 dias
construtora do Rio de Janeiro, curva B, com intervalo histórico menor que 30 dias e sem compra há mais de 14 dias, é atendida a cada 10 dias
construtora do Rio de Janeiro, curva C, com intervalo histórico menor que 30 dias e sem compra há mais de 14 dias, é atendida a cada 14 dias
construtora com intervalo histórico menor que 30 dias e sem compra há mais de 14 dias é atendida a cada 14 dias
construtora ativa com a empresa e sem compra há mais de 45 dias é atendida a cada 10 dias
construtora sem compra há mais de 60 dias é atendida a cada 14 dias
construtora cadastrada a partir de 3 de outubro de 2024 é atendida a cada 7 dias
as demais construtoras são atendidas a cada 45 dias
clientes dos rótulos listados cadastrados a partir de 3 de outubro de 2024 são atendidos a cada 14 dias
clientes dos rótulos listados com compra com a empresa nos últimos 30 dias são atendidos a cada 7 dias
regra que também consta para a mesma situação, com frequência de 30 dias
qualquer cliente não coberto por regra comercial não é agendado

## Estrutura

```yaml
publico: todos os vendedores ativos e time exclusivo de VENDEDOR_01
comuns: []
regras:
  - nome: Condomínio de VENDEDOR_01, novos cadastros
    publico: VENDEDOR_01
    se:
      - {tipo: segmento, op: igual_a, valor: [condomínio]}
      - {tipo: situacao_cadastro, op: igual_a, valor: a partir de 3 de outubro de 2024, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Condomínio de VENDEDOR_01, compra recente
    publico: VENDEDOR_01
    se:
      - {tipo: segmento, op: igual_a, valor: [condomínio]}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Condomínio de VENDEDOR_01, sem compra há mais de 90 dias
    publico: VENDEDOR_01
    se:
      - {tipo: segmento, op: igual_a, valor: [condomínio]}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 90, unidade: dias, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Ativar prospects
    publico: todos os vendedores ativos
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
      - {tipo: situacao_cadastro, op: igual_a, valor: a partir de 1º de agosto de 2024, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Construtoras, boas-vindas
    publico: todos os vendedores ativos
    se:
      - {tipo: segmento, op: igual_a, valor: [construtora]}
      - {tipo: estagio_relacionamento, op: igual_a, valor: compra única}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 60, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Construtoras, compra regular no Rio de Janeiro, curva A
    publico: todos os vendedores ativos
    se:
      - {tipo: segmento, op: igual_a, valor: [construtora]}
      - {tipo: tempo_sem_comprar, op: menor_que, valor: 30, unidade: dias}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 14, unidade: dias}
      - {tipo: localizacao, op: igual_a, valor: [RJ]}
      - {tipo: valor_cliente, op: igual_a, valor: curva A}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Construtoras, compra regular no Rio de Janeiro, curva B
    publico: todos os vendedores ativos
    se:
      - {tipo: segmento, op: igual_a, valor: [construtora]}
      - {tipo: tempo_sem_comprar, op: menor_que, valor: 30, unidade: dias}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 14, unidade: dias}
      - {tipo: localizacao, op: igual_a, valor: [RJ]}
      - {tipo: valor_cliente, op: igual_a, valor: curva B}
    entao: {acao: agendar, frequencia: fixa 10 dias}
  - nome: Construtoras, compra regular no Rio de Janeiro, curva C
    publico: todos os vendedores ativos
    se:
      - {tipo: segmento, op: igual_a, valor: [construtora]}
      - {tipo: tempo_sem_comprar, op: menor_que, valor: 30, unidade: dias}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 14, unidade: dias}
      - {tipo: localizacao, op: igual_a, valor: [RJ]}
      - {tipo: valor_cliente, op: igual_a, valor: curva C}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Construtoras, compra regular nas demais UFs
    publico: todos os vendedores ativos
    se:
      - {tipo: segmento, op: igual_a, valor: [construtora]}
      - {tipo: tempo_sem_comprar, op: menor_que, valor: 30, unidade: dias}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 14, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Construtoras, estimular regularidade
    publico: todos os vendedores ativos
    se:
      - {tipo: segmento, op: igual_a, valor: [construtora]}
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo, alcance: empresa}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 45, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 10 dias}
  - nome: Construtoras, risco de ficar inativo
    publico: todos os vendedores ativos
    se:
      - {tipo: segmento, op: igual_a, valor: [construtora]}
      - {tipo: tempo_sem_comprar, op: maior_que, valor: 60, unidade: dias}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Construtoras, ativar novos clientes
    publico: todos os vendedores ativos
    se:
      - {tipo: segmento, op: igual_a, valor: [construtora]}
      - {tipo: situacao_cadastro, op: igual_a, valor: a partir de 3 de outubro de 2024, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Construtoras, resgate de inativos
    publico: todos os vendedores ativos
    se:
      - {tipo: segmento, op: igual_a, valor: [construtora]}
    entao: {acao: agendar, frequencia: fixa 45 dias}
  - nome: Demais rótulos, novos cadastros
    publico: todos os vendedores ativos
    se:
      - {tipo: segmento, op: igual_a, valor: [shopping, supermercado, indústria, estaleiro, clube, escolas, universidade, igreja, hotel, hospital, clínica, restaurantes, condomínio]}
      - {tipo: situacao_cadastro, op: igual_a, valor: a partir de 3 de outubro de 2024, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Demais rótulos, compra recente a cada 7 dias
    publico: todos os vendedores ativos
    se:
      - {tipo: segmento, op: igual_a, valor: [shopping, supermercado, indústria, estaleiro, clube, escolas, universidade, igreja, hotel, hospital, clínica, restaurantes, condomínio]}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Demais rótulos, compra recente a cada 30 dias
    publico: todos os vendedores ativos
    se:
      - {tipo: segmento, op: igual_a, valor: [shopping, supermercado, indústria, estaleiro, clube, escolas, universidade, igreja, hotel, hospital, clínica, restaurantes, condomínio]}
      - {tipo: tempo_sem_comprar, op: dentro_de, valor: 30, unidade: dias, alcance: empresa}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Não agendar clientes não cobertos
    publico: todos os vendedores ativos
    se: []
    entao: {acao: nao_agendar, frequencia: nao_informada}
termos_fora_vocabulario:
  - rótulo do cliente
  - data de cadastro a partir de dia específico
  - frequência histórica de compra
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Isocom | empresa_foco | EMPRESA_FOCO |
| Bruna, ID 10bruna | vendedor | VENDEDOR_01 |
| rótulo | jargao | etiqueta de segmentação do cliente |
| curva A, B e C | jargao | faixas de cliente por faturamento |
| frequência histórica | jargao | intervalo médio entre compras |
| prospect | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não define os critérios das curvas A, B e C.

## Ambiguidades

- Há duas regras para a mesma situação (rótulos listados com compra nos últimos 30 dias), com 7 e 30 dias; a segunda nunca é alcançada se as regras forem avaliadas em ordem.
- O rótulo condomínio aparece tanto no time de VENDEDOR_01 quanto na lista geral.
