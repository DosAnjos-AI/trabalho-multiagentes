---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_198.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9306
tokens_saida: 388
custo_usd: 0.011246
tempo_segundos: 5.65
timestamp: 2026-11-14T20:00:26-03:00
---

## explicacao_normalizada
Os vendedores de televendas habilitados atendem os clientes seguindo esta prioridade: quem nunca comprou com a empresa é atendido a cada 25 dias. Em seguida, quem fez uma única compra com a empresa e não comprou com o próprio vendedor nos últimos 30 dias é atendido a cada 14 dias.

Para quem comprou com o próprio vendedor nos últimos 30 dias, usamos o intervalo de atendimento baseado no histórico, com mínimo de 7 e máximo de 30 dias. Depois disso, os clientes ativos na empresa são atendidos a cada 14 dias, e todos os demais, a cada 21 dias. Quem se encaixar em mais de uma situação segue a primeira que se aplicar.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
03-secoes/06-01-atividade-inatividade.md
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/06-02-recencia-visita-positivacao.md
03-secoes/06-12-opcoes-de-tempo.md
03-secoes/07-03-frequencia.md#Dinâmica (baseada em dados existentes)
sem_chave: limites mínimo e máximo da frequência histórica
