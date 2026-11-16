"""Configuracao do normalizador. Valores validados por script_normalizacao.validar_config antes de qualquer leitura."""
from pathlib import Path

BASE = Path(__file__).parent
RAIZ = BASE.parents[1]

# ============================================================================
# 1. CAMINHOS (relativos a raiz do projeto, via pathlib)
# ============================================================================
# Pasta com as explicacoes sinteticas (entrada_NNN.md). So leitura.
CAMINHO_ENTRADA = RAIZ / "dados" / "processados" / "regras_entradas"
# Pasta de saida oficial. Nasce so na execucao real; nunca e apagada nem sobrescrita.
CAMINHO_SAIDA = RAIZ / "dados" / "processados" / "regras_normalizadas"
# Respostas invalidas do modelo, guardadas cruas (resposta paga nao se perde).
CAMINHO_REJEITADOS = BASE / "rejeitados"
# Prompt e arquivo auxiliar do manual (material de consulta enviado inteiro ao modelo).
CAMINHO_PROMPT = BASE / "prompt_normalizador_v3.md"
CAMINHO_AUXILIAR = BASE / "regras_para_normalizador_v2.md"

# Manual parseado: cada nome de arquivo citado em regras_extraidas precisa existir aqui.
CAMINHO_MANUAL = RAIZ / "manual"

# Arquivo com as chaves de API (na raiz, ignorado pelo git). So e lido na execucao paga; nunca em --estimar.
CAMINHO_ENV = RAIZ / ".env"
# Nome da variavel de ambiente com a chave de cada fornecedor (copiado da tarefa 02).
VARIAVEL_CHAVE = {"openai": "CHAVE_OPENAI", "gemini": "CHAVE_GEMINI"}

