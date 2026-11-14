"""Tarefa 04: sorteia a amostra de validacao e, validado o conferidor, corrige a base.

    .venv/bin/python -B ENTREGA01/task04_correcao_base/script_correcao.py

Nunca escreve em regras_originais/: a base corrigida nasce em dados_saida/base_corrigida/.
A conferencia vive em src/conferidor_gobr; aqui so ha copia, substituicao e registro.
Nenhum modelo de linguagem: as inferencias foram feitas pelo Executor, caso a caso, e
estao fixadas na tabela CORRECOES com o motivo.
"""

import csv
import hashlib
import random
import sys
from collections import Counter
from dataclasses import dataclass

import config


def _erro_config(msg: str) -> None:
    raise SystemExit(f"erro de configuracao: {msg}. Ajuste em {config.__file__}")


def validar_config() -> None:
    for etapa in config.ETAPAS:
        if etapa not in config.ETAPAS_ACEITAS:
            _erro_config(f"etapa '{etapa}' invalida; aceitas: {', '.join(config.ETAPAS_ACEITAS)}")
    if not isinstance(config.SEMENTE_AMOSTRA, int):
        _erro_config(f"SEMENTE_AMOSTRA={config.SEMENTE_AMOSTRA!r}; esperado inteiro")
    if not isinstance(config.TAMANHO_AMOSTRA, int) or config.TAMANHO_AMOSTRA <= 0:
        _erro_config(f"TAMANHO_AMOSTRA={config.TAMANHO_AMOSTRA!r}; esperado inteiro positivo")
    if config.VALIDACAO_APROVADA not in (True, False):
        _erro_config(f"VALIDACAO_APROVADA={config.VALIDACAO_APROVADA!r}; aceitos: True, False")
    if config.EXTENSAO_ENTRADA != ".gobr":
        _erro_config(f"EXTENSAO_ENTRADA={config.EXTENSAO_ENTRADA!r}; aceita: '.gobr'")
    if config.PASTA_BASE_CORRIGIDA.resolve() == config.PASTA_ENTRADA.resolve():
        _erro_config("PASTA_BASE_CORRIGIDA nao pode coincidir com PASTA_ENTRADA")
    if not (config.PASTA_SRC / "conferidor_gobr" / "conferidor.py").is_file():
        _erro_config(f"PASTA_SRC={config.PASTA_SRC} nao contem conferidor_gobr/conferidor.py")


validar_config()
sys.path.insert(0, str(config.PASTA_SRC))

from conferidor_gobr.conferidor import Laudo, conferir  # noqa: E402
from conferidor_gobr.itens_obrigatorios import CATEGORIAS_DE_FALHA, NAO_DOCUMENTADA  # noqa: E402


@dataclass(frozen=True)
class Correcao:
    arquivo: str
    linha: int  # linha na base original; na insercao, a linha que o texto novo passa a ocupar
    item_obrigatorio: str
    tipo: str
    texto_original: str  # "" na insercao
    texto_novo: str  # igual ao original quando tipo = nao_inferivel
    motivo: str
    insercao: bool = False


