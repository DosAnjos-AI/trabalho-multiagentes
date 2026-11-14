"""Lista fechada dos itens que o manual exige de todo arquivo .gobr, e vocabulario documentado.

Fonte unica: o manual original do fornecedor, govendas-rules.pdf (v0.89.0, gramatica 1.0).
A versao parseada em manual/ aparece apenas como referencia cruzada, porque nao contem
o capitulo 1 nem a secao 2.1 do original.

Convencao de pagina: "pdf p.N" e a pagina do arquivo PDF; "impressa p.M" e o numero
impresso no rodape. No capitulo 1 em diante, pdf = impressa + 4.

Este modulo so contem dados. A logica de conferencia fica em conferidor.py.
"""

from dataclasses import dataclass

# Categorias de achado. A terceira nao e falha do arquivo: por decisao do Mestre,
# onde o manual nao documenta, o exemplo da base sobrepoe o manual.
AUSENTE = "item_obrigatorio_ausente"
DIVERGENCIA = "divergencia_com_manual"
NAO_DOCUMENTADA = "construcao_nao_documentada"
CATEGORIAS = (AUSENTE, DIVERGENCIA, NAO_DOCUMENTADA)
CATEGORIAS_DE_FALHA = (AUSENTE, DIVERGENCIA)


@dataclass(frozen=True)
class ItemObrigatorio:
    identificador: str
    descricao: str
    origem: str
    citacao: str
    verificavel: bool
    categoria: str


