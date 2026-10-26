"""Índice léxico: termo normalizado -> ids das regras cujo dicionário o contém."""
import json
import re
import unicodedata
from pathlib import Path

import config


def normalizar_termo(termo: str) -> str:
    """Minúsculas, sem acento, espaços colapsados.

    NFD + descarte de marcas combinantes para que 'cobrança' e 'cobranca' casem.
    """
    sem_acento = "".join(c for c in unicodedata.normalize("NFD", termo) if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", sem_acento.lower()).strip()


def montar(termos_por_id: dict[str, list[str]]) -> dict[str, list[str]]:
    """termos_por_id: id -> termos originais do Dicionário."""
    indice: dict[str, set[str]] = {}
    for id_regra, termos in termos_por_id.items():
        for t in termos:
            chave = normalizar_termo(t)
            if not chave:
                raise ValueError(f"{id_regra}: termo vazio no Dicionário")
            indice.setdefault(chave, set()).add(id_regra)
    return {k: sorted(v) for k, v in sorted(indice.items())}


def salvar(indice: dict[str, list[str]], caminho: Path = config.ARQUIVO_INDICE_LEXICO) -> None:
    caminho.parent.mkdir(parents=True, exist_ok=True)
    caminho.write_text(json.dumps(indice, ensure_ascii=False, indent=1), encoding="utf-8")


def carregar(caminho: Path = config.ARQUIVO_INDICE_LEXICO) -> dict[str, list[str]]:
    return json.loads(caminho.read_text(encoding="utf-8"))


def consultar(indice: dict[str, list[str]], termo: str) -> list[str]:
    """Ids que contêm exatamente o termo (após normalização)."""
    return indice.get(normalizar_termo(termo), [])
