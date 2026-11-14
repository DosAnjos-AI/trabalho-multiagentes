"""Tarefa 03: calibra o conferidor, confere a base .gobr e grava laudo e inventario.

    .venv/bin/python ENTREGA01/task03_conferencia_base/script_conferencia.py

Nao altera nenhum arquivo .gobr: so le a pasta de entrada e escreve em dados_saida/.
A conferencia em si vive em src/conferidor_gobr; aqui so ha leitura de pasta e escrita.
"""

import csv
import sys
from collections import defaultdict
from pathlib import Path

import config



def _erro_config(msg: str) -> None:
    raise SystemExit(f"erro de configuracao: {msg}. Ajuste em {Path(config.__file__)}")


def validar_config() -> None:
    for etapa in config.ETAPAS:
        if etapa not in config.ETAPAS_ACEITAS:
            _erro_config(f"etapa '{etapa}' invalida; aceitas: {', '.join(config.ETAPAS_ACEITAS)}")
    if "conferencia" in config.ETAPAS and "calibracao" not in config.ETAPAS:
        _erro_config("ETAPAS contem 'conferencia' sem 'calibracao'; a calibracao e obrigatoria")
    if not isinstance(config.CONTAGEM_ESPERADA, int) or config.CONTAGEM_ESPERADA <= 0:
        _erro_config(f"CONTAGEM_ESPERADA={config.CONTAGEM_ESPERADA!r}; esperado inteiro positivo")
    if config.EXTENSAO_ENTRADA != ".gobr":
        _erro_config(f"EXTENSAO_ENTRADA={config.EXTENSAO_ENTRADA!r}; aceita: '.gobr'")
    if not (config.PASTA_SRC / "conferidor_gobr" / "conferidor.py").is_file():
        _erro_config(f"PASTA_SRC={config.PASTA_SRC} nao contem conferidor_gobr/conferidor.py")
    for nome in config.CENARIOS:
        if Path(nome).suffix == ".gobr":
            _erro_config(f"cenario '{nome}' com extensao .gobr; use .txt")


validar_config()
sys.path.insert(0, str(config.PASTA_SRC))

from conferidor_gobr.conferidor import Laudo, conferir  # noqa: E402
from conferidor_gobr.itens_obrigatorios import (  # noqa: E402
    CATEGORIAS,
    ITENS,
    NAO_DOCUMENTADA,
)


def carregar_entrada() -> dict[str, str]:
    pasta = config.PASTA_ENTRADA
    if not pasta.is_dir():
        raise SystemExit(f"abortado: pasta de entrada inexistente: {pasta}")
    arquivos = sorted(pasta.glob("*" + config.EXTENSAO_ENTRADA))
    if len(arquivos) != config.CONTAGEM_ESPERADA:
        raise SystemExit(f"abortado: {len(arquivos)} arquivos {config.EXTENSAO_ENTRADA} em {pasta}; "
                         f"esperado {config.CONTAGEM_ESPERADA}. Nada foi conferido.")
    return {f.name: f.read_text(encoding="utf-8") for f in arquivos}


def calibrar(laudos: dict[str, Laudo]) -> None:
    problemas = []

    caso = config.CALIBRACAO_PARENTESE
    itens = {a.item for a in laudos[caso["arquivo"]].achados}
    for item in caso["itens_esperados"]:
        linhas = [a.linha for a in laudos[caso["arquivo"]].achados if a.item == item]
        print(f"calibracao {caso['arquivo']}: {item} -> {'acusado nas linhas ' + str(linhas) if linhas else 'NAO acusado'}")
        if item not in itens:
            problemas.append(f"{caso['arquivo']} nao acusou {item}")

    caso = config.CALIBRACAO_CAIXA
    acertos = [a for a in laudos[caso["arquivo"]].achados
               if a.item == caso["item"] and a.categoria == caso["categoria"]
               and caso["trecho"] in a.mensagem]
    print(f"calibracao {caso['arquivo']}: {caso['item']}/{caso['categoria']} com '{caso['trecho']}' -> "
          + (f"acusado na linha {[a.linha for a in acertos]}" if acertos else "NAO acusado"))
    if not acertos:
        problemas.append(f"{caso['arquivo']} nao acusou '{caso['trecho']}' como {caso['categoria']}")

    acusados = sorted(nome for nome, laudo in laudos.items()
                      if any(a.item in config.CALIBRACAO_VERSION_ITENS for a in laudo.achados))
    print(f"calibracao version: {len(acusados)} arquivo(s) com achado de "
          f"{'/'.join(config.CALIBRACAO_VERSION_ITENS)} em {len(laudos)}")
    if acusados:
        problemas.append(f"achado de version em {len(acusados)} arquivo(s): {', '.join(acusados)}")

    if problemas:
        raise SystemExit("calibracao FALHOU, nenhum numero vale: " + "; ".join(problemas))
    print("calibracao: os tres casos conhecidos sairam como esperado")