# Cada linha corresponde a um achado de falha do laudo da tarefa 03. O texto original e
# conferido antes da troca: se o arquivo nao for o esperado, o script para.
CORRECOES: tuple[Correcao, ...] = (
    Correcao("regra_140.gobr", 131, "caractere_fora_do_lexico", "deterministica",
             "    quando recencia de positivacao do vendedor em 21 dias\x01",
             "    quando recencia de positivacao do vendedor em 21 dias",
             "Remove o caractere de controle U+0001 no fim da linha; o lexico do manual (p.58) nao o admite."),
    Correcao("regra_135.gobr", 253, "grafia_documentada", "deterministica",
             "           e curva a com a empresa", "           e curva A com a empresa",
             "Manual escreve 'curva A com a empresa' (p.28); so a caixa muda."),
    Correcao("regra_135.gobr", 259, "grafia_documentada", "deterministica",
             "           e curva b com a empresa", "           e curva B com a empresa",
             "Manual escreve 'curva B com a empresa' (p.28); so a caixa muda."),
    Correcao("regra_135.gobr", 265, "grafia_documentada", "deterministica",
             "           e curva c com a empresa", "           e curva C com a empresa",
             "Manual escreve 'curva C com a empresa' (p.28); so a caixa muda."),
    Correcao("regra_228.gobr", 27, "grafia_documentada", "deterministica",
             "        e curva c com a empresa", "        e curva C com a empresa",
             "Manual escreve 'curva C com a empresa' (p.28); so a caixa muda."),
    Correcao("regra_032.gobr", 523, "parenteses_balanceados", "inferencia",
             '    quando ramo de atividade igual("CONS. FINAL"',
             '    quando ramo de atividade igual("CONS. FINAL")',
             "Fecha o parentese. As outras 17 linhas do segmento Corporativo/Consumidor no arquivo "
             "(l.229 a 281 e 471 a 517) sao 'quando ramo de atividade igual(\"CONS. FINAL\")'; "
             "nao ha outro filtro em nenhum bloco 'Inativos Curva C' do arquivo (l.99-104, 159, 219, "
             "279, 341, 401, 461)."),
    Correcao("regra_032.gobr", 524, "parametros_tem_atendimento", "inferencia",
             "", "    frequencia de 28 dias",
             "Insere a frequencia apos a l.523. Nos 8 segmentos do arquivo, o bloco 'Inativos Curva C' "
             "de Norte/Nordeste repete a frequencia do mesmo segmento em Sul/Sudeste (14, 14, 21 nos "
             "tres primeiros); o de Corporativo/Consumidor Sul (l.279-282) usa 28 dias, e os Inativos "
             "Curva A e B de Norte Corporativo (l.509, 515) tambem usam 28 dias.",
             insercao=True),
    Correcao("regra_221.gobr", 48, "aspas_balanceadas", "inferencia",
             '        preferencia nos dias uteis e no sabado"',
             "        preferencia nos dias uteis e no sabado",
             "Remove a aspa solta. As outras 5 linhas de preferencia do arquivo sao exatamente "
             "'preferencia nos dias uteis e no sabado', sem aspa; nada na linha abre string."),
    Correcao("regra_080.gobr", 11, "cabecalho_bem_formado", "inferencia",
             'parametros "Regra Padrao da Empresa Customizavel: mensal para inativos com cnae do erp '
             'que inicia com ("03","47","27")":',
             'parametros "Regra Padrao da Empresa Customizavel: mensal para inativos com cnae do erp '
             "que inicia com ('03','47','27')\":",
             "Troca as aspas duplas internas por simples. O nome copia o filtro da l.13; a base usa "
             "aspa simples para citar dentro de nome (ex.: regra_132, 162 e 187, \"Não agendar 'Inadimplentes'\"). "
             "Texto do rotulo preservado."),
    Correcao("regra_080.gobr", 29, "nomes_parametros_distintos", "nao_inferivel",
             'parametros "Regra Padrao da Empresa Customizavel: 15 dias para inativos":',
             'parametros "Regra Padrao da Empresa Customizavel: 15 dias para inativos":',
             "Bloco l.29-33 e copia byte a byte do bloco l.17-21 (mesmo nome, filtro, frequencia e "
             "preferencia). Nao ha no arquivo nem no modelo semelhante (regra_107) indicio da regra "
             "pretendida; renomear inventaria um nome e apagar mudaria o conteudo. Arquivo mantido."),
    Correcao("regra_083.gobr", 21, "nomes_parametros_distintos", "inferencia",
             'parametros "Regra Padrao do goVendas Customizavel - Frequencia de inativos":',
             'parametros "Regra Padrao do goVendas Customizavel - Frequencia de clientes sem vendas":',
             "Renomeia o segundo bloco. O corpo e 'quando sem venda' (nao 'inativos'); a regra_072 tem "
             "o mesmo modelo, com os mesmos 3 blocos e corpos na mesma ordem, e la o terceiro se chama "
             "'Frequencia de clientes sem vendas'. Mantido o separador ' - ' da propria 083."),
)


def validar_correcoes() -> None:
    for c in CORRECOES:
        if c.tipo not in config.TIPOS_CORRECAO:
            raise SystemExit(f"correcao {c.arquivo}:{c.linha}: tipo '{c.tipo}' invalido; aceitos: "
                             f"{', '.join(config.TIPOS_CORRECAO)} (tabela CORRECOES em {__file__})")
        if c.tipo == "nao_inferivel" and c.texto_novo != c.texto_original:
            raise SystemExit(f"correcao {c.arquivo}:{c.linha}: nao_inferivel nao pode mudar o texto")


