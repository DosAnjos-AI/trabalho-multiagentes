"""Ponto de entrada: conversa de varios turnos pelo terminal, no mesmo estado do grafo.

Uso: .venv/bin/python -B agente.py
Primeira linha: descricao da regra. Linhas seguintes: pedidos de mudanca. Linha vazia (ou Ctrl+D) encerra.
A chave da API vem do arquivo .env, carregado pelo config.py na importacao.
"""
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
sys.path[:0] = [str(RAIZ), str(RAIZ / "src")]

import config
import orquestracao
from script10_orquestracao.script10_orquestracao import construir_grafo

# Fixo: uma conversa por execucao; a memoria do grafo e do processo.
THREAD_ID = "conversa1"


def main() -> None:
    grafo = construir_grafo(config, orquestracao)
    cfg = {"configurable": {"thread_id": THREAD_ID}}
    total = 0.0
    primeiro = True
    while True:
        try:
            texto = input("> " if primeiro else "pedido de mudanca> ").strip()
        except EOFError:
            break
        if not texto:
            break
        entrada = {"id_sessao": THREAD_ID, "descricao_usuario": texto} if primeiro else {"pedido_mudanca": texto}
        estado = grafo.invoke(entrada, cfg)
        primeiro = False
        total += estado["custo_turno"]
        print(f"\n{estado['gobr_atual']}\n\n[custo do turno US$ {estado['custo_turno']:.6f}; total US$ {total:.6f}]\n")


if __name__ == "__main__":
    main()
