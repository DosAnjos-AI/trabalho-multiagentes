"""Construtor do grafo do agente GOBR (LangGraph) e os nos adaptados ao grafo.

O mapa (estado, agentes, tools, nos, arestas) mora em orquestracao.py, na raiz; aqui nao ha mapa proprio. O construtor
le aquele arquivo, resolve cada modulo por nome e liga as funcoes dos nos 30, 50, 60, 80 e 90. Cada no devolve so os campos
do estado que muda. Em disco nada e escrito; no BigQuery so o no 90 escreve, uma linha por aprovacao.

Uso (a raiz do projeto e `src/` precisam estar no sys.path):
    grafo = construir_grafo(config, orquestracao)
    cfg = {"configurable": {"thread_id": "conversa1"}}
    grafo.invoke({"id_sessao": "conversa1", "entrada_bruta": "...", "tipo_entrada": "texto"}, cfg)  # primeira geracao
    grafo.invoke({"entrada_bruta": "...", "tipo_entrada": "texto", "pedido_mudanca": "..."}, cfg)  # reexecucao
"""
import importlib
import operator
from dataclasses import asdict
from types import ModuleType
from typing import Annotated, TypedDict

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph

ARQ_ORQUESTRACAO = "orquestracao.py"
TIPOS_ESTADO = {
    "texto": str, "texto_ou_nada": str | None, "lista": list, "lista_acumulada": Annotated[list, operator.add],
    "numero": float, "objeto": object,
}
EXTREMOS = {"START": START, "END": END}
MEMORIAS = {"em_memoria": MemorySaver}


class ErroOrquestracao(ValueError):
    """Mapa invalido; diz o valor recebido, os aceitos e onde configurar."""


class ErroNo(RuntimeError):
    """Um no recebeu estado incompleto ou o no que ele chama devolveu falha; o grafo para sem escolher por conta propria."""


# ============================================================================
# NOS (estado, modulo, contexto) -> campos do estado que mudam
# ============================================================================

def _turno(estado: dict) -> int:
    return len(estado.get("historico", [])) + 1


def classificar_entrada_turno(estado: dict, modulo: ModuleType, ctx) -> dict:
    """No 30: o turno e de mudanca quando o agente ja pos o pedido no estado. O texto devolvido vai para o campo
    que o no 50 le (descricao_usuario ou pedido_mudanca); `entrada_bruta` fica so como registro."""
    turno = "mudanca" if estado.get("pedido_mudanca") else "primeiro"
    r = modulo.classificar_entrada(estado["tipo_entrada"], turno, estado["entrada_bruta"], ctx)
    campo = "pedido_mudanca" if turno == "mudanca" else "descricao_usuario"
    # custo_turno comeca aqui: o gasto do turno anterior ja foi contado no total do agente.py.
    return {"tipo_entrada": r.tipo, campo: r.texto, "status_entrada": r.status, "faltantes": r.faltantes,
            "custo_turno": r.custo_usd}


def _normalizar(texto: str, estado: dict, modulo: ModuleType, ctx) -> dict:
    # tipo_entrada vem do no 30, nunca fixo aqui; o texto chega sem transformacao.
    r = modulo.normalizar_turno(texto, "usuario", estado["tipo_entrada"],
                                f"{estado['id_sessao']}-turno{_turno(estado)}", ctx)
    if not r.ok:
        raise ErroNo(f"no 50 falhou: {r.erros}; resposta: {r.resposta_crua[:300]!r}")
    return {"descricao_normalizada": r.texto_normalizado, "regras_consulta": r.regras_extraidas["regras_extraidas"],
            "sem_chave": r.regras_extraidas["sem_chave"], "metadados_normalizado": r.metadados,
            "custo_turno": estado["custo_turno"] + float(r.metadados["custo_usd"])}


def normalizar_descricao(estado: dict, modulo: ModuleType, ctx) -> dict:
    return _normalizar(estado["descricao_usuario"], estado, modulo, ctx)


