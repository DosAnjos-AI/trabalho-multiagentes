"""Conferidor deterministico de arquivos .gobr contra a lista fechada do manual.

Contrato: conferir(texto) recebe o texto de um arquivo .gobr e devolve um Laudo.
Nao imprime e nao le disco, porque o agente vai chamar a funcao com texto em memoria.
Nenhum modelo de linguagem participa: o mesmo texto produz sempre o mesmo laudo.
"""

import re
import unicodedata
from dataclasses import dataclass, field

from .itens_obrigatorios import (
    AUSENTE,
    CATEGORIAS_DE_FALHA,
    CLIENTES,
    CLAUSULAS_SIMPLES,
    DIVERGENCIA,
    FILTROS,
    FONTES,
    FREQUENCIA,
    GATILHOS,
    NAO_DOCUMENTADA,
    PREFERENCIA_ELEMENTOS,
    TEMPORAIS,
    VENDEDORES,
)


@dataclass(frozen=True)
class Achado:
    item: str
    categoria: str
    linha: int | None
    mensagem: str
    # Forma normalizada da construcao; preenchida so em construcao_nao_documentada,
    # porque o inventario agrupa por ela.
    construcao: str | None = None
    # Texto original da clausula, para servir de exemplo real.
    trecho: str | None = None


@dataclass
class Laudo:
    achados: list[Achado] = field(default_factory=list)

    @property
    def falhas(self) -> list[Achado]:
        return [a for a in self.achados if a.categoria in CATEGORIAS_DE_FALHA]

    @property
    def aprovado(self) -> bool:
        return not self.falhas


# =============================================================================
# Normalizacao
# =============================================================================

def _dobrar_acentos(texto: str) -> str:
    # A palavra isolada "é" e protegida: dobrada, viraria a conjuncao "e" e o
    # segmentador partiria "cnae é igual(...)" no meio.
    protegido = re.sub(r"(?<!\w)[éÉ](?!\w)", "\x00", texto)
    sem_acento = "".join(
        c for c in unicodedata.normalize("NFD", protegido) if unicodedata.category(c) != "Mn"
    )
    return sem_acento.replace("\x00", "é")


def _normalizar(texto: str) -> str:
    """Forma canonica para casar com o vocabulario; preserva a caixa."""
    t = _dobrar_acentos(texto)
    t = re.sub(r"\s+", " ", t).strip()
    # Espaco junto a parentese e virgula nao e construcao: o manual nao fixa regra de espacamento.
    t = re.sub(r"\s*\(\s*", "(", t)
    t = re.sub(r"\s*\)", ")", t)
    t = re.sub(r"\s*,\s*", ", ", t)
    return t


def _forma(texto: str) -> str:
    """Rotulo da construcao para o inventario: sem valores concretos, em minuscula."""
    t = _normalizar(texto).lower()
    t = re.sub(r'\("[^"]*"(?:, "[^"]*")+\)', '("<texto>", ...)', t)
    t = re.sub(r'"[^"]*"', '"<texto>"', t)
    t = re.sub(r"'\d{2}:\d{2}'", "'<hora>'", t)
    t = re.sub(r"'[\d-]+'", "'<data>'", t)
    t = re.sub(r"\d+(?:[.,]\d+)*", "<N>", t)
    return t


def _sem_comentario(linha: str) -> str:
    # O "#" so abre comentario fora de aspas; dentro de string (ex.: URL) e texto.
    dupla = simples = False
    for i, c in enumerate(linha):
        if c == '"' and not simples:
            dupla = not dupla
        elif c == "'" and not dupla:
            simples = not simples
        elif c == "#" and not dupla and not simples:
            return linha[:i]
    return linha


def _compilar(padroes) -> list[tuple[re.Pattern, re.Pattern]]:
    """Para cada padrao: versao com caixa exata e versao sem caixa."""
    return [(re.compile(p), re.compile(p, re.IGNORECASE)) for p, *_ in padroes]


