"""Объект поля Сапёра."""
import random
import logging
from src.model.cell_type import RCellType, VCellType
from src.model.cell import Cell
# RCellType - типы оригиналього поля
# VCellType - типы игрового поля

# Вводные для генерации поля.
BOMB_PROBABILITY = 0.1
SEED = 42


class Field:
    """Поле Сапёра."""
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.field = self.auto_generate(rows, cols)

    # Генерация
    def auto_generate(self, rows, cols):
        """Автоматическая генерация поля."""
        field = [[None for _ in range(cols)] for _ in range(rows)]
        random.seed(SEED)
        for i in range(rows):
            for j in range(cols):
                field[i][j] = Cell(
                    vtype=VCellType.CLOSED,
                    rtype=random.choices(
                        [RCellType.BOMBED, RCellType.SAFE],
                        [BOMB_PROBABILITY, 1]
                    )[0]
                )
        return field

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

    def open(self, row, col):
        cell = self.get_cell(row, col)
        if cell and not cell.is_opened():
            logging.info(f"{row} {col}")
            if cell.is_bombed():
                logging.warning("Подорвался на мине!")
            else:
                bombs = self.get_bombs(row, col)
                cell.open()
                if bombs:
                    cell.value = bombs
                else:
                    for i in range(row-1, row+2):
                        for j in range(col-1, col+2):
                            self.open(i, j)

    def get_bombs(self, row, col):
        result = 0
        logging.info("Проверка соседей")
        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                cell = self.get_cell(i, j)
                if cell and cell.is_bombed():
                    logging.info("Есть бомба!")
                    result += 1
        return result

    def get_cell(self, row, col):
        if row in range(0, self.rows) and col in range(0, self.cols):
            return self.field[row][col]
        else:
            return None

    # Действие
    ...

    # Вывод
    def __str__(self):
        return self.show()
    
    def show(self, real=False):
        result = ""
        for line in self.field:
            result += " ".join([cell.show(real=real) for cell in line]) + "\n"
        return result