# ============================================================================
# 2. MODELO
# ============================================================================
# Trecho copiado de ENTREGA01/task02_entradas/config.py (linhas 16 a 139), sem alteracao.
# Catalogo de modelos. Precos em dolares por 1 milhao de tokens.
# Fonte dos precos: paginas oficiais de precos dos fornecedores, consultadas em 2026-11-13
# (OpenAI: developers.openai.com/api/docs/pricing; Gemini: aistudio.google.com/docs/pricing).
# Identificadores copiados da listagem da conta (client.models.list() de cada SDK) em 2026-11-13.
# Preco envelhece: reconferir antes de lote grande.
#
# Faixas por fornecedor:
#   "barato"        -> piso de referencia: mostra quanto a qualidade cai quando o custo cai
#   "intermediario" -> modelo de trabalho do fornecedor: candidato real para rodar as 193
#   "melhor"        -> teto de qualidade: referencia para medir o que os outros perdem
#   None            -> fora das tres faixas (mantido porque ja estava no catalogo)
#
# Temperatura: testada em 2026-11-13 com uma chamada minima por modelo nos valores 0.0, 0.3 e 2.0.
#   Os modelos OpenAI da geracao 6 e o gpt-5-mini RECUSAM qualquer valor diferente do padrao. Erro literal da API:
#     "Unsupported value: 'temperature' does not support 0.3 with this model. Only the default (1) value is supported."
#   -> padrao imposto: 1. Nao enviar o parametro.
#   gpt-4.1-mini, gpt-4o-mini e gpt-5.4-mini (e seus snapshots) ACEITARAM 0.0, 0.3 e 2.0 no teste de 2026-11-13.
#   ATENCAO: script_entradas.py nunca envia temperatura para a OpenAI; esses modelos rodam no padrao (1).
#   O metadado distingue: "1.0 (padrao imposto pelo modelo)" para quem so aceita 1, e
#   "nao enviada pelo script (...)" para quem aceitaria outro valor.
#   Os modelos Gemini testados aceitaram 0.0, 0.3 e 2.0 (a listagem informa padrao 1.0 e maximo 2.0).
MODELOS = {
    # --- OpenAI ---
    # Faixa barato (ja estava no catalogo). Descrito como "Our most efficient model for focused, high-volume tasks".
    # Temperatura: so aceita o padrao 1 (erro literal acima).
    "gpt-6-luna": {"fornecedor": "openai", "faixa": "barato", "entrada_por_milhao": 0.10, "saida_por_milhao": 0.50,
                   "temperatura_aceita": (1.0, 1.0)},
    # Faixa intermediario (ja estava no catalogo). Descrito como "clear, natural writing", o que importa aqui.
    # Temperatura: so aceita o padrao 1 (erro literal acima).
    "gpt-6.1-terra": {"fornecedor": "openai", "faixa": "intermediario", "entrada_por_milhao": 1.00, "saida_por_milhao": 5.00,
                      "temperatura_aceita": (1.0, 1.0)},
    # Fora das faixas (ja estava no catalogo): "Near-Astra performance ... at a lower cost". Alternativa ao teto.
    # Temperatura: so aceita o padrao 1 (erro literal acima).
    "gpt-6.1-sol": {"fornecedor": "openai", "faixa": None, "entrada_por_milhao": 2.00, "saida_por_milhao": 10.00,
                    "temperatura_aceita": (1.0, 1.0)},
    # Faixa melhor (novo). Descrito como "Our most capable model for the most demanding work".
    # Temperatura: so aceita o padrao 1 (erro literal acima).
    "gpt-6-astra": {"fornecedor": "openai", "faixa": "melhor", "entrada_por_milhao": 10.00, "saida_por_milhao": 50.00,
                    "temperatura_aceita": (1.0, 1.0)},
    # --- Gemini ---
    # Faixa barato (novo): menor preco de texto entre os Gemini listados. Temperatura: aceita 0.0 a 2.0.
    "gemini-3.1-flash-lite": {"fornecedor": "gemini", "faixa": "barato", "entrada_por_milhao": 0.25, "saida_por_milhao": 1.50,
                              "temperatura_aceita": (0.0, 2.0)},
    # Fora das faixas (ja estava no catalogo): barato, mas mais caro que o 3.1-flash-lite. Temperatura: aceita 0.0 a 2.0.
    "gemini-3.5-flash-lite": {"fornecedor": "gemini", "faixa": None, "entrada_por_milhao": 0.30, "saida_por_milhao": 2.50,
                              "temperatura_aceita": (0.0, 2.0)},
    # Faixa intermediario (ja estava no catalogo). Preco dobra em 2027-01-01 (1.50 / 7.50).
    # Alternativa listada pelo mesmo preco: gemini-3.8-flash. Temperatura: aceita 0.0 a 2.0.
    "gemini-3.6-flash": {"fornecedor": "gemini", "faixa": "intermediario", "entrada_por_milhao": 0.75, "saida_por_milhao": 3.75,
                         "temperatura_aceita": (0.0, 2.0)},
    # Fora das tres faixas, mesmo preco do 3.6-flash (0.75 / 3.75 ate 2026-12-31; 1.50 / 7.50 a partir de 2027-01-01).
    # Incluido em 2026-11-13 como substituto que o proprio Google indica para a familia 2.5 na mensagem de 404.
    # Descrito como "Our previous-generation Flash model for software engineering, autonomous agents...".
    # Temperatura: aceitou 0.0, 0.3 e 2.0 no teste de 2026-11-13 (listagem: padrao 1.0, maximo 2.0).
    "gemini-3.8-flash": {"fornecedor": "gemini", "faixa": None, "entrada_por_milhao": 0.75, "saida_por_milhao": 3.75,
                         "temperatura_aceita": (0.0, 2.0)},
    # Faixa melhor (novo). Descrito como "Our most capable reasoning model".
    # Preco promocional ate 2026-11-30; a partir de 2026-12-01 passa a 4.00 / 20.00. Temperatura: aceita 0.0 a 2.0.
    "gemini-4-carbon": {"fornecedor": "gemini", "faixa": "melhor", "entrada_por_milhao": 2.00, "saida_por_milhao": 10.00,
                        "temperatura_aceita": (0.0, 2.0)},
    # Fora das faixas (ja estava no catalogo). ATENCAO: nao aparece na listagem da conta em 2026-11-13 e a chamada
    # de teste devolveu 404 NOT_FOUND ("models/gemini-3.1-pro-preview is not found for API version v1").
    # Mantido so para nao remover entrada existente; nao usar em MODELOS_ATIVOS.
    "gemini-3.1-pro-preview": {"fornecedor": "gemini", "faixa": None, "entrada_por_milhao": 2.00, "saida_por_milhao": 12.00,
                               "temperatura_aceita": None},
    # --- Familias pedidas pelo Mestre em 2026-11-13 (faixa None: fora da escala barato/intermediario/melhor) ---
    # Identificadores copiados de client.models.list() em 2026-11-13. Precos: developers.openai.com/api/docs/pricing
    # e aistudio.google.com/docs/pricing, consultados em 2026-11-13. Snapshots datados: a pagina nao lista preco
    # proprio; assumido o mesmo do alias.
    # OpenAI mini, geracao 4 (modelos de chat). Temperatura: aceita 0.0 a 2.0 (testado).
    "gpt-4.1-mini": {"fornecedor": "openai", "faixa": None, "familia": "openai-mini-g4", "entrada_por_milhao": 0.40,
                     "saida_por_milhao": 1.60, "temperatura_aceita": (0.0, 2.0)},
    "gpt-4.1-mini-2025-04-14": {"fornecedor": "openai", "faixa": None, "familia": "openai-mini-g4", "entrada_por_milhao": 0.40,
                                "saida_por_milhao": 1.60, "temperatura_aceita": (0.0, 2.0)},
    "gpt-4o-mini": {"fornecedor": "openai", "faixa": None, "familia": "openai-mini-g4", "entrada_por_milhao": 0.15,
                    "saida_por_milhao": 0.60, "temperatura_aceita": (0.0, 2.0)},
    "gpt-4o-mini-2024-07-18": {"fornecedor": "openai", "faixa": None, "familia": "openai-mini-g4", "entrada_por_milhao": 0.15,
                               "saida_por_milhao": 0.60, "temperatura_aceita": (0.0, 2.0)},
    # OpenAI mini, geracao 4, de AUDIO: listados na conta, mas nao sao modelos de chat. Chamada de teste recusada:
    #   "Error code: 404 - This is not a chat model and thus not supported in the v1/chat/completions endpoint."
    # Fora de MODELOS_ATIVOS: o script so chama chat.completions. Temperatura: nao testavel por chat.
    # Preco: transcribe 1.25 entrada / 5.00 saida; tts 0.60 entrada de texto (saida e audio, 12.00; sem preco de texto).
    "gpt-4o-mini-transcribe": {"fornecedor": "openai", "faixa": None, "familia": "openai-mini-g4-audio",
                               "entrada_por_milhao": 1.25, "saida_por_milhao": 5.00, "temperatura_aceita": None},
    "gpt-4o-mini-transcribe-2025-03-20": {"fornecedor": "openai", "faixa": None, "familia": "openai-mini-g4-audio",
                                          "entrada_por_milhao": 1.25, "saida_por_milhao": 5.00, "temperatura_aceita": None},
    "gpt-4o-mini-transcribe-2025-12-15": {"fornecedor": "openai", "faixa": None, "familia": "openai-mini-g4-audio",
                                          "entrada_por_milhao": 1.25, "saida_por_milhao": 5.00, "temperatura_aceita": None},
    "gpt-4o-mini-tts": {"fornecedor": "openai", "faixa": None, "familia": "openai-mini-g4-audio",
                        "entrada_por_milhao": 0.60, "saida_por_milhao": 12.00, "temperatura_aceita": None},
    "gpt-4o-mini-tts-2025-03-20": {"fornecedor": "openai", "faixa": None, "familia": "openai-mini-g4-audio",
                                   "entrada_por_milhao": 0.60, "saida_por_milhao": 12.00, "temperatura_aceita": None},
    "gpt-4o-mini-tts-2025-12-15": {"fornecedor": "openai", "faixa": None, "familia": "openai-mini-g4-audio",
                                   "entrada_por_milhao": 0.60, "saida_por_milhao": 12.00, "temperatura_aceita": None},
    # OpenAI mini, geracao 5.
    # gpt-5-mini: so aceita o padrao 1. Erro literal: "Unsupported value: 'temperature' does not support 0.3 with
    # this model. Only the default (1) value is supported."
    "gpt-5-mini": {"fornecedor": "openai", "faixa": None, "familia": "openai-mini-g5", "entrada_por_milhao": 0.25,
                   "saida_por_milhao": 2.00, "temperatura_aceita": (1.0, 1.0)},
    "gpt-5-mini-2025-08-07": {"fornecedor": "openai", "faixa": None, "familia": "openai-mini-g5", "entrada_por_milhao": 0.25,
                              "saida_por_milhao": 2.00, "temperatura_aceita": (1.0, 1.0)},
    # gpt-5.4-mini: aceita 0.0 a 2.0 (testado).
    "gpt-5.4-mini": {"fornecedor": "openai", "faixa": None, "familia": "openai-mini-g5", "entrada_por_milhao": 0.75,
                     "saida_por_milhao": 4.50, "temperatura_aceita": (0.0, 2.0)},
    "gpt-5.4-mini-2026-03-17": {"fornecedor": "openai", "faixa": None, "familia": "openai-mini-g5", "entrada_por_milhao": 0.75,
                                "saida_por_milhao": 4.50, "temperatura_aceita": (0.0, 2.0)},
    # Gemini 2.5. ATENCAO: flash, flash-lite e pro aparecem na listagem, mas a chamada de teste de 2026-11-13 devolveu
    #   "404 NOT_FOUND ... This model models/gemini-2.5-flash is no longer available to new users" (idem flash-lite e pro).
    # Mantidos em MODELOS_ATIVOS por pedido explicito; a falha fica registrada pelo script, sem custo.
    # Temperatura: nao verificavel (404). Listagem informa padrao 1.0 e maximo 2.0.
    # Precos: 2.5-pro vale para prompt ate 200k tokens. Pagina informa 2.5-pro e 2.5-flash depreciados, com
    # redirecionamento para outros modelos a partir de 2026-12-01.
    "gemini-2.5-flash-lite": {"fornecedor": "gemini", "faixa": None, "familia": "gemini-2.5", "entrada_por_milhao": 0.10,
                              "saida_por_milhao": 0.40, "temperatura_aceita": None},
    "gemini-2.5-flash": {"fornecedor": "gemini", "faixa": None, "familia": "gemini-2.5", "entrada_por_milhao": 0.30,
                         "saida_por_milhao": 2.50, "temperatura_aceita": None},
    "gemini-2.5-pro": {"fornecedor": "gemini", "faixa": None, "familia": "gemini-2.5", "entrada_por_milhao": 1.25,
                       "saida_por_milhao": 10.00, "temperatura_aceita": None},
    # gemini-2.5-flash-image: modelo de imagem, mas respondeu texto no teste. Aceitou 0.0, 0.3 e 2.0, embora a
    # listagem informe maximo 1.0. Preco de texto igual ao 2.5-flash (2.50 saida); saida de IMAGEM custa 30.00 por
    # milhao: se a resposta trouxer imagem, o custo calculado pelo script fica subestimado. Desligamento: 2027-03-15.
    "gemini-2.5-flash-image": {"fornecedor": "gemini", "faixa": None, "familia": "gemini-2.5", "entrada_por_milhao": 0.30,
                               "saida_por_milhao": 2.50, "temperatura_aceita": (0.0, 2.0)},
}