_C_FILTROS = _compilar(FILTROS)
_C_GATILHOS = _compilar(GATILHOS)
_C_VENDEDORES = _compilar(VENDEDORES)
_C_CLIENTES = _compilar(CLIENTES)
_C_FONTES = _compilar(FONTES)
_C_FREQUENCIA = _compilar(FREQUENCIA)
_C_PREFERENCIA = _compilar(PREFERENCIA_ELEMENTOS)
_C_SIMPLES = _compilar(CLAUSULAS_SIMPLES)
_C_TEMPORAIS = [(re.compile(p), re.compile(p, re.IGNORECASE), fam) for p, fam, _ in TEMPORAIS]


def _classificar(texto: str, compilados) -> str | None:
    """'ok' casa com caixa exata; 'caixa' so casa ignorando caixa; None nao casa."""
    for exato, sem_caixa, *_ in compilados:
        if exato.fullmatch(texto):
            return "ok"
    for exato, sem_caixa, *_ in compilados:
        if sem_caixa.fullmatch(texto):
            return "caixa"
    return None


# =============================================================================
# Segmentacao de listas unidas por "e"
# =============================================================================

def _posicoes_e_topo(texto: str) -> list[re.Match]:
    """Ocorrencias de ' e ' fora de aspas e parenteses."""
    resultado = []
    for m in re.finditer(r"\s+e\s+", texto):
        antes = texto[: m.start()]
        if antes.count('"') % 2 == 0 and antes.count("(") == antes.count(")"):
            resultado.append(m)
    return resultado


def _ate_proximo_e(texto: str) -> str:
    # O "e" que fecha um "entre X e Y" pertence ao filtro, nao separa filtros.
    for m in _posicoes_e_topo(texto):
        antes = texto[: m.start()]
        ultimo_entre = None
        for me in re.finditer(r"\bentre\b", antes):
            ultimo_entre = me
        if ultimo_entre and not re.search(r"\s+e\s+", antes[ultimo_entre.end():]):
            continue
        return antes
    return texto


def _segmentar(texto: str, compilados) -> list[str]:
    """Parte uma lista de filtros unidos por 'e', preferindo o maior filtro documentado."""
    partes = []
    resto = texto.strip()
    while resto:
        maior = 0
        for _, sem_caixa, *_ in compilados:
            m = re.compile(r"(?:" + sem_caixa.pattern + r")(?=\s+e\s+|$)", re.IGNORECASE).match(resto)
            if m and m.end() > maior:
                maior = m.end()
        fragmento = resto[:maior] if maior else _ate_proximo_e(resto)
        partes.append(fragmento.strip())
        resto = re.sub(r"^\s+e\s+", "", resto[len(fragmento):]).strip()
    return partes


# =============================================================================
# Leitura em blocos e clausulas
# =============================================================================

_CABECALHOS = (
    ("limpar parametros", "limpar_parametros"),
    ("carteira livre", "carteira"),
    ("segmentacao", "segmentacao"),
    ("carteira", "carteira"),
    ("parametros", "parametros"),
    ("time", "time"),
    ("alertas", "alerta"),
    ("alerta", "alerta"),
    ("tags", "tags"),
    ("tag", "tags"),
)
# Palavras de cabecalho que aparecem nos exemplos do manual; "alertas" e "tags"
# so aparecem como nome de categoria (p.4, p.57), nunca como cabecalho escrito.
_CABECALHOS_DOCUMENTADOS = {"limpar parametros", "carteira livre", "segmentacao", "carteira",
                            "parametros", "time", "alerta"}

_INICIOS = (
    ("vendedores", r"vendedores\b"),
    ("clientes", r"clientes\b"),
    ("quando", r"quando\b"),
    ("frequencia", r"frequencia\b(?! historica)"),
    ("preferencia", r"preferencia\b"),
    ("nao_agendar", r"nao agendar\b"),
    ("restrito", r"restrito\b"),
    ("roteirizavel", r"roteirizavel\b"),
    ("fixo", r"fixo\b"),
    ("sem_choque", r"sem choque\b"),
    ("onde", r"onde\b"),
    ("informe", r"informe\b"),
    ("descreva", r"descreva\b"),
    ("entregue", r"entregue\b"),
    ("canais", r"pelos canais\b"),
    ("fonte", r"(?:da|do|na|no|dos|das) [a-z]+\("),
)

