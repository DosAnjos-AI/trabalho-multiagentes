"""Uso em linha de comando: embrulho fino sobre conferidor.conferir.

    .venv/bin/python src/conferidor_gobr/cli.py ARQUIVO [ARQUIVO ...]
    .venv/bin/python src/conferidor_gobr/cli.py -        (le da entrada padrao)

Codigo de saida: 0 sem falha, 1 com falha (item ausente ou divergencia), 2 erro de uso.
Construcao nao documentada nao muda o codigo de saida, porque nao e falha do arquivo.
"""

import argparse
import sys
from pathlib import Path

# Permite rodar como script sem instalar o pacote: o pai desta pasta e src/.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from conferidor_gobr.conferidor import conferir  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Confere arquivos .gobr contra o manual GoBR.")
    parser.add_argument("arquivos", nargs="+", help="caminhos de arquivos .gobr, ou '-' para stdin")
    parser.add_argument("--so-falhas", action="store_true",
                        help="omite os achados da categoria construcao_nao_documentada")
    args = parser.parse_args(argv)

    houve_falha = False
    for nome in args.arquivos:
        if nome == "-":
            texto = sys.stdin.read()
        else:
            caminho = Path(nome)
            if not caminho.is_file():
                print(f"erro: arquivo nao encontrado: {caminho}", file=sys.stderr)
                return 2
            texto = caminho.read_text(encoding="utf-8")

        laudo = conferir(texto)
        houve_falha = houve_falha or not laudo.aprovado
        achados = laudo.falhas if args.so_falhas else laudo.achados
        for a in achados:
            linha = a.linha if a.linha is not None else "-"
            print(f"{nome}:{linha}: [{a.categoria}] {a.item}: {a.mensagem}")
        print(f"{nome}: {len(laudo.falhas)} falha(s), {len(laudo.achados)} achado(s)")
    return 1 if houve_falha else 0


if __name__ == "__main__":
    sys.exit(main())
