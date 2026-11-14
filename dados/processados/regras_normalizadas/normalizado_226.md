---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_226.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9369
tokens_saida: 494
custo_usd: 0.011839
tempo_segundos: 6.85
timestamp: 2026-11-14T20:03:26-03:00
---

## explicacao_normalizada
Os vendedores de televendas habilitados atendem seus clientes seguindo esta ordem: quando um cliente se encaixar em mais de uma situação, vale o primeiro atendimento aplicável.

Quem nunca comprou com a empresa deve ser atendido a cada 7 dias. Quem comprou com qualquer vendedor da empresa nos últimos 30 dias e fez uma única compra com a empresa deve ser atendido a cada 14 dias. Quem tem frequência histórica de compra de 30 dias e comprou com qualquer vendedor da empresa nos últimos 120 dias deve ser atendido a cada 28 dias.

Quem comprou com o próprio vendedor entre 20 e 30 dias atrás deve ser atendido no intervalo indicado pelo histórico, limitado a no máximo 60 dias. Quem está há mais de 120 dias sem comprar com qualquer vendedor da empresa deve ser atendido a cada 14 dias. Quem está há mais de 180 dias sem comprar com qualquer vendedor da empresa deve ser atendido a cada 28 dias, respeitando a prioridade das situações anteriores.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
03-secoes/06-01-atividade-inatividade.md
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/06-02-recencia-visita-positivacao.md
03-secoes/06-12-opcoes-de-tempo.md
03-secoes/06-08-frequencia-e-parametros.md
03-secoes/07-03-frequencia.md#Dinâmica (baseada em dados existentes)
sem_chave: limite máximo da frequência do histórico