_ATENDIMENTO = {"frequencia", "preferencia", "nao_agendar", "restrito", "roteirizavel", "fixo"}

# Tipos de clausula que o manual mostra em cada categoria de bloco.
_PERMITIDAS = {
    "time": {"vendedores"},
    "segmentacao": {"clientes", "quando"},
    "carteira": {"clientes", "quando"},
    "parametros": {"fonte", "temporal", "quando", "sem_choque"} | _ATENDIMENTO,
    "limpar_parametros": {"fonte"},
    "alerta": {"fonte", "temporal", "quando", "onde", "informe", "descreva", "entregue", "canais"},
}

_ETAPAS_PARAMETROS = {"fonte": 1, "temporal": 2, "quando": 3, "sem_choque": 5}
_ETAPAS_PARAMETROS.update({t: 4 for t in _ATENDIMENTO})
_ETAPAS_ALERTA = {"fonte": 1, "temporal": 2, "quando": 3, "onde": 4, "informe": 5,
                  "descreva": 6, "entregue": 7, "canais": 8}
_OBRIGATORIAS_ALERTA = ("fonte", "temporal", "onde", "informe", "entregue", "canais")

_ORDEM_CATEGORIA = {"time": 0, "segmentacao": 1, "carteira": 2,
                    "parametros": 3, "limpar_parametros": 3, "alerta": 3, "tags": 3}
_TERMINAL = {"parametros": "parametros", "limpar_parametros": "parametros",
             "alerta": "alertas", "tags": "tags"}


@dataclass
class _Clausula:
    tipo: str
    linha: int
    partes_brutas: list[str]

    @property
    def bruto(self) -> str:
        return " ".join(p.strip() for p in self.partes_brutas)

    @property
    def norm(self) -> str:
        return _normalizar(self.bruto)


@dataclass
class _Bloco:
    palavra: str
    tipo: str
    nome: str
    linha: int
    clausulas: list[_Clausula] = field(default_factory=list)


def _inicio_temporal(norm_minusculo: str) -> bool:
    return any(sem_caixa.match(norm_minusculo) for _, sem_caixa, _ in _C_TEMPORAIS)


def _aberta(clausula: _Clausula) -> bool:
    bruto = clausula.bruto
    # Linha terminada em "e" ou "ou" continua na seguinte (exemplo da p.18).
    return (bruto.count('"') % 2 == 1 or bruto.count("(") > bruto.count(")")
            or re.search(r"\s(e|ou)$", bruto) is not None)


def _tipo_de_inicio(norm_minusculo: str, atual: str | None, tipo_bloco: str) -> str | None:
    for tipo, padrao in _INICIOS:
        # "dos supervisores(...)" em linha propria e continuacao de time (p.7), nao fonte.
        if tipo == "fonte" and tipo_bloco not in ("parametros", "limpar_parametros", "alerta"):
            continue
        if re.match(padrao, norm_minusculo):
            return tipo
    # Filtro temporal so abre clausula logo depois da fonte; em outro ponto,
    # "na segunda" e continuacao de preferencia.
    if atual in ("fonte", "temporal") and _inicio_temporal(norm_minusculo):
        return "temporal"
    return None


