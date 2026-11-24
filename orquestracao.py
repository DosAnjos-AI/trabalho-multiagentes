"""Mapa do grafo do agente GOBR. Somente declarativo: strings, listas e dicts, sem import, sem classe, sem chamada.

E a fonte unica do fluxo: src/script10_orquestracao/ le este arquivo e monta o grafo a partir dele. Para mudar uma
ligacao, edite aqui; o codigo nao guarda mapa proprio.

Fluxo:
    primeira geracao:  START -> normalizacao -> recuperacao -> geracao -> END
    reexecucao:        START -> normalizacao_pedido -> recuperacao -> geracao_reexecucao -> END
A escolha acontece em duas arestas condicionais (saida do START e saida da recuperacao), ambas pelo campo
`pedido_mudanca` do estado: vazio e primeira geracao, preenchido e reexecucao.
"""

# Campo do estado -> (tipo, para que serve). Tipos aceitos: texto, texto_ou_nada, lista, lista_acumulada, numero, objeto.
# lista_acumulada: cada no devolve so o item novo e o grafo acrescenta ao que ja existe.
ESTADO = {
    "id_sessao": ("texto", "identifica a conversa; entra no id do turno enviado ao no 50"),
    "descricao_usuario": ("texto", "o que a pessoa descreveu no primeiro turno; nao muda depois"),
    "pedido_mudanca": ("texto_ou_nada", "pedido de mudanca do turno; vazio na primeira geracao"),
    "descricao_normalizada": ("texto", "descricao atual, ja normalizada; na reexecucao incorpora o pedido"),
    "regras_consulta": ("lista", "caminhos do manual que a descricao exige (saida do no 50)"),
    "recuperacao": ("objeto", "exemplos, recorte do manual e apoio devolvidos pelo no 60"),
    "gobr_atual": ("texto_ou_nada", ".gobr vigente; a reexecucao parte dele"),
    "custo_turno": ("numero", "gasto do turno em dolares, somado nos tres nos"),
    "historico": ("lista_acumulada", "um registro por turno: numero, tipo, entrada, .gobr e custo"),
}

# Agentes: nos que chamam modelo de linguagem. `modulo` e pasta.script em src/ que traz construir_contexto(config).
AGENTES = {
    "normalizador": {"modulo": "script50_normalizacao.script50_normalizacao", "papel": "limpa a fala da pessoa e indica as secoes do manual"},
    "gerador": {"modulo": "script80_geracao.script80_geracao", "papel": "escreve o .gobr; na reexecucao recebe o anterior e o pedido"},
}

# Tools: nos que consultam dados sem modelo de linguagem de geracao.
TOOLS = {
    "recuperador": {"modulo": "script60_recuperacao.script60_recuperacao", "papel": "exemplos por busca densa e Jaccard, mais o recorte do manual"},
}

# No -> `executa` (funcao de src/script10_orquestracao) e `usa` (chave de AGENTES ou TOOLS).
NOS = {
    "normalizacao": {"executa": "normalizar_descricao", "usa": "normalizador"},
    "normalizacao_pedido": {"executa": "normalizar_descricao_com_pedido", "usa": "normalizador"},
    "recuperacao": {"executa": "recuperar_exemplos", "usa": "recuperador"},
    "geracao": {"executa": "gerar_primeira", "usa": "gerador"},
    "geracao_reexecucao": {"executa": "gerar_reexecucao", "usa": "gerador"},
}

# Arestas fixas (origem, destino). "START" e "END" sao os extremos do grafo.
ARESTAS = [
    ("normalizacao", "recuperacao"),
    ("normalizacao_pedido", "recuperacao"),
    ("geracao", "END"),
    ("geracao_reexecucao", "END"),
]

# Arestas condicionais: olham o campo do estado; vazio segue para `vazio`, preenchido para `preenchido`.
ARESTAS_CONDICIONAIS = [
    {"origem": "START", "campo": "pedido_mudanca", "vazio": "normalizacao", "preenchido": "normalizacao_pedido"},
    {"origem": "recuperacao", "campo": "pedido_mudanca", "vazio": "geracao", "preenchido": "geracao_reexecucao"},
]

# Memoria entre turnos do mesmo id de conversa: "em_memoria" guarda o estado no processo, sem disco.
MEMORIA = "em_memoria"
