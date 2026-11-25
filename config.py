"""Configuracao do projeto. Uma secao por no do agente que usa configuracao (30, 50, 60, 80 e 90).

O fluxo do grafo nao fica aqui: e declarado em orquestracao.py.

Nao ha credencial aqui: a chave da OpenAI vem do ambiente (variavel nomeada em VARIAVEL_CHAVE), que o fim deste
arquivo preenche a partir do arquivo ARQ_ENV.
A validacao roda na importacao: parametro ausente ou fora da lista aceita impede o modulo de carregar,
antes de qualquer leitura no BigQuery ou chamada paga.
"""

import os
from pathlib import Path

# ============================================================================
# PROJETO (endereco dos dados; sem valor padrao no codigo do no)
# ============================================================================
PROJETO_GCP = "multiagentes-514823"
DATASET = "govendas_gobr"
TABELA_PROMPTS = "prompts"
TABELA_MANUAL = "manual"

# ============================================================================
# NO 50 - NORMALIZACAO
# ============================================================================
# Lista fechada de modelos aceitos, so OpenAI (o no so implementa chat.completions da OpenAI).
# Precos em dolares por 1 milhao de tokens, conferidos em 2026-11-13 nas paginas oficiais de preco.
# Envelhece: reconferir antes de uso em escala. "temperatura_aceita": faixa que a API aceita; os modelos
# da geracao 6 recusam qualquer valor diferente de 1 (erro da API: "Only the default (1) value is supported").
MODELOS = {
    "gpt-6-luna": {"entrada_por_milhao": 0.10, "saida_por_milhao": 0.50,
                   "temperatura_aceita": (1.0, 1.0)},
    "gpt-6.1-terra": {"entrada_por_milhao": 1.00, "saida_por_milhao": 5.00,
                      "temperatura_aceita": (1.0, 1.0)},
    "gpt-6.1-sol": {"entrada_por_milhao": 2.00, "saida_por_milhao": 10.00,
                    "temperatura_aceita": (1.0, 1.0)},
    "gpt-6-astra": {"entrada_por_milhao": 10.00, "saida_por_milhao": 50.00,
                    "temperatura_aceita": (1.0, 1.0)},
}
MODELO = "gpt-6.1-terra"
# O no nao envia o parametro (o modelo so aceita 1); o valor entra apenas nos metadados.
TEMPERATURA = 1.0

TIPOS_ENTRADA = ("texto", "imagem", "audio", "documento", "misto")
ORIGENS = ("sintetico", "usuario")

# Limite de tokens de saida por chamada; tambem entra na projecao de custo antes da chamada.
MAX_TOKENS_SAIDA = 16000
# Teto de gasto por turno, em dolares. O acumulado por sessao e do orquestrador.
# Valor desta rodada, definido pelo Mestre.
TETO_GASTO_USD = 0.10

SECOES_OBRIGATORIAS = ("## explicacao_normalizada", "## regras_extraidas")
PREFIXO_SEM_CHAVE = "sem_chave:"
CAMPO_REGRAS = "regras_extraidas"  # arquivos do manual, sem `#Titulo`, sem repeticao
CAMPO_SEM_CHAVE = "sem_chave"      # descricoes livres das regras sem arquivo no manual
# Campos de metadados na ordem do formato; escritos pelo no, nunca pelo modelo.
CAMPOS_METADADOS = (
    "origem", "tipo_entrada", "id_sessao_turno", "id_explicacao", "id_prompt", "hash_prompt",
    "id_auxiliar_manual", "hash_auxiliar_manual", "versao_normalizador", "hash_normalizador",
    "modelo", "temperatura", "tokens_entrada", "tokens_saida", "custo_usd", "tempo_segundos", "timestamp",
)

# Alem dos treze parametros do contexto medido, o no usa tres (declarados na entrega):
# - CARACTERES_POR_TOKEN_PESSIMISTA: projecao de custo antes da chamada (sem tokenizador local);
#   3.0 e pessimista para portugues acentuado com markdown.
# - VERSAO_NORMALIZADOR: campo versao_normalizador dos metadados.
# - VARIAVEL_CHAVE: nome da variavel de ambiente com a chave (o valor nunca fica aqui).
CARACTERES_POR_TOKEN_PESSIMISTA = 3.0
VERSAO_NORMALIZADOR = "v4"
VARIAVEL_CHAVE = "CHAVE_OPENAI"

