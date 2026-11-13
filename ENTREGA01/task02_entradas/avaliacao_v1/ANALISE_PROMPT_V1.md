# Análise do prompt_v1

## Ressalva

Estou criticando um prompt que eu mesmo escrevi e avaliando reconstruções que eu mesmo fiz. Isso puxa para defender a obra e para atribuir os erros ao modelo em vez de ao prompt ou ao reconstrutor. As três medidas objetivas (`comparacoes/`) são o contrapeso; o que vem abaixo é leitura.

## Números de partida

Inteira correta, critério estrito, todos os blocos (arquivos em `comparacoes/`):

| Modelo | 020 | 228 | 032 | Soma |
|---|---|---|---|---|
| gemini-3.6-flash | 3/3 | 6/7 | 73/78 | 82/88 |
| gpt-6-luna | 3/3 | 6/7 | 3/78 (57 ignorando caixa) | 12/88 (66) |
| gpt-6.1-terra | 3/3 | 6/7 | 3/78 (21 ignorando caixa) | 12/88 (30) |
| gemini-3.5-flash-lite | 3/3 | 4/7 | 2/78 | 9/88 |

Capturadas: 88/88 em três modelos, 86/88 no flash-lite. Inventadas: 0 em todos. Ou seja: **toda descrição deixa reconstruir a estrutura; o que se perde são os detalhes de cada regra.** A 032 domina a soma.

## 1. Defeito do prompt x defeito do modelo x defeito do reconstrutor

### Vem do prompt

| Defeito observado | Onde | Por que é do prompt |
|---|---|---|
| Valores textuais traduzidos ou normalizados: `MATCON` virou "material de construção", `CONS. FINAL` virou "corporativo e consumidor final", "Atacado" virou "atacado e distribuidores" | terra 032 (54 blocos perdidos); luna 032 (caixa alterada, 72 blocos perdidos no estrito) | O prompt exige "números exatamente como estão", mas não diz nada sobre **valores textuais** (códigos de ramo, siglas, UFs). E manda "dizer com palavras do dia a dia" e evitar "identificadores técnicos": o modelo obediente traduz o código. O terra fez exatamente o que o prompt pediu |
| Nenhuma descrição disse que o cliente pode estar nas duas carteiras ao mesmo tempo (`carteira livre`) | as 4 na 032 | O prompt pede "de quais clientes cada um cuida", mas não pede para dizer se os grupos se sobrepõem. Sem pedido explícito, nenhum modelo achou relevante |
| Fonte dos prospects (as duas carteiras) não ficou recuperável | as 4 na 032 | Mesmo motivo: o prompt não pede para dizer de qual grupo cada situação tira os clientes |
| Nome de situação lido como condição: "Curva A" virou filtro de curva | flash-lite 032 (72 blocos) | O prompt incentiva usar os nomes ("quando ajudarem a entender"), sem avisar que nome é rótulo e pode enganar. Em 032 o nome diz "Curva A" e a condição real é só faturamento |
| Descrição que espelha o arquivo: 72 nomes entre parênteses na ordem dos blocos | flash 032 | O mesmo incentivo aos nomes. A frase "não reproduza como lista na mesma ordem do arquivo" não segurou |
| Alcance da condição ("global", "do vendedor", "com a empresa") ou foi vazado como termo técnico, ou foi perdido | luna/flash vazaram "positivação global"; flash-lite perdeu | O prompt não diz que o alcance muda o resultado, nem dá a forma de negócio de dizê-lo. O terra achou sozinho ("compras com todos os vendedores") |
| Comentário sobre o arquivo em vez do negócio | luna 228 e 032 ("a regra chamada X não especifica"); terra 032 em menor grau | O prompt não diz o que fazer com regra incompleta ou estranha. O bloco final da 032 está quebrado no original; sem instrução, o modelo descreve o arquivo |
| Conflito de instruções sobre ordem | todos | "Agrupe pelo sentido de negócio e não pela ordem do arquivo" brigando com "diga a ordem de prioridade quando ela mudar o resultado". Na 228 e na 032 a ordem é a prioridade; três dos quatro modelos ignoraram a primeira instrução e seguiram o arquivo |