# Modelo do normalizador: o mesmo que gerou as explicacoes (decisao do Mestre). Deve existir em MODELOS.
MODELO = "gpt-6.1-terra"
# Fornecedor do modelo escolhido. Este script so implementa a chamada da OpenAI (KISS: sem Gemini nao usado).
FORNECEDOR = "openai"
FORNECEDORES_ACEITOS = ("openai",)
# Temperatura: o gpt-6.1-terra so aceita o padrao 1 (teste de 2026-11-13, comentario do catalogo acima).
# Nao testar de novo (seria chamada paga). O script nao envia o parametro; este valor so vai para os metadados.
TEMPERATURA = 1.0

# ============================================================================
# 3. VERSOES (entram nos metadados; trocar o prompt ou o auxiliar = novo arquivo _v2)
# ============================================================================
ID_PROMPT = CAMINHO_PROMPT.name
ID_AUXILIAR_MANUAL = CAMINHO_AUXILIAR.name
VERSAO_NORMALIZADOR = "v3"

# ============================================================================
# 4. ENTRADA
# ============================================================================
# Lista fechada de tipos de entrada. "misto" so para combinacoes (texto+imagem, imagem+audio...).
TIPOS_ENTRADA = ("texto", "imagem", "audio", "documento", "misto")
# Lista fechada de origens.
ORIGENS = ("sintetico", "usuario")
# Tipo usado no lote das explicacoes sinteticas (sao texto).
TIPO_ENTRADA_CORPUS = "texto"