ITENS: tuple[ItemObrigatorio, ...] = (
    # ---------------------------------------------------------------- forma do arquivo
    ItemObrigatorio(
        "version_no_inicio",
        "A primeira linha significativa (fora comentario e linha vazia) e exatamente 'version 1.0'.",
        "pdf p.9 (impressa p.5), sec. 3.1; pdf p.61 (impressa p.57), sec. 10; "
        "manual/02-invariantes.md, manual/03-secoes/10-gramatica.md",
        "A linha version 1.0 é obrigatória e deve aparecer no início de cada arquivo",
        True,
        AUSENTE,
    ),
    ItemObrigatorio(
        "version_unica",
        "A declaracao 'version' aparece uma unica vez: a gramatica preve um so 'version' no topo.",
        "pdf p.61 (impressa p.57), sec. 10; manual/03-secoes/10-gramatica.md",
        "gorules: version ( regrapadrao | times segmentacoes ( ... ) ) end",
        True,
        DIVERGENCIA,
    ),
    ItemObrigatorio(
        "ao_menos_um_time",
        "O arquivo define pelo menos um bloco 'time'.",
        "pdf p.61 (impressa p.57), sec. 10; manual/03-secoes/10-gramatica.md",
        "deve sempre começar com version 1.0, definir pelo menos um time",
        True,
        AUSENTE,
    ),
    ItemObrigatorio(
        "categoria_final_presente",
        "Depois dos times e segmentacoes, o arquivo tem ao menos uma carteira, parametros, alerta ou tag.",
        "pdf p.61 (impressa p.57), sec. 10; manual/03-secoes/10-gramatica.md",
        "e então conter uma das combinações: somente carteiras, somente parâmetros",
        True,
        AUSENTE,
    ),
    ItemObrigatorio(
        "ordem_das_categorias",
        "Os blocos seguem a ordem time, segmentacao, carteira, e por ultimo parametros, alertas ou tags.",
        "pdf p.7 (impressa p.3), sec. 2.2; pdf p.61 (impressa p.57), sec. 10; "
        "manual/02-invariantes.md (Ordem entre blocos)",
        "pode conter até quatro categorias de regras, usadas em sequência",
        True,
        DIVERGENCIA,
    ),
    ItemObrigatorio(
        "categorias_terminais_exclusivas",
        "Parametros, alertas e tags nao se misturam no mesmo arquivo.",
        "pdf p.51 (impressa p.47), sec. 8; pdf p.61 (impressa p.57), sec. 10; "
        "manual/02-invariantes.md, manual/03-secoes/08-01-alertas-estrutura-e-gatilhos.md",
        "não é possível combinar regras de parametrização e alertas no mesmo conjunto",
        True,
        DIVERGENCIA,
    ),
    ItemObrigatorio(
        "cabecalho_bem_formado",
        "Cabecalho de bloco e palavra-chave, nome entre aspas duplas sem aspas internas, e dois-pontos.",
        "pdf p.9 (impressa p.5), sec. 3.1; pdf p.62 (impressa p.58), sec. 10; "
        "manual/02-invariantes.md (Forma). Os dois-pontos vem dos exemplos, nao de regra escrita",
        "seguida de um nome entre aspas duplas",
        True,
        DIVERGENCIA,
    ),
    ItemObrigatorio(
        "aspas_balanceadas",
        "Toda string aberta com aspas duplas e fechada dentro da mesma clausula.",
        "pdf p.61-62 (impressa p.57-58), sec. 10; manual/03-secoes/10-gramatica.md",
        'String: "texto entre aspas duplas"',
        True,
        DIVERGENCIA,
    ),
    ItemObrigatorio(
        "parenteses_balanceados",
        "Todo parentese aberto numa clausula e fechado dentro da mesma clausula.",
        "pdf p.10 (impressa p.6), sec. 3.3; pdf p.32 (impressa p.28), sec. 6.6; "
        "toda funcao documentada tem a forma nome(argumentos)",
        'porid("id1", "id2", ...)',
        True,
        DIVERGENCIA,
    ),
    ItemObrigatorio(
        "caractere_fora_do_lexico",
        "O texto nao contem caractere de controle invisivel (fora tabulacao e quebra de linha).",
        "pdf p.62 (impressa p.58), sec. 10, regras lexicais; manual/03-secoes/10-gramatica.md",
        "Strings aceitam letras, números, espaços e símbolos especiais",
        True,
        DIVERGENCIA,
    ),
    ItemObrigatorio(
        "nomes_de_time_distintos",
        "Nao ha dois times com o mesmo nome no arquivo.",
        "pdf p.11 (impressa p.7), sec. 3.5; manual/03-secoes/03-01-times.md",
        "os nomes dos times devem ser distintos entre si no mesmo arquivo",
        True,
        DIVERGENCIA,
    ),
    ItemObrigatorio(
        "nomes_carteira_segmentacao_distintos",
        "Nao ha duas carteiras ou segmentacoes com o mesmo nome no arquivo.",
        "pdf p.21 (impressa p.17), sec. 4.7; manual/03-secoes/04-01-carteiras-e-segmentacoes.md",
        "os nomes das carteiras e das segmentações devem ser distintos entre si",
        True,
        DIVERGENCIA,
    ),
    ItemObrigatorio(
        "nomes_parametros_distintos",
        "Nao ha dois blocos de parametros com o mesmo nome no arquivo.",
        "pdf p.50 (impressa p.46), sec. 7.6; manual/03-secoes/07-01-parametros-estrutura-e-exemplos.md",
        "os nomes dos blocos de parâmetros devem ser distintos",
        True,
        DIVERGENCIA,
    ),
    ItemObrigatorio(
        "nomes_alertas_distintos",
        "Nao ha dois alertas com o mesmo nome no arquivo.",
        "pdf p.58 (impressa p.54), sec. 8.8; manual/03-secoes/08-02-alertas-entrega-e-variaveis.md",
        "os nomes dos alertas devem ser distintos",
        True,
        DIVERGENCIA,
    ),
    # ---------------------------------------------------------------- conteudo dos blocos
    ItemObrigatorio(
        "time_tem_vendedores",
        "Todo bloco 'time' tem ao menos uma linha 'vendedores <selecao>'.",
        "pdf p.9 (impressa p.5), sec. 3.1; manual/03-secoes/03-01-times.md",
        "A palavra-chave vendedores define qual conjunto de vendedores pertence ao time",
        True,
        AUSENTE,
    ),
    ItemObrigatorio(
        "carteira_segmentacao_tem_clientes",
        "Todo bloco 'carteira' ou 'segmentacao' tem ao menos uma linha 'clientes <selecao>'.",
        "pdf p.8 (impressa p.4), sec. 2.2; pdf p.19 (impressa p.15), sec. 4.6; "
        "manual/03-secoes/04-01-carteiras-e-segmentacoes.md",
        "A seleção de clientes é feita por meio das seguintes funções",
        True,
        AUSENTE,
    ),
    ItemObrigatorio(
        "carteira_uma_segmentacao",
        "Uma carteira usa no maximo uma segmentacao como fonte de clientes.",
        "pdf p.18 (impressa p.14), sec. 4.5; manual/03-secoes/04-01-carteiras-e-segmentacoes.md",
        "na criação de uma carteira só é permitida a inclusão de uma única segmentação",
        True,
        DIVERGENCIA,
    ),
    ItemObrigatorio(
        "referencia_a_nome_definido",
        "Todo nome referenciado (time, carteira, segmentacao) esta definido em algum bloco do arquivo.",
        "pdf p.9 (impressa p.5), sec. 3.1; pdf p.19 (impressa p.15), sec. 4.6; "
        "manual/03-secoes/04-02-selecao-clientes-ruptura.md",
        "Seleciona os clientes pertencentes a uma segmentação já definida",
        True,
        AUSENTE,
    ),
    ItemObrigatorio(
        "parametros_tem_fonte",
        "Todo bloco de parametros (inclusive 'limpar parametros') abre com a fonte de clientes.",
        "pdf p.42 (impressa p.38), sec. 7.1; pdf p.47 (impressa p.43), sec. 7.3.11; "
        "manual/03-secoes/07-01-parametros-estrutura-e-exemplos.md",
        "Definir a fonte de clientes — referencia uma carteira, segmentação ou time",
        True,
        AUSENTE,
    ),
    ItemObrigatorio(
        "parametros_tem_atendimento",
        "Todo bloco 'parametros' define ao menos um parametro de atendimento (etapa nao marcada como opcional).",
        "pdf p.42 (impressa p.38), sec. 7.1; manual/03-secoes/07-01-parametros-estrutura-e-exemplos.md",
        "Definir os parâmetros de atendimento — frequência, preferência de dias, roteirização",
        True,
        AUSENTE,
    ),
    ItemObrigatorio(
        "parametros_ordem_das_etapas",
        "Etapas de parametros na ordem: fonte, filtro temporal, quando, atendimento, sem choque.",
        "pdf p.42 (impressa p.38), sec. 7.1; manual/02-invariantes.md (Ordem dentro do bloco)",
        "Uma regra de parâmetros segue sempre este fluxo",
        True,
        DIVERGENCIA,
    ),
    ItemObrigatorio(
        "nao_agendar_exclusivo",
        "Bloco com 'nao agendar' nao define frequencia nem preferencia.",
        "pdf p.44 (impressa p.40), sec. 7.3.4; manual/03-secoes/07-01-parametros-estrutura-e-exemplos.md",
        "não é possível definir frequência ou preferência de dias na mesma regra",
        True,
        DIVERGENCIA,
    ),
    ItemObrigatorio(
        "filtros_temporais_em_ordem",
        "Filtros temporais na ordem dia do mes, dia da semana, semana do mes, mes do ano, horario.",
        "pdf p.22 (impressa p.18), sec. 5.1; manual/03-secoes/05-01-filtros-temporais-calendario.md",
        "os filtros devem ser escritos sempre nesta ordem",
        True,
        DIVERGENCIA,
    ),
    ItemObrigatorio(
        "horario_somente_em_alertas",
        "Filtro de horario ('às', 'de hora em hora') so aparece em bloco de alerta.",
        "pdf p.24 (impressa p.20), sec. 5.6; manual/03-secoes/05-02-filtros-de-horario-alertas.md",
        "Os filtros de horário se aplicam exclusivamente a regras de alertas",
        True,
        DIVERGENCIA,
    ),
    ItemObrigatorio(
        "uma_regra_de_horario",
        "Um bloco usa no maximo uma forma de horario: 'às' ou 'de hora em hora'.",
        "pdf p.25 (impressa p.21), sec. 5.6; manual/03-secoes/05-02-filtros-de-horario-alertas.md",
        "só é permitido usar uma das regras de horário por vez",
        True,
        DIVERGENCIA,
    ),
    ItemObrigatorio(
        "alerta_tem_etapas_obrigatorias",
        "Alerta tem fonte, filtro temporal, 'onde', 'informe', 'entregue' e 'pelos canais' (etapas sem 'opcional').",
        "pdf p.51 (impressa p.47), sec. 8.1; manual/03-secoes/08-01-alertas-estrutura-e-gatilhos.md",
        "Definir o gatilho — condição que aciona o alerta (com onde)",
        True,
        AUSENTE,
    ),
    ItemObrigatorio(
        "alerta_ordem_das_etapas",
        "Etapas do alerta na ordem: fonte, temporal, quando, onde, informe, descreva, entregue, pelos canais.",
        "pdf p.51 (impressa p.47), sec. 8.1; manual/02-invariantes.md (Ordem dentro do bloco)",
        "Uma regra de alerta segue as seguintes etapas",
        True,
        DIVERGENCIA,
    ),
    # ---------------------------------------------------------------- vocabulario
    ItemObrigatorio(
        "grafia_documentada",
        "Construcao que o manual documenta e escrita com a mesma caixa do manual (acento e livre, p.58).",
        "pdf p.32 (impressa p.28), sec. 6.7; pdf p.62 (impressa p.58), sec. 10; "
        "manual/03-secoes/06-07-curva-abc-ciclo-de-vida.md",
        "curva C com a empresa",
        True,
        DIVERGENCIA,
    ),
    ItemObrigatorio(
        "vocabulario_do_manual",
        "Cada clausula usa construcao listada no manual. Achado aqui NAO e falha: alimenta o inventario.",
        "pdf p.10-11, 19-20, 22-41, 43-49, 53-55 (impressa p.6-7, 15-16, 18-37, 39-45, 49-51); "
        "manual/03-secoes/*.md",
        "A seleção de clientes é feita por meio das seguintes funções",
        True,
        NAO_DOCUMENTADA,
    ),
    # ---------------------------------------------------------------- nao verificaveis
    ItemObrigatorio(
        "configuracao_do_conjunto",
        "O conjunto tem nome, tipo de execucao, ID da empresa e flag de habilitado, fora do texto da regra.",
        "pdf p.6 (impressa p.2), sec. 1.3; ausente de manual/ (capitulo 1 nao parseado)",
        "Para configurar um conjunto de regras são necessários",
        False,
        AUSENTE,
    ),
    ItemObrigatorio(
        "vendedores_cadastrados",
        "Todo vendedor referenciado esta cadastrado no Govendas.",
        "pdf p.11 (impressa p.7), sec. 3.5; manual/03-secoes/03-01-times.md",
        "todos os vendedores referenciados devem estar cadastrados no Govendas",
        False,
        AUSENTE,
    ),
    ItemObrigatorio(
        "nomes_alertas_distintos_entre_conjuntos",
        "Nomes de alerta distintos entre conjuntos de regras diferentes da mesma empresa.",
        "pdf p.58 (impressa p.54), sec. 8.8; manual/03-secoes/08-02-alertas-entrega-e-variaveis.md",
        "inclusive entre conjuntos de regras diferentes da mesma empresa",
        False,
        DIVERGENCIA,
    ),
    ItemObrigatorio(
        "regra_por_time",
        "Regras se aplicam a times ou carteiras, nao a vendedor individual.",
        "pdf p.20 (impressa p.16), sec. 4.7; pdf p.50 e p.58 (impressa p.46 e p.54); "
        "manual/03-secoes/04-01-carteiras-e-segmentacoes.md",
        "toda regra deve ser aplicada a um time, não diretamente a um vendedor individual",
        False,
        DIVERGENCIA,
    ),
    ItemObrigatorio(
        "regrapadrao",
        "Alternativa 'regrapadrao' da gramatica: o manual nao descreve a sintaxe.",
        "pdf p.61 (impressa p.57), sec. 10; manual/03-secoes/10-gramatica.md",
        "regrapadrao |",
        False,
        DIVERGENCIA,
    ),
    ItemObrigatorio(
        "sintaxe_do_bloco_tags",
        "Bloco de tags: o manual lista gatilhos e filtros mas nao mostra a sintaxe do bloco.",
        "pdf p.59-60 (impressa p.55-56), sec. 9; manual/03-secoes/09-01-tags.md",
        "Os gatilhos disponíveis para tags são distintos dos gatilhos de alertas",
        False,
        DIVERGENCIA,
    ),
)

