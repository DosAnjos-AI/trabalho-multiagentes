# NORMALIZACAO — Contrato de normalização de regras comerciais (padrão 3.1)

Este documento é o contrato seguido na geração dos arquivos `normalizado.md`. Foi escrito antes da
geração e só recebe, ao final, as seções "Decisões de rota" e "Casos em que o padrão não se aplicou
bem". Um terceiro deve conseguir normalizar um input novo lendo apenas este arquivo.

---

## 1. Modelo executor

`claude-opus-5-5` (Opus 5.5), conforme reportado pelo prompt de sistema do ambiente Claude Code.
Não há outra verificação independente do identificador.

## 2. Data e versão

- Data de execução: 2026-10-26
- Versão do padrão: `3.1`

---

## 3. Instrução aplicada a cada documento

### 3.1 Prompt de sistema

~~~~text
Você normaliza descrições de regras comerciais de agendamento de atendimento (visitas, ligações,
contatos) escritas em português por pessoas da área comercial. Sua saída é um único arquivo
Markdown no formato fixado abaixo, e nada além dele.

PRINCÍPIOS
1. A única fonte de conteúdo é o texto de entrada recebido. Não acrescente regra, critério, número,
   frequência ou público que o texto não declare. O que faltar vai para a seção "Lacunas"; o que
   admitir mais de uma leitura vai para "Ambiguidades". Nunca preencha lacuna por inferência.
2. Descreva a regra em termos comerciais genéricos, que funcionem para qualquer sistema de
   agendamento. Não use palavra-chave de nenhuma linguagem de regras (por exemplo: "parametros",
   "quando", "frequencia de", "nao agendar", "do time", "da carteira").
3. Nomes próprios (empresa dona das regras, empresas clientes, supervisores, vendedores, rotas,
   sistemas externos) e URLs nunca aparecem na "Descrição canônica" nem na "Representação
   estruturada". Use os substitutos genéricos: EMPRESA_FOCO, EMPRESA_CLIENTE, SUPERVISOR_A,
   SUPERVISOR_B, ..., VENDEDOR_01, VENDEDOR_02, ..., ROTA_01, ROTA_02, ..., SISTEMA_EXTERNO,
   numerados em ordem de aparição no texto. O nome da plataforma de vendas é jargão e vira
   "plataforma de vendas". Cada substituição é registrada na tabela "Dicionário".
4. URL de chamado ou de sistema de chamados (proofhub, basecamp e similares) é metadado de
   proveniência: vai somente para `origem_solicitacao`, nunca para a prosa.
5. Use apenas os nomes de campo e os valores de vocabulário fixados abaixo. Um critério específico
   demais não vira tipo novo: vira `valor` e `descricao` dentro do tipo mais próximo, e o termo vai
   para `termos_fora_vocabulario`.
6. Não use âncoras nem aliases YAML (&nome, *nome). Listas (estados, ramos, códigos, segmentos)
   são escritas por extenso em cada regra onde aparecem, mesmo repetidas.
7. Todo bloco YAML precisa abrir sem erro num parser YAML padrão. Coloque entre aspas duplas todo
   texto que contenha dois-pontos seguido de espaço, "#", aspas, colchetes, chaves, "%", "@", "&",
   "*", "!", "|", ">" ou que comece com "-", "?" ou dígito seguido de texto.
8. Número presente no texto não implica critério. Todo número vai para `numeros_detectados`, mas
   só vira `valor` ou `frequencia_valor` quando parametriza uma regra declarada. Número incidental
   não gera critério. Na dúvida, registre em "Ambiguidades".

FORMATO DE SAÍDA (reproduza exatamente esta estrutura)

---
id: <id>
origem: <caminho do input>
gobr: <caminho do arquivo de regras de referência, ou null>
tipo_input: <texto_corrido | imagem | audio_transcrito | texto_estruturado>
versao_padrao: 3.1
total_regras: <número de regras descritas no input>
entrada_corrigida: <true | false | null>
origem_real: <true | false>
procedencia: <corpus_sintetico | corpus_real | consulta>
---