def carregar_entrada() -> dict[str, str]:
    pasta = config.PASTA_ENTRADA
    if not pasta.is_dir():
        raise SystemExit(f"abortado: pasta de entrada inexistente: {pasta}")
    arquivos = sorted(pasta.glob("*" + config.EXTENSAO_ENTRADA))
    if len(arquivos) != config.CONTAGEM_ESPERADA:
        raise SystemExit(f"abortado: {len(arquivos)} arquivos em {pasta}; esperado {config.CONTAGEM_ESPERADA}")
    return {f.name: f.read_text(encoding="utf-8") for f in arquivos}


def sortear_amostra(laudos: dict[str, Laudo]) -> list[str]:
    aprovados = sorted(nome for nome, laudo in laudos.items() if laudo.aprovado)
    # Lista ordenada antes do sorteio: a amostra depende so da semente, nao da ordem do disco.
    amostra = sorted(random.Random(config.SEMENTE_AMOSTRA).sample(aprovados, config.TAMANHO_AMOSTRA))
    print(f"amostra: {len(aprovados)} aprovados, semente {config.SEMENTE_AMOSTRA}: {', '.join(amostra)}")
    return amostra


def _sha(caminho) -> str:
    return hashlib.sha256(caminho.read_bytes()).hexdigest()


def copiar_base() -> None:
    destino = config.PASTA_BASE_CORRIGIDA
    destino.mkdir(parents=True, exist_ok=True)
    origem = sorted(config.PASTA_ENTRADA.glob("*" + config.EXTENSAO_ENTRADA))
    # Copia por bytes: qualquer decodificacao poderia normalizar o texto sem aviso.
    for f in origem:
        (destino / f.name).write_bytes(f.read_bytes())
    divergentes = [f.name for f in origem if _sha(f) != _sha(destino / f.name)]
    if divergentes or len(list(destino.glob("*.gobr"))) != len(origem):
        raise SystemExit(f"PARADA: copia nao bate por sha256: {divergentes}")
    print(f"copia: {len(origem)} arquivos, sha256 identico em todos")


def aplicar_correcoes() -> None:
    por_arquivo: dict[str, list[Correcao]] = {}
    for c in CORRECOES:
        por_arquivo.setdefault(c.arquivo, []).append(c)
    for arquivo, correcoes in por_arquivo.items():
        caminho = config.PASTA_BASE_CORRIGIDA / arquivo
        linhas = caminho.read_text(encoding="utf-8").split("\n")
        # De baixo para cima, para que a insercao nao desloque as linhas ainda a corrigir.
        for c in sorted(correcoes, key=lambda c: c.linha, reverse=True):
            if c.insercao:
                anterior = c.linha - 2
                linhas.insert(c.linha - 1, c.texto_novo)
                print(f"correcao {arquivo}: inserida linha {c.linha} apos '{linhas[anterior].strip()}'")
                continue
            atual = linhas[c.linha - 1]
            if atual != c.texto_original:
                raise SystemExit(f"PARADA: {arquivo}:{c.linha} difere do esperado: {atual!r}")
            linhas[c.linha - 1] = c.texto_novo
        caminho.write_text("\n".join(linhas), encoding="utf-8", newline="\n")