ITENS_POR_ID: dict[str, ItemObrigatorio] = {item.identificador: item for item in ITENS}
ITENS_VERIFICAVEIS: tuple[str, ...] = tuple(i.identificador for i in ITENS if i.verificavel)


# =============================================================================
# Vocabulario documentado
# =============================================================================
# Os padroes trabalham sobre texto normalizado pelo conferidor: acento removido
# (exceto a palavra isolada "é", para nao virar a conjuncao "e"), espacos colapsados,
# sem espaco junto a parenteses, ", " entre argumentos. A caixa e preservada: o
# conferidor casa primeiro com caixa exata e, se falhar, sem caixa, para separar
# divergencia de grafia de construcao desconhecida.
#
# Generalizacao: so combino opcoes quando o manual declara a combinacao por escrito
# (ex.: "As duas opções são possíveis: visita ou positivação", p.24). Cada bloco de
# padroes cita a pagina impressa.

_S = r'"[^"]*"'
_LS = r'\(' + _S + r'(?:, ' + _S + r')*\)'
_N = r'\d+'
_VALOR = r'R\$ ?\d+(?:[.,]\d+)*'
_DATA = r"'(?:\d{4}-\d{2}-\d{2}|\d{2}-\d{2}-\d{4})'"
_HORA = r"'\d{2}:\d{2}'"
_UNID = r'(?:anos?|semestres?|trimestres?|bimestres?|mes|meses|semanas?|dias?)'
_UNID_H = r'(?:anos?|semestres?|trimestres?|bimestres?|mes|meses|semanas?|dias?|horas?|minutos?)'
_TEMPO = _N + ' ' + _UNID  # sec. 6.11.1, p.33
_TEMPO_FIXO = (  # sec. 6.11.2, p.33-34
    r'(?:do dia|na semana anterior|na quinzena anterior|no mes anterior|no bimestre anterior'
    r'|no trimestre anterior|no semestre anterior|no ano anterior|na semana|na quinzena|no mes'
    r'|no bimestre|no trimestre|no semestre|no ano|de ontem)'
)
_COND_FUT = (  # sec. 6.13, p.36-37
    r'(?:nos proximos ' + _N + ' ' + _UNID_H + r'|em ' + _N + ' ' + _UNID + r' a frente'
    r'|de ontem|na semana anterior|na quinzena anterior|no mes anterior|no bimestre anterior'
    r'|no trimestre anterior|no semestre anterior|no ano anterior)'
)
# A sec. 6.13 se intitula "Opções para condicionais de tempo em tempo futuro ou intervalo
# no passado": e extensao da 6.12, por isso entra em todo <<condicional de tempo>>.
# A 6.13 vem primeiro porque "em N dias a frente" precisa ganhar de "em N dias".
_COND = (  # sec. 6.12, p.34-36, mais 6.13
    r'(?:' + _COND_FUT[3:-1] + r'|em ' + _N + ' ' + _UNID_H + r'|ha ' + _N + ' ' + _UNID + r' atras'
    r'|na manha|na tarde|na noite|no dia|ontem|na semana|na quinzena|no mes|no bimestre'
    r'|no trimestre|no semestre|no ano|entre ' + _TEMPO + ' e ' + _TEMPO
    + r'|entre ' + _DATA + ' e ' + _DATA + ')'
)
_PERIODO = r'(?:mes|bimestre|trimestre|semestre|ano)'  # p.25 e p.33
_CMP_VALOR = (  # p.25: "podem ser combinados maior que, menor que e igual a utilizando um e"
    r'(?:maior que|menor que|igual a) ' + _VALOR
    + r'(?: e (?:maior que|menor que|igual a) ' + _VALOR + r')*(?: ou indefinido)?'
)
_CMP_N = (  # p.33: "maior que, menor que, ou indefinido ou maior que <<N>> e menor que <<N>>"
    r'(?:maior que ' + _N + ' e menor que ' + _N + r'|(?:maior que|menor que) ' + _N
    + r')(?: ou indefinido)?'
)
_OP_TEXTO = r'(?:igual|diferente|contem|inicia com)'  # p.28
_OP_ID = r'(?:igual|diferente)'  # p.28
_DIA_SEMANA = r'(?:na segunda|na terca|na quarta|na quinta|na sexta(?:-feira)?|no sabado|no domingo)'

