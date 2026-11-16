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

```
trabalho/
  .env                      chaves de API, fora do git
  .venv/                    ambiente virtual do projeto
  .gitignore
  CLAUDE.md                 este arquivo
  govendas-rules.pdf        manual original do fornecedor
  src/
    script50_normalizacao/  normalizacao da entrada; mesmo codigo usado no corpus
    script90_conferidor/    conferidor deterministico de arquivos .gobr
```

Os dados do projeto deixaram de viver em disco e passaram a viver no BigQuery, no dataset
`govendas_gobr` do projeto `multiagentes-514823`, nas tabelas `exemplos`, `prompts` e `manual`.

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
- Credencial vem do mecanismo do ambiente (`.env` ignorado pelo git).
- Para conferir prefixo, mostrar no maximo os 4 primeiros caracteres.
- Segredo em claro em arquivo rastreado: parar, nao comitar, reportar caminho e tipo.

## 10. Honestidade de resultado

- Prova executada, nunca deduzida.
- Numero sem o comando que o produziu nao entra em relatorio.
- Lacuna e declarada, nao omitida.
