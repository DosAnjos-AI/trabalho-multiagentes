"""Interface de chat no navegador (Streamlit): a mesma conversa do agente.py, com progresso no a no.

Uso: .venv/bin/python -B -m streamlit run app.py (tema em .streamlit/config.toml)
A interface so consome o grafo que ja existe (orquestracao.py + construtor do script10) e o Medidor do script20; nao ha
logica de conversa nova aqui. Todo texto que a pessoa le vem do config.py, o mesmo que o terminal usa.
"""
import base64
import sys
import tempfile
import uuid
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
sys.path[:0] = [str(RAIZ), str(RAIZ / "src")]

import requests
import streamlit as st
from google.api_core.exceptions import GoogleAPIError
from openai import OpenAIError

import config
import orquestracao
from script10_orquestracao.script10_orquestracao import construir_contextos, construir_grafo
from script20_middleware.script20_middleware import ErroTeto, Medidor

# Recusa de servico externo (OpenAI, Google Cloud, rede): vira mensagem na conversa, nunca rastro de pilha.
ERROS_SERVICO = (OpenAIError, GoogleAPIError, requests.RequestException)


class MedidorComProgresso(Medidor):
    """Medidor que avisa quando cada no comeca. O sinal de inicio nao existe no Medidor (so a medicao de fim), e o
    middleware e o construtor sao so leitura aqui; por isso a subclasse embrulha por cima do embrulho original."""

    def __init__(self, teto_usd: float) -> None:
        super().__init__(teto_usd)
        self.ao_iniciar = lambda nome: None  # trocado a cada turno pela tela que esta desenhando o progresso

    def embrulhar(self, nome, funcao, zera_custo):
        medido = super().embrulhar(nome, funcao, zera_custo)

        def com_aviso(estado: dict) -> dict:
            # Teto atingido: o no nao roda, entao a etapa nao pode aparecer; o ErroTeto sai do `medido`.
            if self.acumulado < self.teto:
                self.ao_iniciar(nome)
            return medido(estado)
        return com_aviso


# ============================================================================
# ESTADO DA SESSAO DO NAVEGADOR
# ============================================================================

@st.cache_resource(show_spinner="Carregando prompts e exemplos do BigQuery...")
def contextos_compartilhados() -> dict:
    """Leitura unica no BigQuery para todas as sessoes do processo; o contexto de cada no e so leitura."""
    return construir_contextos(config, orquestracao)


def iniciar_sessao() -> None:
    S = st.session_state
    if "thread_id" in S:
        return
    S.thread_id = f"web-{uuid.uuid4().hex[:8]}"   # estavel ate a pagina ser recarregada
    S.medidor = MedidorComProgresso(config.TETO_SESSAO_USD)
    S.grafo = construir_grafo(config, orquestracao, S.medidor, contextos_compartilhados())
    S.mensagens = [{"tipo": "agente", "texto": config.MENSAGEM_BOAS_VINDAS}]
    S.gerou = False        # a primeira regra ja saiu: as entradas seguintes sao pedidos de mudanca
    S.pendente = ""        # texto de uma entrada incompleta; a resposta da pessoa e somada a ele
    S.aguardando = False   # regra na tela esperando aprovar ou pedir mudanca
    S.encerrada = False    # teto atingido
    S.custo_turno = 0.0


def dizer(tipo: str, texto: str) -> None:
    st.session_state.mensagens.append({"tipo": tipo, "texto": texto})


# ============================================================================
# TURNO COM PROGRESSO NO A NO
# ============================================================================