## Descrição canônica

<Prosa normalizada do conjunto inteiro, em português comercial, sem nome próprio e sem URL, só
com substitutos genéricos. Cobre público, todas as regras e suas ações, na ordem do input.>

## Representação estruturada

```yaml
publico_alvo: <quem executa o atendimento, em termo genérico>
regras:
  - nome: <rótulo da regra>
    publico: <quem executa esta regra; repetir o padrão quando não houver exceção>
    descricao: <prosa curta da regra isolada>
    criterios:
      - tipo: <tipo do vocabulário fechado>
        descricao: <o critério em palavras, como um comercial diria>
        operador: <dentro_de | fora_de | igual_a | maior_que | menor_que | entre>
        valor: <número, texto, [min, max] com entre e fora_de, ou lista com igual_a e fora_de>
        unidade: <dias | meses | reais | percentual | periodo_nomeado | none>
        alcance: <vendedor | outro_vendedor | empresa | grupo | nao_informado>
    acao:
      tipo: <agendar | nao_agendar | limitar_capacidade | nao_declarado>
      frequencia_tipo: <fixa | calculada | nao_informada>
      frequencia_valor: <número ou null>
      frequencia_unidade: <dias | none>
```

## Dicionário

| Termo original | Categoria | Substituto genérico |
|---|---|---|

## Metadados

```yaml
numeros_detectados: [<todos os números do input, em dígito>]
criterios_usados: [<tipos de critério usados neste arquivo>]
termos_fora_vocabulario: [<termos que não couberam no vocabulário fechado>]
jargoes: [<jargão da área identificado>]
origem_solicitacao: <URL de proveniência, ou null>
```

## Lacunas

- <O que o input não informou. Se nada faltar: nenhuma>

## Ambiguidades

- <O que admite mais de uma leitura. Se nada: nenhuma>

VOCABULÁRIO DE criterios.tipo
- tempo_sem_comprar: janelas de tempo desde a última compra ou pedido
- tempo_sem_visita: janelas de tempo desde o último atendimento ou visita
- estagio_relacionamento: nunca comprou, comprando, parou de comprar, voltou a comprar, compra única
- carteira: vínculo do cliente com vendedor ou time (carteira fixa, carteira livre, sem vendedor)
- situacao_financeira: pendência em aberto, crédito disponível, limite
- situacao_cadastro: situação do cadastro do cliente e tempo de cadastro
- valor_cliente: faturamento, ticket médio, classificação por porte ou curva
- localizacao: cidade, bairro, estado, região
- agenda_rota: já agendado, presença em rota, conflito de agenda
- segmento: ramo de atividade, tipo de cliente, segmentação declarada
- periodo_vigencia: quando a regra vale (dia, semana, mês, período do ano)
- capacidade: limite de atendimentos por período
- identificacao: seleção por código ou identificador específico

REGRAS DE PREENCHIMENTO
- Uma entrada em `regras` para cada regra que o input descreve. `total_regras` é esse número.
- Regra de fallback (vale para quem não caiu em nenhuma outra, sem critério próprio):
  `criterios: []`.
- Vínculo de carteira (carteira fixa, carteira do time, clientes sem vendedor) é sempre tipo
  `carteira`, nunca `agenda_rota`. `agenda_rota` é só para agenda e rota (já agendado, rota
  programada, visita marcada, conflito).
- Operadores: "nos últimos N", "até N", "em N dias" -> dentro_de N; "há mais de N", "sem ... nos
  últimos N" -> maior_que N; "menos de N" -> menor_que N; "entre A e B" -> entre [A, B]; "não
  entre A e B" -> fora_de [A, B]; condição sem número ou lista de itens -> igual_a (valor texto ou
  lista); exclusão de lista de itens -> fora_de (lista). fora_de nunca recebe número isolado.
