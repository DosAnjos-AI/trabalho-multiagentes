# Tarefa

Você vai receber o conteúdo de um arquivo de configuração de uma ferramenta de agendamento de visitas e atendimentos comerciais a clientes. Seu trabalho é escrever o texto que uma pessoa do comercial da empresa escreveria, ou diria em voz alta, para explicar a política de atendimento que esse arquivo representa.

O texto será usado como pedido de entrada: outra pessoa (ou outro sistema) vai ler só o seu texto e precisará conseguir reconstruir a configuração inteira a partir dele. Por isso o texto precisa ser, ao mesmo tempo, natural e completo.

# Quem escreve

Escreva como alguém do negócio: um gerente comercial, um coordenador de televendas, um dono de distribuidora. Essa pessoa conhece os clientes, os vendedores, a política da empresa e o cadastro do sistema de vendas que usa todo dia. Ela não conhece a ferramenta de agendamento nem a sua linguagem de configuração, e nunca falaria dela.

Escreva em português do Brasil, em texto corrido, em primeira pessoa do plural ou impessoal ("a gente", "nós", "a empresa"). Pode ser um parágrafo único ou alguns parágrafos curtos. Tom de explicação por escrito ou falada, não de documento técnico.

# Natural e literal ao mesmo tempo

As duas exigências não brigam. A pessoa do negócio fala com as próprias palavras sobre a política, mas quando cita um dado do cadastro ela copia o que está no sistema, do jeito que está, porque é assim que ela encontra o cliente lá.

- Palavras sobre a política: suas, do dia a dia. "Quem comprou nos últimos 45 dias", "atender a cada 14 dias", "não agendar".
- Dados do cadastro: copiados exatamente. Códigos e nomes de ramo de atividade, siglas de estado, nomes de cidade, bairro, rota, classificação, códigos de vendedor, de cliente, de cobrança ou de pagamento. Mantenha maiúsculas, minúsculas, pontos, abreviações e a grafia. Não traduza, não expanda, não corrija, não junte com sinônimos. Se o cadastro diz `DIST. BEB`, escreva DIST. BEB, e não "distribuidora de bebidas". Se diz `AUTOPECAS`, escreva AUTOPECAS, e não "autopeças" nem "loja de peças". Se a lista tem só `VAREJO`, não acrescente "varejo e atacarejo".
- Exemplo do tom certo: "Em MG e GO, os clientes dos ramos AUTOPECAS e DIST. BEB que compraram com qualquer vendedor da empresa nos últimos 45 dias e faturam em média mais de R$ 8000 por ano são atendidos a cada 10 dias."

Os dados do cadastro não são termos da ferramenta. Os termos da ferramenta são proibidos (ver adiante); os dados do cadastro são obrigatórios.

# O que o texto precisa conter

Tudo o que muda o resultado da configuração:

- Quem atende: quais vendedores ou equipes, se são todos os vendedores ou só os que estão habilitados no sistema, e de quais clientes cada um cuida (por exemplo, os clientes fixos de cada vendedor, ou só uma equipe específica).
- Como os clientes são separados em grupos, e se um mesmo cliente pode estar em mais de um grupo ao mesmo tempo ou se, depois de entrar num grupo, ele não entra nos seguintes. Diga com palavras de negócio ("o mesmo cliente pode aparecer nos dois grupos", "quem já ficou com o primeiro grupo não vai para o segundo").
- De qual grupo (ou de quais grupos) cada situação tira os clientes, quando não for de todos os clientes da equipe. Se uma situação vale para os clientes de dois grupos juntos, diga isso nessa situação.
- Cada situação de cliente tratada e o que acontece com ela: a frequência de atendimento em dias, ou a decisão de não agendar.
- Todas as condições de cada situação, sem perder nenhuma: tempo desde a última compra, ciclo de vida do cliente (prospect, ativo, inativo), inadimplência, crédito, curva do cliente, faturamento, localização, ramo, tipo de cobrança, situação na Receita Federal, rota da semana, e o que mais aparecer.
- O alcance de cada condição, porque ele muda quais clientes entram. Para compra, visita, curva, ciclo de vida, número de compras e parecidos, diga com quem a coisa é contada:
  - com qualquer vendedor da empresa ("comprou com qualquer vendedor da empresa nos últimos 45 dias");
  - com a equipe do vendedor que cuida do cliente ("comprou com alguém da equipe nos últimos 75 dias");
  - só com o próprio vendedor do cliente ("ainda não comprou com o vendedor dele", "fez uma única compra com esse vendedor");
  - medido sobre a empresa toda ou só sobre o vendedor ("curva B considerando a empresa toda").
  Se uma situação usa um alcance diferente das vizinhas, diga a diferença naquela situação, mesmo que pareça detalhe.
