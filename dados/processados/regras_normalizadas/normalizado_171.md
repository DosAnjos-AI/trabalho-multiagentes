---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_171.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9422
tokens_saida: 743
custo_usd: 0.013137
tempo_segundos: 10.83
timestamp: 2026-11-14T19:56:58-03:00
---

## explicacao_normalizada
Os vendedores do televendas cuidam dos seus clientes seguindo esta ordem de prioridade: primeiro, não agendamos clientes inadimplentes, bloqueados, filiais ou com situação baixada na Receita Federal.

Entre os demais, atendemos a cada 14 dias os clientes que nunca compraram com a empresa. Quem fez uma única compra com a empresa e está cadastrado há 30 dias é atendido a cada 10 dias.

Depois, para quem comprou com qualquer vendedor da empresa nos últimos 30 dias e tem intervalo histórico de compras menor que 14 dias, o atendimento é a cada 14 dias. Se esse intervalo histórico for menor que 30 dias, usamos o próprio intervalo histórico para o atendimento, respeitando o mínimo de 14 e o máximo de 28 dias.

Em seguida, atendemos a cada 14 dias quem fez a última compra com qualquer vendedor da empresa entre 21 e 60 dias atrás, e a cada 7 dias quem fez a última compra entre 61 e 90 dias atrás. Por fim, os clientes cuja última compra com qualquer vendedor da empresa estiver fora do intervalo de 90 a 180 dias são atendidos a cada 21 dias. Quem se encaixar em mais de uma dessas situações fica com o primeiro tratamento da sequência.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/04-02-selecao-clientes-ruptura.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
03-secoes/06-03-financeiros.md
03-secoes/06-05-localizacao-classificacao.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/06-01-atividade-inatividade.md
03-secoes/06-11-outros-filtros.md
03-secoes/06-12-opcoes-de-tempo.md
03-secoes/06-02-recencia-visita-positivacao.md
03-secoes/06-08-frequencia-e-parametros.md
03-secoes/07-03-frequencia.md#Dinâmica (baseada em dados existentes)
sem_chave: limites mínimo e máximo da frequência histórica
