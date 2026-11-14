# Tabela avaliativa (0 a 10 por coluna; sem nota composta)

Fonte: `medicao_cega.md` (hash congelado antes de abrir o mapa) e metadados dos 30 normalizados. Cobertura, precisao e consistencia excluem a chave "Fluxo de uma regra" nas tres versoes.

| Versao | Cobertura de chaves | Precisao de chaves | Temas fora do manual (`sem_chave`) | Consistencia | Fidelidade do texto (semelhanca media) | Qualidade da prosa | Custo medio/arquivo (US$) e projecao 183 (US$) | Rejeicoes | Fluxo emitido (de 10, sem nota) |
|---|---|---|---|---|---|---|---|---|---|
| v1 (A) | 8,49 | 9,24 | 2,86 (2 acertos / 7) | 9,07 | 10,0 (0,9984) | 9,2 | 0,011422 / 2,09 | 0 | 9 |
| v2 (C) | 8,49 | 9,04 | 4,00 (2 acertos / 5) | 9,07 | 10,0 (1,0000) | 10,0 | 0,011749 / 2,15 | 0 | 0 |
| v3 (B) | 9,92 | 9,55 | 5,00 (2 acertos / 4) | 9,07 | 10,0 (1,0000) | 10,0 | 0,012012 / 2,20 | 0 | 0 |

Notas:
- Empate em Consistencia (9,07) e em Fidelidade (10,0) nas tres; nao desempatado.
- Temas fora do manual: acertos / (temas fora do manual do gabarito + `sem_chave` sem tema correspondente), agregado dos 10 ids.
- Nenhum tema do gabarito foi excluido por divergencia texto x `.gobr`; as divergencias (128: "dia 20" no rotulo vs 16; 169: rotulos "entre 7d e 30d") ficaram registradas no gabarito, sem penalidade.
- Sensibilidade (informativa, nao e a nota): se `04-01#Cenario 3` fosse aceita como chave de ordem, v1/A 9,07 de cobertura e 9,63 de precisao; v2/C 9,31 e 9,71; v3/B 9,92 e 9,55 (saida de `julgar.py` em `medicao_cega.md`).
