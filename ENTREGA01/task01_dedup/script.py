"""Remove duplicados e quase-duplicados de arquivos .gobr."""
import csv
import difflib
import re
import shutil
from itertools import combinations
from pathlib import Path

import config

MODOS_ACEITOS = ("par_a_par", "transitivo")


def validar_config() -> None:
    """Falha com erro claro se o modo de agrupamento for invalido."""
    if config.MODO_AGRUPAMENTO not in MODOS_ACEITOS:
        raise ValueError(
            f"MODO_AGRUPAMENTO invalido: {config.MODO_AGRUPAMENTO!r}. "
            f"Valores aceitos: {MODOS_ACEITOS}. Configure em config.py."
        )


def normalizar(texto: str) -> list[str]:
    """Normaliza o texto em lista de linhas para comparacao."""
    resultado: list[str] = []
    for linha in texto.splitlines():
        if not config.CONSIDERAR_COMENTARIOS and linha.lstrip().startswith("#"):
            continue
        linha = linha.rstrip()
        # colapsa sequencias de linhas vazias em uma so
        if linha == "" and resultado and resultado[-1] == "":
            continue
        resultado.append(linha)
    return resultado


RE_VERSION = re.compile(r"^\s*version\b")


def garantir_version(texto: str) -> tuple[str, str]:
    """Garante a linha version. Retorna (texto, status).

    status: "primeira" (ja tinha como primeira linha de conteudo),
    "inserida" ou "posicao_inesperada" (tinha, mas fora da primeira posicao).
    """
    linhas = texto.splitlines(keepends=True)
    primeira = next(
        (i for i, l in enumerate(linhas)
         if l.strip() and not l.lstrip().startswith("#")),
        None,
    )
    if primeira is not None and RE_VERSION.match(linhas[primeira]):
        return texto, "primeira"
    if any(RE_VERSION.match(l) for l in linhas):
        return texto, "posicao_inesperada"
    nova = f"version {config.VERSAO_PADRAO}\n"
    if primeira is None:
        if linhas and not linhas[-1].endswith("\n"):
            linhas[-1] += "\n"
        linhas.append(nova)
    else:
        linhas.insert(primeira, nova)
    return "".join(linhas), "inserida"


def similaridade(a: list[str], b: list[str]) -> float:
    """Razao de similaridade entre duas listas de linhas."""
    return difflib.SequenceMatcher(None, a, b, autojunk=False).ratio()


def numero_regra(caminho: Path) -> int:
    """Extrai o numero da regra do nome do arquivo."""
    return int(re.search(r"(\d+)", caminho.stem).group(1))


def main() -> dict:
    validar_config()
    arquivos = sorted(config.CAMINHO_ENTRADA.glob("*.gobr"), key=numero_regra)
    brutos: dict[Path, str] = {}
    status_version: dict[Path, str] = {}
    for a in arquivos:
        # 1) garantir version, 2) normalizar, 3) comparar
        brutos[a], status_version[a] = garantir_version(a.read_text(encoding="utf-8"))
    norm = {a: normalizar(t) for a, t in brutos.items()}
    # preferencia: mais caracteres no texto bruto, depois menor numero
    ordem = sorted(arquivos, key=lambda a: (-len(brutos[a]), numero_regra(a)))
    limiar = config.LIMIAR_SIMILARIDADE

    removidos: list[tuple] = []  # (removido, mantido, sim, grupo)
    abaixo: list[tuple] = []  # (sim, a, b) abaixo do limiar
    mantidos: list[Path] = []

    if config.MODO_AGRUPAMENTO == "par_a_par":
        for a in ordem:
            melhor = None
            for m in mantidos:
                s = similaridade(norm[a], norm[m])
                if s >= limiar:
                    melhor = (m, s)
                    break
                abaixo.append((s, a, m))
            if melhor:
                removidos.append((a, melhor[0], melhor[1], ""))
            else:
                mantidos.append(a)
    else:
        pai = {a: a for a in arquivos}

        def raiz(x: Path) -> Path:
            while pai[x] != x:
                pai[x] = pai[pai[x]]
                x = pai[x]
            return x

        for a, b in combinations(arquivos, 2):
            s = similaridade(norm[a], norm[b])
            if s >= limiar:
                pai[raiz(a)] = raiz(b)
            else:
                abaixo.append((s, a, b))
        grupos: dict[Path, list[Path]] = {}
        for a in ordem:
            grupos.setdefault(raiz(a), []).append(a)
        for i, membros in enumerate(grupos.values(), start=1):
            fica = membros[0]  # ja em ordem de preferencia
            mantidos.append(fica)
            for r in membros[1:]:
                removidos.append(
                    (r, fica, similaridade(norm[r], norm[fica]), f"G{i:03d}")
                )

    # escrita: apaga a saida primeiro
    saida = config.CAMINHO_SAIDA
    if saida.exists():
        shutil.rmtree(saida)
    saida.mkdir(parents=True, exist_ok=True)
    for m in mantidos:
        (saida / m.name).write_text(brutos[m], encoding="utf-8")
    removidos.sort(key=lambda r: numero_regra(r[0]))
    with open(saida / "000_relatorio_dedup.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["arquivo_removido", "arquivo_mantido", "similaridade", "grupo",
                    "modo", "limiar", "considerar_comentarios"])
        for r, m, s, g in removidos:
            w.writerow([r.name, m.name, f"{s:.4f}", g, config.MODO_AGRUPAMENTO,
                        limiar, config.CONSIDERAR_COMENTARIOS])

    abaixo.sort(key=lambda t: -t[0])
    print(f"modo={config.MODO_AGRUPAMENTO} entrada={len(arquivos)} "
          f"mantidos={len(mantidos)} removidos={len(removidos)} "
          f"soma={len(mantidos) + len(removidos)}")
    print("top5 abaixo do limiar:")
    for s, a, b in abaixo[:5]:
        print(f"  {s:.4f} {a.name} x {b.name}")
    cont = {k: sum(1 for v in status_version.values() if v == k)
            for k in ("primeira", "inserida", "posicao_inesperada")}
    print(f"version: {cont}")
    for a, v in status_version.items():
        if v == "posicao_inesperada":
            print(f"  posicao inesperada: {a.name}")
    return {"entrada": len(arquivos), "mantidos": len(mantidos), "removidos": len(removidos)}


if __name__ == "__main__":
    main()
