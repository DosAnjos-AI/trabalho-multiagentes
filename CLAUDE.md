# CLAUDE.md

Regras gerais para qualquer tarefa neste repositorio. O projeto constroi um agente que
escreve regras na linguagem GOBR do goVendas (arquivos `.gobr`) a partir da descricao do
negocio feita por uma pessoa.

## 1. Papeis e escada de aprovacao

- O Mestre decide; o Executor executa o que o prompt da rodada pede.
- Investigar, planejar, implementar, comitar e enviar sao degraus separados. Um degrau nao
  se funde ao seguinte.
- Commit e envio ao remoto (`git push`) so com autorizacao explicita do Mestre na rodada.
- Arquivo entra em commit pelo caminho exato. Nunca `git add -A`, `git add .` ou
  `git commit -a`. Nunca `--no-verify`: hook que falha e reportado, nao contornado.

## 2. Pastas de trabalho

- O Mestre define a cada rodada quais pastas sao trabalhadas. So trabalhar nelas.
- Achado fora dessas pastas vira uma linha no relatorio, sem correcao.

## 3. Mapa do repositorio

| Pasta ou arquivo | O que e |
|---|---|
| `ENTREGA01/task02_entradas/readme.md` | Documentacao da `task02_entradas` |
| `govendas-rules.pdf` | Manual original da linguagem GOBR |
| `manual/` | Manual parseado em markdown |
| `exemplos/` | Pares reais do fornecedor (`.gobr` e `.pdf`) |
| `simulacao/` | Corpus sintetico de origem, uma pasta por regra |
| `dados/originais/regras_gobr/` | Base bruta, referencia intocada |
| `dados/processados/regras_gobr/` | Base deduplicada e corrigida, com `CORRECOES.md` |
| `dados/processados/regras_entradas/` | Fichas em linguagem natural das regras |
| `src/conferidor_gobr/` | Codigo permanente reutilizavel: conferidor deterministico de `.gobr` |
| `ENTREGA01/` | Entregas parciais ja concluidas |
| `.env` | Chaves de API, ignorado pelo git |
| `.venv/` | Ambiente virtual do projeto |

## 4. Padrao de pastas das entregas

- Cada entrega parcial e uma pasta `ENTREGAnn/` na raiz, com uma subpasta por tarefa no
  formato `taskNN_nome/`.
- Cada tarefa tem `config.py` (parametros), um `script_*.py` e um `readme.md` com entrada,
  saida, configuracao, uso e avisos.
- Dados de uso geral vao para `dados/`; codigo reutilizavel entre tarefas vai para `src/`.
- Saida oficial vai para `dados/processados/`; saida de teste e de avaliacao fica dentro
  da pasta da tarefa.
- `ENTREGA01/` esta entregue. Nao se edita nem se roda nada dentro dela sem pedido do
  Mestre. Rodar `ENTREGA01/task01_dedup/script_dedup.py` apaga a pasta de saida dele.
- `ENTREGA02/` esta prevista para padronizacao, embedding e banco vetorial. So e criada
  quando o Mestre abrir a discussao.

## 5. Padroes de codigo

| Padrao | Regra | Motivo |
|---|---|---|
| Caminhos | Sempre `pathlib.Path`. Nunca `os.path.join`, nunca concatenacao de string | O projeto roda em Linux e em Windows |
| Criacao de pasta | Sempre `mkdir(parents=True, exist_ok=True)` | - |
| Leitura e escrita de texto | Sempre `encoding="utf-8"` explicito | Sem isso o Windows usa a codificacao local e corrompe acento |
| Escrita de texto | Sempre `newline="\n"` | Sem isso o Windows grava CRLF e o mesmo script gera bytes diferentes |
| Escrita de CSV | `encoding="utf-8"` e `newline=""` | Evita linha vazia entre registros no Windows |
| Comentarios | Em portugues, explicando por que assim, nao o que o codigo faz | Comentario que repete o codigo nao protege contra a limpeza futura |
| Emojis | Nenhum em codigo. Permitidos so em documentacao | - |
| Interpretador | `.venv/bin/python -B`, nunca o Python do sistema | O Ubuntu recusa instalacao no Python do sistema; `-B` evita `__pycache__` |

## 6. Scripts

- Um script por tarefa.
- Dividir em mais de um so com ganho alto, e declarar o ganho no relatorio.

## 7. Falha alta

- A configuracao e validada antes de qualquer leitura ou chamada paga.
- Valor fora da lista de aceitos falha com mensagem que diz o valor recebido, os valores
  aceitos e o arquivo onde configurar.
- Sem valor padrao embutido para configuracao que aponta para recurso externo.

## 8. Saida paga e saida refazivel

- Saida de processamento local e apagada antes de reescrever.
- O script so apaga pasta que ele mesmo criou e que contem apenas saida dele; caso
  contrario, aborta.
- Saida de API paga nunca e apagada. Cada execucao cria pasta propria com carimbo de data
  e hora, modelo e versao de prompt no nome.
- Lote pago longo grava cada arquivo logo apos a chamada e aceita chave de retomada.
- Teto de gasto por execucao fica no arquivo de configuracao, com projecao antes de cada
  chamada.

## 9. Segredos e credenciais

- Ler e permitido; imprimir nao. Nenhum valor de segredo em terminal, arquivo ou relatorio.
- Chave nunca em arquivo rastreado, nunca em configuracao, nunca em codigo.
- Credencial vem do mecanismo do ambiente (`.env` ignorado pelo git).
- Para conferir prefixo, mostrar no maximo os 4 primeiros caracteres.
- Segredo em claro em arquivo rastreado: parar, nao comitar, reportar caminho e tipo.

## 10. Honestidade de resultado

- Prova executada, nunca deduzida.
- Numero sem o comando que o produziu nao entra em relatorio.
- Lacuna e declarada, nao omitida.
