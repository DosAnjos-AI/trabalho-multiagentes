"""Índice léxico: termo normalizado -> ids das regras cujo dicionário o contém."""
import json
import re
import unicodedata
from pathlib import Path

import config


TAMANHO_MINIMO = 2
PALAVRAS_VAZIAS = frozenset({"de", "da", "do", "em", "no", "na", "com", "por", "para", "ou", "as", "os", "um", "uma"})


def normalizar_termo(termo: str) -> str:
    """Minúsculas, sem acento, espaços colapsados.

    NFD + descarte de marcas combinantes para que 'cobrança' e 'cobranca' casem.
    """
    sem_acento = "".join(c for c in unicodedata.normalize("NFD", termo) if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", sem_acento.lower()).strip()


def separar_celula(celula: str) -> set[str]:
    """Chaves de uma célula 'Termo original': cada item inteiro e cada token dele.

    O token isolado existe porque códigos como 'DH' aparecem dentro de itens compostos
    ('tipo de cobrança DH'). Mínimo de 2 caracteres sempre, sem exceção, para que ruído
    como 'b' (de 'curva A, B e C') não entre; palavras vazias não viram chave.
    """
    chaves = set()
    for item in re.split(r"[,;]", celula):
        t = normalizar_termo(item)
        for chave in [t, *t.split()]:
            if len(chave) >= TAMANHO_MINIMO and chave not in PALAVRAS_VAZIAS:
                chaves.add(chave)
    return chaves


def montar(celulas_por_id: dict[str, list[str]]) -> dict[str, list[str]]:
    """celulas_por_id: id -> células 'Termo original' do Dicionário, sem separar."""
    indice: dict[str, set[str]] = {}
    for id_regra, celulas in celulas_por_id.items():
        for celula in celulas:
            for chave in separar_celula(celula):
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