def _ler(texto: str, achados: list[Achado]) -> list[_Bloco]:
    significativas = []
    for numero, linha in enumerate(texto.replace("\r\n", "\n").replace("\r", "\n").split("\n"), 1):
        conteudo = _sem_comentario(linha).strip()
        if conteudo:
            significativas.append((numero, conteudo))

    if not significativas:
        achados.append(Achado("version_no_inicio", AUSENTE, None,
                              "texto sem nenhuma linha significativa; falta 'version 1.0'"))
        return []

    primeiro_num, primeiro = significativas[0]
    if _normalizar(primeiro) != "version 1.0":
        achados.append(Achado("version_no_inicio", AUSENTE, primeiro_num,
                              f"primeira linha significativa e '{primeiro}', esperado 'version 1.0'"))

    blocos: list[_Bloco] = []
    for indice, (numero, conteudo) in enumerate(significativas):
        norm = _normalizar(conteudo)
        minusculo = norm.lower()

        if re.match(r"version\b", minusculo):
            if indice > 0:
                achados.append(Achado("version_unica", DIVERGENCIA, numero,
                                      f"declaracao '{conteudo}' repetida fora do inicio"))
            continue

        cabecalho = _cabecalho(norm, conteudo, numero, achados)
        if cabecalho:
            blocos.append(cabecalho)
            continue

        if not blocos:
            achados.append(Achado("ordem_das_categorias", DIVERGENCIA, numero,
                                  f"linha fora de qualquer bloco: '{conteudo}'"))
            continue

        bloco = blocos[-1]
        ultima = bloco.clausulas[-1] if bloco.clausulas else None
        # Texto de string ou argumento em varias linhas (ex.: descreva com o texto, p.48)
        # continua a clausula aberta, mesmo que a linha comece com palavra-chave.
        if ultima and _aberta(ultima):
            ultima.partes_brutas.append(conteudo)
            continue
        tipo = _tipo_de_inicio(minusculo, ultima.tipo if ultima else None, bloco.tipo)
        if tipo:
            bloco.clausulas.append(_Clausula(tipo, numero, [conteudo]))
        elif bloco.clausulas:
            bloco.clausulas[-1].partes_brutas.append(conteudo)
        else:
            bloco.clausulas.append(_Clausula("desconhecida", numero, [conteudo]))
    return blocos


def _cabecalho(norm: str, bruto: str, numero: int, achados: list[Achado]) -> _Bloco | None:
    minusculo = norm.lower()
    for palavra, tipo in _CABECALHOS:
        if re.match(re.escape(palavra) + r' ?"', minusculo):
            break
    else:
        # Cabecalho com palavra-chave que o manual nao lista.
        m = re.match(r'([a-z]+(?: [a-z]+)?) "[^"]*" ?:$', minusculo)
        if not m:
            return None
        achados.append(Achado("vocabulario_do_manual", NAO_DOCUMENTADA, numero,
                              f"palavra de bloco nao documentada: '{m.group(1)}'",
                              construcao=f"cabecalho: {m.group(1)}", trecho=bruto))
        return _Bloco(m.group(1), "desconhecido", _nome_bruto(bruto), numero)

    if not re.fullmatch(re.escape(palavra) + r' "[^"]*" ?:', minusculo):
        achados.append(Achado("cabecalho_bem_formado", DIVERGENCIA, numero,
                              "cabecalho fora da forma palavra \"nome\": (aspas internas, "
                              "dois-pontos ausente ou texto sobrando)"))
    if not norm.startswith(palavra):
        achados.append(Achado("grafia_documentada", DIVERGENCIA, numero,
                              f"palavra de bloco '{norm[:len(palavra)]}' difere do manual '{palavra}'"))
    if palavra not in _CABECALHOS_DOCUMENTADOS:
        achados.append(Achado("vocabulario_do_manual", NAO_DOCUMENTADA, numero,
                              f"palavra de bloco '{palavra}' sem exemplo no manual",
                              construcao=f"cabecalho: {palavra}", trecho=bruto))
    return _Bloco(palavra, tipo, _nome_bruto(bruto), numero)


def _nome_bruto(bruto: str) -> str:
    inicio, fim = bruto.find('"'), bruto.rfind('"')
    return bruto[inicio + 1:fim] if 0 <= inicio < fim else ""


# =============================================================================
# Conferencia
# =============================================================================

def _balanco(clausula: _Clausula, achados: list[Achado]) -> bool:
    bruto = clausula.bruto
    ok = True
    controle = re.search(r"[\x00-\x08\x0b-\x1f\x7f]", bruto)
    if controle:
        # Caractere invisivel faria a construcao parecer nao documentada; e defeito do texto.
        achados.append(Achado("caractere_fora_do_lexico", DIVERGENCIA, clausula.linha,
                              f"caractere de controle {controle.group()!r} na clausula",
                              trecho=bruto))
        ok = False
    if bruto.count('"') % 2:
        achados.append(Achado("aspas_balanceadas", DIVERGENCIA, clausula.linha,
                              "numero impar de aspas duplas na clausula", trecho=bruto))
        ok = False
    profundidade, fora_de_string = 0, True
    for c in bruto:
        if c == '"':
            fora_de_string = not fora_de_string
        elif fora_de_string and c == "(":
            profundidade += 1
        elif fora_de_string and c == ")":
            profundidade -= 1
            if profundidade < 0:
                break
    if profundidade != 0:
        achados.append(Achado("parenteses_balanceados", DIVERGENCIA, clausula.linha,
                              "parentese aberto sem fechar (ou fechado sem abrir) na clausula",
                              trecho=bruto))
        ok = False
    return ok


