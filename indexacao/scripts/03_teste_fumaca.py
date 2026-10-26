"""Consulta de verificação: o texto de ## Regras da regra_166 deve achar a própria regra_166 em 1º.

Uso (da raiz do projeto): .venv/bin/python indexacao/scripts/03_teste_fumaca.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import config
from conversao.leitor_v40 import ler_v40
from indice import embeddings, vetorial


def main() -> int:
    caminho = config.PASTA_SIMULACAO / config.ID_TESTE_FUMACA / config.NOME_NORMALIZADO
    texto = "\n".join(ler_v40(caminho)["regras"])
    vetor = embeddings.embeddar_consultas([texto])[0]
    resultados = vetorial.consultar(vetorial.abrir_colecao(criar=False), vetor, n=5)
    for pos, r in enumerate(resultados, 1):
        print(f"{pos}. {r['id']}  distancia={r['distancia']:.4f}")
    if not resultados or resultados[0]["id"] != config.ID_TESTE_FUMACA:
        print(f"FALHOU: {config.ID_TESTE_FUMACA} não está em primeiro lugar", file=sys.stderr)
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
