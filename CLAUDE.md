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
- Toda sessao de implementacao termina em commit, ou o relatorio diz por que nao terminou.
- git add arquivo por arquivo. git add . e git add -A sao proibidos.
- Commit por assunto, nao por arquivo.
- Mensagem sem emoji, sem segredo e sem URL de tarefa.
- Antes de qualquer git add: provar que o arquivo de ambiente esta ignorado e nao rastreado.
- Enviar ao remoto e degrau separado, com autorizacao propria do Mestre.

## 2. Pastas de trabalho

- O Mestre define a cada rodada quais pastas sao trabalhadas. So trabalhar nelas.
- Achado fora dessas pastas vira uma linha no relatorio, sem correcao.

## 3. Mapa do repositorio

```
trabalho/
  .env                      chaves de API, fora do git; carregado pelo config.py na importacao (so biblioteca padrao)
  .venv/                    ambiente virtual do projeto
  .gitignore
  CLAUDE.md                 este arquivo
  govendas-rules.pdf        manual original do fornecedor
  config.py                 configuracao, uma secao por no (30, 50, 60, 80 e 90)
  agente.py                 ponto de entrada: conversa de varios turnos no terminal (`.venv/bin/python -B agente.py [id_da_conversa]`); pergunta se a pessoa aprova a regra
  orquestracao.py           mapa declarativo do grafo (estado, agentes, tools, nos, arestas); fonte unica do fluxo
  src/
    script30_entrada/       converte a entrada em texto e confere os minimos (texto, imagem e documento); prompt `entrada_minimos` no BigQuery
    script50_normalizacao/  normalizacao da entrada; mesmo codigo usado no corpus
    script60_recuperacao/   exemplos (denso + Jaccard) e recorte do manual
    script80_geracao/       escreve o .gobr (modelo padrao gpt-6-luna; prompt no BigQuery)
    script90_persistencia/  grava a regra aprovada em `exemplos` (INSERT, status `pendente`); unica escrita do projeto no BigQuery
    script20_middleware/    Medidor: latencia por no, custo acumulado da sessao e parada dura no teto (`TETO_SESSAO_USD`); transversal, nao e no do grafo
    script10_orquestracao/  constroi o grafo LangGraph a partir de orquestracao.py e traz os nos adaptados; o campo `sem_chave` do estado leva ao usuario o que o manual nao cobriu
```

Os dados do projeto deixaram de viver em disco e passaram a viver no BigQuery, no dataset
`govendas_gobr` do projeto `multiagentes-514823`, nas tabelas `exemplos`, `prompts` e `manual`. O adendo de reexecucao do no 80 e a linha ativa de `prompts` com `tipo` `adendo_reexecucao_gobr`. O prompt do no 30 e a linha ativa de `prompts` com `tipo` `entrada_minimos` (v1, `prompt_entrada_minimos_v1.md`).

Entrada aceita pelo no 30: `texto` e, por caminho de arquivo digitado no `agente.py`, `imagem` (`.png`, ate 5 000 000 bytes), `documento` (`.pdf`, ate 10 000 000 bytes), convertidos pelo modelo do no (`gpt-6.1-terra`, provado em 2026-11-24), e `audio` (`.wav`, ate 5 000 000 bytes e 55 s), transcrito pelo Speech-to-Text v2 do Google Cloud (modelo `long`, pt-BR, REST com ADC, reconhecimento direto sem bucket; o modelo do no recusa audio) antes de ir ao modelo. `misto` (um arquivo por turno) fica de fora, depende de decisao do Mestre. Tipos, extensoes e limites moram no `config.py`.

Estado do grafo, campos da entrada: `entrada_bruta` (so registro), `tipo_entrada`, `status_entrada` (`aprovado`, `incompleto`, `fora_de_escopo`) e `faltantes` (`quem_atende`, `desfecho`, `conflito`). O no 30 devolve o texto em `descricao_usuario` (primeiro turno) ou `pedido_mudanca` (mudanca), e o no 50 le esses campos e `tipo_entrada`. Entrada reprovada encerra o turno; o `agente.py` pergunta o que falta, soma a resposta e chama de novo.

Campos de aprovacao do estado: `aprovacao` (vazio | `aprovado`, preenchido pelo `agente.py`; o `START` e condicional por ele e leva ao no `persistencia`, que o esvazia), `exemplo_gravado` (`exemplo_id` da linha gravada) e `metadados_normalizado` e `metadados_geracao` (o que os nos 50 e 80 devolveram, para a gravacao). Operacao de escrita: o no 90 faz `INSERT` na tabela `exemplos` com `origem` `usuario` e `status_revisao` `pendente` (`ORIGEM_GRAVACAO` e `STATUS_GRAVACAO` em `config.py`); a recuperacao filtra `aprovado`, entao a linha so entra como exemplo depois da revisao do Mestre. Nenhum `UPDATE` nem `DELETE`: as 193 linhas do corpus sao congeladas.