# ============================================================================
# NO 30 - ENTRADA (converte a entrada em texto e confere os minimos)
# ============================================================================
# Mesmo modelo do no 50; limite de saida, teto por chamada e preco vem das chaves da secao do no 50.
MODELO_NO30 = MODELO
# Valor da coluna `tipo` da tabela de prompts; o no exige exatamente uma linha ativa deste tipo.
TIPO_PROMPT_NO30 = "entrada_minimos"
# Limite de caracteres da secao `## texto` devolvida pelo modelo. Texto acima disso (eco de prompt, resposta
# inflada por injecao) levanta erro. Valor desta rodada: cobre cerca de 6 paginas de PDF transcrito e fica bem abaixo
# do que MAX_TOKENS_SAIDA permitiria; ajustar se documentos reais passarem disso.
LIMITE_CARACTERES_TEXTO_NO30 = 20000
# Tipos que o no converte hoje. Fora desta lista, mas dentro de TIPOS_ENTRADA, o no levanta erro.
# Misto ficou de fora: o agente.py entrega um arquivo por turno, entao nao ha como compor dois tipos.
# Audio entra por servico de reconhecimento de fala (secao abaixo): o modelo do no recusa bloco de audio
# (prova de 2026-11-24), entao ele so recebe o texto ja transcrito.
TIPOS_ENTRADA_IMPLEMENTADOS = ("texto", "imagem", "documento", "audio")
# Extensao do arquivo -> (tipo de entrada, tipo MIME). So entra formato que a prova mostrou que o conversor aceita.
# Audio: so .wav, o unico formato provado e o unico cuja duracao o no confere com a biblioteca padrao.
EXTENSOES_ENTRADA = {
    ".png": ("imagem", "image/png"),
    ".pdf": ("documento", "application/pdf"),
    ".wav": ("audio", "audio/wav"),
}
# Limite de tamanho do arquivo, em bytes, por tipo. Valor desta rodada (decisao de custo e de seguranca do Mestre).
# Audio: 5 MB cobre 55 s de WAV mono em 44,1 kHz; o servico aceita mais (HIPOTESE, nao provado), mas nao e preciso.
LIMITE_BYTES_ENTRADA = {"imagem": 5_000_000, "documento": 10_000_000, "audio": 5_000_000}
# Tokens de entrada que a projecao de custo supoe para a midia lida pelo modelo (nao ha tokenizador local; imagem e
# pagina nao crescem com os bytes). Medido: 480 tokens (imagem) e 277 (PDF de uma pagina). Margem: cerca de 2x na
# imagem e 5x no documento, que pode ter varias paginas. Audio nao entra: o modelo recebe texto transcrito.
TOKENS_PROJECAO_MIDIA = {"imagem": 1000, "documento": 1500}

# --- Reconhecimento de fala (audio do no 30) ---
# Speech-to-Text v2, chamada direta (sincrona) com reconhecedor implicito `_`: nao cria recurso no projeto.
# {projeto} e {localizacao} saem de PROJETO_GCP e LOCALIZACAO_FALA.
ENDERECO_FALA = ("https://speech.googleapis.com/v2/projects/{projeto}/locations/{localizacao}"
                 "/recognizers/_:recognize")
# `global` e a localizacao onde o modelo `long` tem pt-BR (lista lida do servico em 2026-11-24).
LOCALIZACAO_FALA = "global"
MODELO_FALA = "long"
IDIOMA_FALA = "pt-BR"
# O servico recusa audio acima de 60 s no reconhecimento direto ("Audio can be of a maximum of 60 seconds.",
# provado em 2026-11-24). Acima disso so por lote, que exige bucket. 55 deixa margem.
LIMITE_SEGUNDOS_AUDIO = 55
# HIPOTESE: US$ por minuto de audio, faixa inicial dos modelos padrao (as paginas de preco consultadas divergem entre
# si; confirmar na fatura). A duracao faturada e real (vem na resposta); so o preco e hipotese.
PRECO_FALA_USD_POR_MINUTO = 0.016

