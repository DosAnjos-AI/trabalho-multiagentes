# Filtros de horário, somente para alertas (manual 5.6, p.20-21)

Exemplo:
```
na carteira("televendas")
nos dias uteis e de hora em hora a partir de '07:00'
```
Dispara em dias úteis, a cada hora, a partir das 7h.

| Filtro | Efeito |
|---|---|
| `às 'hh:mm'` | horário exato (janela de até 15 minutos) |
| `às 'hh:mm' e às 'hh:mm'` | vários horários |
| `de hora em hora` | a cada hora, o dia todo |
| `de hora em hora entre 'hh:mm' e 'hh:mm'` | a cada hora dentro do intervalo |
| `de hora em hora a partir de 'hh:mm'` | a cada hora a partir do horário |

Só uma forma de horário por vez (`às` ou `de hora em hora`). Se a checagem roda a cada 15 minutos e o filtro é `às '15:00'`, o evento dispara se o horário atual estiver entre 15:00 e 15:15.