## 4. Padrao de pastas

1. **`config.py` na raiz do projeto.** E o unico arquivo de configuracao. Tem secoes internas,
   uma por no do agente. Configuracao nao e codigo: a raiz e o que se edita, `src/` e o que se
   importa.
2. **Cada passo do workflow vive em `src/scriptNN_{nome}/`**, com o script principal chamado
   `scriptNN_{nome}.py`, mais a documentacao e os arquivos que so aquele passo usa.
3. **A numeracao vai de 10 em 10** e segue a ordem do passo no workflow, para que a sequencia
   seja legivel sem executar nada. O intervalo entre dois numeros existe para acomodar um passo
   novo sem renomear os seguintes.
4. **A documentacao de cada passo mora na pasta do passo**, nao na raiz.

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
| Hash | Todo hash gravado em arquivo ou metadado e SHA-256, e o nome do campo nao leva o algoritmo (ex.: `hash_prompt`). Arquivos antigos podem manter `sha256` no nome | Nome estavel nao muda se o algoritmo mudar |
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
- Credencial vem do ambiente; o `config.py` o preenche a partir do `.env` (ignorado pelo git) e falha se faltar arquivo ou variavel.
- Para conferir prefixo, mostrar no maximo os 4 primeiros caracteres.
- Segredo em claro em arquivo rastreado: parar, nao comitar, reportar caminho e tipo.

## 10. Honestidade de resultado

- Prova executada, nunca deduzida.
- Numero sem o comando que o produziu nao entra em relatorio.
- Lacuna e declarada, nao omitida.

## 11. Decisoes e evidencias

Resultados completos dos testes: pasta local `resultados_teste_v3/`, ao lado do repositorio, nao versionada.

| Tema | Decisao | Evidencia |
|---|---|---|
| Modelo do no 80 | `gpt-6-luna` e o padrao | 10 regras reservadas com o prompt v2c: 0 altas, 1 media, cerca de US$ 0,0022 por regra |
| Alternativas testadas | terra, lite, 3.8-flash e carbon ficaram de fora | terra: 7 a 8 vezes mais caro; lite: 2 altas; 3.8-flash: mais caro e equivalente; carbon: cortou a regra 135 e custou 3,8 vezes mais |
| Prompt | v2c ativo no BigQuery (tipo `geracao_gobr`) | v3 empatou e e 5,6% menor, mas fica inativo; v1 inativa (licenca para omitir trecho) |
| Recuperacao | `N1_DENSO` = 2 e `N2_JACCARD` = 2 mantidos | A uniao denso + Jaccard entregou 138 de 139 secoes exigidas, no melhor caso: a consulta usou as regras do proprio corpus; em producao virao do normalizador |

Middleware (script20): o construtor do grafo embrulha a chamada de cada no; o `Medidor` soma o `custo_turno` que o no
ja devolve e bloqueia a proxima chamada quando o acumulado da sessao atinge `TETO_SESSAO_USD` (US$ 0,60 = 5 x US$ 0,0147
x 8 turnos; modelo, embedding e fala; BigQuery nao conta). O `agente.py` imprime custo do turno, acumulado e latencia por
no, e encerra a sessao ao bloquear. Contador vale por processo.

Teste de injecao de prompt (2026-11-24, so medicao, sem contencao): ataque A (instrucao direta no texto), B (trocar o papel
do no de entrada e pedir o prompt) e C (instrucao dentro de imagem .png) ficaram CONTIDOS. Nenhum trecho do prompt
`entrada_minimos` vazou. Amostra de um ataque por tipo: nao prova imunidade.

## 12. Dividas

- `langgraph` instalado no `.venv` sem arquivo de dependencias no repositorio.
- Lacuna do manual sobre o limite da frequencia do historico (29 de 193 exemplos usam a construcao); caso 190.
- Decisao pendente do Mestre: `sem venda ou prospects` (manual 06-01) contra `sem venda` (corpus).
- O gabarito de algumas regras usa escopo de grupo onde a descricao diz "do vendedor".
- Cobertura real do manual em producao ainda nao medida (precisa do normalizador na cadeia).
- Nao existe rotina de edicao de prompts e manual no BigQuery.
- Teste de injecao com uma amostra por ataque; variar redacao e repetir antes de afirmar robustez.

## 13. Configuracao e metadado

- Decisao mora no config.py, nunca no codigo do no. Prefixo, modelo, dimensao,
  nome de tabela, nome de tipo de prompt e endereco de servico sao configuracao.
  Mudar o prefixo ou o modelo de embedding invalida todos os vetores ja gravados.
- Metadado so com valor real da execucao. Campo que o no nao tem como preencher
  fica vazio e e nomeado no relatorio, com o motivo. Nunca preencher com valor
  plausivel, porque falso positivo em metadado contamina analise futura sem
  deixar rastro.