# ============================================================================
# NO 60 - RECUPERACAO
# ============================================================================
TABELA_EXEMPLOS = "exemplos"
# Filtro da busca: so entra exemplo com este status de revisao (a origem nao filtra: exemplo de usuario aprovado entra).
STATUS_BUSCA = "aprovado"
# Quantos exemplos cada ramo traz. Independentes: a uniao tem ate N1_DENSO + N2_JACCARD (menos se os ramos coincidirem).
N1_DENSO = 2
N2_JACCARD = 2
# Lista fechada de modelos de embedding. O preco e HIPOTESE de referencia (US$ por 1M de tokens), nao conferido na
# pagina oficial; o custo real usa os tokens que a API devolve.
MODELOS_EMBEDDING = {
    "gemini-embedding-2": {"dimensoes": 3072, "usd_por_milhao": 0.20},
}
MODELO_EMBEDDING = "gemini-embedding-2"
DIMENSOES = 3072
LOCALIZACAO_EMBEDDING = "us"
# Endereco do servico de embedding; {projeto}, {localizacao} e {modelo} saem das chaves PROJETO_GCP,
# LOCALIZACAO_EMBEDDING e MODELO_EMBEDDING. Os nos 60 e 90 so preenchem o molde, nenhum escreve o endereco.
ENDERECO_EMBEDDING = ("https://aiplatform.googleapis.com/v1/projects/{projeto}/locations/{localizacao}"
                      "/publishers/google/models/{modelo}:embedContent")
# ATENCAO: o texto embutido e PREFIXO_EMBEDDING + descricao, sem corte de espaco, nos dois nos. O prefixo entra no
# calculo do `hash_texto_embedding` das linhas de `exemplos`: mudar este valor, MODELO_EMBEDDING ou DIMENSOES invalida
# todos os vetores ja gravados (busca e gravacao deixam de combinar, sem erro e sem aviso).
PREFIXO_EMBEDDING = "task: sentence similarity | query: "
# Teto de gasto do embedding por execucao, em dolares. Valor desta rodada, definido pelo Mestre.
TETO_GASTO_NO60_USD = 0.10

# ============================================================================
# NO 80 - GERACAO DO .gobr
# ============================================================================
# Lista fechada dos modelos que o no 80 aceita; precos e limites vem de MODELOS (secao do no 50).
# Padrao: gpt-6-luna (US$ 0,10 entrada e US$ 0,50 saida por 1M; preco relido em developers.openai.com/api/docs/pricing em 2026-11-16).
# O terra continua valido como alternativa. Todos os modelos da geracao 6 so aceitam a temperatura padrao.
MODELOS_NO80 = ("gpt-6-luna", "gpt-6.1-terra", "gpt-6.1-sol")
MODELO_NO80 = "gpt-6-luna"
# Valor da coluna `tipo` da tabela de prompts; o no exige exatamente uma linha ativa deste tipo.
TIPO_PROMPT_NO80 = "geracao_gobr"
# Adendo de reexecucao: linha ativa da tabela de prompts com este `tipo`, lida pelo mesmo mecanismo do prompt principal.
TIPO_ADENDO_NO80 = "adendo_reexecucao_gobr"
# Teto de gasto por execucao do no, em dolares. Valor desta rodada, definido pelo Mestre.
TETO_GASTO_NO80_USD = 0.50

# ============================================================================
# NO 90 - PERSISTENCIA DA REGRA APROVADA
# ============================================================================
# Tabela onde a regra aprovada e gravada: a mesma lida pela recuperacao. A linha entra com este status e so vira
# exemplo de recuperacao (STATUS_BUSCA) depois da revisao do Mestre.
TABELA_GRAVACAO = TABELA_EXEMPLOS
ORIGEM_GRAVACAO = "usuario"
STATUS_GRAVACAO = "pendente"
# Embedding da gravacao: mesmo modelo, dimensao e prefixo do no 60. Teto por execucao, valor desta rodada.
TETO_GASTO_NO90_USD = 0.10