# Filtros de clientes, usados apos "quando" (sec. 6, p.22-37).
FILTROS: tuple[tuple[str, str], ...] = (
    # 6.1 atividade e inatividade, p.22-23
    ("ativos( para o vendedor| para a empresa)?", "p.22"),
    ("inativos( para o vendedor| para a empresa)?", "p.22"),
    ("inatividade( global)? de " + _TEMPO, "p.22"),
    ("sem venda ou prospects", "p.22"),
    ("unica compra com (a empresa|o vendedor)", "p.22-23"),
    ("prospects (do vendedor|da empresa)", "p.23"),
    ("tem venda (do vendedor|da empresa) " + _COND, "p.23"),
    ("nao tem venda( do vendedor| da empresa)? " + _COND, "p.23"),
    ("tem " + _N + "% de visita (remota|incerta) " + _TEMPO, "p.23"),
    ("atividade (global |do vendedor )?de " + _TEMPO, "p.23"),
    # 6.2 recencia, p.24: "As duas opções são possíveis: visita ou positivação"
    ("(fora da )?recencia de (visita|positivacao)( global| do vendedor)? " + _COND, "p.24"),
    # 6.3 financeiros, p.24-25
    ("(in)?adimplentes", "p.24"),
    ("(nao )?tem credito", "p.24"),
    ("com limite de " + _VALOR + " de credito", "p.24"),
    ("com " + _VALOR + " de credito", "p.24"),
    ("com menos de " + _VALOR + " de credito disponivel", "p.25"),
    ("com " + _N + "% de credito", "p.25"),
    ("com ticket medio " + _CMP_VALOR, "p.25"),
    ("(total faturado|media faturada) no " + _PERIODO + " com a empresa " + _CMP_VALOR, "p.25"),
    # 6.4 agenda, p.25-26: opcoes padrao, ruptura, complementar; tempo ou tempo fixo
    ("(na|fora da) agenda( padrao| de ruptura| complementar)?( do vendedor| global)? "
     "(de hoje|em " + _TEMPO + "|" + _TEMPO_FIXO + ")", "p.25-26"),
    ("(nao )?agendavel", "p.26"),
    ("(nao )?reagendado( para o vendedor| para a empresa)?", "p.26"),
    # 6.5 localizacao e classificacao, p.26-28
    ("(nome da cidade|nome do bairro|uf do estado|nome da rota|conteudo da nota|nome da nota"
     "|o rotulo|nome do cnae da receita) " + _OP_TEXTO + _LS, "p.26-27"),
    ("cnae( da receita| do erp)? " + _OP_ID + _LS, "p.27"),
    ("status na receita federal definido como (ativa|suspensa|inapta|baixada)", "p.27"),
    ("pessoa (fisica|juridica)", "p.27"),
    ("cliente (principal|filial)", "p.27"),
    ("(nao )?excluidos", "p.27"),
    ("(nao )?bloqueados", "p.27"),
    ("(nao )?tem coordenada confiavel", "p.28"),
    # 6.6 classificacao por id, p.28
    ("(ramo de atividade|codigo da rota|id do cliente principal|id do cliente|tipo de pagamento"
     "|tipo de cobranca) " + _OP_ID + _LS, "p.28"),
    # 6.7 curva ABC e ciclo de vida, p.28-29: "com a empresa ou com o vendedor"
    ("curva [ABC] com (a empresa|o vendedor)", "p.28"),
    ("no ciclo de vida (ativo|inativo|prospect|ativado|reativado) com (a empresa|o vendedor)", "p.29"),
    # 6.8 frequencia e parametros, p.29-30
    ("nao tem parametro( manual)?", "p.29"),
    ("fora da frequencia de venda( indicada( " + _COND + ")?)?( ou maior que " + _TEMPO + ")?", "p.29"),
    ("frequencia historica (maior que " + _TEMPO + "|menor que " + _TEMPO + "|entre " + _TEMPO
     + " e " + _TEMPO + ")( ou indefinida)?", "p.29"),
    ("atendimentos " + _N + "% (menor|maior) que o parametrizado", "p.30"),
    ("a ultima positivacao " + _N + "% (menor|maior) que o ticket medio", "p.30"),
    ("parametro de frequencia " + _N + "% (menor|maior) que o previsto", "p.30"),
    # 6.9 segmentacao, p.30
    ("(nao )?contido na segmentacao" + _LS, "p.30"),
    # 6.10 ruptura, p.30-31
    ("em ruptura global do (bimestre|trimestre|semestre|ano)", "p.30-31"),
    ("(sem|com) contato no ultimo agendamento( para o vendedor| para a empresa)?", "p.31"),
    ("(sem|com) contato nos ultimos " + _N + " agendamentos( para o vendedor| para a empresa)?", "p.31"),
    # 6.11 outros, p.31-33
    ("positivado (de hoje|" + _TEMPO + "|" + _TEMPO_FIXO + ")", "p.31"),
    ("atendimento remoto em " + _TEMPO, "p.31"),
    ("sem perfil com (o vendedor|a empresa)", "p.31"),
    ("total de compras com (o vendedor|a empresa) " + _CMP_N, "p.31"),
    ("compras no " + _PERIODO + " com (o vendedor|a empresa) " + _CMP_N, "p.32"),
    ("queda de faturamento (menor|maior) que " + _N + "%", "p.32"),
    ("cadastrado faz " + _TEMPO, "p.32"),
    ("cadastrado a partir do dia " + _DATA, "p.32"),
    ("elegivel( incluindo roteirizavel)?", "p.32"),
    # p.33: "Podem ser utilizados o <<tempo>>, <<tempo fixo>> ou <<tempo futuro>>"
    ("data da (proxima|ultima) visita do representante (" + _COND + "|" + _TEMPO_FIXO + ")", "p.32"),
    ("data da rota( futura)?( do vendedor)? (" + _COND + "|" + _TEMPO_FIXO + ")", "p.32-33"),
)

