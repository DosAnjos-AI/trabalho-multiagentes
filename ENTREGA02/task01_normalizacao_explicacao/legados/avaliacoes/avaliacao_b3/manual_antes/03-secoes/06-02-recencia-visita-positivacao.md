# Filtros de recência de visita ou positivação/compra (manual 6.2, p.23-24)

Duas opções de objeto: `visita` ou `positivação` (compra). Argumento: `<condicional de tempo>` (ver 06-12-opcoes-de-tempo.md).

Exemplo: `recencia de visita entre 10 dias e 90 dias`.

| Filtro | Descrição |
|---|---|
| `recencia de visita <condicional de tempo>` | última visita no intervalo, por algum vendedor do mesmo grupo do vendedor que tem o cliente |
| `recencia de positivação global ...` | última positivação no intervalo, por qualquer vendedor da empresa |
| `recencia de visita do vendedor ...` | última visita no intervalo foi do vendedor que tem o cliente |
| `fora da recencia de visita <condicional de tempo>` | última visita fora do intervalo, por algum vendedor do grupo |
| `fora da recencia de visita global ...` | última visita fora do intervalo, por qualquer vendedor da empresa |
| `fora da recencia de positivação do vendedor ...` | última positivação fora do intervalo foi do vendedor |