def invocar_com_progresso(entrada: dict) -> dict:
    """Roda o grafo mostrando, enquanto cada no roda, a etapa em curso. Devolve o estado final."""
    S = st.session_state
    etapas: list[str] = []

    with st.chat_message("assistant"):
        painel = st.status("Trabalhando", expanded=True)
        linhas = painel.empty()

        def desenhar() -> None:
            # Etapas concluidas em texto simples; a que esta rodando em negrito com reticencias.
            corpo = [f"- {t}" for t in etapas[:-1]] + [f"- **{etapas[-1]}...**"] if etapas else []
            linhas.markdown("\n".join(corpo))

        def ao_iniciar(nome: str) -> None:
            etapas.append(config.ETAPAS_PROGRESSO[nome])
            desenhar()

        S.medidor.ao_iniciar = ao_iniciar
        try:
            estado = S.grafo.invoke(entrada, {"configurable": {"thread_id": S.thread_id}})
        except BaseException:
            painel.update(label="Interrompido", state="error", expanded=False)
            raise
        finally:
            S.medidor.ao_iniciar = lambda nome: None
            latencias = list(S.medidor.fechar_turno().values())
        painel.update(label=config.ETAPA_PRONTO, state="complete", expanded=False)

    # Guardada na conversa: depois do rerun a lista fica recolhida, com o tempo de cada etapa.
    S.mensagens.append({"tipo": "etapas", "linhas": [f"{t} ({s:.1f} s)".replace(".", ",")
                                                     for t, s in zip(etapas, latencias)]})
    return estado


def turno_de_entrada(texto: str, arquivo) -> None:
    """Mesma logica do agente.py: entrada, pergunta do que falta, fora de escopo ou regra gerada.

    Um arquivo mais texto digitado na mesma mensagem vira o tipo `misto`: o no 30 recebe o caminho na primeira linha e o
    texto digitado nas seguintes.
    """
    S = st.session_state
    tipo, caminho = "texto", None
    with tempfile.TemporaryDirectory() as pasta:   # pasta temporaria do sistema, nunca dentro do repositorio
        if arquivo is not None:
            extensao = Path(arquivo.name).suffix.lower()
            if extensao not in config.EXTENSOES_ENTRADA:
                dizer("agente", config.MENSAGEM_EXTENSAO.format(extensao=repr(extensao),
                                                                aceitas=list(config.EXTENSOES_ENTRADA)))
                return
            tipo = config.EXTENSOES_ENTRADA[extensao][0]   # tipo do arquivo, que manda no limite de tamanho
            if arquivo.size > config.LIMITE_BYTES_ENTRADA[tipo]:
                dizer("agente", config.MENSAGEM_ARQUIVO_GRANDE.format(tamanho=arquivo.size,
                                                                      limite=config.LIMITE_BYTES_ENTRADA[tipo]))
                return
            caminho = Path(pasta) / f"entrada{extensao}"
            caminho.write_bytes(arquivo.getvalue())
            fala = f"Arquivo enviado: {arquivo.name}"
            if texto:
                tipo, fala = "misto", f"{fala}\n{texto}"
                texto = f"{caminho}\n{texto}"
            else:
                texto = str(caminho)
        else:
            fala = texto
        dizer("usuario", fala)
        with st.chat_message("user"):   # aparece ja, sem esperar o rerun do fim do turno
            st.text(fala)
        bruta = f"{S.pendente}\n{texto}" if S.pendente else texto
        entrada = {"entrada_bruta": bruta, "tipo_entrada": tipo}
        entrada.update({"pedido_mudanca": bruta} if S.gerou else {"id_sessao": S.thread_id})
        try:
            estado = invocar_com_progresso(entrada)
        except ERROS_SERVICO as erro:
            dizer("agente", config.MENSAGEM_SERVICO_RECUSOU.format(erro=type(erro).__name__))
            return
        except ValueError as erro:
            if tipo == "texto":
                raise
            dizer("agente", config.MENSAGEM_ARQUIVO_INVALIDO.format(erro=erro))
            return
    S.custo_turno = estado["custo_turno"]
    status = estado["status_entrada"]
    transcrito = estado["pedido_mudanca"] if S.gerou else estado["descricao_usuario"]
    if tipo != "texto":
        dizer("agente", config.MENSAGEM_TRANSCRICAO.format(tipo=tipo, texto=transcrito))
    if status == "incompleto":
        S.pendente = bruta if tipo == "texto" else transcrito
        dizer("agente", "\n\n".join(config.PERGUNTAS_FALTANTES[t] for t in estado["faltantes"]))
        return
    S.pendente = ""   # fora_de_escopo descarta a entrada alheia; aprovado ja a consumiu
    if status == "fora_de_escopo":
        dizer("agente", config.MENSAGEM_FORA_DE_ESCOPO)
        return
    S.gerou = True
    dizer("gobr", estado["gobr_atual"])
    if estado["sem_chave"]:
        itens = "\n".join(f"- {item}" for item in estado["sem_chave"])
        dizer("agente", config.MENSAGEM_RESSALVA.format(itens=itens))
    S.aguardando = True


