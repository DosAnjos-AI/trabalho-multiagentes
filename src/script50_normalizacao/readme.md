# script50_normalizacao

No do agente que normaliza o texto de um turno: limpa o texto sem mudar o conteudo e indica quais arquivos
do manual a regra exige. A mesma funcao serve ao corpus (origem `sintetico`) e a fala de um usuario
(origem `usuario`); so muda quem chama.

## O que recebe

`normalizar_turno(texto, origem, tipo_entrada, id_sessao_turno, ctx, *, id_explicacao=None)`

- `texto`: o texto do turno.
- `origem` e `tipo_entrada`: valores aceitos definidos em `config.py` (`ORIGENS`, `TIPOS_ENTRADA`).
- `id_sessao_turno`: obrigatorio para `usuario`, `None` para `sintetico`.
- `id_explicacao`: obrigatorio para `sintetico`, `None` para `usuario`.
- `ctx`: o `Contexto`, criado uma vez por `construir_contexto(config)`.

## O que devolve

Um `Resultado`: `ok`, `texto_normalizado`, `regras_extraidas` (`{"regras_extraidas": [caminhos do manual],
"sem_chave": [textos]}`), `metadados`, `erros` e `resposta_crua`. A resposta crua vai sempre, inclusive
quando a validacao falha, porque a chamada e paga.

## De onde vem o conteudo

Tudo vem do BigQuery (`PROJETO_GCP` e `DATASET` do `config.py`), lido uma vez em `construir_contexto`:

- Prompt e auxiliar do manual: tabela `prompts`, linha unica com `tipo` (`normalizador`, `auxiliar_manual`)
  e `ativo`. Zero ou mais de uma linha ativa, ou hash gravado diferente do hash do texto, interrompe.
- Caminhos validos do manual: coluna `caminho` da tabela `manual`.

A chave da API vem da variavel de ambiente configurada em `VARIAVEL_CHAVE` (`.env`, ignorado pelo git).

## O que nao faz

Nao escreve em disco nem no BigQuery. Quem persiste o resultado e outro no.

## O que valida

- Argumentos e configuracao antes da chamada paga (valor recebido, valores aceitos e onde configurar).
- Projecao de custo da chamada contra `TETO_GASTO_USD`.
- Resposta: cabecalhos exatos, chaves existentes no auxiliar, sem repeticao, `sem_chave` com descricao,
  resposta nao cortada, caminhos existentes no manual.
