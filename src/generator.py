"""Генератор поля Сапёра.

Обозначения:
"0" - безопасная клетка
"-1" - бомба
"""
import random

ELEMENTS = [-1, 0]
PROBABILITY = [1, 10]


class Generator:
    """Генератор поля Сапёра."""

    @staticmethod
    def auto_generate(x, y):
        """Автоматическая генерация поля."""
        field = [[None for _ in range(x)] for _ in range(y)]
        random.seed(42)
        for i in range(x):
            for j in range(y):
                field[j][i] = random.choices(ELEMENTS, PROBABILITY)[0]
        return field