# ============================================================================
# 5. CUSTO
# ============================================================================
# Precos por milhao de tokens: ver MODELOS acima (fonte: paginas oficiais de preco dos fornecedores,
# consultadas em 2026-11-13, copiadas da tarefa 02; preco envelhece, reconferir antes do lote).
# Teto de gasto por execucao, em DOLARES (USD). Sem valor padrao: o Mestre preenche depois de ver a
# estimativa (--estimar). Enquanto for None, o script recusa qualquer chamada paga. O modo estimar nao usa.
# Teto da rodada B1, autorizado pelo Mestre em 2026-11-14; o lote exigira novo valor.
TETO_GASTO_USD = 0.20
# Estimativa local (sem tokenizador instalado): caracteres por token.
# 4.12 = calibrado nas 193 chamadas da tarefa 02 (caracteres de prompt_v2 + .gobr / tokens_entrada reais).
# 3.0 = [HIPOTESE] pessimista, para o auxiliar (portugues acentuado e markdown tokeniza pior que o .gobr).
CARACTERES_POR_TOKEN_OTIMISTA = 4.12
CARACTERES_POR_TOKEN_PESSIMISTA = 3.0
# Saida projetada = caracteres da explicacao / caracteres por token + tokens das chaves (faixa minima),
# ou caracteres da explicacao * TOKENS_SAIDA_POR_CARACTERE_MAX + tokens das chaves (faixa maxima).
# 0.53 = media observada na tarefa 02 de tokens_saida por caractere de explicacao, ja incluindo raciocinio
# interno do modelo (74442 tokens / 149104 caracteres = 0.50 no agregado; media por arquivo 0.53).
TOKENS_CHAVES_MIN = 100
TOKENS_CHAVES_MAX = 400
TOKENS_SAIDA_POR_CARACTERE_MAX = 0.53

