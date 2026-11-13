from pathlib import Path

BASE = Path(__file__).parent

# Arquivo com as chaves de API (na raiz do repositorio, nunca versionado)
CAMINHO_ENV = BASE.parents[1] / ".env"
# Nome da variavel de ambiente com a chave de cada fornecedor
VARIAVEL_CHAVE = {"openai": "CHAVE_OPENAI", "gemini": "CHAVE_GEMINI"}
# Pasta com os .gobr de entrada (copia dos deduplicados da task01)
CAMINHO_REGRAS = BASE / "regras_originais"
# Pasta de saida; nunca apagada, cada execucao cria subpastas novas
CAMINHO_SAIDA = BASE / "regras_explicadas"
# Arquivo de prompt usado nesta execucao
CAMINHO_PROMPT = BASE / "prompt_v2.md"  # v1 movido para prompt_legados/prompt_v1.md

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
# Modelos da validacao do prompt_v2 (12). Gerados em duas execucoes do script sem alteracao:
#   20261113-180708: luna, terra, os 4 mini datados, gemini-3.5-flash-lite e gemini-3.6-flash;
#   20261113-183339: gpt-6-astra, gemini-3.1-flash-lite, gemini-3.8-flash e gemini-4-carbon, rodados sozinhos.
# Fora: apelidos sem data dos mini (proveniencia, decisao D9), familia Gemini 2.5 (404 ou modelo de imagem),
# mini de audio (nao sao modelos de chat), gemini-3.1-pro-preview (404), gpt-6.1-sol (faixa "melhor" ja tem astra).
# Lote das 193 fichas (decisao do Mestre): somente gpt-6.1-terra com prompt_v2.md.
# Segunda opcao, so se o terra falhar de forma que impeca a execucao: gpt-6-luna com o mesmo prompt.
MODELOS_ATIVOS = ["gpt-6.1-terra"]
# Temperatura aplicada aos modelos Gemini; o script nunca a envia para a OpenAI (todos rodam no padrao 1)
TEMPERATURA = 0.3
# Teto de gasto por execucao, em DOLARES (USD), nao em reais
TETO_GASTO_USD = 3.00  # folga, nao meta: projecao pessimista para as 193 com o terra e US$ 1,27
# Limite de tokens de saida por chamada; tambem entra na projecao de custo antes de cada chamada
MAX_TOKENS_SAIDA = 16000
# Versao do prompt; entra no nome da pasta de saida
VERSAO_PROMPT = "v2"
# Quantidade de regras: 3 = menor, mediana e maior em numero de blocos de parametros; 193 = todas
QUANTIDADE_REGRAS = 193
# Retomada: caminho de uma pasta de saida ja existente (ex.: CAMINHO_SAIDA / "20261113-190000_gpt-6.1-terra_v2").
# Preenchida: o script escreve nela e pula toda regra que ja tenha entrada_{id}.md gravada. Exige um unico modelo ativo.
# Vazia (""): cria pasta nova com timestamp.
PASTA_RETOMADA = ""