def _registrar(resultado: str | None, rotulo: str, fragmento: str, clausula: _Clausula,
               achados: list[Achado]) -> None:
    if resultado == "caixa":
        achados.append(Achado("grafia_documentada", DIVERGENCIA, clausula.linha,
                              f"{rotulo} '{fragmento}' so casa com o manual ignorando maiuscula/minuscula",
                              trecho=clausula.bruto))
    elif resultado is None:
        forma = _forma(fragmento) if fragmento else "(vazia)"
        achados.append(Achado("vocabulario_do_manual", NAO_DOCUMENTADA, clausula.linha,
                              f"{rotulo} sem correspondente no manual: '{fragmento}'",
                              construcao=f"{rotulo}: {forma}", trecho=clausula.bruto))


def _corpo(norm: str, palavra: str) -> str:
    return re.sub(r"^" + palavra + r"\b\s*", "", norm, flags=re.IGNORECASE)


def _conferir_vocabulario(bloco: _Bloco, clausula: _Clausula, achados: list[Achado]) -> list[int]:
    """Confere a clausula contra o vocabulario; devolve familias temporais encontradas."""
    norm = clausula.norm
    tipo = clausula.tipo
    familias: list[int] = []

    if tipo == "desconhecida":
        _registrar(None, "clausula", norm, clausula, achados)
    elif tipo in ("vendedores", "clientes", "fonte", "frequencia"):
        tabela = {"vendedores": _C_VENDEDORES, "clientes": _C_CLIENTES,
                  "fonte": _C_FONTES, "frequencia": _C_FREQUENCIA}[tipo]
        _registrar(_classificar(norm, tabela), tipo, norm, clausula, achados)
    elif tipo in ("nao_agendar", "roteirizavel", "fixo", "restrito", "sem_choque"):
        _registrar(_classificar(norm, _C_SIMPLES), tipo.replace("_", " "), norm, clausula, achados)
    elif tipo in ("quando", "onde"):
        tabela = _C_FILTROS if tipo == "quando" else _C_GATILHOS
        rotulo = "filtro" if tipo == "quando" else "gatilho"
        corpo = _corpo(norm, tipo)
        if not corpo:
            _registrar(None, rotulo, "", clausula, achados)
        for fragmento in _segmentar(corpo, tabela):
            _registrar(_classificar(fragmento, tabela), rotulo, fragmento, clausula, achados)
    elif tipo == "preferencia":
        corpo = _corpo(norm, "preferencia")
        if not corpo:
            _registrar(None, "preferencia", "", clausula, achados)
        for fragmento in _segmentar(corpo, _C_PREFERENCIA):
            _registrar(_classificar(fragmento, _C_PREFERENCIA), "preferencia", fragmento,
                       clausula, achados)
    elif tipo == "temporal":
        for fragmento in _segmentar(norm, _C_TEMPORAIS):
            achou = None
            for exato, sem_caixa, familia in _C_TEMPORAIS:
                if exato.fullmatch(fragmento):
                    achou = ("ok", familia)
                    break
            if not achou:
                for exato, sem_caixa, familia in _C_TEMPORAIS:
                    if sem_caixa.fullmatch(fragmento):
                        achou = ("caixa", familia)
                        break
            _registrar(achou[0] if achou else None, "temporal", fragmento, clausula, achados)
            if achou:
                familias.append(achou[1])
    # informe, descreva, entregue e canais: so presenca e ordem (ver readme, lacunas).
    return familias


