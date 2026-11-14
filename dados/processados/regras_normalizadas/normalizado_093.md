---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_093.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9391
tokens_saida: 448
custo_usd: 0.011631
tempo_segundos: 6.40
timestamp: 2026-11-14T19:50:07-03:00
---

## explicacao_normalizada
Cada vendedor atende seus próprios clientes fixos. No campo do interior, trabalham os vendedores 18, 212, 300, 376, 395, 421, 43, 449, 486, 488, 489, 490, 6 e 68. No campo da capital, ficam todos os demais vendedores de campo. No televendas, entram todos os vendedores de televendas.

Para os clientes do campo da capital e do televendas, atendemos semanalmente os que estão ativos para seu vendedor e estão em dia; os ativos para seu vendedor que estão inadimplentes, a cada 14 dias; os inativos para seu vendedor, a cada 30 dias; e os clientes sem vendas, a cada 30 dias.

No campo do interior, atendemos os clientes ativos para seu vendedor a cada 14 dias, os inativos para seu vendedor a cada 30 dias e os clientes sem vendas a cada 30 dias. Em todas essas situações, preferimos atender nos dias úteis. Se um cliente se encaixar em mais de uma situação, seguimos a ordem apresentada para a equipe dele.

## regras_extraidas
03-secoes/03-01-times.md
03-secoes/04-02-selecao-clientes-ruptura.md
03-secoes/07-03-frequencia.md#Fixa por período
03-secoes/06-01-atividade-inatividade.md
03-secoes/06-03-financeiros.md
sem_chave: clientes sem vendas
03-secoes/07-02-preferencia-dia-semana.md
03-secoes/07-01-parametros-estrutura-e-exemplos.md#Ordem entre regras de parâmetros