- Período nomeado sem número ("semana anterior", "mês atual", "dezembro") -> unidade
  periodo_nomeado, valor em texto.
- Condição sem número -> unidade none.
- alcance: vendedor (com o próprio vendedor), outro_vendedor (com vendedor diferente do que vai
  atender), empresa (com qualquer vendedor ou com a empresa toda), grupo (com um time, equipe ou
  grupo de vendedores ou de empresas), nao_informado (o input não diz).
- acao.tipo: agendar (há frequência ou ordem de atender), nao_agendar (tirar da agenda),
  limitar_capacidade (teto de atendimentos), nao_declarado (o input não diz o que fazer).
- Frequência em número de dias -> fixa, com o número. Frequência derivada de média, histórico ou
  cálculo da empresa ou do vendedor -> calculada, valor null, unidade none. Sem frequência ->
  nao_informada, valor null, unidade none. Para nao_agendar: nao_informada, null, none.
- Palavra de periodicidade sem número: diário 1, semanal 7, quinzenal 15, mensal 30, bimestral 60,
  em dias; registrar em "Ambiguidades" quando o texto não confirmar o número.
- Números por extenso viram dígito em `numeros_detectados` ("sete" -> 7). Entram os que indicam
  quantidade, inclusive valores em reais e percentuais; saem ordinais e expressões como "uma
  única". Cada valor aparece uma vez, na ordem em que surge no input. Palavras de periodicidade
  ("semanal") não são números do texto e não entram.
- `criterios_usados`: tipos efetivamente usados, sem repetição, em ordem de primeira aparição.
- `jargoes`: termos técnicos da área comercial presentes no input (por exemplo positivação,
  prospect, curva ABC, carteira fixa, televendas, inadimplente), sem repetição.
- Dicionário: uma linha por nome próprio substituído, uma linha por jargão relevante e uma
  linha por código. Categorias:
  empresa_foco (a distribuidora dona das regras), empresa_cliente, supervisor, vendedor, rota,
  sistema_externo, jargao, codigo. A plataforma de vendas é jargao. Para jargão, o substituto é a
  expressão comercial simples equivalente. Código é valor de um campo do sistema do cliente
  (tipo de cobrança, tipo de pagamento, código de rota, ramo de atividade) e não é substituído
  no texto: o substituto repete o próprio código. Em "Termo original", cada item da célula é um
  termo, separado por vírgula (por exemplo "tipo de cobrança, DH, BK"). Sem nada a registrar, manter a tabela com uma linha
  "| nenhum | - | - |".
~~~~

### 3.2 Prompt de usuário (modelo)

~~~~text
Normalize o input abaixo seguindo exatamente o formato e os vocabulários do prompt de sistema.

id: {id}
origem: {caminho_do_input}
gobr: {caminho_do_gobr_ou_null}
tipo_input: {tipo_input}
entrada_corrigida: {true_false_ou_null}
origem_real: {true_ou_false}
procedencia: {corpus_sintetico_corpus_real_ou_consulta}
origem_solicitacao: {url_ou_null}

<input>
{texto_do_input}
</input>
~~~~

No corpus, `origem_solicitacao` é preenchido com a URL do comentário do arquivo de regras, quando
houver; é o único dado que passa do arquivo de regras para o normalizado.

---

## 4. Formato e vocabulários fechados

### 4.1 Formato

O formato é o reproduzido no prompt de sistema (seção 3.1), sem alteração. Cabeçalho YAML entre
`---`, seguido das seções nesta ordem: Descrição canônica, Representação estruturada (bloco
`yaml`), Dicionário (tabela), Metadados (bloco `yaml`), Lacunas, Ambiguidades.

### 4.2 `criterios.tipo`

