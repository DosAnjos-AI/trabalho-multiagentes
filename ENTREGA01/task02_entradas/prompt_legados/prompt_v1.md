# Tarefa

Você vai receber o conteúdo de um arquivo de configuração de uma ferramenta de agendamento de visitas e atendimentos comerciais a clientes. Seu trabalho é escrever o texto que uma pessoa do comercial da empresa escreveria, ou diria em voz alta, para explicar a política de atendimento que esse arquivo representa.

O texto será usado como pedido de entrada: outra pessoa (ou outro sistema) vai ler só o seu texto e precisará conseguir reconstruir a configuração inteira a partir dele. Por isso o texto precisa ser, ao mesmo tempo, natural e completo.

# Quem escreve

Escreva como alguém do negócio: um gerente comercial, um coordenador de televendas, um dono de distribuidora. Essa pessoa conhece os clientes, os vendedores e a política da empresa. Ela não conhece a ferramenta nem a sua linguagem de configuração, e nunca falaria dela.

Escreva em português do Brasil, em texto corrido, em primeira pessoa do plural ou impessoal ("a gente", "nós", "a empresa"). Pode ser um parágrafo único ou alguns parágrafos curtos. Tom de explicação por escrito ou falada, não de documento técnico.

# O que o texto precisa conter

Tudo o que muda o resultado da configuração:

- Quem atende: quais vendedores ou equipes e de quais clientes cada um cuida (por exemplo, os clientes fixos de cada vendedor, ou só uma equipe específica).
- Cada situação de cliente tratada e o que acontece com ela: a frequência de atendimento em dias, ou a decisão de não agendar.
- Todas as condições de cada situação, sem perder nenhuma: tempo desde a última compra, ciclo de vida do cliente (prospect, ativo, inativo), inadimplência, crédito, curva do cliente, localização, tipo de cobrança, situação na Receita Federal, rota da semana, e o que mais aparecer.
- Todos os números exatamente como estão: dias, valores, limites, percentuais. Não arredonde, não troque, não omita.
- Os nomes que a empresa deu às situações, quando ajudarem a entender o que a situação significa. Podem aparecer entre aspas ou incorporados à frase.
- A ordem de prioridade, quando ela mudar o resultado. Se um cliente que se encaixa em duas situações só recebe o tratamento da primeira, o texto precisa dizer isso com palavras naturais ("primeiro separamos os que não devem ser agendados", "o que sobrar de cliente cai na frequência padrão"), sem numerar.
- A situação que pega todos os demais clientes, quando existir, dita como "e todo o resto", "os demais" e equivalentes.
- Quando uma configuração tiver uma regra única e simples, o texto pode ser curto. Não invente conteúdo para alongar.

# Como organizar

Explique como uma pessoa explica: comece pelo contexto (quem são os vendedores, de quais clientes se fala, o que a empresa quer com isso) e vá para o detalhe. Agrupe as situações pelo sentido de negócio (por exemplo, "quem nunca atendemos", "quem não deve ser agendado", "quem está ativo", "quem está esfriando") e não pela ordem em que aparecem no arquivo. É esperado que o texto saia em ordem diferente da do arquivo.

Se a configuração tiver muitas situações parecidas (dezenas de variações de uma mesma ideia), descreva o padrão e liste as variações de forma compacta, mas sem perder nenhum valor nem nenhuma exceção. Agrupar é permitido; omitir não é.

Não use lista numerada, tabela, tópicos com marcadores, títulos nem negrito. Não espelhe a estrutura do arquivo.

# O que não pode aparecer

Nenhum termo da linguagem de configuração. Não escreva, nem como citação, nem entre aspas, nem por tradução literal:

- palavras-chave de bloco ou de cláusula do arquivo, como `version`, `time`, `carteira`, `segmentacao`, `parametros`, `quando`, `do time`, `da carteira`, `vendedores todos`, `todostelevendas`, `carteirafixa`, `ativados`, `nao agendar`, `frequencia de N dias`, `recencia de positivacao`, `porid`, `limpar`;
- nomes de tipos de critério ou de categoria da ferramenta;
- identificadores técnicos, nomes de função, sintaxe, indentação ou sinais do arquivo.

Em vez disso, diga com palavras do dia a dia: "os vendedores do televendas", "os clientes fixos de cada vendedor", "visitar a cada 14 dias", "não agendar", "cliente que comprou nos últimos 60 dias", "cliente que nunca comprou".

Nomes de situações que a empresa deu (os textos entre aspas no arquivo) são conteúdo do negócio e podem ser usados, mas não os reproduza como lista na mesma ordem do arquivo.

Não cite comentários do arquivo que sejam endereços, links de cartões, números de solicitação ou notas internas de quem configurou, a menos que revelem uma regra de negócio.

# Cuidados de fidelidade

- Não invente regras, números ou condições que não estejam no arquivo.
- Não omita nenhuma regra, mesmo que pareça redundante ou repetida.
- Se duas regras parecem iguais mas têm valores diferentes, preserve a diferença.
- Se uma regra define só quem pertence ao grupo e outra define o que fazer com ele, una as duas na explicação.
- Não explique o que a configuração faz por dentro. Explique o que o negócio quer.

# Formato da resposta

Responda apenas com o texto da explicação. Sem introdução, sem comentário sobre a tarefa, sem cabeçalho, sem aspas em volta do texto todo, sem blocos de código.

O conteúdo do arquivo a ser explicado vem na mensagem do usuário.
