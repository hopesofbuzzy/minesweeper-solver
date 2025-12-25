"""Объект поля Сапёра."""
import random
import logging
from src.model.cell_type import RCellType, VCellType
# RCellType - типы оригиналього поля
# VCellType - типы игрового поля

# Вводные для генерации поля.
BOMB_PROBABILITY = 0.1
SEED = 42


class Field:
    """Поле Сапёра."""
    def __init__(self, x, y):
        self._real = self.auto_generate(x, y)
        self.visible = [[VCellType.CLOSED for _ in range(x)] for _ in range(y)]

    # Генерация
    def auto_generate(self, x, y):
        """Автоматическая генерация поля."""
        real = [[None for _ in range(x)] for _ in range(y)]
        random.seed(SEED)
        for i in range(x):
            for j in range(y):
                real[j][i] = random.choices(
                    [RCellType.BOMBED, RCellType.FREE],
                    [BOMB_PROBABILITY, 1]
                )[0]
        return real

    # Решение
    def solve(self):
        """Универсальное решение."""
        while True:
            if self.logic_solve():
                break
            else:
                self.prob_solve()

    def logic_solve(self):
        """Логическое решение."""
        pass

    def prob_solve(self):
        """Вероятностное решение."""
        pass

    # Действие
    def open(self, x, y):
        if self._real[y][x] is RCellType.BOMBED:
            logging.warning("Подорвался на мине!")
            return False

    # Вывод
    def __str__(self):
        return f"{self._real}"
