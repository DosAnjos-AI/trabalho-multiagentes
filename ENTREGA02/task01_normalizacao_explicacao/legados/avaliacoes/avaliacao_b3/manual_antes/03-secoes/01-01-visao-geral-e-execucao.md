# Visão geral do GoBR e tipos de execução (manual capítulo 1, p.1-2)

O Govendas Business Rules (GoBR) é um sistema de regras de negócio que permite:
- construir e organizar carteiras de clientes para equipes de vendedores;
- parametrizar o comportamento de atendimento dos clientes segundo as regras comerciais do distribuidor;
- analisar eventos complexos (rupturas de venda, inadimplência, campanhas) baseados nas mesmas regras;
- automatizar a execução dessas regras em horários pré-definidos ou sob demanda.

As regras são processadas durante a geração da agenda ou em outros momentos programados. O GoBR é usado ao planejar ou mapear as ações comerciais do distribuidor, e acessa dados de comportamento do cliente (recência de visita, recência de compra, inadimplência, ticket médio, etc.).

As regras são escritas numa linguagem próxima do discurso comercial, sem programação; um único conjunto de regras pode mapear muitas combinações de clientes e vendedores. As regras podem ser alteradas e executadas a qualquer momento, sem customização da engenharia.

## Como configurar um conjunto de regras (p.2)
O GoBR é acessado pela Tela de Administração Govendas (requer VPN interna). São necessários:
1. Um nome descritivo para o conjunto de regras.
2. Um tipo de execução, que determina quando as regras são processadas (tabela abaixo).
3. O ID da empresa à qual a regra pertence.
4. Se a regra está habilitada ou não.
5. O texto com as regras escritas na linguagem gorules.

| Tipo | Código | Quando executa |
|---|---|---|
| DAILY | 2 | toda madrugada, antes de gerar as agendas |
| HOURLY | 3 | a cada hora |
| WEEKLY | 4 | uma vez por semana, no fim de semana |
| DETACHED | 5 | sob demanda (execução manual) |
| ONLUNCH | 6 | entre 12:00 e 14:00 |
| DAWN | 7 | entre 08:00 e 10:00 |
| DARK | 8 | entre 16:00 e 18:00 |
| HALFANHOUR | 9 | a cada 30 minutos |
| SHORTLY | 10 | a cada 15 minutos |

A combinação do tipo da regra com as configurações internas permite, por exemplo: carteiras que se atualizam diariamente, alertas que disparam a cada hora, parametrizações que só se aplicam nos finais de semana.
