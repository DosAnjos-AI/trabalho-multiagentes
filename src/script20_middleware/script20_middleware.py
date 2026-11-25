"""Middleware de observabilidade: latencia por no, custo acumulado da sessao e parada dura no teto.

Transversal ao fluxo (por isso o numero 20, antes do no de entrada). Nao e no do grafo: o construtor do grafo embrulha a
funcao de cada no com `Medidor.embrulhar`, e nenhum no conhece o middleware. O medidor nao calcula custo; so soma o
`custo_turno` que o no ja devolve. Nada e escrito em disco.
"""
import time
from typing import Callable


class ErroTeto(RuntimeError):
    """O acumulado da sessao atingiu o teto; a chamada do no foi bloqueada antes de rodar."""


class Medidor:
    """Contador unico da sessao (vive enquanto o processo vive)."""

    def __init__(self, teto_usd: float) -> None:
        self.teto = teto_usd
        self.acumulado = 0.0
        self.chamadas: dict[str, int] = {}
        self.latencias_turno: dict[str, float] = {}   # esvaziado por `fechar_turno`

    def embrulhar(self, nome: str, funcao: Callable[[dict], dict], zera_custo: bool) -> Callable[[dict], dict]:
        """Devolve a funcao do no com medicao. `zera_custo`: o no recomeca `custo_turno` do zero (entrada e
        persistencia); nos demais, `custo_turno` e o do estado de entrada mais o custo do proprio no."""
        def medido(estado: dict) -> dict:
            # O bloqueio vem antes da chamada: no que nao roda nao gasta.
            if self.acumulado >= self.teto:
                raise ErroTeto(f"Teto da sessao atingido: acumulado US$ {self.acumulado:.6f}, teto US$ {self.teto:.6f}. "
                               f"Chamada do no {nome!r} bloqueada.")
            inicio = time.perf_counter()
            saida = funcao(estado)
            self.latencias_turno[nome] = round(self.latencias_turno.get(nome, 0.0) + time.perf_counter() - inicio, 3)
            self.chamadas[nome] = self.chamadas.get(nome, 0) + 1
            if "custo_turno" in saida:
                anterior = 0.0 if zera_custo else float(estado.get("custo_turno") or 0.0)
                self.acumulado += float(saida["custo_turno"]) - anterior
            return saida
        return medido

    def fechar_turno(self) -> dict[str, float]:
        """Latencia por no do turno que acabou; zera para o proximo."""
        latencias, self.latencias_turno = self.latencias_turno, {}
        return latencias