def aprovar() -> None:
    S = st.session_state
    try:
        estado = invocar_com_progresso({"aprovacao": "aprovado"})
    except ERROS_SERVICO as erro:
        S.aguardando = True   # a regra continua na tela para aprovar de novo
        dizer("agente", config.MENSAGEM_SERVICO_RECUSOU.format(erro=type(erro).__name__))
        return
    S.custo_turno = estado["custo_turno"]
    dizer("agente", config.MENSAGEM_GRAVADA.format(exemplo_id=estado["exemplo_gravado"],
                                                   status=config.STATUS_GRAVACAO))


# ============================================================================
# TELA
# ============================================================================

def estilo() -> str:
    p = config.PALETA
    logo = base64.b64encode((RAIZ / config.ARQ_LOGO).read_bytes()).decode("ascii")
    return f"""
<style>
html, body, [class*="css"], .stApp {{ font-family: "Helvetica Neue", Arial, "Liberation Sans", sans-serif; }}
[data-testid="stHeader"] {{ display: none; }}
.block-container {{ padding-top: 0 !important; max-width: 52rem; }}
.faixa {{ background: {p['verde']}; width: 100vw; margin: 0 0 1.2rem calc(50% - 50vw); padding: 0.8rem 0 0.8rem calc(50vw - 50%); display: flex;
          align-items: center; gap: 1rem; }}
.faixa img {{ height: 2.6rem; }}
.faixa span {{ color: {p['branco']}; font-size: 1.25rem; font-weight: 700; }}
.faixa b {{ color: {p['amarelo']}; }}
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) {{
    background: {p['verde_claro']}; color: {p['escuro']}; border: 1px solid {p['verde']}; border-radius: 1.2rem;
    padding-right: 1.5rem; }}
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) p,
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) li {{ color: {p['escuro']}; }}
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) {{
    background: {p['cinza_claro']}; color: {p['escuro']}; border-radius: 1.2rem; }}
[data-testid="stChatMessage"] [data-testid="stExpander"], [data-testid="stChatMessage"] details {{
    background: {p['branco']}; color: {p['escuro']}; border-radius: 0.8rem; }}
[data-testid="stChatMessage"] details p, [data-testid="stChatMessage"] details li,
[data-testid="stChatMessage"] details summary {{ color: {p['escuro']} !important; }}
.stButton button {{ background: {p['verde']}; color: {p['branco']}; border: none; border-radius: 999px;
                    font-weight: 700; padding: 0.4rem 1.6rem; }}
.stButton button:hover {{ background: {p['escuro']}; color: {p['branco']}; }}
.rodape {{ color: {p['escuro']}; font-size: 0.85rem; opacity: 0.8; margin-top: 0.5rem; }}
</style>
<div class="faixa"><img src="data:image/png;base64,{logo}" alt="goVendas"><span>{config.NOME_AGENTE}</span></div>
"""


