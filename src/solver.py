"""Движок решения Сапёра."""
from typing import List


class Solver:
    @staticmethod
    def solve(field: List[List]):
        """Универсальное решение."""
        if Solver.logic_solve(field):
            pass
        else:
            Solver.prob_solve(field)

    @staticmethod
    def logic_solve(field: List[List]):
        """Логическое решение."""
        pass

    @staticmethod
    def prob_solve(field: List[List]):
        pass
