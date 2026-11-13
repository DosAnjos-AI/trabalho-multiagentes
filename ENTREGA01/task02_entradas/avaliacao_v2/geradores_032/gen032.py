"""Gerador da regra_032 a partir de escolhas explicitas por modelo (decididas lendo a descricao)."""
from fmt import bloco, grava

SUL = '"PR", "SC", "RS", "SP", "RJ", "MG", "ES", "GO", "MT", "MS", "DF"'
NOR = '"AC", "AP", "AM", "PA", "RO", "RR", "TO", "AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"'
RAMOS = {
    "matcon": '"MATCON", "FERRAGISTA", "AGROPECUARIA", "HOME CENTER"',
    "epi": '"EPI", "LICITACAO"',
    "atacado": '"ATACADO"',
    "consfinal": '"CONS. FINAL"',
}
LIM = {"matcon": [25000, 10000, None], "epi": [25000, 10000, None],
       "atacado": [50000, 25000, None], "consfinal": [15000, 10000, None]}
# frequencias padrao: (ativo, pre, inativo) por grupo
FREQ = {"matcon": ([14, 21, 28], [14, 14, 14], [14, 14, 14]),
        "epi": ([14, 21, 28], [14, 14, 14], [14, 14, 14]),
        "atacado": ([10, 14, 21], [7, 10, 14], [10, 10, 21]),
        "consfinal": ([28, 28, 28], [14, 14, 14], [28, 28, 28])}
REG = (("sul", 120, 150, SUL), ("norte", 150, 180, NOR))


def gera(caminho, o):
    """o: dicionario de escolhas. Chaves usadas abaixo; ver cada script de modelo."""
    B = [bloco(f'time "{o.get("time_nome", "televendas")}"', [o.get("time", "vendedores todostelevendas ativados")])]
    cart = {}
    for reg, a, b, ufs in REG:
        nome = {"sul": "sul sudeste centro-oeste", "norte": "norte nordeste"}[reg]
        cart[reg] = nome
        if o.get("regiao_como", "carteira") != "nenhuma":
            B.append(bloco(f'{o.get("regiao_como", "carteira")} "{nome}"',
                           [f'clientes {o.get("fonte_regiao", "carteirafixa")}("televendas")'],
                           [f'uf do estado {o.get("op_uf", "igual")}({ufs})']))
    src = (lambda reg: f'da carteira("{cart[reg]}")') if o.get("regiao_como", "carteira").startswith("carteira") else \
          (lambda reg: f'da segmentacao("{cart[reg]}")')
    if o.get("regiao_como") == "nenhuma":
        src = lambda reg: 'do time("televendas")'
    for blk in o.get("pre", ["baixada", "prospect"]):
        if blk == "baixada":
            B.append(bloco('parametros "baixados na receita"', [o.get("src_baixada", 'do time("televendas")')],
                           ["status na receita federal definido como baixada"], ["nao agendar"]))
        elif blk == "prospect":
            if o.get("prospect_por", "carteira") == "carteira":
                for reg, *_ in REG:
                    B.append(bloco(f'parametros "prospects {cart[reg]}"', [src(reg)], [o["prospect"]],
                                   [f'frequencia de {o.get("freq_prospect", 14)} dias']))
            else:
                B.append(bloco('parametros "prospects"', ['do time("televendas")'], [o["prospect"]],
                               [f'frequencia de {o.get("freq_prospect", 14)} dias']))
    ramo = o.get("ramo", "ramo de atividade igual({})")
    for reg, a, b, ufs in REG:
        for g in o.get("grupos", ["matcon", "epi", "atacado", "consfinal"]):
            freqs = o.get("freq", {}).get((reg, g), FREQ[g])
            for t, dias in (("ativo", a), ("pre", b), ("inativo", None)):
                ti = ("ativo", "pre", "inativo").index(t)
                lims = list(enumerate(LIM[g]))
                if (g, t) in o.get("colapsa", set()):
                    lims = [(2, None)]  # um bloco so, sem faixa de faturamento
                for i, v in lims:
                    f = freqs[ti][i]
                    rec = o["rec"](reg, g, t, i, dias)  # filtro de recencia ou None
                    q = [ramo.format(RAMOS[g])] + ([rec] if rec else [])
                    if v:
                        q.append(f'{o.get("fat", "media faturada")} no ano com a empresa maior que R$ {v}')
                    dep = [f"frequencia de {f} dias"] if f else []
                    B.append(bloco(f'parametros "{cart[reg]} {g} {t} {v or "demais"}"', [src(reg)], q, dep))
    if o.get("fallback", True):
        B.append(bloco('parametros "restante"', ['do time("televendas")'], None, ["nao agendar"]))
    grava(caminho, B)
    return len(B)