# ============================================================================
# MIDDLEWARE (script20) - CONTADOR DE CUSTO E TETO DA SESSAO
# ============================================================================
# Teto acumulado da sessao (um processo do agente.py), em dolares: modelo de linguagem, embedding e reconhecimento de
# fala. BigQuery nao conta (a conta ja tem limite automatico). Conta: 5 x US$ 0,0147 (media medida por turno) x
# 8 turnos previstos = US$ 0,588, arredondado para cima: US$ 0,60. E rede de protecao contra laco descontrolado:
# ao atingir o teto, a proxima chamada de no e bloqueada.
TETO_SESSAO_USD = 0.60

# ============================================================================
# CONVERSA E INTERFACE (agente.py no terminal e app.py no navegador leem daqui)
# ============================================================================
# Texto fixo que a pessoa le. O no 30 so devolve tokens (`faltantes`); a frase de cada um e daqui.
PERGUNTAS_FALTANTES = {
    "quem_atende": "Quais vendedores ou equipes a regra cobre?",
    "desfecho": "O que o conjunto de regras faz: monta carteira, define atendimento, dispara alerta ou marca tag?",
    "conflito": "Atendimento e alerta são dois conjuntos de regras separados; qual vem agora?",
}
MENSAGEM_FORA_DE_ESCOPO = ("Eu escrevo regras de atendimento comercial na linguagem GOBR do goVendas. "
                           "Descreva a regra que você quer, por exemplo quem atende e o que deve acontecer.")
# {erro}: nome da excecao do servico (sem a mensagem dela, que pode trazer dados da conta).
MENSAGEM_SERVICO_RECUSOU = "Um serviço externo recusou a chamada ({erro}). Aguarde um instante e tente de novo."
PERGUNTA_MUDANCA = "O que você quer mudar na regra?"
# {itens} e a lista de itens que o manual nao cobriu; a ressalva sai na conversa, nunca dentro do .gobr.
MENSAGEM_RESSALVA = ("Ressalva: os itens abaixo não foram encontrados no manual e podem não estar cobertos "
                     "pela regra gerada acima:\n{itens}")
# {exemplo_id} e {status}: identificador da linha gravada e STATUS_GRAVACAO.
MENSAGEM_GRAVADA = "Regra gravada como {exemplo_id} (status {status}, aguarda revisão)."

# Interface no navegador (Streamlit).
NOME_AGENTE = "Agente de regras GOBR"
ARQ_LOGO = "logo.png"  # na raiz do projeto; desenho branco com fundo transparente, por isso vai sobre o verde
# Etapa que a pessoa ve enquanto cada no roda (uma chave por no de orquestracao.py).
ETAPAS_PROGRESSO = {
    "entrada": "Lendo a sua entrada",
    "normalizacao": "Organizando a descrição",
    "normalizacao_pedido": "Organizando a descrição com o seu pedido de mudança",
    "recuperacao": "Buscando exemplos",
    "geracao": "Escrevendo a regra",
    "geracao_reexecucao": "Reescrevendo a regra com a sua mudança",
    "persistencia": "Gravando a regra",
}
ETAPA_PRONTO = "Pronto"
BOTAO_APROVAR = "Aprovar a regra"
BOTAO_MUDANCA = "Pedir mudança"
CAMPO_ENTRADA = "Descreva a regra ou envie um arquivo (.png, .pdf, .wav)"
MENSAGEM_BOAS_VINDAS = ("Olá. Descreva a regra de atendimento que você quer, por texto ou por arquivo "
                        "(imagem .png, documento .pdf ou áudio .wav). Eu escrevo a regra na linguagem GOBR.")
# {extensao}, {aceitas}
MENSAGEM_EXTENSAO = "Extensão {extensao} não aceita. Aceitas: {aceitas}. Envie outro arquivo ou digite o texto."
# {tamanho}, {limite}: bytes
MENSAGEM_ARQUIVO_GRANDE = "Arquivo com {tamanho} bytes, acima do limite de {limite} bytes para este tipo. Envie um menor."
MENSAGEM_ARQUIVO_INVALIDO = "Não foi possível usar o arquivo: {erro}"
MENSAGEM_TEXTO_E_ARQUIVO = "Envie o texto ou o arquivo, um por vez."
MENSAGEM_ARQUIVO_NA_PERGUNTA = "Responda a pergunta acima em texto; o arquivo foi descartado."
MENSAGEM_ENTRADA_ENCERRADA = "Sessão encerrada: o teto de custo foi atingido."
# {tipo}, {texto}
MENSAGEM_TRANSCRICAO = "Texto transcrito de {tipo}:\n\n{texto}"
# Cores da marca, lidas da pagina do goVendas. HIPOTESE: estimativa a partir de captura de tela, nao do estilo do site.
PALETA = {"verde": "#00E08A", "amarelo": "#FFD200", "branco": "#FFFFFF", "escuro": "#15241C"}