def _nomes_referenciados(clausula: _Clausula) -> list[str]:
    bruto = clausula.bruto
    if clausula.tipo in ("clientes", "fonte", "sem_choque"):
        return re.findall(r'"([^"]*)"', bruto)
    if clausula.tipo == "quando":
        nomes = []
        for m in re.finditer(r"contido na segmenta[cç][aã]o\s*\(([^)]*)\)", bruto, re.IGNORECASE):
            nomes += re.findall(r'"([^"]*)"', m.group(1))
        return nomes
    return []


def _conferir_bloco(bloco: _Bloco, definidos: set[str], achados: list[Achado]) -> None:
    tipos = [c.tipo for c in bloco.clausulas]
    permitidas = _PERMITIDAS.get(bloco.tipo)
    familias_bloco: list[tuple[int, int]] = []
    formas_horario = set()

    for clausula in bloco.clausulas:
        balanceada = _balanco(clausula, achados)
        if permitidas is not None and clausula.tipo not in permitidas and clausula.tipo != "desconhecida":
            _registrar(None, f"clausula em {bloco.tipo}", clausula.norm, clausula, achados)
        elif balanceada:
            for familia in _conferir_vocabulario(bloco, clausula, achados):
                familias_bloco.append((familia, clausula.linha))
        if clausula.tipo == "temporal":
            minusculo = clausula.norm.lower()
            if re.search(r"(?:^| )as '", minusculo):
                formas_horario.add("às")
            if "de hora em hora" in minusculo:
                formas_horario.add("de hora em hora")

        for nome in dict.fromkeys(_nomes_referenciados(clausula)):
            if nome not in definidos:
                achados.append(Achado("referencia_a_nome_definido", AUSENTE, clausula.linha,
                                      f"nome \"{nome}\" referenciado e nao definido no arquivo",
                                      trecho=clausula.bruto))

    # Filtros temporais: ordem das familias e horario restrito a alertas.
    maior = 0
    for familia, linha in familias_bloco:
        if familia < maior:
            achados.append(Achado("filtros_temporais_em_ordem", DIVERGENCIA, linha,
                                  "filtro temporal fora da ordem dia do mes > dia da semana > "
                                  "semana > mes > horario"))
        maior = max(maior, familia)
        if familia == 5 and bloco.tipo != "alerta":
            achados.append(Achado("horario_somente_em_alertas", DIVERGENCIA, linha,
                                  f"filtro de horario em bloco '{bloco.palavra}'"))
    if len(formas_horario) > 1:
        achados.append(Achado("uma_regra_de_horario", DIVERGENCIA, bloco.linha,
                              "bloco usa 'às' e 'de hora em hora' ao mesmo tempo"))

    if bloco.tipo == "time" and "vendedores" not in tipos:
        achados.append(Achado("time_tem_vendedores", AUSENTE, bloco.linha,
                              f"time \"{bloco.nome}\" sem linha 'vendedores'"))

    if bloco.tipo in ("carteira", "segmentacao") and "clientes" not in tipos:
        achados.append(Achado("carteira_segmentacao_tem_clientes", AUSENTE, bloco.linha,
                              f"{bloco.palavra} \"{bloco.nome}\" sem linha 'clientes'"))

    if bloco.tipo == "carteira":
        fontes_segmentacao = 0
        for c in bloco.clausulas:
            if c.tipo != "clientes":
                continue
            minusculo = c.norm.lower()
            for m in re.finditer(r"segmentados\(([^)]*)\)", minusculo):
                fontes_segmentacao += max(1, m.group(1).count('"') // 2)
            fontes_segmentacao += len(re.findall(r"ruptura da segmentacao\(", minusculo))
        if fontes_segmentacao > 1:
            achados.append(Achado("carteira_uma_segmentacao", DIVERGENCIA, bloco.linha,
                                  f"carteira \"{bloco.nome}\" usa {fontes_segmentacao} segmentacoes"))

    if bloco.tipo in ("parametros", "limpar_parametros"):
        if "fonte" not in tipos:
            achados.append(Achado("parametros_tem_fonte", AUSENTE, bloco.linha,
                                  f"bloco \"{bloco.nome}\" sem fonte (da carteira / do time / na carteira)"))
        if bloco.tipo == "parametros" and not _ATENDIMENTO.intersection(tipos):
            achados.append(Achado("parametros_tem_atendimento", AUSENTE, bloco.linha,
                                  f"bloco \"{bloco.nome}\" sem parametro de atendimento "
                                  "(frequencia, preferencia, nao agendar, restrito, roteirizavel, fixo)"))
        if "nao_agendar" in tipos and {"frequencia", "preferencia"}.intersection(tipos):
            achados.append(Achado("nao_agendar_exclusivo", DIVERGENCIA, bloco.linha,
                                  f"bloco \"{bloco.nome}\" combina 'nao agendar' com frequencia ou preferencia"))
        _conferir_ordem(bloco, _ETAPAS_PARAMETROS, "parametros_ordem_das_etapas", achados)

    if bloco.tipo == "alerta":
        faltando = [t for t in _OBRIGATORIAS_ALERTA if t not in tipos]
        if faltando:
            achados.append(Achado("alerta_tem_etapas_obrigatorias", AUSENTE, bloco.linha,
                                  f"alerta \"{bloco.nome}\" sem: {', '.join(faltando)}"))
        _conferir_ordem(bloco, _ETAPAS_ALERTA, "alerta_ordem_das_etapas", achados)


def _conferir_ordem(bloco: _Bloco, etapas: dict[str, int], item: str, achados: list[Achado]) -> None:
    maior = 0
    for c in bloco.clausulas:
        etapa = etapas.get(c.tipo)
        if etapa is None:
            continue
        if etapa < maior:
            achados.append(Achado(item, DIVERGENCIA, c.linha,
                                  f"etapa '{c.tipo}' depois de etapa posterior no bloco \"{bloco.nome}\""))
        maior = max(maior, etapa)


def _conferir_arquivo(blocos: list[_Bloco], achados: list[Achado]) -> None:
    tipos = [b.tipo for b in blocos]
    if "time" not in tipos:
        achados.append(Achado("ao_menos_um_time", AUSENTE, None, "nenhum bloco 'time' no arquivo"))
    if not {"carteira", "parametros", "limpar_parametros", "alerta", "tags"}.intersection(tipos):
        achados.append(Achado("categoria_final_presente", AUSENTE, None,
                              "nenhuma carteira, parametros, alerta ou tag depois dos times"))

    maior = 0
    for b in blocos:
        ordem = _ORDEM_CATEGORIA.get(b.tipo)
        if ordem is None:
            continue
        if ordem < maior:
            achados.append(Achado("ordem_das_categorias", DIVERGENCIA, b.linha,
                                  f"bloco '{b.palavra}' depois de categoria posterior"))
        maior = max(maior, ordem)

    terminais = sorted({_TERMINAL[t] for t in tipos if t in _TERMINAL})
    if len(terminais) > 1:
        achados.append(Achado("categorias_terminais_exclusivas", DIVERGENCIA, None,
                              f"arquivo mistura {', '.join(terminais)}"))

    grupos = (
        ("nomes_de_time_distintos", {"time"}),
        ("nomes_carteira_segmentacao_distintos", {"carteira", "segmentacao"}),
        ("nomes_parametros_distintos", {"parametros", "limpar_parametros"}),
        ("nomes_alertas_distintos", {"alerta"}),
    )
    for item, grupo in grupos:
        vistos: set[str] = set()
        for b in blocos:
            if b.tipo not in grupo:
                continue
            if b.nome in vistos:
                achados.append(Achado(item, DIVERGENCIA, b.linha, f"nome \"{b.nome}\" repetido"))
            vistos.add(b.nome)


def conferir(texto: str) -> Laudo:
    """Confere o texto de um arquivo .gobr e devolve o laudo com todos os achados."""
    achados: list[Achado] = []
    blocos = _ler(texto, achados)
    definidos = {b.nome for b in blocos}
    for bloco in blocos:
        _conferir_bloco(bloco, definidos, achados)
    _conferir_arquivo(blocos, achados)
    achados.sort(key=lambda a: (a.linha if a.linha is not None else 0, a.item))
    return Laudo(achados)
