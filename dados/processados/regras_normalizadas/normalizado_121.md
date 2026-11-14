---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_121.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9341
tokens_saida: 581
custo_usd: 0.012246
tempo_segundos: 8.08
timestamp: 2026-11-14T19:51:34-03:00
---

## explicacao_normalizada
Os vendedores do televendas habilitados no sistema atendem seus clientes seguindo esta ordem: primeiro, não agendamos clientes com situação baixada na Receita Federal nem clientes que sejam filiais.

Entre os demais, atendemos a cada 3 dias os clientes reativados com a empresa e também os que fizeram uma única compra com a empresa. Depois, para quem comprou com o próprio vendedor nos últimos 30 dias, seguimos o histórico de atendimento, com intervalo mínimo de 3 dias e máximo de 21 dias.

Para quem ainda não se enquadrou nas situações anteriores, atendemos a cada 14 dias se comprou com o próprio vendedor nos últimos 60 dias; a cada 21 dias se comprou nos últimos 90 dias; e a cada 14 dias se comprou nos últimos 120 dias. Os demais clientes são atendidos a cada 7 dias.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
03-secoes/06-05-localizacao-classificacao.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Remoção de agendamento (exclusivo)
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/06-07-curva-abc-ciclo-de-vida.md
03-secoes/06-01-atividade-inatividade.md
03-secoes/06-02-recencia-visita-positivacao.md
03-secoes/06-12-opcoes-de-tempo.md
03-secoes/07-03-frequencia.md#Dinâmica (baseada em dados existentes)
sem_chave: limites mínimo e máximo da frequência histórica