### Vem do modelo

| Defeito | Onde |
|---|---|
| Inventou frequência (28 dias) para o bloco do original que não tem frequência | flash-lite 032 |
| Inventou contexto ("novos cadastros") e inferência ("ou seja, as curvas A e B") | flash-lite 228 |
| Trocou "única compra" por "primeira compra" | flash-lite 228 |
| Omitiu "vendedores ativos" (o prompt pede "quais vendedores") | flash-lite 228 e 032 |
| Leu `recencia de positivacao` (grupo do vendedor) como "compra vinculada ao vendedor" | terra 032 |
| Falou do arquivo, contrariando "não explique o que a configuração faz por dentro" | luna 228 e 032 |

### Vem do reconstrutor (eu), não da descrição

| Defeito | Onde | Efeito na medida |
|---|---|---|
| "Entre 91 e 180 dias" reconstruído como `em 180 dias` (cascata), copiando o padrão de `exemplos/RegraMaxlub` | 228, os 4 modelos | -1 em cada; não muda a comparação entre modelos |
| Valores de ramo escritos na caixa da descrição, sem normalizar para caixa alta | luna 032 | É o que derruba o luna de 57 para 3 no estrito. A descrição dava os nomes em caixa mista; eu poderia ter adivinhado caixa alta, mas seria adivinhar |
| Fonte dos prospects | 032, os 4 | A descrição flash dizia "os clientes das carteiras de ambas as regiões"; eu tinha a pista e escolhi `do time`. O manual não mostra fonte com duas carteiras, o que pesou na escolha |

## 2. Instrução que faltou, instrução que atrapalhou

**Faltou:**
1. Valores textuais (códigos, siglas, listas de UF, nomes cadastrados) devem ser copiados literalmente.
2. Dizer o alcance de cada condição (compra com qualquer vendedor da empresa, com a equipe, só com o vendedor do cliente), em palavras de negócio, e apontar exceções.
3. Dizer se um cliente pode estar em mais de um grupo, e de qual grupo cada situação parte.
4. Nome de situação é rótulo: não pode ser confundido com condição.
5. O que fazer com situação incompleta (sem ação definida): dizer em termos de negócio, sem falar de "regra" ou "arquivo".

**Atrapalhou:**
1. "Agrupe pelo sentido de negócio e não pela ordem do arquivo. É esperado que o texto saia em ordem diferente": brigava com a prioridade e foi ignorada; quando obedecida (terra 032), funcionou porque a ordem não importava ali.
2. "Os nomes que a empresa deu às situações, quando ajudarem": abriu a porta para o espelhamento (flash 032) e para a leitura do nome como condição (flash-lite 032).
3. "Identificadores técnicos" na lista do que não pode aparecer, sem ressalva para valores de dado: o terra tratou `MATCON` como identificador técnico e traduziu.

**Funcionou e deve ficar:** "todos os números exatamente como estão". Nenhum número errado em nenhuma das 12 descrições, inclusive nas 72 variações da 032.

## 3. Mudanças propostas e efeito esperado

