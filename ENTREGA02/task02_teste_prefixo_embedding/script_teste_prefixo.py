"""Mede o formato de prefixo do texto enviado ao gemini-embedding-2 (leave-one-out, so mede).

Uso (da raiz do projeto):
    .venv/bin/python -B ENTREGA02/task02_teste_prefixo_embedding/script_teste_prefixo.py --estimar
    .venv/bin/python -B ENTREGA02/task02_teste_prefixo_embedding/script_teste_prefixo.py --executar

Nao grava no BigQuery nem altera dados existentes. Autenticacao: ADC.
"""
import argparse
import hashlib
import json
import sys
import time
from pathlib import Path

import google.auth
import google.auth.transport.requests
import numpy as np
import requests

RAIZ = Path(__file__).resolve().parents[2]
BASE = Path(__file__).resolve().parent
ENTRADA = RAIZ / "dados" / "processados" / "regras_normalizadas"
CACHE = BASE / "embeddings.jsonl"
RESULTADO = BASE / "resultado.json"

PROJETO = "multiagentes-514823"
MODELO = "gemini-embedding-2"
DIMENSOES = 3072
URL = (f"https://aiplatform.googleapis.com/v1/projects/{PROJETO}/locations/us/publishers/google/models/"
       f"{MODELO}:embedContent")
# Referencia da rodada (hipotese): US$ 0,20 por 1M de tokens. O custo real usa os tokens que a API devolve.
USD_POR_MILHAO = 0.20
TETO_USD = 1.00
# Caracteres por token: as duas calibracoes do config.py da tarefa de normalizacao (so para a projecao).
CARACTERES_POR_TOKEN = (4.12, 3.0)
KS = (3, 5, 10)
TENTATIVAS = 5

# Cada formato aponta para a chave do texto de consulta e a do documento.
FORMATOS = {"A": ("A_consulta", "A_doc"), "B": ("B", "B"), "C": ("C", "C")}
CHAVES = ("A_doc", "A_consulta", "B", "C")


def montar_texto(chave: str, t: str) -> str:
    """Texto enviado ao modelo para cada chave; a instrucao de tarefa vai dentro do texto."""
    return {
        "A_doc": f"title: none | text: {t}",
        "A_consulta": f"task: search result | query: {t}",
        "B": f"task: sentence similarity | query: {t}",
        "C": t,
    }[chave]


def ler_exemplos() -> list[dict]:
    """Le os normalizados; devolve id, explicacao_normalizada e conjunto de regras_extraidas."""
    exemplos = []
    for caminho in sorted(ENTRADA.glob("normalizado_*.md")):
        texto = caminho.read_text(encoding="utf-8")
        t = texto.split("## explicacao_normalizada\n", 1)[1].split("\n## regras_extraidas", 1)[0].strip()
        regras = json.loads(texto.split("## regras_extraidas\n", 1)[1])["regras_extraidas"]
        exemplos.append({"id": caminho.stem.removeprefix("normalizado_"), "t": t, "regras": set(regras)})
    return exemplos


def hash_texto(texto: str) -> str:
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()


def estimar(exemplos: list[dict]) -> None:
    """Projecao de tokens e custo sem chamar a API."""
    chars = sum(len(montar_texto(c, e["t"])) for e in exemplos for c in CHAVES)
    print(f"exemplos={len(exemplos)} textos={len(exemplos) * len(CHAVES)} caracteres={chars}")
    for cpt in CARACTERES_POR_TOKEN:
        tok = chars / cpt
        print(f"  {cpt} car/token: tokens={tok:,.0f} custo_usd={tok / 1e6 * USD_POR_MILHAO:.4f}")


def carregar_cache() -> dict[tuple[str, str], dict]:
    cache = {}
    if CACHE.exists():
        for linha in CACHE.read_text(encoding="utf-8").splitlines():
            r = json.loads(linha)
            cache[(r["id"], r["chave"])] = r
    return cache


def chamar_api(sessao: requests.Session, credenciais, texto: str) -> tuple[list[float], int]:
    """Uma chamada embedContent com repeticao curta em 429 e 5xx. Devolve (vetor, tokens)."""
    corpo = {"content": {"parts": [{"text": texto}]}, "outputDimensionality": DIMENSOES}
    for tentativa in range(1, TENTATIVAS + 1):
        if not credenciais.valid:
            credenciais.refresh(google.auth.transport.requests.Request())
        r = sessao.post(URL, json=corpo, timeout=60, headers={
            "Authorization": f"Bearer {credenciais.token}", "x-goog-user-project": PROJETO})
        if r.status_code == 200:
            j = r.json()
            return j["embedding"]["values"], int(j["usageMetadata"]["promptTokenCount"])
        if r.status_code in (429, 500, 502, 503, 504) and tentativa < TENTATIVAS:
            time.sleep(2 ** tentativa)
            continue
        raise RuntimeError(f"embedContent HTTP {r.status_code}: {r.text[:300]}")