| Tipo | Cobre |
|---|---|
| `tempo_sem_comprar` | Janelas de tempo desde a última compra ou pedido |
| `tempo_sem_visita` | Janelas de tempo desde o último atendimento ou visita |
| `estagio_relacionamento` | Nunca comprou, comprando, parou de comprar, voltou a comprar, compra única |
| `carteira` | Vínculo do cliente com um vendedor ou time: carteira fixa, carteira livre, cliente sem vendedor |
| `situacao_financeira` | Pendência em aberto, crédito disponível, limite |
| `situacao_cadastro` | Situação do cadastro do cliente e tempo de cadastro |
| `valor_cliente` | Faturamento, ticket médio, classificação por porte ou curva |
| `localizacao` | Cidade, bairro, estado, região |
| `agenda_rota` | Já agendado, presença em rota, conflito de agenda |
| `segmento` | Ramo de atividade, tipo de cliente, segmentação declarada |
| `periodo_vigencia` | Quando a regra vale: dia, semana, mês, período do ano |
| `capacidade` | Limite de atendimentos por período |
| `identificacao` | Seleção por código ou identificador específico |

### 4.3 Demais vocabulários

| Campo | Valores |
|---|---|
| `criterios.operador` | `dentro_de`, `fora_de`, `igual_a`, `maior_que`, `menor_que`, `entre` |
| `criterios.unidade` | `dias`, `meses`, `reais`, `percentual`, `periodo_nomeado`, `none` |
| `criterios.alcance` | `vendedor`, `outro_vendedor`, `empresa`, `grupo`, `nao_informado` |
| `acao.tipo` | `agendar`, `nao_agendar`, `limitar_capacidade`, `nao_declarado` |
| `acao.frequencia_tipo` | `fixa`, `calculada`, `nao_informada` |
| `acao.frequencia_unidade` | `dias`, `none` |
| `tipo_input` | `texto_corrido` (corpus); em consulta também `imagem`, `audio_transcrito`, `texto_estruturado` |
| Categoria do dicionário | `empresa_foco`, `empresa_cliente`, `supervisor`, `vendedor`, `rota`, `sistema_externo`, `jargao`, `codigo` |
| Substitutos | `EMPRESA_FOCO`, `EMPRESA_CLIENTE`, `SUPERVISOR_A`, `SUPERVISOR_B`, ..., `VENDEDOR_01`, `VENDEDOR_02`, ..., `ROTA_01`, ..., `SISTEMA_EXTERNO` |

**`codigo`** — categoria do dicionário para valor de um campo do sistema do cliente: tipo de
cobrança, tipo de pagamento, código de rota, ramo de atividade e semelhantes. Diferença para
`jargao`: jargão é vocabulário do negócio ("carteira fixa", "inadimplente"); código é valor de
campo ("DH", "BK"). Diferença para nome próprio: código não identifica empresa nem pessoa, por
isso **não é substituído** no texto; permanece como está e serve de chave de busca. Na tabela do
dicionário o substituto repete o próprio código.

**`procedencia`** — lista fechada, identifica a origem do item:

| Valor | Significado |
|---|---|
| `corpus_sintetico` | Item do corpus, com entrada gerada a partir de um arquivo de regras |
| `corpus_real` | Item do corpus cuja origem é um exemplo real documentado |
| `consulta` | Pedido recebido de usuário em tempo de execução |

---

## 5. Regras de normalização

**Fonte de conteúdo.** O normalizado é derivado exclusivamente do texto de entrada. No corpus, o
arquivo de regras (`.gobr`) serve só para conferir a entrada antes (regra faltando, regra
inventada, números) e para fornecer `origem_solicitacao`. Informação que falta na entrada e existe
no `.gobr` entra pela correção da entrada, nunca direto no normalizado. Assim os normalizados do
corpus não ficam mais ricos do que os produzidos em consulta.

**Substitutos genéricos.** Viram substituto: nome de empresa dona das regras (EMPRESA_FOCO),
empresa cliente (EMPRESA_CLIENTE), supervisor (SUPERVISOR_A, B...), vendedor (VENDEDOR_01, 02...),
rota nomeada (ROTA_01...), sistema externo (SISTEMA_EXTERNO). Numeração por ordem de aparição.
Identificador de vendedor numérico (código) também vira VENDEDOR_NN quando designa uma pessoa;
códigos de cliente, de segmento ou de região permanecem como `valor` de `identificacao`, pois não
identificam pessoa. Nome de time genérico ("televendas", "campo") não é nome próprio.

