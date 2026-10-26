"""Leitura de normalizado.md no formato 3.1 para uma estrutura em memória."""
import re
from pathlib import Path

import yaml


class ErroConversao(Exception):
    """Erro explícito de leitura/conversão; sempre carrega o id e o motivo."""

    def __init__(self, id_regra: str, motivo: str):
        super().__init__(f"{id_regra}: {motivo}")
        self.id_regra = id_regra
        self.motivo = motivo


def dividir_secoes(texto: str) -> tuple[str, dict[str, str]]:
    """Separa o front matter das seções '## ...'.

    Rastreia cercas ``` para que um '## ' dentro de bloco de código nunca seja
    confundido com título de seção.
    """
    m = re.match(r"---\n(.*?)\n---\n", texto, re.S)
    if not m:
        raise ValueError("front matter ausente")
    corpo = texto[m.end():]
    secoes: dict[str, list[str]] = {}
    atual = None
    em_cerca = False
    for linha in corpo.splitlines():
        if linha.startswith("```"):
            em_cerca = not em_cerca
        if not em_cerca and linha.startswith("## "):
            atual = linha[3:].strip()
            if atual in secoes:
                raise ValueError(f"seção duplicada: {atual}")
            secoes[atual] = []
        elif atual is not None:
            secoes[atual].append(linha)
    return m.group(1), {k: "\n".join(v).strip("\n") for k, v in secoes.items()}


def extrair_yaml(corpo_secao: str, id_regra: str, secao: str) -> dict:
    """Abre o único bloco ```yaml da seção."""
    blocos = re.findall(r"```yaml\n(.*?)```", corpo_secao, re.S)
    if len(blocos) != 1:
        raise ErroConversao(id_regra, f"seção '{secao}' deveria ter 1 bloco yaml, tem {len(blocos)}")
    try:
        dado = yaml.safe_load(blocos[0])
    except yaml.YAMLError as e:
        raise ErroConversao(id_regra, f"YAML inválido em '{secao}': {e}") from e
    if not isinstance(dado, dict):
        raise ErroConversao(id_regra, f"YAML de '{secao}' não é um mapa")
    return dado


def ler_tabela(corpo_secao: str, id_regra: str) -> list[list[str]]:
    """Lê a tabela markdown do Dicionário como lista de linhas de 3 células."""
    linhas = [l for l in corpo_secao.splitlines() if l.strip().startswith("|")]
    if len(linhas) < 2:
        raise ErroConversao(id_regra, "tabela do Dicionário sem cabeçalho")
    resultado = []
    for l in linhas[2:]:  # pula cabeçalho e separador
        celulas = [c.strip() for c in l.strip().strip("|").split("|")]
        if len(celulas) != 3:
            raise ErroConversao(id_regra, f"linha do Dicionário com {len(celulas)} células: {l!r}")
        resultado.append(celulas)
    return resultado


def ler_v31(caminho: Path) -> dict:
    """Devolve {cabecalho, publico_alvo, regras, dicionario, termos_fora_vocabulario,
    lacunas, ambiguidades}. Não interpreta nem corrige conteúdo."""
    id_regra = caminho.parent.name
    try:
        texto = caminho.read_text(encoding="utf-8")
        bruto_cab, secoes = dividir_secoes(texto)
        cab = yaml.safe_load(bruto_cab)
    except (OSError, ValueError, yaml.YAMLError) as e:
        raise ErroConversao(id_regra, f"não foi possível abrir: {e}") from e

    if str(cab.get("versao_padrao")) != "3.1":
        raise ErroConversao(id_regra, f"versao_padrao é {cab.get('versao_padrao')!r}, esperado 3.1")
    if cab.get("id") != id_regra:
        raise ErroConversao(id_regra, f"id do cabeçalho ({cab.get('id')!r}) difere da pasta")

    for obrigatoria in ("Representação estruturada", "Dicionário", "Metadados", "Lacunas", "Ambiguidades"):
        if obrigatoria not in secoes:
            raise ErroConversao(id_regra, f"seção ausente: {obrigatoria}")

    estrutura = extrair_yaml(secoes["Representação estruturada"], id_regra, "Representação estruturada")
    meta = extrair_yaml(secoes["Metadados"], id_regra, "Metadados")
    for campo in ("publico_alvo", "regras"):
        if campo not in estrutura:
            raise ErroConversao(id_regra, f"campo ausente na estrutura: {campo}")
    if "termos_fora_vocabulario" not in meta:
        raise ErroConversao(id_regra, "Metadados sem termos_fora_vocabulario")
    if len(estrutura["regras"]) != cab["total_regras"]:
        raise ErroConversao(
            id_regra, f"total_regras={cab['total_regras']} mas há {len(estrutura['regras'])} regras"
        )

    return {
        "cabecalho": cab,
        "publico_alvo": estrutura["publico_alvo"],
        "regras": estrutura["regras"],
        "dicionario": ler_tabela(secoes["Dicionário"], id_regra),
        "termos_fora_vocabulario": meta["termos_fora_vocabulario"],
        "lacunas": secoes["Lacunas"].strip(),
        "ambiguidades": secoes["Ambiguidades"].strip(),
    }