| # | Mudança | Efeito esperado | Como verificar na próxima rodada |
|---|---|---|---|
| 1 | Seção nova "Valores que vão literais": códigos, siglas, UFs e nomes cadastrados copiados exatamente, inclusive caixa | Terra 032 recupera os 54 blocos perdidos por valor; luna 032 recupera os 72 do estrito. Maior ganho isolado previsto | Medida "inteira correta" na 032, sem precisar da coluna "ignorando caixa" |
| 2 | Pedir o alcance de cada condição de compra/visita/curva com exemplos de negócio ("compra com qualquer vendedor da empresa", "compra com a equipe do vendedor", "compra com o próprio vendedor"), e que exceções a esse alcance sejam ditas | Some o vazamento "positivação global" sem perder a distinção; flash-lite deixa de perder o `global` | Vazamento de "global"/"positivação" na leitura subjetiva; exceção do pré-inativo C na 032 |
| 3 | Pedir que se diga se os grupos de clientes se sobrepõem e de qual grupo cada situação parte | Carteira `livre` e fonte com duas carteiras passam a ser recuperáveis | Os 2 blocos de carteira e o de prospects na 032 |
| 4 | Nome de situação: usar só se não puder ser lido como condição; nunca um nome por situação em sequência | Some o espelhamento do flash e a leitura "Curva A = filtro" do flash-lite | Leitura subjetiva da 032; filtros inventados de curva |
| 5 | Situação sem ação definida: dizer "para esse grupo ainda não definimos o intervalo" e não comentar o arquivo; reforçar a proibição de falar de "regra", "arquivo", "configuração" | Some o comentário sobre o arquivo do luna; flash-lite deixa de inventar frequência | Último bloco da 032; leitura subjetiva |
| 6 | Trocar a instrução de ordem por: "quando a ordem decide quem recebe qual tratamento, siga essa ordem; fora disso, organize como preferir" | Remove o conflito; não espero ganho de medida, espero menos texto se justificando | Leitura subjetiva |
| 7 | Mencionar "vendedores ativos/todos os vendedores" como item explícito de "quem atende" | Flash-lite deixa de perder `ativados` | Bloco `time` em 228 e 032 |

O que **não** muda: o tom, a proibição de vocabulário técnico (lista atual), a exigência de números exatos, a liberdade de texto curto para regra simples.

Risco previsto: a mudança 1 pode reintroduzir aparência técnica (códigos em caixa alta no meio do texto). Aceito o custo: código cadastrado é dado do negócio, a pessoa do comercial também usaria o código que aparece no sistema dela.

## 4. Versão final do prompt_v2 (rodada seguinte, com leitura liberada)

Revisão feita com acesso aos `.gobr` de teste, às 12 descrições e às comparações. A proposta da seção 3 foi mantida; abaixo, o que entrou de fato no `prompt_v2.md`, com a razão e o efeito esperado de cada mudança. Os marcadores `[M1]..[M7]` da proposta foram retirados do arquivo, porque o prompt é enviado ao modelo.