def gerar_embeddings(exemplos: list[dict]) -> dict[tuple[str, str], dict]:
    """Gera o que falta e grava cada vetor logo apos a chamada (retomavel; nunca regera o que existe)."""
    cache = carregar_cache()
    credenciais, _ = google.auth.default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
    sessao = requests.Session()
    chamadas = falhas = 0
    tokens_novos = 0
    with CACHE.open("a", encoding="utf-8", newline="\n") as saida:
        for e in exemplos:
            for chave in CHAVES:
                texto = montar_texto(chave, e["t"])
                h = hash_texto(texto)
                existente = cache.get((e["id"], chave))
                if existente and existente["hash_texto"] == h:
                    continue
                if tokens_novos / 1e6 * USD_POR_MILHAO > TETO_USD:
                    raise RuntimeError(f"teto de US$ {TETO_USD} atingido; parado (cache preservado).")
                try:
                    vetor, tok = chamar_api(sessao, credenciais, texto)
                except RuntimeError as erro:
                    falhas += 1
                    print(f"FALHA {e['id']} {chave}: {erro}")
                    continue
                registro = {"id": e["id"], "chave": chave, "hash_texto": h, "tokens": tok, "vetor": vetor}
                saida.write(json.dumps(registro) + "\n")
                saida.flush()
                cache[(e["id"], chave)] = registro
                chamadas += 1
                tokens_novos += tok
    print(f"chamadas={chamadas} falhas={falhas} tokens_novos={tokens_novos} "
          f"custo_usd_novo={tokens_novos / 1e6 * USD_POR_MILHAO:.6f}")
    return cache


def jaccard(a: set, b: set) -> float:
    return len(a & b) / len(a | b)


def pontuar(exemplos: list[dict], cache: dict) -> dict:
    """Leave-one-out: media do Jaccard medio dos top-k vizinhos, por formato e k."""
    n = len(exemplos)
    ids = [e["id"] for e in exemplos]
    jac = np.array([[jaccard(a["regras"], b["regras"]) for b in exemplos] for a in exemplos])
    resultado = {}
    for formato, (chave_q, chave_d) in FORMATOS.items():
        def matriz(chave: str) -> np.ndarray:
            m = np.array([cache[(i, chave)]["vetor"] for i in ids], dtype=np.float64)
            return m / np.linalg.norm(m, axis=1, keepdims=True)
        sim = matriz(chave_q) @ matriz(chave_d).T
        np.fill_diagonal(sim, -np.inf)  # exclui o proprio exemplo dos candidatos
        ordem = np.argsort(-sim, axis=1)
        resultado[formato] = {
            f"k={k}": float(np.mean([jac[i, ordem[i, :k]].mean() for i in range(n)])) for k in KS}
    return resultado


def main() -> int:
    ap = argparse.ArgumentParser(description="Teste de formato de prefixo para embeddings (so mede).")
    grupo = ap.add_mutually_exclusive_group(required=True)
    grupo.add_argument("--estimar", action="store_true", help="projeta tokens e custo; nao chama a API")
    grupo.add_argument("--executar", action="store_true", help="chama a API (paga), pontua e grava resultado.json")
    args = ap.parse_args()
    exemplos = ler_exemplos()
    if args.estimar:
        estimar(exemplos)
        return 0
    cache = gerar_embeddings(exemplos)
    faltam = [(e["id"], c) for e in exemplos for c in CHAVES if (e["id"], c) not in cache]
    if faltam:
        print(f"INCOMPLETO: {len(faltam)} embeddings ausentes (ex.: {faltam[:3]}). Rode de novo para retomar.")
        return 1
    tokens_total = sum(r["tokens"] for r in cache.values())
    resultado = {"modelo": MODELO, "dimensoes": DIMENSOES, "exemplos": len(exemplos), "chamadas_no_cache": len(cache),
                 "tokens_total": tokens_total, "custo_usd_total": tokens_total / 1e6 * USD_POR_MILHAO,
                 "usd_por_milhao_referencia": USD_POR_MILHAO, "pontuacao": pontuar(exemplos, cache)}
    RESULTADO.write_text(json.dumps(resultado, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    print("| Formato | k=3 | k=5 | k=10 |\n|---|---|---|---|")
    for f, p in resultado["pontuacao"].items():
        print(f"| {f} | {p['k=3']:.4f} | {p['k=5']:.4f} | {p['k=10']:.4f} |")
    print(f"tokens_total={tokens_total} custo_usd_total={resultado['custo_usd_total']:.6f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