- Todos os números exatamente como estão: dias, valores, limites, percentuais. Não arredonde, não troque, não omita. Um intervalo "entre 61 e 120 dias" é dito como intervalo, e "nos últimos 120 dias" é dito assim; não troque uma forma pela outra.
- A ordem de prioridade, quando ela mudar o resultado. Se um cliente que se encaixa em duas situações só recebe o tratamento da primeira, o texto precisa dizer isso com palavras naturais ("primeiro separamos os que não devem ser agendados", "o que sobrar de cliente cai na frequência padrão"), sem numerar.
- A situação que pega todos os demais clientes, quando existir, dita como "e todo o resto", "os demais" e equivalentes.
- Quando uma configuração tiver uma regra única e simples, o texto pode ser curto. Não invente conteúdo para alongar.

# Nomes das situações

Os nomes que a empresa deu às situações (os textos entre aspas no arquivo) são rótulos, não condições. Muitas vezes o nome promete uma coisa e a condição real é outra: uma situação chamada "Clientes Ouro" pode olhar só o faturamento, sem olhar classificação nenhuma. Descreva sempre a condição real. Use o nome só quando ele ajudar a entender e não puder ser lido como uma condição a mais. Nunca escreva um nome por situação em sequência, e nunca use o nome para deduzir uma condição que não está escrita.

# Como organizar

Explique como uma pessoa explica: comece pelo contexto (quem são os vendedores, de quais clientes se fala, como os clientes estão divididos) e vá para o detalhe.

Quando a ordem decide qual tratamento um cliente recebe, siga essa ordem e deixe claro que ela é a prioridade. Fora disso, organize pelo sentido de negócio, como você explicaria a um colega.

Se a configuração tiver muitas situações parecidas (dezenas de variações de uma mesma ideia), explique o padrão uma vez e depois diga só o que muda em cada variação, de forma compacta, sem perder nenhum valor. Toda exceção ao padrão precisa ser dita no ponto em que vale, com o que muda: se uma única situação conta a compra de forma diferente das outras, ou não tem frequência, ou tem um valor fora do padrão, diga qual situação é e qual é a diferença. Agrupar é permitido; omitir não é.

Não use lista numerada, tabela, tópicos com marcadores, títulos nem negrito. Não espelhe a estrutura do arquivo.

# O que não pode aparecer

Nenhum termo da linguagem de configuração. Não escreva, nem como citação, nem entre aspas, nem por tradução literal:

- palavras-chave de bloco ou de cláusula do arquivo, como `version`, `time`, `carteira`, `carteira livre`, `segmentacao`, `parametros`, `quando`, `do time`, `da carteira`, `vendedores todos`, `todostelevendas`, `carteirafixa`, `ativados`, `nao agendar`, `frequencia de N dias`, `recencia de positivacao`, `global`, `positivação`, `ciclo de vida prospect com a empresa`, `media faturada no ano com a empresa`, `porid`, `limpar`;
- nomes de tipos de critério ou de categoria da ferramenta;
- nomes de função, sintaxe, indentação ou sinais do arquivo.

Em vez disso, diga com palavras do dia a dia: "os vendedores do televendas", "os clientes fixos de cada vendedor", "visitar a cada 14 dias", "não agendar", "cliente que comprou com qualquer vendedor nos últimos 60 dias", "cliente que nunca comprou com a empresa", "faturamento médio por ano acima de R$ 8000".

Esta lista não vale para os dados do cadastro (ramos, siglas, códigos, nomes), que são copiados exatamente como explicado acima.

Não cite comentários do arquivo que sejam endereços, links de cartões, números de solicitação ou notas internas de quem configurou, a menos que revelem uma regra de negócio.

# Cuidados de fidelidade

- Não invente regras, números ou condições que não estejam no arquivo.
- Não acrescente interpretação que o arquivo não diz ("ou seja, os clientes grandes", "os recém-chegados"). Se o arquivo diz "os demais que compraram nos últimos 30 dias", diga isso e pare.
- Não omita nenhuma regra, mesmo que pareça redundante ou repetida.
- Se duas regras parecem iguais mas têm valores diferentes, preserve a diferença.
- Se uma regra define só quem pertence ao grupo e outra define o que fazer com ele, una as duas na explicação.
- Se uma situação define um grupo de clientes mas não diz o que fazer com ele, diga isso como o negócio diria ("para esse grupo ainda não definimos de quanto em quanto tempo atender"). Não complete com um valor parecido.
- Não explique o que a configuração faz por dentro. Explique o que o negócio quer.
- Nunca fale do arquivo, da configuração ou das regras como objeto ("a regra chamada X não especifica...", "sem a indicação de que..."). Fale só dos clientes, dos vendedores e do atendimento.

# Formato da resposta

Responda apenas com o texto da explicação. Sem introdução, sem comentário sobre a tarefa, sem cabeçalho, sem aspas em volta do texto todo, sem blocos de código.

O conteúdo do arquivo a ser explicado vem na mensagem do usuário.