| # | Mudança no `prompt_v2.md` | Razão (defeito medido) | Efeito esperado |
|---|---|---|---|
| V1 | Seção nova "Natural e literal ao mesmo tempo": separa **palavras sobre a política** (livres) de **dados do cadastro** (copiados exatamente, com caixa, pontos e abreviações), com exemplo do certo e do errado | Código traduzido: terra escreveu "material de construção" no lugar de `MATCON` (54 blocos perdidos na 032); luna mudou a caixa (72 no estrito). O v1 dizia "números exatos" mas não "valores de texto exatos", e mandava evitar "identificadores técnicos" | Valores de ramo e UF literais em todos os modelos. É a mudança que mira a tensão central: a pessoa do negócio copia o cadastro porque é como acha o cliente no sistema, então o literal não quebra o tom |
| V2 | Frase explícita: "os dados do cadastro não são termos da ferramenta", repetida na lista do que não pode aparecer | No v1 a lista de proibição e a exigência de fidelidade puxavam em sentidos opostos para o mesmo item (`MATCON` parecia identificador técnico) | Remove a ambiguidade que levou o terra a traduzir |
| V3 | Item novo "alcance de cada condição", com quatro formas de negócio (qualquer vendedor da empresa / equipe do vendedor / só o próprio vendedor / medido na empresa ou no vendedor) e pedido de dizer exceções no lugar onde valem | Alcance perdido (flash-lite) ou só preservado vazando "positivação global" (luna, flash); terra leu a exceção sem `global` como "vinculada ao vendedor" | A distinção `global` x grupo x `do vendedor` vira texto de negócio; o reconstrutor recupera o filtro sem o termo técnico. Exceção do pré-inativo C da 032 dita explicitamente |
| V4 | `global`, `positivação`, `ciclo de vida prospect com a empresa` e `media faturada no ano com a empresa` acrescentados à lista de termos proibidos | Foram os vazamentos mais frequentes nas 12 descrições | Menos texto com cara de arquivo, sem perder conteúdo, porque V3 dá a forma substituta |
| V5 | Itens novos sobre grupos: se um cliente pode estar em mais de um grupo ou se sai do pool, e de qual grupo (ou grupos) cada situação parte | Sobreposição perdida: nenhuma descrição permitia recuperar `carteira livre` nem `da carteira("a","b")` | Recuperar o modificador `livre` e a fonte com duas carteiras na 032 |
| V6 | "Quem atende" passa a pedir se são todos os vendedores ou só os habilitados no sistema | flash-lite omitiu `ativados` na 228 e na 032 | Bloco `time` inteiro correto também no flash-lite |
| V7 | Seção "Nomes das situações": nome é rótulo, nunca condição; não deduzir condição do nome; nunca um nome por situação em sequência | flash-lite leu "Curva A" como filtro de curva (72 blocos); flash listou os 72 nomes em ordem, espelhando o arquivo | Some o filtro de curva inventado e o espelhamento do flash |
| V8 | Instrução de ordem trocada: segue a ordem só quando ela decide o tratamento; fora disso, organiza pelo sentido | Conflito no v1 entre "não siga a ordem do arquivo" e "diga a prioridade"; três modelos ignoraram a primeira parte | Menos conflito; não espero ganho de medida |
| V9 | Regra de agrupamento reforçada: explicar o padrão uma vez e dizer cada exceção no ponto em que vale (alcance diferente, falta de frequência, valor fora do padrão) | O terra comprimiu bem a 032, mas a exceção ficou ambígua; luna e flash só preservaram exceções escrevendo bloco a bloco | Descrições curtas como a do terra, sem perder exceção. É a segunda metade da tensão: compressão sem perda |
| V10 | "Entre X e Y dias" deve ser dito como intervalo, e "nos últimos Y dias" assim; uma forma não substitui a outra | Na 228 as descrições acertaram, mas o reconstrutor trocou intervalo por cascata. A instrução protege a descrição de fazer a mesma troca | Sem efeito esperado na medida da 228 (as descrições já acertavam); preventivo |
| V11 | Proibição de interpretação acrescentada ("ou seja...", "os recém-chegados") | flash-lite acrescentou "ou seja, as curvas A e B" e "novos cadastros" na 228 | Menos invenção no flash-lite |
| V12 | Situação sem ação definida: dizer em termos de negócio, não completar com valor parecido | flash-lite e flash completaram com 28 dias o bloco final da 032, que no original não tem frequência | Bloco final da 032 descrito como "sem intervalo definido" por todos |
| V13 | Proibição de falar do arquivo ou das regras como objeto | luna escreveu "a regra chamada 'Curva A e B' não especifica..." e "sem a indicação de que seja global" | Some o metacomentário do luna |
| V14 | "Quem escreve" passa a dizer que a pessoa conhece "o cadastro do sistema de vendas que usa todo dia" | Dá ao modelo o motivo de negócio para copiar o código sem soar técnico (apoia V1) | Códigos literais com tom natural |

**Decisão de cuidado:** todos os exemplos do `prompt_v2.md` usam valores **fictícios** (`AUTOPECAS`, `DIST. BEB`, `VAREJO`, MG e GO, 45 dias, R$ 8000, "Clientes Ouro"). A primeira redação usava `MATCON`, `CONS. FINAL` e "entre 91 e 180", tirados das regras de teste. Isso foi trocado antes de qualquer execução: exemplo com valor do gabarito daria ganho artificial justamente nas regras medidas e poderia contaminar as outras 190 regras com valores que não são delas.

**Risco declarado:** V1 e V3 aumentam o tamanho do prompt e a quantidade de exigências; modelos baratos podem passar a escrever mais "técnico" para cumprir todas. A leitura subjetiva da próxima rodada é o que vai mostrar isso.
