"""Formatador de .gobr: recebe blocos ja decididos e escreve o arquivo."""
from pathlib import Path


def bloco(cab: str, linhas: list[str], quando: list[str] | None = None, depois: list[str] | None = None) -> str:
    """Monta um bloco: cabecalho, linhas de fonte, quando (filtros com e), linhas finais."""
    out = [cab + ":"]
    out += ["    " + l for l in linhas]
    if quando:
        out.append("    quando " + quando[0])
        out += ["    e " + q for q in quando[1:]]
    out += ["    " + l for l in (depois or [])]
    return "\n".join(out)


def grava(caminho: str, blocos: list[str]) -> None:
    p = Path(caminho)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("version 1.0\n\n" + "\n\n".join(blocos) + "\n", encoding="utf-8", newline="\n")


def fat(tipo: str, valor: int | None) -> str | None:
    """Filtro de faturamento do ano com a empresa; None = demais casos."""
    if valor is None:
        return None
    return f"{tipo} no ano com a empresa maior que R$ {valor}"