def _escrever(caminho: Path, texto: str) -> None:
    caminho.write_text(texto, encoding="utf-8", newline="\n")


def gravar_laudo(laudos: dict[str, Laudo]) -> int:
    caminho = config.PASTA_SAIDA / "laudo_conformidade.csv"
    linhas = 0
    with caminho.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["arquivo", "item", "categoria", "linha", "mensagem", "construcao"])
        for nome, laudo in laudos.items():
            for a in laudo.achados:
                w.writerow([nome, a.item, a.categoria, "" if a.linha is None else a.linha,
                            a.mensagem, a.construcao or ""])
                linhas += 1
    return linhas


def gravar_resumo(laudos: dict[str, Laudo], linhas_laudo: int) -> None:
    contagem: dict[tuple[str, str], int] = defaultdict(int)
    arquivos_por_item: dict[tuple[str, str], set[str]] = defaultdict(set)
    for nome, laudo in laudos.items():
        for a in laudo.achados:
            contagem[(a.item, a.categoria)] += 1
            arquivos_por_item[(a.item, a.categoria)].add(nome)
    total = sum(contagem.values())
    if total != linhas_laudo:
        raise SystemExit(f"inconsistencia: resumo soma {total}, laudo tem {linhas_laudo} linhas")

    sem_falha = [n for n, l in laudos.items() if l.aprovado]
    com_falha = [n for n, l in laudos.items() if not l.aprovado]
    sem_achado = [n for n, l in laudos.items() if not l.achados]

    o = ["# Resumo de conformidade da base .gobr", ""]
    o.append(f"Entrada: `{config.PASTA_ENTRADA.relative_to(config.RAIZ).as_posix()}/`, "
             f"{len(laudos)} arquivos.")
    o.append("Falha = categoria `item_obrigatorio_ausente` ou `divergencia_com_manual`. "
             "`construcao_nao_documentada` nao e falha do arquivo.")
    o += ["", "## Arquivos", "", "| Situacao | Arquivos |", "|---|---|",
          f"| Sem nenhuma falha | {len(sem_falha)} |",
          f"| Com ao menos uma falha | {len(com_falha)} |",
          f"| Total | {len(laudos)} |", "",
          f"Arquivos sem nenhum achado, de nenhuma categoria: {len(sem_achado)}.", ""]

    o += ["## Achados por item", "",
          "| Item | Categoria | Achados | Arquivos |", "|---|---|---:|---:|"]
    for (item, cat) in sorted(contagem, key=lambda k: (CATEGORIAS.index(k[1]), -contagem[k], k[0])):
        o.append(f"| `{item}` | {cat} | {contagem[(item, cat)]} | {len(arquivos_por_item[(item, cat)])} |")
    o.append(f"| **Total** | | **{total}** | |")
    o += ["", f"O total ({total}) e igual ao numero de linhas de dados de `laudo_conformidade.csv`.", ""]

    por_categoria = defaultdict(int)
    for (_, cat), n in contagem.items():
        por_categoria[cat] += n
    o += ["## Achados por categoria", "", "| Categoria | Achados |", "|---|---:|"]
    for cat in CATEGORIAS:
        o.append(f"| {cat} | {por_categoria[cat]} |")
    o.append("")

    o += ["## Arquivos com falha", "", "| Arquivo | Itens que falharam |", "|---|---|"]
    for nome in com_falha:
        itens = sorted({f"`{a.item}` (l.{a.linha})" for a in laudos[nome].falhas})
        o.append(f"| {nome} | {', '.join(itens)} |")
    o.append("")

    conferidos_sem_achado = [i.identificador for i in ITENS if i.verificavel
                             and not any(k[0] == i.identificador for k in contagem)]
    o += ["## Itens verificaveis conferidos e sem nenhum achado", ""]
    o += [f"- `{i}`" for i in conferidos_sem_achado]
    o += ["", "## Itens nao verificaveis (na lista, fora da conferencia)", ""]
    o += [f"- `{i.identificador}`: {i.descricao}" for i in ITENS if not i.verificavel]
    o += ["", "## Arquivos sem nenhum achado", ""]
    o += [f"- {n}" for n in sem_achado] if sem_achado else ["- nenhum"]
    o.append("")
    _escrever(config.PASTA_SAIDA / "resumo_conformidade.md", "\n".join(o))


