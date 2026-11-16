---
origem: sintetico
tipo_entrada: texto
id_sessao_turno: null
id_explicacao: entrada_160.md
id_prompt: prompt_normalizador_v3.md
hash_prompt: ac77cd72a5f36d9ade3bf4509c1e6369ec40895d012818891fcd26be2541c68a
id_auxiliar_manual: regras_para_normalizador_v2.md
hash_auxiliar_manual: 5f555d020aadb380bbf4eb4b32e43d7a824bf33f1f5c8f416c323fe059bc5971
versao_normalizador: v3
hash_normalizador: 8a1d0d2c189a0ac425e33f91bce0abd4995fe1566aac9f9370316c3df41dc65e
modelo: gpt-6.1-terra
temperatura: 1.0 (padrao imposto pelo modelo)
tokens_entrada: 9523
tokens_saida: 597
custo_usd: 0.012508
tempo_segundos: 7.98
timestamp: 2026-11-14T19:55:28-03:00
---

## explicacao_normalizada
Trabalhamos com os vendedores de televendas habilitados, exceto 2136, 2179, 2134 e 1865, e também com os vendedores 2136, 2179, 2134 e 1865. Cada um atende seus clientes. Quando um cliente se encaixa em mais de uma situação, seguimos a primeira situação na ordem abaixo.

Primeiro, para os clientes pessoa jurídica com data da rota no próximo 1 dia e cuja última visita ocorreu entre 4 e 3000 dias atrás, o atendimento é a cada 1 dia. Isso vale para quem ainda não comprou com o próprio vendedor, para quem comprou com ele entre 31 e 60 dias atrás ou entre 61 e 90 dias atrás, para quem está ativo para ele considerando 30 dias, para quem está inativo para ele e também para os demais clientes que atendam às condições da rota e da visita.

Depois disso, para pessoa jurídica que ainda não comprou com o próprio vendedor, atendemos a cada 7 dias quando o vendedor é 2136, 2179, 2134 ou 1865; com os demais vendedores de televendas habilitados, atendemos a cada 14 dias.

Ainda entre os clientes pessoa jurídica, quem comprou com o próprio vendedor entre 61 e 90 dias atrás é atendido a cada 7 dias; quem comprou entre 31 e 60 dias atrás, a cada 14 dias. Quem está ativo para o próprio vendedor considerando 30 dias é atendido a cada 14 dias, e quem está inativo para ele, a cada 21 dias.

Os clientes pessoa física são atendidos a cada 14 dias. Todo o resto também é atendido a cada 14 dias.

## regras_extraidas
{
  "regras_extraidas": [
    "03-secoes/03-01-times.md",
    "03-secoes/04-02-selecao-clientes-ruptura.md",
    "03-secoes/07-01-parametros-estrutura-e-exemplos.md",
    "03-secoes/06-05-localizacao-classificacao.md",
    "03-secoes/06-11-outros-filtros.md",
    "03-secoes/06-12-opcoes-de-tempo.md",
    "03-secoes/06-02-recencia-visita-positivacao.md",
    "03-secoes/07-03-frequencia.md",
    "03-secoes/06-01-atividade-inatividade.md"
  ],
  "sem_chave": []
}
