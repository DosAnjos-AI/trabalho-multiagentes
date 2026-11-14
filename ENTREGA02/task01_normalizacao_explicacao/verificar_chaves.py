"""Confere o arquivo auxiliar de regras contra o manual/.

Falha alta: qualquer chave inexistente ou topico de regra sem entrada encerra
com codigo 1 e mensagem que diz o valor recebido e onde procurar.
"""
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
MANUAL = RAIZ / "manual"
AUXILIAR_PADRAO = Path(__file__).resolve().parent / "regras_para_normalizador_v2.md"


def chaves_do_auxiliar(texto: str) -> list[str]:
    """Chaves declaradas no arquivo auxiliar (antes de '## Sem entrada'), na ordem do arquivo.

    Funcao propria para o normalizador importar: a mesma lista decide se a chave devolvida
    pelo modelo existe, sem duplicar a regra de leitura do auxiliar.
    """
    corpo = texto.partition("## Sem entrada")[0]
    return re.findall(r"^- chave: (.+)$", corpo, flags=re.M)


def titulos(arquivo: Path) -> set[str]:
    """Titulos '## ' do arquivo; linhas dentro de bloco de codigo nao contam."""
    achados, em_codigo = set(), False
    for linha in arquivo.read_text(encoding="utf-8").splitlines():
        if linha.startswith("```"):
            em_codigo = not em_codigo
        elif not em_codigo and linha.startswith("## "):
            achados.add(linha[3:].strip())
    return achados


def main() -> int:
    # Caminho do auxiliar pode ser trocado por argumento (usado no teste do caminho de erro).
    # Lido aqui e nao no import, para o normalizador importar este arquivo sem herdar o argv dele.
    AUXILIAR = Path(sys.argv[1]) if len(sys.argv) > 1 else AUXILIAR_PADRAO
    texto = AUXILIAR.read_text(encoding="utf-8")
    corpo, _, sem_entrada = texto.partition("## Sem entrada")
    erros, arquivos_citados = [], set()

    chaves = chaves_do_auxiliar(texto)
    for chave in chaves:
        caminho, _, secao = chave.partition("#")
        alvo = MANUAL / caminho.strip()
        if not alvo.is_file():
            erros.append(f"chave '{chave}': arquivo nao existe; procurar em {MANUAL}")
            continue
        arquivos_citados.add(alvo.relative_to(MANUAL).as_posix())
        if secao and secao.strip() not in titulos(alvo):
            erros.append(f"chave '{chave}': secao '{secao}' nao existe; procurar titulos '## ' em {alvo}")

    # Topico de regra = todo .md de manual/. Cobre quem tem chave ou esta em "Sem entrada".
    declarados = {
        p.as_posix().replace("03-secoes/", "")
        for p in map(Path, re.findall(r"^- ([\w./-]+\.md)", sem_entrada, flags=re.M))
    }
    for md in sorted(MANUAL.rglob("*.md")):
        rel = md.relative_to(MANUAL).as_posix()
        cobertos = {a.replace("03-secoes/", "") for a in arquivos_citados} | declarados
        # 'Sem entrada' pode listar varios arquivos na mesma linha, separados por virgula.
        listados = set(re.findall(r"[\w./-]+\.md", sem_entrada))
        if rel.replace("03-secoes/", "") not in cobertos and rel not in listados and md.name not in listados:
            erros.append(f"topico '{rel}': sem chave e fora de 'Sem entrada' em {AUXILIAR.name}")

    if erros:
        print("FALHA\n" + "\n".join(erros))
        return 1
    print(f"OK: {len(chaves)} chaves validas, {len(arquivos_citados)} arquivos citados, "
          f"{len(list(MANUAL.rglob('*.md')))} topicos conferidos em {MANUAL}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