def normalizar_descricao_com_pedido(estado: dict, modulo: ModuleType, ctx) -> dict:
    """Consulta composta: a descricao vigente e o pedido seguem juntos, e o no 50 indica o manual para os dois."""
    if not estado.get("gobr_atual"):
        raise ErroNo("pedido_mudanca recebido sem gobr_atual: nao ha regra anterior para alterar. "
                     "Faca a primeira geracao antes, no mesmo id de conversa.")
    return _normalizar(f"{estado['descricao_normalizada']}\n\nPedido de mudanca: {estado['pedido_mudanca']}",
                       estado, modulo, ctx)


def recuperar_exemplos(estado: dict, modulo: ModuleType, ctx) -> dict:
    rec = modulo.recuperar(estado["descricao_normalizada"], estado["regras_consulta"], ctx)
    # Dicionario simples no estado: o objeto Recuperacao nao precisa atravessar a memoria do grafo.
    return {"recuperacao": asdict(rec), "custo_turno": estado["custo_turno"] + rec.custo_usd}


def _gerar(estado: dict, modulo: ModuleType, ctx, tipo: str, **reexecucao) -> dict:
    rec = estado["recuperacao"]
    r = modulo.gerar_gobr(estado["descricao_normalizada"], rec["exemplos"], rec["secoes_manual"], rec["apoio"], ctx,
                          **reexecucao)
    if not r.ok:
        raise ErroNo(f"no 80 falhou: {r.erros}")
    custo = estado["custo_turno"] + float(r.metadados["custo_usd"])
    entrada = estado["pedido_mudanca"] if reexecucao else estado["descricao_usuario"]
    return {"gobr_atual": r.texto_gobr, "custo_turno": custo, "metadados_geracao": r.metadados,
            "historico": [{"turno": _turno(estado), "tipo": tipo, "entrada": entrada, "gobr": r.texto_gobr,
                           "custo_usd": custo}]}


def gerar_primeira(estado: dict, modulo: ModuleType, ctx) -> dict:
    return _gerar(estado, modulo, ctx, "primeira")


def gerar_reexecucao(estado: dict, modulo: ModuleType, ctx) -> dict:
    return _gerar(estado, modulo, ctx, "reexecucao", gobr_anterior=estado["gobr_atual"],
                  pedido=estado["pedido_mudanca"])


def persistir_regra(estado: dict, modulo: ModuleType, ctx) -> dict:
    """No 90: grava a regra vigente, aprovada pela pessoa. Nao passa pela entrada: aprovar nao e pedir regra.

    O turno gravado e o da ultima geracao (o mesmo numero que o no 50 usou). `entrada` junta o que a pessoa escreveu:
    a descricao e os pedidos de mudanca ate esta regra. Esvazia `aprovacao` para a proxima conversa nao regravar.
    """
    if not estado.get("gobr_atual"):
        raise ErroNo("aprovacao recebida sem gobr_atual: nao ha regra gerada para gravar.")
    ultimo = estado["historico"][-1]
    entrada = "\n\nPedido de mudanca: ".join(h["entrada"] for h in estado["historico"])
    g = modulo.gravar_regra(f"{estado['id_sessao']}-turno{ultimo['turno']}", entrada, estado["descricao_normalizada"],
                            estado["regras_consulta"], estado["sem_chave"], estado["gobr_atual"],
                            estado["metadados_normalizado"], estado["metadados_geracao"], ctx)
    # custo_turno recomeca aqui, como na entrada: o gasto do turno anterior ja entrou no total do agente.py.
    return {"exemplo_gravado": g.exemplo_id, "aprovacao": "", "custo_turno": g.custo_usd}


# ============================================================================
# CONSTRUTOR
# ============================================================================

def _aceitar(nome: str, valor, aceitos) -> None:
    if valor not in aceitos:
        raise ErroOrquestracao(f"{nome} recebido: {valor!r}. Aceitos: {list(aceitos)}. Configure em {ARQ_ORQUESTRACAO}.")