# ============================================================================
# AMBIENTE
# ============================================================================
# Arquivo com as chaves de API (ignorado pelo git), na mesma pasta deste arquivo. Variaveis esperadas: VARIAVEL_CHAVE.
ARQ_ENV = ".env"

# ============================================================================
# VALIDACAO (roda na importacao)
# ============================================================================
_AUSENTE = object()


class ErroConfig(ValueError):
    """Configuracao invalida; diz o parametro, o valor recebido, os aceitos e onde configurar."""


def _valor(nome: str):
    valor = globals().get(nome, _AUSENTE)
    if valor is _AUSENTE:
        raise ErroConfig(f"{nome} recebido: ausente. Defina em config.py.")
    return valor


def _em(nome: str, aceitos) -> object:
    valor = _valor(nome)
    if valor not in aceitos:
        raise ErroConfig(f"{nome} recebido: {valor!r}. Aceitos: {list(aceitos)}. Configure em config.py.")
    return valor


def _texto(nome: str) -> str:
    valor = _valor(nome)
    if not isinstance(valor, str) or not valor.strip():
        raise ErroConfig(f"{nome} recebido: {valor!r}. Aceita texto nao vazio. Configure em config.py.")
    return valor


def _numero_positivo(nome: str, tipos=(int, float)) -> None:
    valor = _valor(nome)
    if isinstance(valor, bool) or not isinstance(valor, tipos) or valor <= 0:
        raise ErroConfig(f"{nome} recebido: {valor!r}. Aceita numero > 0. Configure em config.py.")


def _validar() -> None:
    for nome in ("PROJETO_GCP", "DATASET", "TABELA_PROMPTS", "TABELA_MANUAL", "VARIAVEL_CHAVE", "VERSAO_NORMALIZADOR",
                 "CAMPO_REGRAS", "CAMPO_SEM_CHAVE", "PREFIXO_SEM_CHAVE"):
        _texto(nome)
    modelos = _valor("MODELOS")
    modelo = _em("MODELO", modelos)
    info = modelos[modelo]
    for nome in ("entrada_por_milhao", "saida_por_milhao", "temperatura_aceita"):
        if nome not in info:
            raise ErroConfig(f"MODELOS[{modelo!r}] recebido sem o campo {nome!r}. Configure em config.py.")
    faixa = info["temperatura_aceita"]
    if not (faixa[0] <= _valor("TEMPERATURA") <= faixa[1]):
        raise ErroConfig(f"TEMPERATURA recebido: {TEMPERATURA!r}. Aceito para {modelo}: {faixa}. "
                         f"Configure em config.py.")
    if tuple(_valor("TIPOS_ENTRADA")) != ("texto", "imagem", "audio", "documento", "misto"):
        raise ErroConfig(f"TIPOS_ENTRADA recebido: {TIPOS_ENTRADA!r}. Aceito: lista fechada texto, imagem, audio, "
                         f"documento, misto. Configure em config.py.")
    if set(_valor("ORIGENS")) != {"sintetico", "usuario"}:
        raise ErroConfig(f"ORIGENS recebido: {ORIGENS!r}. Aceito: ('sintetico', 'usuario'). Configure em config.py.")
    _numero_positivo("MAX_TOKENS_SAIDA", (int,))
    _numero_positivo("TETO_GASTO_USD")
    _numero_positivo("CARACTERES_POR_TOKEN_PESSIMISTA")
    if tuple(_valor("SECOES_OBRIGATORIAS")) != ("## explicacao_normalizada", "## regras_extraidas"):
        raise ErroConfig(f"SECOES_OBRIGATORIAS recebido: {SECOES_OBRIGATORIAS!r}. Aceito: "
                         f"('## explicacao_normalizada', '## regras_extraidas'). Configure em config.py.")
    campos = _valor("CAMPOS_METADADOS")
    if len(campos) != 17 or len(set(campos)) != 17:
        raise ErroConfig(f"CAMPOS_METADADOS recebido: {campos!r}. Aceita 17 campos distintos. "
                         f"Configure em config.py.")


