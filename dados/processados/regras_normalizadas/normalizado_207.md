---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_207.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9353
tokens_saida: 517
custo_usd: 0.011938
tempo_segundos: 7.12
timestamp: 2026-11-14T20:01:40-03:00
---

## explicacao_normalizada
Os vendedores de televendas habilitados atendem seus clientes seguindo esta ordem de prioridade: clientes pessoa física não devem ser agendados. Para os demais, quem ainda não comprou com seu vendedor deve ser atendido a cada 14 dias.

Para quem já comprou com seu vendedor, olhamos o tempo desde a última compra com ele. Se comprou nos últimos 14 dias, usamos o intervalo do histórico de compras acrescido de 7 dias, com limite de 14 dias. Se a última compra foi entre 14 e 30 dias atrás, atendemos a cada 14 dias; entre 30 e 45 dias, a cada 21 dias; entre 45 e 90 dias, a cada 14 dias. Quem está há mais de 90 dias sem comprar com seu vendedor é atendido a cada 28 dias. Quando o cliente se encaixar em mais de uma dessas situações, vale a primeira nessa ordem.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
03-secoes/06-05-localizacao-classificacao.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)
03-secoes/06-01-atividade-inatividade.md
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/06-02-recencia-visita-positivacao.md
03-secoes/06-12-opcoes-de-tempo.md
03-secoes/07-03-frequencia.md#Dinâmica (baseada em dados existentes)
sem_chave: limite sobre frequência do histórico
