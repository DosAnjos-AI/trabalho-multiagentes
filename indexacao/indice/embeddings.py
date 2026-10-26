"""Modelo de embeddings e prefixos do e5."""
from functools import lru_cache

import config


@lru_cache(maxsize=1)
def carregar_modelo():
    # Import tardio: importar sentence-transformers leva segundos, e quem só
    # converte arquivos não deve pagar esse custo. O cache evita recarregar ~1 GB.
    from sentence_transformers import SentenceTransformer

    return SentenceTransformer(config.NOME_MODELO)


def _embeddar(textos: list[str], prefixo: str) -> list[list[float]]:
    if not textos:
        raise ValueError("lista de textos vazia")
    # normalize_embeddings: a coleção usa cosseno e o e5 foi treinado com vetores normalizados.
    vetores = carregar_modelo().encode(
        [prefixo + t for t in textos],
        batch_size=config.TAMANHO_LOTE,
        normalize_embeddings=True,
        show_progress_bar=False,
    )
    if vetores.shape[1] != config.DIMENSAO_VETOR:
        raise RuntimeError(
            f"dimensão do vetor {vetores.shape[1]} difere de config.DIMENSAO_VETOR={config.DIMENSAO_VETOR}"
        )
    return vetores.tolist()


def embeddar_passagens(textos: list[str]) -> list[list[float]]:
    """Documentos do corpus, com o prefixo 'passage: '."""
    return _embeddar(textos, config.PREFIXO_PASSAGEM)


def embeddar_consultas(textos: list[str]) -> list[list[float]]:
    """Consultas de usuário, com o prefixo 'query: '."""
    return _embeddar(textos, config.PREFIXO_CONSULTA)