_validar()


def _validar_middleware() -> None:
    """Validacao do middleware; roda na importacao."""
    _numero_positivo("TETO_SESSAO_USD")


_validar_middleware()


def _validar_no60() -> None:
    """Validacao do no 60; roda na importacao, depois da validacao do no 50."""
    for nome in ("TABELA_EXEMPLOS", "STATUS_BUSCA", "LOCALIZACAO_EMBEDDING", "PREFIXO_EMBEDDING",
                 "ENDERECO_EMBEDDING"):
        _texto(nome)
    _em("STATUS_BUSCA", ("aprovado",))
    _numero_positivo("N1_DENSO", (int,))
    _numero_positivo("N2_JACCARD", (int,))
    _numero_positivo("TETO_GASTO_NO60_USD")
    modelos = _valor("MODELOS_EMBEDDING")
    modelo = _em("MODELO_EMBEDDING", modelos)
    info = modelos[modelo]
    for nome in ("dimensoes", "usd_por_milhao"):
        if nome not in info:
            raise ErroConfig(f"MODELOS_EMBEDDING[{modelo!r}] recebido sem o campo {nome!r}. Configure em config.py.")
    if _valor("DIMENSOES") != info["dimensoes"]:
        raise ErroConfig(f"DIMENSOES recebido: {DIMENSOES!r}. Aceito para {modelo}: {info['dimensoes']}. "
                         f"Configure em config.py.")


_validar_no60()


def _validar_no80() -> None:
    """Validacao do no 80; roda na importacao, depois da validacao do no 60."""
    _texto("TIPO_PROMPT_NO80")
    _texto("TIPO_ADENDO_NO80")
    _numero_positivo("TETO_GASTO_NO80_USD")
    aceitos = _valor("MODELOS_NO80")
    if not set(aceitos) <= set(_valor("MODELOS")):
        raise ErroConfig(f"MODELOS_NO80 recebido: {list(aceitos)!r}. Cada modelo precisa existir em MODELOS: "
                         f"{list(MODELOS)}. Configure em config.py.")
    _em("MODELO_NO80", aceitos)


_validar_no80()


def _validar_no30() -> None:
    """Validacao do no 30; roda na importacao, depois da validacao do no 80."""
    _texto("TIPO_PROMPT_NO30")
    _numero_positivo("LIMITE_CARACTERES_TEXTO_NO30", (int,))
    _em("MODELO_NO30", _valor("MODELOS"))
    implementados = _valor("TIPOS_ENTRADA_IMPLEMENTADOS")
    fora = [t for t in implementados if t not in TIPOS_ENTRADA]
    if "texto" not in implementados or fora:
        raise ErroConfig(f"TIPOS_ENTRADA_IMPLEMENTADOS recebido: {list(implementados)!r}. Aceitos: 'texto' mais "
                         f"subconjunto de {list(TIPOS_ENTRADA)}. Configure em config.py.")
    midia = [t for t in implementados if t != "texto"]
    extensoes = _valor("EXTENSOES_ENTRADA")
    for ext, par in extensoes.items():
        if not ext.startswith(".") or ext != ext.lower() or len(par) != 2 or par[0] not in midia:
            raise ErroConfig(f"EXTENSOES_ENTRADA recebido: {ext!r}: {par!r}. Aceita extensao minuscula com ponto "
                             f"-> (tipo em {midia}, MIME). Configure em config.py.")
    # Audio nao tem projecao de tokens: o modelo recebe o texto transcrito, que a projecao mede pelo tamanho.
    for nome, tipos in (("LIMITE_BYTES_ENTRADA", midia), ("TOKENS_PROJECAO_MIDIA", [t for t in midia if t != "audio"])):
        tabela = _valor(nome)
        if set(tabela) != set(tipos) or any(isinstance(v, bool) or not isinstance(v, int) or v <= 0
                                            for v in tabela.values()):
            raise ErroConfig(f"{nome} recebido: {tabela!r}. Aceita uma chave por tipo de midia {tipos}, "
                             f"com inteiro > 0. Configure em config.py.")
    if "audio" in implementados:
        for nome in ("ENDERECO_FALA", "LOCALIZACAO_FALA", "MODELO_FALA", "IDIOMA_FALA"):
            _texto(nome)
        _numero_positivo("LIMITE_SEGUNDOS_AUDIO")
        _numero_positivo("PRECO_FALA_USD_POR_MINUTO")
        if _valor("LIMITE_SEGUNDOS_AUDIO") >= 60:
            raise ErroConfig(f"LIMITE_SEGUNDOS_AUDIO recebido: {LIMITE_SEGUNDOS_AUDIO!r}. Aceito: abaixo de 60, o "
                             f"limite do reconhecimento direto. Configure em config.py.")


