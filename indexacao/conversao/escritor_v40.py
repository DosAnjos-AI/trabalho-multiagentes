"""Escrita do formato 4.0 a partir da estrutura devolvida por leitor_v31."""
import copy

import yaml

import config
from conversao.leitor_v31 import ErroConversao


class _Fluxo(dict):
    """Mapa emitido em estilo flow ({a: 1, b: 2}), uma linha por critério."""


class _Dumper(yaml.SafeDumper):
    # ignore_aliases: o mesmo objeto Python em dois lugares geraria âncora/alias
    # (&id001), e a validação exige YAML sem âncoras.
    def ignore_aliases(self, data):
        return True

    # Sem isto as listas ficam coladas à chave pai ('regras:\n- nome'); com
    # indentação o arquivo fica legível para quem abre à mão.
    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)


_Dumper.add_representer(
    _Fluxo, lambda d, dado: d.represent_mapping("tag:yaml.org,2002:map", dado, flow_style=True)
)


def _chave_criterio(c: dict) -> tuple:
    """Igualdade exata dos campos, sem interpretação; 'descricao' fica fora porque
    é o campo que o 4.0 descarta e pode variar entre regras sem mudar o critério."""
    return (c["tipo"], c["operador"], repr(c["valor"]), c["unidade"], c["alcance"])


def _criterio_v40(c: dict) -> _Fluxo:
    saida = _Fluxo(tipo=c["tipo"], op=c["operador"], valor=copy.deepcopy(c["valor"]))
    if c["unidade"] != config.UNIDADE_PADRAO:
        saida["unidade"] = c["unidade"]
    if c["alcance"] != config.ALCANCE_PADRAO:
        saida["alcance"] = c["alcance"]
    return saida


def _entao(acao: dict, id_regra: str) -> _Fluxo:
    freq_tipo = acao["frequencia_tipo"]
    if freq_tipo == "fixa":
        if acao["frequencia_valor"] is None or acao["frequencia_unidade"] in (None, "none"):
            raise ErroConversao(id_regra, f"frequência fixa sem valor/unidade: {acao}")
        frequencia = f"fixa {acao['frequencia_valor']} {acao['frequencia_unidade']}"
    else:
        # Se houvesse valor/unidade aqui, o colapso em 'entao' o perderia em silêncio.
        if acao["frequencia_valor"] is not None or acao["frequencia_unidade"] != "none":
            raise ErroConversao(id_regra, f"frequência '{freq_tipo}' com valor/unidade: {acao}")
        frequencia = freq_tipo
    return _Fluxo(acao=acao["tipo"], frequencia=frequencia)


def montar_estrutura_v40(dados: dict) -> dict:
    """Aplica as regras de enxugamento e devolve o mapa do bloco '## Estrutura'."""
    id_regra = dados["cabecalho"]["id"]
    regras = dados["regras"]

    # Com uma única regra todo critério seria "comum a todas" e a regra ficaria
    # com 'se' vazio; içar nesse caso só esconde a regra, então não se iça.
    comuns: list[dict] = []
    if len(regras) > 1:
        chaves_por_regra = [{_chave_criterio(c) for c in r["criterios"]} for r in regras]
        em_todas = set.intersection(*chaves_por_regra)
        vistos = set()
        for c in regras[0]["criterios"]:
            k = _chave_criterio(c)
            if k in em_todas and k not in vistos:
                comuns.append(c)
                vistos.add(k)
    chaves_comuns = {_chave_criterio(c) for c in comuns}

    regras_v40 = []
    for r in regras:
        item = {"nome": r["nome"]}
        if r["publico"] != dados["publico_alvo"]:
            item["publico"] = r["publico"]
        item["se"] = [_criterio_v40(c) for c in r["criterios"] if _chave_criterio(c) not in chaves_comuns]
        item["entao"] = _entao(r["acao"], id_regra)
        regras_v40.append(item)

    return {
        "publico": dados["publico_alvo"],
        "comuns": [_criterio_v40(c) for c in comuns],
        "regras": regras_v40,
        "termos_fora_vocabulario": copy.deepcopy(dados["termos_fora_vocabulario"]),
    }


def _yaml(mapa: dict) -> str:
    return yaml.dump(
        mapa, Dumper=_Dumper, allow_unicode=True, sort_keys=False, width=10**6, default_flow_style=False
    )


def escrever_v40(dados: dict) -> str:
    """Devolve o texto completo do arquivo 4.0."""
    cab = dados["cabecalho"]
    id_regra = cab["id"]
    linhas_regras = []
    for r in dados["regras"]:
        desc = r["descricao"]
        if not isinstance(desc, str) or not desc.strip() or "\n" in desc.strip():
            raise ErroConversao(id_regra, f"descricao inválida na regra {r['nome']!r}")
        linhas_regras.append(desc.strip())

    cabecalho = {
        "id": id_regra,
        "origem": cab["origem"],
        "gobr": cab["gobr"],
        "tipo_input": cab["tipo_input"],
        "versao_padrao": config.VERSAO_DESTINO,
        "total_regras": cab["total_regras"],
        "procedencia": cab["procedencia"],
    }
    # versao_padrao como string explícita para o YAML manter "4.0" e não o float 4.0
    cab_txt = _yaml(cabecalho).replace("versao_padrao: '4.0'", "versao_padrao: 4.0")

    tabela = ["| Termo original | Categoria | Substituto genérico |", "|---|---|---|"]
    tabela += [f"| {a} | {b} | {c} |" for a, b, c in dados["dicionario"]]

    partes = [
        f"---\n{cab_txt}---\n",
        "## Regras\n\n" + "\n".join(linhas_regras) + "\n",
        "## Estrutura\n\n```yaml\n" + _yaml(montar_estrutura_v40(dados)) + "```\n",
        "## Dicionário\n\n" + "\n".join(tabela) + "\n",
        "## Lacunas\n\n" + dados["lacunas"] + "\n",
        "## Ambiguidades\n\n" + dados["ambiguidades"] + "\n",
    ]
    return "\n".join(partes)
