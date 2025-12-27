"""Объект поля Сапёра."""
import random
from typing import List, Optional
import logging
from src.model.cell import Cell

# Вводные для генерации поля.
BOMB_PROBABILITY = 0.1
SEED = 43


class Board:
    """Поле Сапёра (матрица)."""
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.field = []

    # Генерация
    def auto_generate(self, row, col) -> None:
        """Автоматическая генерация поля.

        Учитывает первый ход"""
        field = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        random.seed(SEED)
        for i in range(self.rows):
            for j in range(self.cols):
                if (i, j) == (row, col):
                    is_mine = False
                else:
                    is_mine = random.choices(
                        [True, False],
                        [BOMB_PROBABILITY, 1]
                    )[0]
                field[i][j] = Cell(is_mine=is_mine)
        self.field = field

    def calc_mines(self) -> None:
        """Высчитывает число каждой клетки (количество бомб соседей)."""
        for i in range(self.rows):
            for j in range(self.cols):
                cell = self.get_cell(i, j)
                if cell:
                    cell.adj_mines = sum(
                        [n.is_mine for n in self.get_neighbors(i, j)]
                    )

    # Решение
    def solve(self) -> bool:
        """Универсальное решение."""
        while True:
            if self.logic_solve():
                break
            else:
                self.prob_solve()

    def logic_solve(self) -> bool:
        """Логическое решение."""
        pass

    def prob_solve(self) -> bool:
        """Вероятностное решение."""
        pass

    # Действие
    def open(self, row, col) -> bool:
        """Сделать ход (открыть клетку)."""
        # Генерируем поле только после первого хода
        if not self.field:
            self.auto_generate(row, col)
            self.calc_mines()
        # Открываем клетку
        cell = self.get_cell(row, col)
        if cell and not cell.is_opened():
            if cell.is_mine:
                logging.warning("Подорвался на мине!")
                return False
            else:
                mines = cell.adj_mines
                cell.open()
                if not mines:
                    for i in range(row-1, row+2):
                        for j in range(col-1, col+2):
                            self.open(i, j)
        return True

    def get_neighbors(self, row, col) -> List[Cell]:
        """Получить всех соседей клетки."""
        neighbors = []
        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                if (i, j) != (row, col):
                    cell = self.get_cell(i, j)
                    if cell:
                        neighbors.append(cell)
        return neighbors

    def get_cell(self, row, col) -> Optional[Cell]:
        """Получить клетку."""
        if row in range(0, self.rows) and col in range(0, self.cols):
            return self.field[row][col]
        else:
            return None

    # ...
    ...

    # Вывод
    def as_visible(self):
        """Вывод игровой доски"""
        return "\n".join(
            [" ".join(
                [cell.visible_char() for cell in line]
            ) for line in self.field]
        )

    def as_truth(self):
        """Вывод настоящей доски"""
        return "\n".join(
            [" ".join(
                [cell.truth_char() for cell in line] 
            ) for line in self.field]
        )