_validar_no30()


def _validar_no90() -> None:
    """Validacao do no 90; roda na importacao, depois da validacao do no 30."""
    _texto("TABELA_GRAVACAO")
    _em("ORIGEM_GRAVACAO", _valor("ORIGENS"))
    _em("STATUS_GRAVACAO", ("pendente",))  # gravar direto como aprovado pularia a revisao do Mestre
    _numero_positivo("TETO_GASTO_NO90_USD")


_validar_no90()


def _validar_interface() -> None:
    """Validacao do texto da conversa e da interface; roda na importacao, depois da validacao do no 90."""
    for nome in ("MENSAGEM_FORA_DE_ESCOPO", "MENSAGEM_SERVICO_RECUSOU", "PERGUNTA_MUDANCA", "MENSAGEM_RESSALVA", "MENSAGEM_GRAVADA", "NOME_AGENTE",
                 "ARQ_LOGO", "ETAPA_PRONTO", "BOTAO_APROVAR", "BOTAO_MUDANCA", "CAMPO_ENTRADA", "MENSAGEM_BOAS_VINDAS",
                 "MENSAGEM_EXTENSAO", "MENSAGEM_ARQUIVO_GRANDE", "MENSAGEM_ARQUIVO_INVALIDO", "MENSAGEM_TEXTO_E_ARQUIVO",
                 "MENSAGEM_ARQUIVO_NA_PERGUNTA", "MENSAGEM_ENTRADA_ENCERRADA", "MENSAGEM_TRANSCRICAO"):
        _texto(nome)
    for nome, chaves in (("PERGUNTAS_FALTANTES", ("quem_atende", "desfecho", "conflito")),
                         ("ETAPAS_PROGRESSO", ("entrada", "normalizacao", "normalizacao_pedido", "recuperacao",
                                               "geracao", "geracao_reexecucao", "persistencia")),
                         ("PALETA", ("verde", "amarelo", "branco", "escuro"))):
        tabela = _valor(nome)
        if set(tabela) != set(chaves) or any(not isinstance(v, str) or not v.strip() for v in tabela.values()):
            raise ErroConfig(f"{nome} recebido: {tabela!r}. Aceita uma chave por item de {list(chaves)}, com texto "
                             f"nao vazio. Configure em config.py.")


_validar_interface()


def _carregar_env() -> None:
    """Copia o arquivo ARQ_ENV (CHAVE=valor por linha) para o ambiente do processo, so com a biblioteca padrao.

    Roda na importacao, antes de qualquer chamada paga. Nao imprime valor: o erro cita so o nome da variavel.
    """
    caminho = Path(__file__).with_name(ARQ_ENV)
    if not caminho.is_file():
        raise ErroConfig(f"Arquivo {ARQ_ENV} inexistente em {caminho.parent}. Crie-o com a variavel {VARIAVEL_CHAVE}.")
    for linha in caminho.read_text(encoding="utf-8").splitlines():
        linha = linha.strip()
        if not linha or linha.startswith("#") or "=" not in linha:
            continue
        nome, valor = linha.removeprefix("export ").split("=", 1)
        os.environ.setdefault(nome.strip(), valor.strip().strip("\"'"))
    if not os.environ.get(VARIAVEL_CHAVE, "").strip():
        raise ErroConfig(f"Variavel {VARIAVEL_CHAVE} ausente ou vazia em {ARQ_ENV}. Defina-a em {caminho}.")


_carregar_env()