**Dicionário.** Registra cada substituição (termo original, categoria, substituto) e os jargões
relevantes com seu equivalente comercial simples. A plataforma de vendas é `jargao` e vira
"plataforma de vendas". Valor de campo do sistema do cliente (tipo de cobrança, tipo de
pagamento, código de rota, ramo de atividade) é `codigo`: entra no dicionário, mas **não é
substituído** no texto. Cada célula da coluna "Termo original" lista **um termo por item**,
separados por vírgula: "tipo de cobrança, DH, BK" são três termos, e nunca uma frase única com
os códigos dentro. O índice léxico separa a célula por vírgula e ponto e vírgula e indexa cada
item inteiro e cada token dele (mínimo de 2 caracteres, sem palavras vazias).

**Proveniência.** URL de chamado (domínios proofhub, basecamp e similares) e nome de sistema de
chamados ficam fora da prosa e da estrutura; a URL vai para `origem_solicitacao`. Sem URL: `null`.

**Número por extenso.** Convertido para dígito em `numeros_detectados`. Entram quantidades
(dias, meses, reais, percentuais, contagens como "três situações"); saem ordinais ("primeiro",
"terceira") e "uma única". Cada valor uma vez, na ordem de primeira aparição.

**Lacuna.** O que a entrada não diz (frequência ausente, público vago, critério sem valor, ação
não declarada) é registrado em "Lacunas" e marcado no campo correspondente com `null`,
`nao_informada`, `nao_informado` ou `nao_declarado`. Nunca se completa por inferência.

**Conferência da entrada no corpus (lista fechada de divergências).** Corrige-se na entrada apenas:
regra presente no `.gobr` e ausente na entrada; regra na entrada sem bloco no `.gobr`; valor
numérico diferente; critério de natureza diferente; ação trocada; público diferente; URL de
chamado ou nome de sistema de chamados na prosa. Fraseado, ordem, estilo, sinônimos, entradas
idênticas entre pastas e menção a lacuna real do `.gobr` ficam como estão. Toda correção vai para
`CORRECOES.md`.

---

## 6. Limitações conhecidas

- O normalizado herda as omissões e ambiguidades da entrada; não há segunda fonte para resolvê-las
  além da correção da entrada pela lista fechada.
- A conversão de critérios para operador e unidade depende do fraseado; formulações como "em 60
  dias" admitem leitura de janela (dentro de) ou de limite, e a regra fixa a leitura "dentro de".
- O vocabulário de 13 tipos força critérios específicos (ex.: situação na Receita Federal,
  filial) para o tipo mais próximo; a especificidade fica em `descricao`, `valor` e
  `termos_fora_vocabulario`.
- Defeitos reais do `.gobr` (bloco truncado, nome de bloco que contradiz o valor, blocos repetidos)
  não são corrigidos; a entrada os descreve e o normalizado os reflete como lacuna ou ambiguidade.
- O corpus atual foi normalizado antes da criação da categoria `codigo`. Códigos existentes
  (por exemplo "tipo de cobrança DH, BK" nas regras 153, 166, 176, 177 e 233) podem estar
  categorizados como `jargao`, em células com vírgula. A inconsistência não afeta o índice
  léxico, que ignora a categoria e separa por item e token; uma passada dirigida pode corrigir
  depois.
- O identificador do modelo é o declarado pelo ambiente, sem verificação independente.

---

## 7. Aplicação a input novo

Uso em tempo de consulta: chega um pedido de usuário e não existe `.gobr`.