# Selecao de vendedores (sec. 3.3, p.6-7). Modificadores opcionais "nesta ordem".
VENDEDORES: tuple[tuple[str, str], ...] = (
    ("vendedores (todos|todostelevendas|todosdecampo)"
     "( dos supervisores" + _LS + "| do supervisor\\(" + _S + "\\))?"
     "( ativados| inativados)?( menos" + _LS + ")?", "p.6-7"),
    ("vendedores porid" + _LS, "p.6"),
)

# Selecao de clientes (sec. 4.6, p.15-16).
_OPCAO_RUPTURA = (
    r"(?:de positivacao\(" + _TEMPO + r"\)|de visita\(" + _TEMPO + r"\)|de inativos\(" + _S
    + ", " + _TEMPO + r"\))(?: ou prospects)?"
)
CLIENTES: tuple[tuple[str, str], ...] = (
    ("clientes (carteirafixa|carteiraacessivel|carteiraruptura|portfolio|todos)\\(" + _S + "\\)", "p.15"),
    ("clientes inativos\\(" + _S + ", " + _TEMPO + "\\)", "p.15"),
    ("clientes segmentados\\(" + _S + "\\)", "p.15"),
    ("clientes ruptura( da segmentacao)?\\(" + _S + " para " + _S + "\\) " + _OPCAO_RUPTURA
     + "( e " + _OPCAO_RUPTURA + ")*", "p.15-16"),
)

