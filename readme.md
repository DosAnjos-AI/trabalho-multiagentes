# Agente de regras GOBR (goVendas)

Escreve regras na linguagem GOBR a partir da descricao do negocio. Duas portas, o mesmo grafo.

## Preparar

```
.venv/bin/python -B -m pip install -r requirements.txt
```

Precisa do arquivo `.env` com a chave da OpenAI (variavel `CHAVE_OPENAI`) e de `gcloud auth application-default login`
com acesso ao projeto `multiagentes-514823`.

## Terminal

```
.venv/bin/python -B agente.py [id_da_conversa]
```

## Navegador

```
.venv/bin/python -B -m streamlit run app.py
```

Tema claro e paleta em `.streamlit/config.toml`. Abre em http://localhost:8501. A primeira pagina leva cerca de 45 s (leitura do BigQuery, quase toda dos exemplos com vetor); depois fica em cache enquanto
o processo viver. Entrada por texto, por arquivo (`.png`, `.pdf`, `.wav`) ou por um arquivo mais texto na mesma mensagem (nunca dois arquivos); o progresso de cada no aparece durante o turno. A barra lateral traz o teto de custo da sessao (editavel, so para a sessao do navegador; vale a partir da proxima chamada de no) e o rodape mostra os valores em dolar e em real aproximado (`CAMBIO_BRL_POR_USD`). O icone da aba e `icone.png`: o logo sobre quadrado verde, gerado com Pillow a partir de `logo.png`.
Textos, etapas e cores ficam em `config.py`.