# ============================================================================
# 6. EXECUCAO
# ============================================================================
# Retomada: arquivo normalizado_{id}.md ja existente e pulado, nunca sobrescrito. Unico modo aceito.
RETOMADA = "pular_existentes"
RETOMADAS_ACEITAS = ("pular_existentes",)
# Limite de tokens de saida por chamada; tambem entra na projecao de custo antes de cada chamada.
MAX_TOKENS_SAIDA = 16000

# ============================================================================
# 7. VALIDACAO
# ============================================================================
# Secoes que a resposta do modelo deve ter, nesta ordem, com cabecalho exato.
SECOES_OBRIGATORIAS = ("## explicacao_normalizada", "## regras_extraidas")
# Prefixo de chave sem correspondente no arquivo auxiliar.
PREFIXO_SEM_CHAVE = "sem_chave:"
# Campos do bloco de metadados, na ordem em que sao gravados (17). Escritos pelo script, nunca pelo modelo.
CAMPOS_METADADOS = (
    "origem", "tipo_entrada", "id_sessao_turno", "id_explicacao", "id_prompt", "hash_prompt",
    "id_auxiliar_manual", "hash_auxiliar_manual", "versao_normalizador", "hash_normalizador",
    "modelo", "temperatura", "tokens_entrada", "tokens_saida", "custo_usd", "tempo_segundos", "timestamp",
)

# Formato final da secao `## regras_extraidas`: objeto JSON com dois vetores, montado pelo script (o modelo
# continua devolvendo uma chave por linha). Pensado para outro script carregar no BigQuery.
CAMPO_REGRAS = "regras_extraidas"  # nomes de arquivo do manual, sem `#Titulo`, sem repeticao
CAMPO_SEM_CHAVE = "sem_chave"      # descricoes livres das regras sem arquivo correspondente no manual
