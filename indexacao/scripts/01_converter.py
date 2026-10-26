"""Converte os 249 normalizado.md do formato 3.1 para o 4.0, no mesmo caminho.

Uso (da raiz do projeto): .venv/bin/python indexacao/scripts/01_converter.py
"""
import re
import sys
from pathlib import Path

# Os scripts moram em indexacao/scripts; o pacote (config, conversao, indice) fica um nível acima.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import yaml

import config
from conversao.escritor_v40 import escrever_v40
from conversao.leitor_v31 import ErroConversao, ler_v31
from conversao.leitor_v40 import ler_v40


def conferir_estrutura() -> list[Path]:
    """Aborta se simulacao/ não tiver regra_001..regra_249 com normalizado.md."""
    esperados = [f"{config.PREFIXO_PASTA}{i:03d}" for i in range(1, config.TOTAL_PASTAS + 1)]
    faltando = [e for e in esperados if not (config.PASTA_SIMULACAO / e / config.NOME_NORMALIZADO).is_file()]
    if faltando:
        sys.exit(f"ABORTADO: estrutura diferente do esperado; sem {config.NOME_NORMALIZADO}: {faltando[:10]}")
    return [config.PASTA_SIMULACAO / e / config.NOME_NORMALIZADO for e in esperados]


def sem_ancoras(texto: str) -> bool:
    """Confere o front matter e o bloco yaml; o resto do arquivo é markdown, não YAML."""
    trechos = [texto.split("\n---\n", 1)[0]] + re.findall(r"```yaml\n(.*?)```", texto, re.S)
    return not any(
        t.__class__.__name__ in ("AnchorToken", "AliasToken") for tr in trechos for t in yaml.scan(tr)
    )


def converter(caminho: Path) -> tuple[int, int]:
    """Converte um arquivo; só grava depois de reabrir o resultado e validar."""
    id_regra = caminho.parent.name
    linhas_antes = len(caminho.read_text(encoding="utf-8").splitlines())
    novo = escrever_v40(ler_v31(caminho))

    # Valida o texto antes de tocar no arquivo, para uma falha nunca deixar meio-termo.
    tmp = caminho.with_suffix(".tmp40")
    tmp.write_text(novo, encoding="utf-8")
    try:
        lido = ler_v40(tmp)  # o temporário fica na mesma pasta, então o id da regra é o mesmo
        if len(lido["regras"]) != lido["cabecalho"]["total_regras"]:
            raise ErroConversao(id_regra, "linhas de ## Regras diferem de total_regras")
        if not sem_ancoras(novo):
            raise ErroConversao(id_regra, "YAML gerado contém âncoras")
        tmp.replace(caminho)
    finally:
        tmp.unlink(missing_ok=True)
    return linhas_antes, len(novo.splitlines())


def main() -> int:
    arquivos = conferir_estrutura()
    falhas: list[tuple[str, str]] = []
    reducoes: list[float] = []
    for caminho in arquivos:
        try:
            antes, depois = converter(caminho)
            reducoes.append(100 * (antes - depois) / antes)
        except ErroConversao as e:
            falhas.append((e.id_regra, e.motivo))
            print(f"FALHA {e}", file=sys.stderr)
    print(f"convertidos: {len(reducoes)}/{len(arquivos)}")
    if reducoes:
        print(f"redução média de linhas: {sum(reducoes) / len(reducoes):.1f}%")
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