# Fonte de parametros e alertas: p.39 (da carteira), p.48 (do time), p.18 (na carteira).
FONTES: tuple[tuple[str, str], ...] = (
    ("(da carteira|do time|na carteira)\\(" + _S + "\\)", "p.18, p.39, p.48"),
)

# Frequencia (sec. 7.4, p.43-45). Cascata com "ou" mostrada na p.41.
_FREQ_FIXA = (
    r"(?:diaria\(\)|semanal\(\)|quinzenal\((?:" + _DATA + r")?\)|mensal\(\)|bimestral\((?:"
    + _DATA + r")?\)|trimestral\(\)|semestral\(\)|anual\(\)|de " + _N + " dias?)"
)
_FREQ_DINAMICA = (
    r"(?:do govendas|do vendedor(?: (?:menos|mais) " + _N + " dias?)?|do historico"
    r"|de qualquer vendedor|de (?:ativos|inativos) (?:da empresa|do vendedor)|remover)"
)
_FREQ_REGRA = "(?:" + _FREQ_FIXA + "|" + _FREQ_DINAMICA + ")"
FREQUENCIA: tuple[tuple[str, str], ...] = (
    ("frequencia " + _FREQ_REGRA + "( ou " + _FREQ_REGRA + ")*", "p.41, p.43-45"),
    # Modificador de limite: documentado so sobre frequencia fixa, isolado (p.44)
    ("frequencia no (maximo|minimo) " + _FREQ_FIXA, "p.44"),
)