def gravar_correcoes() -> None:
    campos = ["arquivo", "linha", "item_obrigatorio", "tipo", "texto_original", "texto_novo", "motivo"]
    with (config.PASTA_SAIDA / "correcoes.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(campos)
        for c in CORRECOES:
            w.writerow([c.arquivo, c.linha, c.item_obrigatorio, c.tipo,
                        c.texto_original.replace("\x01", "\\x01"), c.texto_novo, c.motivo])

    o = ["# Registro de correcoes da base .gobr", "",
         "Base original (somente leitura): `ENTREGA01/task02_entradas/regras_originais/`.",
         "Base corrigida: `ENTREGA01/task04_correcao_base/dados_saida/base_corrigida/`.",
         "Linha = numero na base original (na insercao, a linha que o texto novo ocupa).", "",
         "| Tipo | Correcoes |", "|---|---:|"]
    contagem = Counter(c.tipo for c in CORRECOES)
    o += [f"| {t} | {contagem[t]} |" for t in config.TIPOS_CORRECAO]
    o.append("")
    titulos = {"deterministica": "Correcoes deterministicas",
               "inferencia": "Correcoes por inferencia (revisar uma por uma)",
               "nao_inferivel": "Casos nao inferiveis (arquivo mantido)"}
    for tipo in config.TIPOS_CORRECAO:
        o += [f"## {titulos[tipo]}", ""]
        for c in (c for c in CORRECOES if c.tipo == tipo):
            original = c.texto_original.replace("\x01", "\\x01") or "(linha inexistente: insercao)"
            o += [f"### {c.arquivo}, linha {c.linha} — `{c.item_obrigatorio}`", "",
                  "Antes:", "", "```", original, "```", "",
                  "Depois:", "", "```", c.texto_novo, "```", "",
                  f"Motivo: {c.motivo}", ""]
    (config.PASTA_SAIDA / "correcoes.md").write_text("\n".join(o), encoding="utf-8", newline="\n")


def conferir_base_corrigida(laudos_antes: dict[str, Laudo]) -> None:
    arquivos = sorted(config.PASTA_BASE_CORRIGIDA.glob("*.gobr"))
    laudos = {f.name: conferir(f.read_text(encoding="utf-8")) for f in arquivos}
    with (config.PASTA_SAIDA / "laudo_pos_correcao.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["arquivo", "item", "categoria", "linha", "mensagem", "construcao"])
        for nome, laudo in laudos.items():
            for a in laudo.achados:
                w.writerow([nome, a.item, a.categoria, "" if a.linha is None else a.linha,
                            a.mensagem, a.construcao or ""])

    def falhas(ls):
        return Counter((n, a.item) for n, l in ls.items() for a in l.achados if a.categoria in CATEGORIAS_DE_FALHA)

    def nao_doc(ls):
        return Counter((n, a.construcao) for n, l in ls.items() for a in l.achados if a.categoria == NAO_DOCUMENTADA)

    antes, depois = falhas(laudos_antes), falhas(laudos)
    corrigidas = Counter((c.arquivo, c.item_obrigatorio) for c in CORRECOES if c.tipo != "nao_inferivel")
    esperadas = Counter((c.arquivo, c.item_obrigatorio) for c in CORRECOES if c.tipo == "nao_inferivel")
    novas = depois - antes
    remanescentes_inesperadas = depois - esperadas
    nd_antes, nd_depois = nao_doc(laudos_antes), nao_doc(laudos)
    print(f"pos-correcao: falhas antes {sum(antes.values())}, depois {sum(depois.values())}; "
          f"corrigidas {sum(corrigidas.values())}; nao_inferivel {sum(esperadas.values())}")
    print(f"pos-correcao: remanescentes {dict(depois)}")
    print(f"pos-correcao: falhas novas {dict(novas) or 'nenhuma'}")
    print(f"pos-correcao: nao documentadas antes {sum(nd_antes.values())}, depois {sum(nd_depois.values())}; "
          f"mesmas (arquivo, construcao): {nd_antes == nd_depois}")
    if sum(nd_antes.values()) != config.NAO_DOCUMENTADAS_LAUDO_ANTERIOR:
        raise SystemExit(f"PARADA: laudo da base original tem {sum(nd_antes.values())} nao documentadas; "
                         f"esperado {config.NAO_DOCUMENTADAS_LAUDO_ANTERIOR}")
    if novas or remanescentes_inesperadas or nd_antes != nd_depois:
        raise SystemExit("PARADA: base corrigida diverge do esperado (ver linhas acima)")


def main() -> None:
    validar_correcoes()
    textos = carregar_entrada()
    laudos = {nome: conferir(texto) for nome, texto in textos.items()}
    if "amostra" in config.ETAPAS:
        sortear_amostra(laudos)
    if "correcao" in config.ETAPAS:
        if not config.VALIDACAO_APROVADA:
            raise SystemExit("correcao bloqueada: VALIDACAO_APROVADA = False em config.py; "
                             "a conferencia manual da amostra tem de passar antes")
        falhas_antes = sum(len(l.falhas) for l in laudos.values())
        if falhas_antes != config.FALHAS_LAUDO_ANTERIOR or len(CORRECOES) != falhas_antes:
            raise SystemExit(f"PARADA: {falhas_antes} falhas no laudo, {len(CORRECOES)} correcoes, "
                             f"esperado {config.FALHAS_LAUDO_ANTERIOR}")
        copiar_base()
        aplicar_correcoes()
        gravar_correcoes()
        conferir_base_corrigida(laudos)


if __name__ == "__main__":
    main()