def gravar_inventario(laudos: dict[str, Laudo], linhas_laudo: int) -> tuple[int, int, int]:
    arquivos: dict[str, list[str]] = defaultdict(list)
    ocorrencias: dict[str, int] = defaultdict(int)
    exemplo: dict[str, tuple[str, int | None, str]] = {}
    for nome, laudo in laudos.items():
        for a in laudo.achados:
            if a.categoria != NAO_DOCUMENTADA:
                continue
            ocorrencias[a.construcao] += 1
            if nome not in arquivos[a.construcao]:
                arquivos[a.construcao].append(nome)
            exemplo.setdefault(a.construcao, (nome, a.linha, a.trecho or ""))

    ordem = sorted(arquivos, key=lambda c: (-len(arquivos[c]), -ocorrencias[c], c))
    soma_arquivos = sum(len(v) for v in arquivos.values())
    soma_ocorrencias = sum(ocorrencias.values())

    with (config.PASTA_SAIDA / "inventario_nao_documentado.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["construcao", "quantidade_arquivos", "ocorrencias", "arquivos"])
        for c in ordem:
            w.writerow([c, len(arquivos[c]), ocorrencias[c], ";".join(arquivos[c])])

    o = ["# Inventario de construcoes nao documentadas pelo manual", "",
         "Uma linha por construcao, da mais usada para a menos usada (por quantidade de arquivos).",
         "Valores concretos aparecem abstraidos: `\"<texto>\"`, `<N>`, `'<data>'`.",
         "Nao e falha do arquivo: por decisao do Mestre, onde o manual nao documenta, a base sobrepoe o manual.",
         "",
         f"- Construcoes distintas: {len(ordem)}",
         f"- Ocorrencias (= achados `construcao_nao_documentada` no laudo): {soma_ocorrencias}",
         f"- Soma das quantidades de arquivos por construcao: {soma_arquivos}",
         f"- Arquivos com ao menos uma construcao nao documentada: "
         f"{len({n for v in arquivos.values() for n in v})} de {len(laudos)}",
         "",
         "Ocorrencias superam a soma de arquivos porque o mesmo arquivo repete a mesma construcao "
         "em varios blocos.", ""]
    for i, c in enumerate(ordem, 1):
        nome, linha, trecho = exemplo[c]
        o += [f"## {i}. `{c}`", "",
              f"Arquivos: {len(arquivos[c])} | Ocorrencias: {ocorrencias[c]}", "",
              f"Exemplo real ({nome}, linha {linha}):", "", "```", trecho, "```", ""]
    _escrever(config.PASTA_SAIDA / "inventario_nao_documentado.md", "\n".join(o))
    return len(ordem), soma_ocorrencias, soma_arquivos


def rodar_cenarios() -> None:
    for nome, texto in config.CENARIOS.items():
        caminho = config.PASTA_SAIDA / nome
        _escrever(caminho, texto)
        laudo = conferir(caminho.read_text(encoding="utf-8"))
        print(f"cenario {nome}: {len(laudo.falhas)} falha(s), {len(laudo.achados)} achado(s)")
        for a in laudo.achados:
            print(f"    linha {a.linha}: [{a.categoria}] {a.item}: {a.mensagem}")


def main() -> None:
    config.PASTA_SAIDA.mkdir(parents=True, exist_ok=True)
    laudos: dict[str, Laudo] = {}
    if {"calibracao", "conferencia"} & set(config.ETAPAS):
        textos = carregar_entrada()
        laudos = {nome: conferir(texto) for nome, texto in textos.items()}
        print(f"entrada: {len(textos)} arquivos {config.EXTENSAO_ENTRADA} em {config.PASTA_ENTRADA}")
    if "calibracao" in config.ETAPAS:
        calibrar(laudos)
    if "conferencia" in config.ETAPAS:
        linhas = gravar_laudo(laudos)
        gravar_resumo(laudos, linhas)
        distintas, ocorr, soma_arq = gravar_inventario(laudos, linhas)
        sem_falha = sum(1 for l in laudos.values() if l.aprovado)
        cat3 = sum(1 for l in laudos.values() for a in l.achados if a.categoria == NAO_DOCUMENTADA)
        print(f"laudo: {linhas} achados; {sem_falha} arquivos sem falha, {len(laudos) - sem_falha} com falha")
        print(f"inventario: {distintas} construcoes, {ocorr} ocorrencias (laudo cat.3 = {cat3}), "
              f"soma de arquivos por construcao = {soma_arq}")
        if ocorr != cat3:
            raise SystemExit("inconsistencia entre inventario e laudo")
    if "cenarios" in config.ETAPAS:
        rodar_cenarios()


if __name__ == "__main__":
    main()
