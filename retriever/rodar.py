"""Roda o retriever sobre o único arquivo de ENTRADA/ e grava o relatório em SAIDA/.

Uso (da raiz do projeto):
    .venv/bin/python retriever/rodar.py [--top-n N] [--rerank]

Casca fina sobre recuperar.py: localiza, valida, chama e grava. Toda a lógica de
recuperação é a de recuperar.main(), chamada sem cópia; o modo antigo por
argumento continua lá, intacto.
"""
import argparse
import base64
import contextlib
import datetime as dt
import io
import sys
import traceback
from pathlib import Path

# Antes do import de recuperar: senão ele próprio deixaria retriever/__pycache__.
sys.dont_write_bytecode = True

import recuperar  # noqa: E402  (retriever/ está no sys.path por ser a pasta deste script)

cfg = recuperar.cfg

PASTA_ENTRADA = cfg.RAIZ_PROJETO / "ENTRADA"
PASTA_SAIDA = cfg.RAIZ_PROJETO / "SAIDA"

# Lista fechada por desenho: formato fora dela deve falhar, não ser adivinhado.
EXT_TEXTO = (".txt", ".md")
EXT_IMAGEM = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp"}
EXT_AUDIO = (".mp3", ".wav", ".m4a", ".ogg", ".opus", ".flac", ".aac", ".wma")
# LEIAME.txt é a instrução versionada da própria pasta; contá-lo faria toda execução
# com pedido falhar por "mais de um arquivo".
IGNORADOS = ("LEIAME.txt",)

MARCADOR_IMAGEM = "[pedido enviado como imagem anexa: {nome}]"


def localizar_entrada() -> Path:
    """O único arquivo de pedido em ENTRADA/, ou ErroRetriever dizendo o que corrigir."""
    aceitos = ", ".join(EXT_TEXTO + tuple(EXT_IMAGEM))
    if not PASTA_ENTRADA.is_dir():
        raise recuperar.ErroRetriever(f"pasta {PASTA_ENTRADA} ausente. Crie-a e coloque nela o pedido ({aceitos}).")
    arquivos = sorted(p for p in PASTA_ENTRADA.iterdir()
                      if p.is_file() and not p.name.startswith(".") and p.name not in IGNORADOS)
    if not arquivos:
        raise recuperar.ErroRetriever(
            f"ENTRADA/ está vazia. Coloque nela um arquivo com o pedido: texto ({', '.join(EXT_TEXTO)}) "
            f"ou imagem ({', '.join(EXT_IMAGEM)}).")
    if len(arquivos) > 1:
        # Escolher um por conta própria rodaria um pedido que o usuário talvez não quisesse.
        nomes = ", ".join(repr(p.name) for p in arquivos)
        raise recuperar.ErroRetriever(
            f"ENTRADA/ tem {len(arquivos)} arquivos: {nomes}. Só um é aceito por execução; "
            "deixe apenas o pedido a processar.")
    arquivo = arquivos[0]
    ext = arquivo.suffix.lower()
    if ext in EXT_AUDIO:
        raise recuperar.ErroRetriever(
            f"{arquivo.name!r}: áudio ({ext}) não é suportado nesta versão, porque não há transcrição. "
            f"Transcreva o pedido para {' ou '.join(EXT_TEXTO)}.")
    if ext not in EXT_TEXTO and ext not in EXT_IMAGEM:
        raise recuperar.ErroRetriever(
            f"{arquivo.name!r}: extensão {ext or '(nenhuma)'!r} não aceita. Aceitos: {aceitos}.")
    return arquivo


