"""Leitura do formato 4.0, usada pela validação e pela indexação.

Fica em conversao/ porque conhece o layout do arquivo; o código de índice só
consome o resultado.
"""
from pathlib import Path

import yaml

from conversao.leitor_v31 import ErroConversao, dividir_secoes, extrair_yaml, ler_tabela


def ler_v40(caminho: Path) -> dict:
    """Devolve {cabecalho, regras (lista de linhas), estrutura, dicionario}."""
    id_regra = caminho.parent.name
    try:
        bruto_cab, secoes = dividir_secoes(caminho.read_text(encoding="utf-8"))
        cab = yaml.safe_load(bruto_cab)
    except (OSError, ValueError, yaml.YAMLError) as e:
        raise ErroConversao(id_regra, f"não foi possível abrir: {e}") from e
    if str(cab.get("versao_padrao")) != "4.0":
        raise ErroConversao(id_regra, f"versao_padrao é {cab.get('versao_padrao')!r}, esperado 4.0")
    for s in ("Regras", "Estrutura", "Dicionário"):
        if s not in secoes:
            raise ErroConversao(id_regra, f"seção ausente: {s}")
    return {
        "cabecalho": cab,
        "regras": [l for l in secoes["Regras"].splitlines() if l.strip()],
        "estrutura": extrair_yaml(secoes["Estrutura"], id_regra, "Estrutura"),
        "dicionario": ler_tabela(secoes["Dicionário"], id_regra),
    }