def desenhar_historico() -> None:
    for m in st.session_state.mensagens:
        if m["tipo"] == "usuario":
            with st.chat_message("user"):
                st.text(m["texto"])
        elif m["tipo"] == "etapas":
            with st.chat_message("assistant"):
                with st.status(config.ETAPA_PRONTO, state="complete", expanded=False):
                    st.markdown("\n".join(f"- {linha}" for linha in m["linhas"]))
        elif m["tipo"] == "gobr":
            with st.chat_message("assistant"):
                st.code(m["texto"], language=None)   # o st.code ja traz o botao de copiar
        else:
            with st.chat_message("assistant"):
                st.markdown(m["texto"])


def aplicar_teto() -> None:
    """Campo do teto na barra lateral. Vale so para esta sessao do navegador e nao altera o config.py.

    Forma escolhida: o valor digitado e entregue ao medidor ja existente e vale a partir da proxima chamada de no (a
    conversa nao reinicia). Se a pessoa sobe o teto depois de a sessao encerrar por ele, a entrada reabre.
    """
    S = st.session_state
    with st.sidebar:
        valor = st.number_input(config.ROTULO_TETO, min_value=config.TETO_MINIMO_USD, value=float(config.TETO_SESSAO_USD),
                                step=config.TETO_PASSO_USD, format="%.3f")
        st.caption(config.AJUDA_TETO.format(reais=f"{valor * config.CAMBIO_BRL_POR_USD:.2f}",
                                            cambio=config.CAMBIO_BRL_POR_USD))
    S.medidor.teto = valor
    if S.encerrada and S.medidor.acumulado < valor:
        S.encerrada = False


def main() -> None:
    st.set_page_config(page_title=config.TITULO_ABA, page_icon=str(RAIZ / config.ARQ_ICONE), layout="centered")
    st.markdown(estilo(), unsafe_allow_html=True)
    iniciar_sessao()
    S = st.session_state
    aplicar_teto()

    entrada = st.chat_input(config.CAMPO_ENTRADA, accept_file="multiple",
                            disabled=S.aguardando or S.encerrada)
    desenhar_historico()

    try:
        if entrada is not None:
            texto = (entrada.text or "").strip()
            arquivos = list(entrada.files or [])
            if len(arquivos) > 1:
                dizer("agente", config.MENSAGEM_VARIOS_ARQUIVOS)   # recusa a mensagem inteira; a sessao continua
            elif arquivos and S.pendente:
                dizer("agente", config.MENSAGEM_ARQUIVO_NA_PERGUNTA)
            elif arquivos or texto:
                turno_de_entrada(texto, arquivos[0] if arquivos else None)
            st.rerun()
        if S.aguardando:
            col_a, col_m, _ = st.columns([1, 1, 2])
            if col_a.button(config.BOTAO_APROVAR):
                S.aguardando = False
                aprovar()
                st.rerun()
            if col_m.button(config.BOTAO_MUDANCA):
                S.aguardando = False
                dizer("agente", config.PERGUNTA_MUDANCA)
                st.rerun()
    except ErroTeto as erro:
        # Teto e rede de protecao: a mensagem do middleware vai para a conversa e a entrada fecha.
        S.encerrada, S.aguardando = True, False
        dizer("agente", f"{erro}\n\n{config.MENSAGEM_ENTRADA_ENCERRADA}")
        S.medidor.fechar_turno()
        st.rerun()

    m = S.medidor
    if m.acumulado >= m.teto and not S.encerrada:
        S.encerrada = True
        dizer("agente", config.MENSAGEM_ENTRADA_ENCERRADA)
        st.rerun()
    brl = config.CAMBIO_BRL_POR_USD
    st.markdown('<div class="rodape">' + config.RODAPE_CUSTO.format(
        turno=f"{S.custo_turno:.6f}", turno_brl=f"{S.custo_turno * brl:.4f}",
        acumulado=f"{m.acumulado:.6f}", acumulado_brl=f"{m.acumulado * brl:.4f}",
        teto=f"{m.teto:g}", teto_brl=f"{m.teto * brl:.2f}") + '</div>', unsafe_allow_html=True)


main()