# Elementos de preferencia (sec. 7.2-7.3, p.38-42), unidos com "e".
PREFERENCIA_ELEMENTOS: tuple[tuple[str, str], ...] = (
    ("((maior|menor|normal) )?" + _DIA_SEMANA, "p.39-40"),
    ("nos dias uteis", "p.41"),
    ("do historico( ou (remover|nos dias uteis))?", "p.41-42"),
)

# Clausulas simples de parametros (sec. 7.3, p.40-43).
CLAUSULAS_SIMPLES: tuple[tuple[str, str], ...] = (
    ("nao agendar", "p.40"),
    ("roteirizavel", "p.43"),
    ("fixo", "p.43"),
    ("restrito (a partir da|ate a) (primeira|segunda|terceira|quarta) semana", "p.42, p.45"),
    ("sem choque( (na rota|fora da rota|na pasta)( e (na rota|fora da rota|na pasta))*)? "
     "(na carteira|do time)\\(" + _S + "\\)", "p.42"),
)

# Filtros temporais (sec. 5, p.18-21). O inteiro e a familia, para conferir a ordem.
TEMPORAIS: tuple[tuple[str, int, str], ...] = (
    ("no dia " + _N, 1, "p.18"),
    ("no ultimo dia do mes", 1, "p.18"),
    ("(antes|depois) do dia " + _N, 1, "p.18"),
    ("a partir do dia " + _N, 1, "p.19"),
    ("entre os dias " + _N + " e " + _N, 1, "p.19"),
    (_DIA_SEMANA, 2, "p.19"),
    ("todos os dias|nos dias uteis|no fim de semana", 2, "p.19"),
    ("na (primeira|segunda|terceira|quarta|ultima) semana", 3, "p.19-20"),
    ("na (primeira|segunda) quinzena", 3, "p.20"),
    ("em (janeiro|fevereiro|marco|abril|maio|junho|julho|agosto|setembro|outubro|novembro|dezembro)",
     4, "p.20"),
    ("no (primeiro|segundo|terceiro|quarto|quinto|sexto) bimestre", 4, "p.20"),
    ("no (primeiro|segundo|terceiro|quarto) trimestre", 4, "p.20"),
    ("no (primeiro|segundo) semestre", 4, "p.20"),
    ("as " + _HORA + "( e as " + _HORA + ")*", 5, "p.21"),
    ("de hora em hora( entre " + _HORA + " e " + _HORA + "| a partir de " + _HORA + ")?", 5, "p.21"),
)

# Gatilhos de alerta, usados apos "onde" (sec. 8.4, p.49-51).
GATILHOS: tuple[tuple[str, str], ...] = (
    ("(nao )?tem venda( do vendedor)? em " + _TEMPO, "p.50"),
    ("(nao )?tem visita( da empresa)? em " + _TEMPO, "p.50"),
    ("fora da frequencia de venda( indicada)? ou maior que " + _TEMPO, "p.50"),
    ("atendimento " + _N + "% menor que o parametrizado", "p.50"),
    ("nao tem parametro( manual)?", "p.50"),
    ("parametro de frequencia " + _N + "% menor que o previsto", "p.50"),
    ("tem " + _N + "% de visita (remota|incerta) em " + _PERIODO, "p.51"),
    ("ultima positivacao " + _N + "% menor que o ticket medio", "p.51"),
    ("nao tem coordenada confiavel", "p.51"),
    ("tem produtos com promocoes sugeridas", "p.51"),
    ("tem produtos sugeridos", "p.51"),
)
