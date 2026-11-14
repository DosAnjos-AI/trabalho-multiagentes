---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_188.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9334
tokens_saida: 520
custo_usd: 0.011934
tempo_segundos: 7.36
timestamp: 2026-11-14T19:59:19-03:00
---

## explicacao_normalizada
Os vendedores habilitados do televendas cuidam dos seus clientes. Primeiro, não agendamos clientes inadimplentes, clientes filiais nem aqueles com situação baixada na Receita Federal.

Para os demais, seguimos esta ordem: quem ainda não comprou com o vendedor responsável é atendido a cada 21 dias. Quem comprou com esse vendedor nos últimos 30 dias é atendido conforme o histórico de compras, com intervalo mínimo de 7 dias e máximo de 30 dias.

Quem está entre 31 e 45 dias sem comprar com o vendedor responsável é atendido a cada 14 dias; quem está entre 46 e 60 dias sem comprar com ele, a cada 7 dias. Todos os demais são atendidos a cada 14 dias. Se o cliente se encaixar em mais de uma situação, vale a primeira dessa ordem.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/04-02-selecao-clientes-ruptura.md
03-secoes/06-03-financeiros.md
03-secoes/06-05-localizacao-classificacao.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
03-secoes/06-01-atividade-inatividade.md
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/06-02-recencia-visita-positivacao.md
03-secoes/06-12-opcoes-de-tempo.md
03-secoes/07-03-frequencia.md#Dinâmica (baseada em dados existentes)
sem_chave: limites mínimo e máximo da frequência histórica