- O campo `gobr` do cabeçalho fica `null`. `entrada_corrigida` perde sentido, pois não há segunda
  fonte para conferir; preencher `null`. `procedencia` recebe `consulta`. `origem_real` fica
  `false`: o campo indica apenas se o item veio de um exemplo real do corpus, e não se o pedido é
  de um usuário real.
- A conferência de números passa a ser input bruto contra normalizado, sem terceira referência:
  todo número do input precisa estar em `numeros_detectados`. Virar `valor` ou `frequencia_valor`
  acontece **apenas** quando o número for parâmetro de alguma regra descrita. Número incidental —
  quantidade de vendedores, tempo de casa, qualquer valor que não parametrize regra — fica
  registrado em `numeros_detectados` e não gera critério. Na dúvida sobre o papel do número,
  registrar em "Ambiguidades" em vez de criar critério.
- `tipo_input` aceita `texto_corrido`, `imagem`, `audio_transcrito` e `texto_estruturado`. Para
  imagem, normalizar o texto e as relações legíveis do diagrama; o que não for legível vai para
  "Lacunas".
- Input real costuma trazer menos informação que os exemplos do corpus: tudo que faltar vai para
  "Lacunas", e nada é preenchido por inferência.
- `origem_solicitacao` recebe a URL do pedido, se o usuário informar; senão `null`.
- O restante do procedimento — formato, vocabulários fechados, dicionário, substitutos genéricos,
  tratamento de número por extenso — é idêntico ao da construção do corpus: usar os prompts da
  seção 3 sem alteração, trocando apenas os campos do prompt de usuário.

---

## 8. Decisões de rota

- **Pastas com entrada e `.gobr` idênticos a outra já processada**: o `normalizado.md` foi
  replicado da pasta-irmã, com troca de `id`, caminhos e campos próprios (URL, empresa,
  números), e cada cópia foi validada isoladamente. Isso aconteceu nas famílias de 001/002/004,
  em 166, 176 e 177 (derivadas de 153/166), em 216 (igual a 179 depois da correção da entrada)
  e em 248/249. Para 248/249 só a estrutura foi aproveitada (mesmo `.gobr` de 173 e 194); o
  texto, os alcances e os metadados foram refeitos a partir da própria entrada. Parte dessas
  réplicas foi feita com `sed` em laço de shell. Isso é exceção ao "uma pasta por vez, sem
  script" e fica registrado aqui.
- **Periodicidade por extenso**: semanal = 7 dias, quinzenal = 15, mensal = 30, diário = 1.
  `frequencia_valor` traz o valor convertido e a descrição mantém a palavra original.
- **Preferência de dia da semana** ("dia útil e sábado", "preferência máxima na segunda"):
  registrada como critério `periodo_vigencia` com `unidade: periodo_nomeado` e anotada em
  Ambiguidades. O vocabulário não tem campo próprio para preferência.
- **Frequência pelo histórico com mínimo, máximo, acréscimo ou redução**: `frequencia_tipo:
  calculada`, `frequencia_valor: null`. Os limites e ajustes ficam só na `descricao` da regra
  e em Ambiguidades.
- **Intervalo histórico entre compras** ("frequência histórica menor que 16 dias"): registrado
  como `tempo_sem_comprar`, por falta de tipo próprio. O termo vai para
  `termos_fora_vocabulario`.
- **"Sem compra entre X e Y dias"**: `fora_de [X, Y]`. **"Compra entre X e Y dias"**:
  `entre [X, Y]`.
- **Regras residuais** (sem condição no `.gobr`, descritas como "o restante", "inativos",
  "fora das regras"): `criterios: []`.
