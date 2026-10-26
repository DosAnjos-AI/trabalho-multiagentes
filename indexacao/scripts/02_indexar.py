"""Embedda a seção '## Regras' de cada arquivo 4.0, faz upsert no Chroma e monta o índice léxico.

Uso (da raiz do projeto): .venv/bin/python indexacao/scripts/02_indexar.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import config
from conversao.leitor_v31 import ErroConversao
from conversao.leitor_v40 import ler_v40
from indice import embeddings, lexico, vetorial


def metadados_de(doc: dict, caminho: Path) -> dict:
    cab = doc["cabecalho"]
    id_regra = cab["id"]
    est = doc["estrutura"]
    presentes = {c["tipo"] for c in est.get("comuns", [])}
    for r in est["regras"]:
        presentes |= {c["tipo"] for c in r["se"]}
    # Tipo fora do vocabulário seria perdido em silêncio nos booleanos; melhor parar.
    fora = presentes - set(config.TIPOS_CRITERIO)
    if fora:
        raise ErroConversao(id_regra, f"tipos de critério fora do vocabulário: {sorted(fora)}")
    meta = {f"crit_{t}": (t in presentes) for t in config.TIPOS_CRITERIO}
    meta.update(
        total_regras=int(cab["total_regras"]),
        procedencia=str(cab["procedencia"]),
        gobr_path=str(cab["gobr"]),  # só a string; o .gobr nunca é aberto
        normalizado_path=str(caminho.relative_to(config.RAIZ_PROJETO)),
    )
    return meta


def main() -> int:
    caminhos = sorted(config.PASTA_SIMULACAO.glob(f"{config.PREFIXO_PASTA}*/{config.NOME_NORMALIZADO}"))
    if len(caminhos) != config.TOTAL_PASTAS:
        sys.exit(f"ABORTADO: {len(caminhos)} arquivos, esperado {config.TOTAL_PASTAS}")

    ids, textos, metas, termos_por_id = [], [], [], {}
    for c in caminhos:
        doc = ler_v40(c)  # erro explícito com id e motivo se não abrir
        id_regra = doc["cabecalho"]["id"]
        if len(doc["regras"]) != doc["cabecalho"]["total_regras"]:
            raise ErroConversao(id_regra, "linhas de ## Regras diferem de total_regras")
        ids.append(id_regra)
        textos.append("\n".join(doc["regras"]))  # somente a seção Regras vai para o vetor
        metas.append(metadados_de(doc, c))
        termos_por_id[id_regra] = [linha[0] for linha in doc["dicionario"]]

    try:
        vetores = embeddings.embeddar_passagens(textos)
    except Exception as e:
        raise RuntimeError(f"falha ao embeddar documentos: {e}") from e

    colecao = vetorial.abrir_colecao()
    vetorial.upsert(colecao, ids, vetores, textos, metas)

    indice = lexico.montar(termos_por_id)
    lexico.salvar(indice)
    print(f"documentos na coleção: {vetorial.contar(colecao)}")
    print(f"termos distintos no índice léxico: {len(indice)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
