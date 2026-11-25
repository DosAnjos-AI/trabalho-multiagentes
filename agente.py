"""Ponto de entrada: conversa de varios turnos pelo terminal, no mesmo estado do grafo.

Uso: .venv/bin/python -B agente.py [id_da_conversa]
Primeira linha: descricao da regra, ou o caminho de um arquivo (extensoes em config.EXTENSOES_ENTRADA). Depois de cada regra gerada o programa pergunta se a pessoa aprova: sim grava a
regra no BigQuery (status pendente de revisao); nao pede o que mudar, e a linha seguinte e um pedido de mudanca.
Linha vazia (ou Ctrl+D) encerra.
Se a entrada nao traz o minimo, o programa pergunta o que falta e soma a resposta ao que a pessoa ja disse.
A chave da API vem do arquivo .env, carregado pelo config.py na importacao.
"""
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
sys.path[:0] = [str(RAIZ), str(RAIZ / "src")]

import config
import orquestracao
from script10_orquestracao.script10_orquestracao import construir_grafo

# Uma conversa por execucao; a memoria do grafo e do processo. O id e o primeiro argumento (padrao: conversa1) e
# entra no exemplo_id da regra gravada.
THREAD_ID = sys.argv[1] if len(sys.argv) > 1 else "conversa1"

# O no 30 so devolve tokens; o texto que a pessoa le e daqui.
PERGUNTAS = {
    "quem_atende": "Quais vendedores ou equipes a regra cobre?",
    "desfecho": "O que o conjunto de regras faz: monta carteira, define atendimento, dispara alerta ou marca tag?",
    "conflito": "Atendimento e alerta sao dois conjuntos de regras separados; qual vem agora?",
}
MENSAGEM_FORA_DE_ESCOPO = ("Eu escrevo regras de atendimento comercial na linguagem GOBR do goVendas. "
                           "Descreva a regra que voce quer, por exemplo quem atende e o que deve acontecer.")


def achar_arquivo(linha: str) -> Path | None:
    """Caminho do arquivo se a linha digitada for um arquivo existente; None se for texto."""
    try:
        caminho = Path(linha.strip().strip("'\"")).expanduser()
        return caminho if caminho.is_file() else None
    except (OSError, ValueError):  # texto longo demais ou com caractere invalido nao e caminho
        return None


def perguntar_aprovacao() -> bool | None:
    """True se a pessoa aprova; False se recusa; None se a entrada acabou (Ctrl+D)."""
    while True:
        try:
            resposta = input("Aprovar a regra? (sim/nao)> ").strip().lower()
        except EOFError:
            return None
        if resposta in ("s", "sim"):
            return True
        if resposta in ("n", "nao", "não"):
            return False


def main() -> None:
    grafo = construir_grafo(config, orquestracao)
    cfg = {"configurable": {"thread_id": THREAD_ID}}
    total = 0.0
    gerou = False      # a primeira regra ja saiu: as entradas seguintes sao pedidos de mudanca
    pendente = ""      # texto de uma entrada incompleta; a resposta da pessoa e somada a ele
    while True:
        try:
            texto = input("resposta> " if pendente else ("pedido de mudanca> " if gerou else "> ")).strip()
        except EOFError:
            break
        if not texto:
            break
        # Caminho de arquivo existente vira midia; o tipo sai da extensao (o no 30 nao adivinha). Com pergunta
        # pendente a linha e sempre resposta em texto: trocar a entrada no meio perderia o que a pessoa ja disse.
        arquivo = None if pendente else achar_arquivo(texto)
        tipo = "texto"
        if arquivo is not None:
            if arquivo.suffix.lower() not in config.EXTENSOES_ENTRADA:
                print(f"\nExtensao {arquivo.suffix!r} nao aceita. Aceitas: {list(config.EXTENSOES_ENTRADA)}. "
                      "Envie outro arquivo ou digite o texto.\n")
                continue
            tipo = config.EXTENSOES_ENTRADA[arquivo.suffix.lower()][0]
            texto = str(arquivo)
        # Soma, nunca substitui: o no 30 recebe o pedido original e o complemento, na ordem em que a pessoa falou.
        bruta = f"{pendente}\n{texto}" if pendente else texto
        entrada = {"entrada_bruta": bruta, "tipo_entrada": tipo}
        entrada.update({"pedido_mudanca": bruta} if gerou else {"id_sessao": THREAD_ID})
        try:
            estado = grafo.invoke(entrada, cfg)
        except ValueError as erro:
            # Midia invalida (arquivo grande, ilegivel) nao derruba a conversa; erro de texto continua fatal.
            if tipo == "texto":
                raise
            print(f"\nNao foi possivel usar o arquivo: {erro}\n")
            continue
        total += estado["custo_turno"]
        status = estado["status_entrada"]
        if tipo != "texto":
            transcrito = estado["pedido_mudanca"] if gerou else estado["descricao_usuario"]
            print(f"\nTexto transcrito de {tipo}:\n{transcrito}")
        if status == "incompleto":
            # Em midia, o que fica pendente e o texto transcrito: a resposta da pessoa soma a ele.
            pendente = bruta if tipo == "texto" else transcrito
            print("\n" + "\n".join(PERGUNTAS[t] for t in estado["faltantes"]))
            print(f"\n[custo do turno US$ {estado['custo_turno']:.6f}; total US$ {total:.6f}]\n")
            continue
        pendente = ""  # fora_de_escopo descarta a entrada alheia; aprovado ja a consumiu
        if status == "fora_de_escopo":
            print(f"\n{MENSAGEM_FORA_DE_ESCOPO}")
            print(f"\n[custo do turno US$ {estado['custo_turno']:.6f}; total US$ {total:.6f}]\n")
            continue
        gerou = True
        print(f"\n{estado['gobr_atual']}")
        # A ressalva sai na conversa, nunca dentro do arquivo: o prompt de geracao proibe texto alheio a regra.
        if estado["sem_chave"]:
            itens = "\n".join(f"  - {item}" for item in estado["sem_chave"])
            print("\nRessalva: os itens abaixo nao foram encontrados no manual e podem nao estar cobertos "
                  f"pela regra gerada acima:\n{itens}")
        print(f"\n[custo do turno US$ {estado['custo_turno']:.6f}; total US$ {total:.6f}]\n")
        aprovada = perguntar_aprovacao()
        if aprovada is None:
            break
        if not aprovada:
            print("\nO que voce quer mudar na regra?")
            continue
        estado = grafo.invoke({"aprovacao": "aprovado"}, cfg)
        total += estado["custo_turno"]
        print(f"\nRegra gravada como {estado['exemplo_gravado']} (status {config.STATUS_GRAVACAO}, aguarda revisao).")
        print(f"\n[custo do turno US$ {estado['custo_turno']:.6f}; total US$ {total:.6f}]\n")


if __name__ == "__main__":
    main()
