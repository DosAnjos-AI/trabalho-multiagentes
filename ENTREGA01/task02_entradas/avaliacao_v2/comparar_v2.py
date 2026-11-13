"""Comparador da validacao v2: aplica o CRITERIO_AVALIACAO_v1 as reconstrucoes.

Uso (da raiz do projeto):
    .venv/bin/python ENTREGA01/task02_entradas/avaliacao_v2/comparar_v2.py [--caixa-estrita] > saida.json

Extensoes declaradas (ver RESULTADO_V2.md):
  E1. Caixa de palavra-chave (fora de aspas) ignorada; valores entre aspas comparados literais
      (decidido em ORDEM_DE_TRABALHO.md antes do gabarito). --caixa-estrita compara tudo literal.
  E2. Parentese nao fechado no fim de um bloco e fechado na normalizacao (bloco truncado do gabarito 032).
  E3. Fonte com varias carteiras `da carteira("a","b")` vira conjunto de papeis; pareia com fonte
      que contenha ao menos um dos papeis, ou com `do time` do mesmo time.
  E4. Papel de negocio: o filtro de estado `inativos`/`inatividade` e ignorado no pareamento
      (blocos de "inativos/sobra" pareiam entre si); os demais conceitos de filtro definem o papel.
  E5. Papel de time/carteira = posicao do time no arquivo e definicao da carteira; a definicao
      do time e julgada no proprio bloco time, nao em cada bloco que o referencia.
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
ORIG = RAIZ.parent / "regras_originais"
CATS = ("limpar parametros", "carteira livre", "segmentacao", "carteira", "parametros", "alerta", "tags", "time")
CAIXA_ESTRITA = "--caixa-estrita" in sys.argv


def sem_acento(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def norm(s: str) -> str:
    """Normaliza caixa (E1) e acento so fora de aspas; valores entre aspas ficam literais."""
    partes = re.split(r'("[^"]*"?)', s)
    if CAIXA_ESTRITA:
        s = "".join(x if x.startswith('"') else sem_acento(x) for x in partes)
    else:
        s = "".join(x if x.startswith('"') else sem_acento(x).lower() for x in partes)
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"\s*\(\s*", "(", s)
    s = re.sub(r"\s*\)", ")", s)
    s = re.sub(r"\s*,\s*", ",", s)
    if s.count("(") > s.count(")"):  # E2
        s += ")" * (s.count("(") - s.count(")"))
    return s


def blocos(texto: str) -> list[dict]:
    """Divide o arquivo em blocos de nivel superior e separa fonte, quando e parametros."""
    out, atual = [], None
    for linha in texto.splitlines():
        # remove comentario '#' fora de aspas
        sem_coment = re.sub(r'^((?:[^"#]|"[^"]*")*)#.*$', r"\1", linha)
        if not sem_coment.strip() or sem_coment.strip().startswith("version"):
            continue
        if not sem_coment[0].isspace():
            cab = sem_acento(sem_coment).lower().strip()
            cat = next((c for c in CATS if cab.startswith(c + " ") or cab.startswith(c + '"')), None)
            if cat:
                atual = {"cat": cat, "nome": re.findall(r'"([^"]*)"', sem_coment)[:1], "linhas": []}
                out.append(atual)
                continue
        if atual is not None:
            atual["linhas"].append(sem_coment.strip())
    for b in out:
        juntas, buf = [], ""
        for l in b["linhas"]:  # junta linhas com parentese aberto
            buf = (buf + " " + l).strip() if buf else l
            if buf.count("(") <= buf.count(")"):
                juntas.append(buf)
                buf = ""
        if buf:
            juntas.append(buf)
        fonte, quando, params, em_quando = [], [], [], False
        for l in juntas:
            n = norm(l)
            nl = n.lower()
            if nl.startswith("quando "):
                quando.append(n[7:]); em_quando = True
            elif nl.startswith("e ") and em_quando:
                quando.append(n[2:])
            elif re.match(r"(da carteira|do time|na carteira|da segmentacao|clientes|vendedores)\b", nl):
                fonte.append(n); em_quando = False
            else:
                params.append(n); em_quando = False
        b.update(fonte=fonte, quando=quando, params=params)
        del b["linhas"]
    return out


def papeis_fonte(bs: list[dict]) -> dict:
    """E5: nome de time -> posicao; nome de carteira -> definicao sem nomes."""
    times = {}
    for b in bs:
        if b["cat"] == "time":
            times[b["nome"][0] if b["nome"] else ""] = f"T:{len(times)}"
    cart = {}
    for b in bs:
        if b["cat"] in ("carteira", "carteira livre", "segmentacao"):
            d = [re.sub(r'\("([^"]*)"\)', lambda m: "(" + times.get(m.group(1), m.group(1)) + ")", f) for f in b["fonte"]]
            cart[b["nome"][0]] = "C:" + "|".join(sorted(d)) + "?" + "|".join(sorted(b["quando"]))
    return {"times": times, "cart": cart}


def fonte_papel(b: dict, mp: dict) -> frozenset:
    out = set()
    for f in b["fonte"]:
        m = re.match(r"(da carteira|na carteira|da segmentacao|do time)\((.*)\)$", f, re.I)
        if m and m.group(1).lower() != "do time":
            for nome in re.findall(r'"([^"]*)"', m.group(2)):
                out.add(mp["cart"].get(nome, "?" + nome))
        elif m:
            for nome in re.findall(r'"([^"]*)"', m.group(2)):
                out.add(mp["times"].get(nome, "?" + nome))
        else:
            out.add(re.sub(r'"([^"]*)"', lambda x: mp["times"].get(x.group(1), x.group(1)), f))
    return frozenset(out)


def conceito(f: str) -> str | None:
    """Conceito de negocio de um filtro (so para o pareamento por papel)."""
    f = f.lower()
    if "prospect" in f:
        return "prospect"
    if f.startswith("unica compra"):
        return "unica compra"
    if f.startswith("inativ"):
        return None  # E4
    if "recencia de positivacao" in f:
        return "recencia positivacao"
    if f.startswith("media faturada") or f.startswith("total faturado"):
        return "faturamento"
    if f.startswith("uf do estado"):
        return re.sub(r"^uf do estado [a-z ]+\(", "uf(", f)
    return f


def fontes_compat(a: frozenset, b: frozenset) -> bool:
    if a & b:
        return True
    ta = {x for x in a if x.startswith("T:")}
    tb = {x for x in b if x.startswith("T:")}
    return bool((ta and any(t in y for t in ta for y in b)) or (tb and any(t in y for t in tb for y in a)))


def componentes(b: dict, fp: frozenset) -> dict:
    return {"cat": b["cat"], "fonte": fp, "quando": frozenset(b["quando"]), "params": frozenset(b["params"])}


def compara(rec_txt: str, ori_txt: str) -> dict:
    R, O = blocos(rec_txt), blocos(ori_txt)
    mr, mo = papeis_fonte(R), papeis_fonte(O)
    fr = [fonte_papel(b, mr) for b in R]
    fo = [fonte_papel(b, mo) for b in O]
    nums = lambda q: {(conceito(f), tuple(re.findall(r"\d+", f))) for f in q}
    cand = []
    for i, r in enumerate(R):
        for j, o in enumerate(O):
            if r["cat"].replace("carteira livre", "carteira") != o["cat"].replace("carteira livre", "carteira"):
                continue
            pr = frozenset(c for c in map(conceito, r["quando"]) if c)
            po = frozenset(c for c in map(conceito, o["quando"]) if c)
            if r["cat"] != "time" and pr != po:
                continue
            if r["cat"] in ("parametros", "limpar parametros", "alerta") and not fontes_compat(fr[i], fo[j]):
                continue
            ca, cb = componentes(r, fr[i]), componentes(o, fo[j])
            iguais = sum(ca[k] == cb[k] for k in ca) + len(ca["quando"] & cb["quando"]) + len(ca["params"] & cb["params"])
            parecidos = len(nums(r["quando"]) & nums(o["quando"]))  # desempate 1
            dist = abs(i / max(len(R), 1) - j / max(len(O), 1))  # desempate 2
            cand.append((-iguais, -parecidos, dist, i, j))
    cand.sort()
    usados_r, usados_o, pares = set(), set(), []
    for _, _, _, i, j in cand:
        if i in usados_r or j in usados_o:
            continue
        usados_r.add(i); usados_o.add(j); pares.append((i, j))
    pares.sort(key=lambda p: p[1])
    dif = {}
    for i, j in pares:
        ca, cb = componentes(R[i], fr[i]), componentes(O[j], fo[j])
        dif[(i, j)] = {k: sorted(map(str, ca[k] ^ cb[k])) if isinstance(ca[k], frozenset) else [ca[k], cb[k]]
                       for k in ca if ca[k] != cb[k]}
    # posicao relativa entre parametros pareados (a ordem decide o tratamento)
    pp = [(i, j) for i, j in pares if O[j]["cat"] == "parametros"]
    for a in range(len(pp)):
        for b in range(a + 1, len(pp)):
            (i1, j1), (i2, j2) = pp[a], pp[b]
            if (i1 - i2) * (j1 - j2) < 0:
                dif[pp[a]]["posicao"] = ["invertido"]
                dif[pp[b]]["posicao"] = ["invertido"]
    neg = lambda bl: bl["cat"] != "time"
    return {
        "total_orig": len(O), "total_rec": len(R),
        "orig_negocio": sum(map(neg, O)), "rec_negocio": sum(map(neg, R)),
        "capturadas": len(pares), "capturadas_negocio": sum(neg(O[j]) for _, j in pares),
        "inventadas": len(R) - len(pares),
        "inventadas_negocio": sum(1 for i, r in enumerate(R) if i not in usados_r and neg(r)),
        "corretas": sum(1 for p in pares if not dif[p]),
        "corretas_negocio": sum(1 for p in pares if not dif[p] and neg(O[p[1]])),
        "faltaram": [{"orig": j, "cat": O[j]["cat"], "nome": O[j]["nome"], "quando": O[j]["quando"], "params": O[j]["params"]}
                     for j in range(len(O)) if j not in usados_o],
        "inventadas_lista": [{"rec": i, "cat": R[i]["cat"], "nome": R[i]["nome"], "quando": R[i]["quando"], "params": R[i]["params"]}
                             for i in range(len(R)) if i not in usados_r],
        "pares": [{"rec": i, "orig": j, "cat": O[j]["cat"], "nome_orig": O[j]["nome"], "nome_rec": R[i]["nome"], "dif": dif[(i, j)]}
                  for i, j in pares],
    }


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    pasta = Path(args[0]) if args else RAIZ / "reconstrucoes"
    todos = {}
    for f in sorted(pasta.glob("*/regra_*.gobr")):
        rid = f.stem.split("_")[1]
        ori = (ORIG / f"regra_{rid}.gobr").read_text(encoding="utf-8")
        todos[f"{f.parent.name}|{rid}"] = compara(f.read_text(encoding="utf-8"), ori)
    print(json.dumps(todos, ensure_ascii=False, default=list, indent=1))
