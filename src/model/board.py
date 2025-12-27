"""Объект поля Сапёра."""
import random
from typing import List, Optional
import logging
from src.model.cell import Cell


class Board:
    """
    Поле Сапёра (матрица).
    Генерирует поле только после первого хода.

    Args:
        rows: количество строк
        cols: количество столбцов
        seed: зерно рандома
        mine_prob: вероятность появления бомбы в клетке
    """
    def __init__(self, rows, cols, seed=42, mine_prob=0.2):
        self.rows = rows
        self.cols = cols
        self._field = []
        random.seed(seed)
        self._mine_prob = mine_prob

    # Генерация
    def _auto_generate(self, row, col) -> None:
        """Автоматическая генерация поля.

        Учитывает первый ход."""
        field = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                # Первый ход всегда верный.
                # Важно, чтобы поле вокруг него было чистым.
                if i in range(row-1, row+2) and j in range(col-1, col+2):
                    is_mine = False
                else:
                    is_mine = random.choices(
                        [True, False],
                        [self._mine_prob, 1]
                    )[0]
                field[i][j] = Cell(row=i, col=j, is_mine=is_mine)
        self._field = field

    def _calc_mines(self) -> None:
        """Высчитывает число каждой клетки (количество бомб соседей)."""
        for i in range(self.rows):
            for j in range(self.cols):
                cell = self.get_cell(i, j)
                if cell:
                    cell._adj_mines = sum(
                        [n._is_mine for n in self.get_neighbors(i, j)]
                    )

    # Действие
    def open(self, row, col) -> bool:
        """Сделать ход (открыть клетку)."""
        # Генерируем поле только после первого хода
        if self.is_empty:
            self._auto_generate(row, col)
            self._calc_mines()
        # Открываем клетку
        cell = self.get_cell(row, col)
        if cell and not cell.is_opened:
            if cell._is_mine:
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
        return True

    def flag(self, row, col) -> bool:
        """Пометить клетку."""
        cell = self.get_cell(row, col)
        if cell and not cell.is_flagged:
            cell.flag()

    # Вспомогательные функции
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
            return self._field[row][col]
        else:
            return None

    @property
    def all_cells(self) -> List[Cell]:
        cells = []
        for line in self._field:
            for cell in line:
                cells.append(cell)
        return cells

    @property
    def field(self) -> List[List[Cell]]:
        return self._field

    @property
    def is_empty(self) -> bool:
        return not self._field

    @property
    def is_solved(self) -> bool:
        closed_cells = len(
            [cell for cell in self.all_cells if cell.is_closed]
        )
        return (closed_cells == 0) and not self.is_empty
    # Вывод
    def as_visible(self) -> str:
        """Вывод игровой доски"""
        return "\n".join(
            [" ".join(
                [cell.visible_char() for cell in line]
            ) for line in self.field]
        )

    def as_truth(self) -> str:
        """Вывод настоящей доски"""
        return "\n".join(
            [" ".join(
                [cell.truth_char() for cell in line]
            ) for line in self.field]
        )
