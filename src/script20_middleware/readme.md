# Passo 20 - Middleware de observabilidade

`script20_middleware.py` traz o `Medidor`: contador unico da sessao (um processo do `agente.py`), com latencia por no,
custo acumulado e parada dura no teto. Nao e no do grafo, nao tem aresta e nenhum no o conhece: o construtor
(`script10_orquestracao.construir_grafo`) embrulha a funcao de cada no com `Medidor.embrulhar`.

- Antes de cada no: se `acumulado >= teto`, levanta `ErroTeto` dizendo acumulado, teto e o no bloqueado. O no nao roda.
- Depois de cada no: soma a latencia (segundos, tres casas) e o custo. O medidor nao calcula custo: so soma o
  `custo_turno` que o no ja devolve. Os nos que recomecam `custo_turno` do zero (entrada e persistencia, lista
  `FUNCOES_QUE_ZERAM_CUSTO` no script10) entram sem descontar o valor do turno anterior.
- `fechar_turno()` devolve as latencias do turno e as zera; o `agente.py` as imprime na linha de custo.
- Teto: `TETO_SESSAO_USD` no `config.py` (US$ 0,60 = 5 x US$ 0,0147 x 8 turnos, arredondado). Conta modelo de
  linguagem, embedding e fala; BigQuery nao conta. Sem aviso antes do teto: e rede de protecao contra laco, nao
  controle fino. Ao bloquear, o `agente.py` imprime a mensagem e encerra a sessao.
- Nada e escrito em disco. O acumulado vale enquanto o processo vive; nova execucao do `agente.py` zera o contador.