- **Chamados na prosa**: toda menção a sistema de chamados ("Pedido do ProofHub", "card do
  Basecamp", "Ticket CS-xx do Atlassian", "ticket IMP-xxx") foi substituída na entrada por
  "Pedido de uma solicitação" e registrada em `CORRECOES.md`. Identificadores de chamado
  isolados (149, 152, 155) receberam o mesmo tratamento dado à URL de chamado.
- **URLs**: vão sempre para `origem_solicitacao`. Quando há duas URLs no `.gobr` (147, 195),
  o campo vira lista.
- **Substitutos**: vendedores viram `VENDEDOR_NN` na ordem de aparição; pessoas que dão nome a
  times viram `SUPERVISOR_A`/`B` (papel suposto e anotado em Ambiguidades); a empresa dona da
  regra vira `EMPRESA_FOCO`; a empresa de onde a regra foi copiada vira `EMPRESA_CLIENTE`; o
  nome da plataforma vira jargão ("plataforma de vendas"). Cidades, bairros, UFs e códigos de
  ramo foram mantidos, porque não identificam pessoas.
- **Faixas de códigos escritas com "a"** (246: "101001 a 101007"): expandidas código a código
  em `valor`. `numeros_detectados` guarda só os números que aparecem literalmente na entrada.
- **"Igual ou menor"/"ou mais"**: sem operador inclusivo, foi usado `menor_que`/`maior_que`, com
  nota em Ambiguidades (233, 235).
- Padrão 3.1 corrigido após revisão: `procedencia` separado de `origem_real`, porque o segundo
  campo acumulava dois significados incompatíveis; e a verificação de número em tempo de consulta
  deixou de exigir que todo número vire parâmetro de regra, porque a exigência induzia criação de
  critério para número incidental.
- Correção do índice léxico e categoria `codigo`: o índice tratava cada célula "Termo original"
  como um termo inteiro, então "tipo de cobrança DH, BK" não era encontrado por `BK` nem por `DH`.
  Passou-se a separar a célula por vírgula e ponto e vírgula e a indexar item inteiro e tokens
  (mínimo de 2 caracteres, sem as palavras vazias de, da, do, em, no, na, com, por, para, ou,
  as, os, um, uma). Token genérico como "cobranca" pode apontar para muitos documentos; isso é
  aceito, porque o canal léxico só produz candidatos e a fusão com o canal denso resolve o
  ranking. Criou-se também a categoria `codigo`, pois valor de campo não é nome próprio nem
  jargão. Os 249 normalizados não foram reescritos.

---

## 9. Casos em que o padrão não se aplicou bem

- **Nome do bloco contradiz o critério ou o valor no `.gobr`** (062/064, 130, 214, 237): a
  entrada segue o código e o normalizado segue a entrada. A contradição foi anotada, sem
  correção.
- **Regras possivelmente inalcançáveis por ordem de avaliação** (178, 226, 230, 245, 247): o
  formato não representa precedência. A sobreposição foi anotada em Ambiguidades.
- **Sentido de "fora da recência entre X e Y"** (108): a entrada lê o nome do bloco; pode haver
  inversão de sentido. A entrada foi mantida e o caso registrado.
- **"Na última semana"** (151): leitura ambígua (semana anterior ou última semana do mês). A
  entrada foi mantida.
- **Grafia de cidades no `.gobr`** (154, 205): truncamentos e erros no código, como
  "JAGUARUMA" e "ADRINOPOLIS". A entrada usa a grafia correta. Não foi tratado como
  divergência.
- **Listas geográficas extensas** (236, 245): a descrição canônica resume as listas, que
  ficam completas na representação estruturada. A entrada de 236 já resumia os bairros ("com
  variações de grafia"), então o normalizado não traz a lista integral do `.gobr`.
- **Bloco sem ação declarada** (032): uma regra ficou com `acao.tipo: nao_declarado`, por ser o
  único uso desse valor no corpus.
- **Tipo `capacidade` e ação `limitar_capacidade`**: não foram usados em nenhuma pasta.
- **Intervalo histórico, preferência de dia, crédito percentual e tipo de cobrança** não têm
  tipo próprio no vocabulário. Foram aproximados por `tempo_sem_comprar`, `periodo_vigencia` e
  `situacao_financeira`, o que mistura semânticas dentro do mesmo tipo.
- **`referencias/`** tem 246 arquivos; a `regra_247` não tem cópia ali.
