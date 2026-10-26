---
id: regra_154
origem: simulacao/regra_154/entrada.md
gobr: simulacao/regra_154/regra_154.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 14
procedencia: corpus_sintetico
---

## Regras

clientes das cidades da rota de segunda são atendidos semanalmente, na segunda, com frequência fixa
clientes das cidades da rota de terça são atendidos semanalmente, na terça, com frequência fixa
clientes das cidades da rota de quarta são atendidos semanalmente, na quarta, com frequência fixa
clientes das cidades da rota de quinta são atendidos semanalmente, na quinta, com frequência fixa
clientes de Brusque são atendidos semanalmente, na segunda, terça ou sexta
clientes de Nova Trento são atendidos semanalmente, na terça ou sexta
clientes de Guaramirim, Jaraguá do Sul, Joinville e Schroeder são atendidos semanalmente, na segunda ou quinta
clientes de Barra Velha, Navegantes, Penha e Balneário Piçarras são atendidos semanalmente, na terça ou quinta
clientes das cidades sem dia definido são atendidos semanalmente
prospect que não caiu nas rotas é atendido a cada 30 dias
ativo de curva A é atendido a cada 14 dias
ativo de curva B é atendido a cada 21 dias
os demais ativos são atendidos a cada 28 dias
inativos são atendidos a cada 30 dias

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Rota fixa de segunda-feira
    se:
      - {tipo: localizacao, op: igual_a, valor: [Balneário Barra do Sul, Bela Vista, Campo Alegre, Canoinhas, Corupá, Itaiópolis, Mafra, Major Vieira, Monte Castelo, Papanduva, Porto União, Rio Negrinho, São Bento do Sul, Três Barras]}
      - {tipo: periodo_vigencia, op: igual_a, valor: segunda, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rota fixa de terça-feira
    se:
      - {tipo: localizacao, op: igual_a, valor: [Apiúna, Ascurra, Benedito Novo, Blumenau, Doutor Pedrinho, Gaspar, Ibirama, Indaial, Pomerode, Presidente Getúlio, Rio dos Cedros, Timbó]}
      - {tipo: periodo_vigencia, op: igual_a, valor: terça, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rota fixa de quarta-feira
    se:
      - {tipo: localizacao, op: igual_a, valor: [Araranguá, Biguaçu, Braço do Norte, Capivari de Baixo, Cocal do Sul, Criciúma, Florianópolis, Forquilhinha, Gravatal, Içara, Imbituba, Jaguaruna, Laguna, Luiz Alves, Morro da Fumaça, Orleans, Palhoça, Paulo Lopes, Pedras Grandes, Pescaria Brava, Praia Grande, Sangão, Santa Rosa do Sul, São João do Sul, São José, São Ludgero, Sombrio, Tubarão, Urussanga]}
      - {tipo: periodo_vigencia, op: igual_a, valor: quarta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rota fixa de quinta-feira
    se:
      - {tipo: localizacao, op: igual_a, valor: [Araquari, Massaranduba, Pirabeiraba, São João do Itaperiú]}
      - {tipo: periodo_vigencia, op: igual_a, valor: quinta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rota dinâmica de segunda, terça ou sexta
    se:
      - {tipo: localizacao, op: igual_a, valor: [Brusque]}
      - {tipo: periodo_vigencia, op: igual_a, valor: [segunda, terça, sexta], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rota dinâmica de terça ou sexta
    se:
      - {tipo: localizacao, op: igual_a, valor: [Nova Trento]}
      - {tipo: periodo_vigencia, op: igual_a, valor: [terça, sexta], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rota dinâmica de segunda ou quinta
    se:
      - {tipo: localizacao, op: igual_a, valor: [Guaramirim, Jaraguá do Sul, Joinville, Schroeder]}
      - {tipo: periodo_vigencia, op: igual_a, valor: [segunda, quinta], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rota dinâmica de terça ou quinta
    se:
      - {tipo: localizacao, op: igual_a, valor: [Barra Velha, Navegantes, Penha, Balneário Piçarras]}
      - {tipo: periodo_vigencia, op: igual_a, valor: [terça, quinta], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Rota de dias variados
    se:
      - {tipo: localizacao, op: igual_a, valor: [Balneário Camboriú, Camboriú, Canelinha, Itajaí, Itapema, Porto Belo, São João Batista, Tijucas]}
    entao: {acao: agendar, frequencia: fixa 7 dias}
  - nome: Prospects fora das rotas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: nunca comprou}
    entao: {acao: agendar, frequencia: fixa 30 dias}
  - nome: Ativos curva A fora das rotas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: valor_cliente, op: igual_a, valor: curva A}
    entao: {acao: agendar, frequencia: fixa 14 dias}
  - nome: Ativos curva B fora das rotas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
      - {tipo: valor_cliente, op: igual_a, valor: curva B}
    entao: {acao: agendar, frequencia: fixa 21 dias}
  - nome: Demais ativos fora das rotas
    se:
      - {tipo: estagio_relacionamento, op: igual_a, valor: ativo}
    entao: {acao: agendar, frequencia: fixa 28 dias}
  - nome: Inativos fora das rotas
    se: []
    entao: {acao: agendar, frequencia: fixa 30 dias}
termos_fora_vocabulario:
  - rota fixa por cidade
  - preferência de dias da semana
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| Binatti Itapema | empresa_foco | EMPRESA_FOCO |
| televendas | jargao | atendimento por telefone |
| rota fixa | jargao | dia de atendimento fixo e travado |
| rota dinâmica | jargao | dias de atendimento preferenciais, sem trava |
| curva A, B e C | jargao | faixas de cliente por faturamento |
| prospect | jargao | cliente que nunca comprou |

## Lacunas

- A entrada não define os critérios das curvas A e B.

## Ambiguidades

- A distinção entre rota fixa e rota dinâmica é a trava da frequência, que não tem campo próprio; ambas aparecem com frequência fixa de 7 dias.
- "Semanal" foi registrado como 7 dias pela convenção de periodicidade; a entrada não dá o número para as rotas.
