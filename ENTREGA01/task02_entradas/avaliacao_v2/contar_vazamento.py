"""Conta custo (metadado) e termos da linguagem GOBR em cada descricao da validacao v2.

Uso (da raiz do projeto): .venv/bin/python ENTREGA01/task02_entradas/avaliacao_v2/contar_vazamento.py
"""
import json
import re
import unicodedata
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent / "regras_explicadas"
MODELOS = {
    "gpt-6-luna": "20261113-180708", "gpt-6.1-terra": "20261113-180708", "gpt-6-astra": "20261113-183339",
    "gpt-4.1-mini-2025-04-14": "20261113-180708", "gpt-4o-mini-2024-07-18": "20261113-180708",
    "gpt-5-mini-2025-08-07": "20261113-180708", "gpt-5.4-mini-2026-03-17": "20261113-180708",
    "gemini-3.1-flash-lite": "20261113-183339", "gemini-3.5-flash-lite": "20261113-180708",
    "gemini-3.6-flash": "20261113-180708", "gemini-3.8-flash": "20261113-183339", "gemini-4-carbon": "20261113-183339",
}
# Termos na forma da linguagem (sem acento, minusculas). Termo de negocio comum nao entra.
SINTAXE = [
    r"recencia de positivac", r"(?<!recencia de )positivac", r"ciclo de vida", r"definido como",
    r"media faturada", r"curva [abc] com a empresa", r"prospects? com (?:o vendedor|a empresa)",
    r"carteira fixa", r"carteiras? livres?", r"ativados", r"nao agendar", r"global", r"\bdays\b",
]
# Nomes de blocos/carteiras copiados do arquivo (texto livre do .gobr, nao do negocio)
NOMES = [
    r"sul_sudeste_centrooeste", r"norte_nordeste", r"ative este novo cliente",
    r"cliente ativado", r"compra com regularidade", r"resgatar cliente inativo",
    r"caminhando para inatividade", r"corporativo/ ?consumidor", r"atacado/ ?distribuidores", r"pre-inativo",
]


def plano(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()


out = {}
for m, ts in MODELOS.items():
    for rid in ("020", "228", "032"):
        p = BASE / f"{ts}_{m}_v2" / f"regra_{rid}" / f"entrada_{rid}.md"
        txt = p.read_text(encoding="utf-8")
        meta, corpo = txt.split("---", 2)[1], txt.split("---", 2)[2]
        custo = float(re.search(r"custo_usd:\s*([\d.]+)", meta).group(1))
        tok = int(re.search(r"tokens_saida:\s*(\d+)", meta).group(1))
        c = plano(corpo)
        sint = {t: len(re.findall(t, c)) for t in SINTAXE if re.findall(t, c)}
        nom = {t: len(re.findall(t, c)) for t in NOMES if re.findall(t, c)}
        if rid == "020" and "empresa toda" in c:  # nome do time e da carteira na 020
            nom["empresa toda"] = c.count("empresa toda")
        out[f"{m}|{rid}"] = {"custo": custo, "tokens_saida": tok, "palavras": len(corpo.split()),
                             "sintaxe": sint, "nomes": nom, "n_sintaxe": sum(sint.values()), "n_nomes": sum(nom.values())}
print(json.dumps(out, ensure_ascii=False, indent=1))
