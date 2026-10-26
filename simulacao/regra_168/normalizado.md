---
id: regra_168
origem: simulacao/regra_168/entrada.md
gobr: simulacao/regra_168/regra_168.gobr
tipo_input: texto_corrido
versao_padrao: 4.0
total_regras: 8
procedencia: corpus_sintetico
---

## Regras

cliente com cadastro baixado na Receita Federal não é agendado
cliente bloqueado não é agendado
clientes da rota de todo dia são agendados diariamente, com preferência máxima de segunda a sexta, roteirizável e fixo
clientes da rota de terça são agendados na segunda, diariamente, roteirizável e fixo
clientes da rota de quarta são agendados na terça, diariamente, roteirizável e fixo
clientes da rota de quinta são agendados na quarta, diariamente, roteirizável e fixo
clientes da rota de sexta são agendados na quinta, diariamente, roteirizável e fixo
cliente que não se enquadrou nas regras do dia não é agendado

## Estrutura

```yaml
publico: vendedores de televendas ativos
comuns: []
regras:
  - nome: Não agendar baixados na Receita Federal
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: baixado na Receita Federal}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Não agendar bloqueados
    se:
      - {tipo: situacao_cadastro, op: igual_a, valor: bloqueado}
    entao: {acao: nao_agendar, frequencia: nao_informada}
  - nome: Rota de todo dia
    se:
      - {tipo: localizacao, op: igual_a, valor: [Balneário Camboriú, Bombinhas, Camboriú, Itajaí, Itapema, Porto Belo]}
      - {tipo: periodo_vigencia, op: igual_a, valor: [segunda, terça, quarta, quinta, sexta], unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 1 dias}
  - nome: Rota de terça, agendada na segunda
    se:
      - {tipo: localizacao, op: igual_a, valor: [Cascavel, Lages, Bom Retiro, São Joaquim, Biguaçu, Blumenau, Brusque, Florianópolis, Governador Celso Ramos, Guabiruba, Ibirama, Palhoça, Pomerode, Rio do Sul, São José, Tijucas, Luiz Alves, Gaspar, Indaial, Botuvera, Ilhota, Rio dos Cedros]}
      - {tipo: periodo_vigencia, op: igual_a, valor: segunda, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 1 dias}
  - nome: Rota de quarta, agendada na terça
    se:
      - {tipo: localizacao, op: igual_a, valor: [Irati, Ponta Grossa, Fernandes Pinheiro, Teixeira Soares, Araucária, Curitiba, São José dos Pinhais, Piraquara, Colombo, Pinhais, Campo Largo, Jaraguá do Sul, Balneário Barra do Sul, Balneário Piçarras, Campo Alegre, Joinville, Navegantes, Penha, Pouso Redondo, Corupá, Guaramirim, São Bento do Sul, Barra Velha, Schroeder, Rebouças, Rio Azul]}
      - {tipo: periodo_vigencia, op: igual_a, valor: terça, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 1 dias}
  - nome: Rota de quinta, agendada na quarta
    se:
      - {tipo: localizacao, op: igual_a, valor: [Bento Gonçalves, Cachoeirinha, Campo Bom, Canoas, Capão da Canoa, Caxias do Sul, Gramado, Novo Hamburgo, Porto Alegre, Torres, Três Coroas, Xangri-lá, Biguaçu, Blumenau, Cocal do Sul, Criciúma, Brusque, Forquilhinhas, Garopaba, Florianópolis, Governador Celso Ramos, Guabiruba, Imbituba, Ibirama, Palhoça, Jaguaruna, Laguna, Pomerode, Rio do Sul, São José, Praia Grande, Tijucas, Luiz Alves, Gaspar, Tubarão, Indaial, Botuvera, Ilhota, Rio dos Cedros]}
      - {tipo: periodo_vigencia, op: igual_a, valor: quarta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 1 dias}
  - nome: Rota de sexta, agendada na quinta
    se:
      - {tipo: localizacao, op: igual_a, valor: [Guaratuba, Matinhos, Itapoá, Morretes, Paranaguá, Araucária, Curitiba, São José dos Pinhais, Piraquara, Colombo, Pinhais, Campo Largo, Balneário Barra do Sul, Balneário Piçarras, Campo Alegre, Joinville, São Francisco do Sul, Navegantes, Penha, Pouso Redondo, Corupá, Guaramirim, São Bento do Sul, Barra Velha, Schroeder, Biguaçu, Florianópolis, Governador Celso Ramos, Palhoça, São José, Tijucas]}
      - {tipo: periodo_vigencia, op: igual_a, valor: quinta, unidade: periodo_nomeado}
    entao: {acao: agendar, frequencia: fixa 1 dias}
  - nome: Não agendar os demais
    se: []
    entao: {acao: nao_agendar, frequencia: nao_informada}
termos_fora_vocabulario:
  - baixado na Receita Federal
  - bloqueado
  - roteirizável
  - agendamento no dia anterior à rota
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|
| televendas | jargao | atendimento por telefone |
| rota | jargao | roteiro de visitas por cidade e dia |
| roteirizável | jargao | pode ser encaixado no roteiro do dia |
| bloqueado | jargao | cliente com cadastro bloqueado |
| baixado na Receita | jargao | cadastro encerrado no órgão fiscal |

## Lacunas

- A entrada não traz regra de frequência por perfil de compra; só o agendamento por rota.

## Ambiguidades

- "Diário" foi registrado como 1 dia pela convenção de periodicidade; combinado com dia único de agendamento, o efeito prático é semanal.
- "Roteirizável" não tem campo próprio e foi registrado apenas na descrição.