def _validar(orq: ModuleType) -> None:
    """Falha alto antes de qualquer leitura no BigQuery."""
    for campo, (tipo, _) in orq.ESTADO.items():
        _aceitar(f"ESTADO[{campo!r}] tipo", tipo, TIPOS_ESTADO)
    ligados = {**orq.AGENTES, **orq.TOOLS}
    for no, d in orq.NOS.items():
        _aceitar(f"NOS[{no!r}] executa", d["executa"], FUNCOES_NOS)
        _aceitar(f"NOS[{no!r}] usa", d["usa"], ligados)
    origens, destinos = [*orq.NOS, "START"], [*orq.NOS, "END"]
    for origem, destino in orq.ARESTAS:
        _aceitar("ARESTAS origem", origem, origens)
        _aceitar("ARESTAS destino", destino, destinos)
    for c in orq.ARESTAS_CONDICIONAIS:
        _aceitar("ARESTAS_CONDICIONAIS origem", c["origem"], origens)
        _aceitar("ARESTAS_CONDICIONAIS campo", c["campo"], orq.ESTADO)
        _aceitar("ARESTAS_CONDICIONAIS vazio", c["vazio"], destinos)
        _aceitar("ARESTAS_CONDICIONAIS preenchido", c["preenchido"], destinos)
        if "exceto" in c:
            _aceitar("ARESTAS_CONDICIONAIS exceto campo", c["exceto"]["campo"], orq.ESTADO)
            for valor, destino in c["exceto"]["valores"].items():
                _aceitar(f"ARESTAS_CONDICIONAIS exceto valor {valor!r}", destino, destinos)
    _aceitar("MEMORIA", orq.MEMORIA, MEMORIAS)


def _rotulo(estado: dict, campo: str, exceto: dict) -> str:
    """Rotulo da aresta: o valor de `exceto` quando casa, senao vazio ou preenchido conforme o campo."""
    if estado.get(exceto["campo"]) in exceto["valores"]:
        return estado[exceto["campo"]]
    return "preenchido" if estado.get(campo) else "vazio"


def construir_contextos(cfg: ModuleType, orq: ModuleType) -> dict:
    """Um contexto por agente e tool: modulo, contexto lido uma vez do BigQuery. Chave = nome em orquestracao.py."""
    _validar(orq)
    contextos = {}
    for nome, d in {**orq.AGENTES, **orq.TOOLS}.items():
        modulo = importlib.import_module(d["modulo"])
        contextos[nome] = (modulo, modulo.construir_contexto(cfg))
    return contextos


def construir_grafo(cfg: ModuleType, orq: ModuleType, contextos: dict | None = None):
    """Monta e compila o grafo a partir do mapa de orquestracao.py. `contextos` evita reler o BigQuery em testes."""
    _validar(orq)
    contextos = contextos or construir_contextos(cfg, orq)
    estado = TypedDict("Estado", {campo: TIPOS_ESTADO[tipo] for campo, (tipo, _) in orq.ESTADO.items()})
    grafo = StateGraph(estado)
    for no, d in orq.NOS.items():
        modulo, ctx = contextos[d["usa"]]
        # Fecha sobre modulo e contexto; o argumento padrao evita que todos os nos apontem para o ultimo do laco.
        grafo.add_node(no, lambda e, _f=FUNCOES_NOS[d["executa"]], _m=modulo, _c=ctx: _f(e, _m, _c))
    for origem, destino in orq.ARESTAS:
        grafo.add_edge(EXTREMOS.get(origem, origem), EXTREMOS.get(destino, destino))
    for c in orq.ARESTAS_CONDICIONAIS:
        exceto = c.get("exceto", {"campo": None, "valores": {}})
        destinos = {"vazio": c["vazio"], "preenchido": c["preenchido"], **exceto["valores"]}
        grafo.add_conditional_edges(
            EXTREMOS.get(c["origem"], c["origem"]),
            lambda e, _campo=c["campo"], _ex=exceto: _rotulo(e, _campo, _ex),
            {rotulo: EXTREMOS.get(d, d) for rotulo, d in destinos.items()})
    return grafo.compile(checkpointer=MEMORIAS[orq.MEMORIA]())


# Resolvido depois das funcoes: o nome em orquestracao.py ("executa") escolhe a funcao aqui.
FUNCOES_NOS = {f.__name__: f for f in (classificar_entrada_turno, normalizar_descricao, normalizar_descricao_com_pedido, recuperar_exemplos,
                                       gerar_primeira, gerar_reexecucao, persistir_regra)}
