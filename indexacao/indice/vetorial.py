"""Ciclo completo da coleção no Chroma: criar, inserir, atualizar, remover, consultar."""
import chromadb

import config


def abrir_colecao(criar: bool = True):
    """Abre (e por padrão cria) a coleção persistente.

    A métrica é fixada na criação; mudar depois exige recriar a coleção, por isso
    ela vem de config e não de um argumento solto.
    """
    config.PASTA_CHROMA.mkdir(parents=True, exist_ok=True)
    cliente = chromadb.PersistentClient(path=str(config.PASTA_CHROMA))
    if criar:
        return cliente.get_or_create_collection(
            name=config.NOME_COLECAO, metadata={"hnsw:space": config.METRICA_DISTANCIA}
        )
    return cliente.get_collection(name=config.NOME_COLECAO)


def _em_lotes(n: int):
    for i in range(0, n, config.TAMANHO_LOTE):
        yield slice(i, i + config.TAMANHO_LOTE)


def _conferir(ids, vetores, documentos, metadados):
    if not (len(ids) == len(vetores) == len(documentos) == len(metadados)):
        raise ValueError("ids, vetores, documentos e metadados com tamanhos diferentes")
    if len(set(ids)) != len(ids):
        raise ValueError("ids repetidos no mesmo lote")


def inserir(colecao, ids, vetores, documentos, metadados) -> None:
    """Insere só ids novos; id existente é erro (use upsert/atualizar)."""
    _conferir(ids, vetores, documentos, metadados)
    for s in _em_lotes(len(ids)):
        colecao.add(ids=ids[s], embeddings=vetores[s], documents=documentos[s], metadatas=metadados[s])


def upsert(colecao, ids, vetores, documentos, metadados) -> None:
    """Insere ou substitui por id estável; é o que torna a indexação idempotente."""
    _conferir(ids, vetores, documentos, metadados)
    for s in _em_lotes(len(ids)):
        colecao.upsert(ids=ids[s], embeddings=vetores[s], documents=documentos[s], metadatas=metadados[s])


def atualizar(colecao, ids, vetores=None, documentos=None, metadados=None) -> None:
    """Atualiza ids que já existem; falha se algum não existir, para não criar por engano."""
    existentes = set(colecao.get(ids=ids)["ids"])
    ausentes = [i for i in ids if i not in existentes]
    if ausentes:
        raise KeyError(f"ids inexistentes na coleção: {ausentes}")
    colecao.update(ids=ids, embeddings=vetores, documents=documentos, metadatas=metadados)


def remover(colecao, ids: list[str]) -> None:
    colecao.delete(ids=ids)


def contar(colecao) -> int:
    return colecao.count()


def consultar(colecao, vetor: list[float], n: int = 5, filtro: dict | None = None) -> list[dict]:
    """Consulta simples por vetor. Devolve [{id, distancia, documento, metadados}] por proximidade."""
    r = colecao.query(query_embeddings=[vetor], n_results=n, where=filtro)
    return [
        {"id": i, "distancia": d, "documento": doc, "metadados": m}
        for i, d, doc, m in zip(r["ids"][0], r["distances"][0], r["documents"][0], r["metadatas"][0])
    ]
