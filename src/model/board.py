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
    def __init__(self, rows, cols, seed=42, mine_prob=0.1):
        self.rows = rows
        self.cols = cols
        self._field = [[Cell(i, j) for j in range(cols)] for i in range(rows)]
        random.seed(seed)
        self._mine_prob = mine_prob
        self._lay_mines()
        self._calc_mines()

    # Генерация
    def _lay_mines(self) -> None:
        """Расстановка мин."""
        for cell in self.all_cells:
            is_mine = random.choices([True, False], [self._mine_prob, 1])[0]
            cell._is_mine = is_mine

    def _calc_mines(self) -> None:
        """Высчитывает число каждой клетки (количество мин соседей)."""
        for cell in self.all_cells:
            if cell:
                neighbors = self.get_neighbors(cell.row, cell.col)
                cell._adj_mines = sum([n._is_mine for n in neighbors])

    # Действие
    def first_open(self) -> bool:
        """Безопасное первое открытие клетки."""
        for cell in self.all_cells:
            neighbors = self.get_neighbors(cell.row, cell.col)
            is_mine = cell._is_mine
            are_adj_mines = any([n._is_mine for n in neighbors])
            if not (is_mine or are_adj_mines):
                self.open(cell.row, cell.col)
                return True
        return False

    def open(self, row, col) -> bool:
        """Открыть клетку."""
        # Открываем клетку
        cell = self.get_cell(row, col)
        if cell and not cell.is_opened:
            if cell._is_mine:
                logging.warning("Подорвался на мине!")
                return False
            else:
                mines = cell.adj_mines
                cell._open()
                if not mines:
                    for i in range(row-1, row+2):
                        for j in range(col-1, col+2):
                            self.open(i, j)
                    return True

    def flag(self, row, col) -> bool:
        """Пометить клетку."""
        cell = self.get_cell(row, col)
        if cell and not cell.is_flagged:
            cell._flag()

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