def preparar_imagem(arquivo: Path) -> None:
    """Faz recuperar.main() enviar a imagem à API sem alterar recuperar.py.

    Três ajustes, só em memória e só nesta execução:
    - main() lê a entrada com read_text, o que quebraria num binário; o caminho
      passa a devolver um marcador, que é o que fica no rastro em entrada.texto;
    - a mensagem de usuário vira [texto do modelo, imagem], formato de conteúdo
      multimodal da API; o texto é exatamente o que montar_usuario produziria;
    - tipo_input vai como 'imagem', valor que NORMALIZACAO.md (seção 4.3) prevê
      para consulta. Mandar 'texto_corrido' mentiria ao modelo sobre o input.
    Da resposta do modelo em diante nada muda: o contrato e as falhas são os de texto.
    """
    url = f"data:{EXT_IMAGEM[arquivo.suffix.lower()]};base64,{base64.b64encode(arquivo.read_bytes()).decode('ascii')}"
    marcador = MARCADOR_IMAGEM.format(nome=arquivo.name)

    alvo = arquivo.resolve()

    class _CaminhoImagem(type(Path())):
        # main() também usa Path para a cópia do banco: só o arquivo de entrada é trocado.
        def read_text(self, encoding=None, errors=None, newline=None):
            if self == alvo:
                return marcador
            return super().read_text(encoding, errors, newline)

    montar_original = recuperar.montar_usuario

    def montar_com_imagem(*args) -> list[dict]:
        return [{"type": "text", "text": montar_original(*args)},
                {"type": "image_url", "image_url": {"url": url}}]

    recuperar.Path = _CaminhoImagem
    recuperar.montar_usuario = montar_com_imagem
    cfg.CAMPOS_CONSULTA["{tipo_input}"] = "imagem"


class _Tee(io.TextIOBase):
    """Escreve no terminal e num buffer: o relatório de SAIDA/ é o texto do terminal."""

    def __init__(self, terminal, buffer: io.StringIO):
        self.terminal, self.buffer = terminal, buffer

    def write(self, s: str) -> int:
        self.terminal.write(s)
        self.buffer.write(s)
        return len(s)

    def flush(self) -> None:
        self.terminal.flush()


def gravar_relatorio(texto: str, arquivo: Path, agora: dt.datetime) -> Path:
    """Grava em SAIDA/ sem nunca sobrescrever: no mesmo segundo, ganha sufixo _2, _3..."""
    PASTA_SAIDA.mkdir(exist_ok=True)
    base = f"{agora:%Y%m%dT%H%M%S}Z_{arquivo.name}"
    k = 1
    while True:
        caminho = PASTA_SAIDA / (f"{base}.txt" if k == 1 else f"{base}_{k}.txt")
        try:
            with open(caminho, "x", encoding="utf-8") as f:
                f.write(texto)
            return caminho
        except FileExistsError:
            k += 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--top-n", type=int, default=cfg.TOP_N_PADRAO)
    ap.add_argument("--rerank", action="store_true", help="liga o reranking (desligado por padrão)")
    args = ap.parse_args()

    agora = dt.datetime.now(dt.timezone.utc)
    try:
        arquivo = localizar_entrada()
    except recuperar.ErroRetriever as e:
        print(f"ERRO: {e}", file=sys.stderr)
        return 1
    if arquivo.suffix.lower() in EXT_IMAGEM:
        preparar_imagem(arquivo)

    sys.argv = ["recuperar.py", str(arquivo), "--top-n", str(args.top_n)] + (["--rerank"] if args.rerank else [])
    buffer = io.StringIO()
    codigo = 1
    with contextlib.redirect_stdout(_Tee(sys.stdout, buffer)), contextlib.redirect_stderr(_Tee(sys.stderr, buffer)):
        try:
            codigo = recuperar.main()
        except Exception:
            # Impresso aqui dentro para que o erro inesperado também chegue ao relatório.
            traceback.print_exc()
    relatorio = gravar_relatorio(buffer.getvalue(), arquivo, agora)
    print(f"RELATÓRIO: {relatorio.relative_to(cfg.RAIZ_PROJETO)}")
    return codigo


if __name__ == "__main__":
    sys.exit(main())
