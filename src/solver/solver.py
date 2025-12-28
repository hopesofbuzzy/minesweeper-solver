import logging
import random
from src.model.cell import Cell
from src.model.board import Board


class Solver:
    """Решатель поля Сапёра."""
    def __init__(self, seed=42):
        random.seed(seed)

    def solve(self, board: Board) -> bool:
        """Универсальное решение."""
        if not board.first_open():
            logging.error("Не удалось совершить безопасный первый ход!")
        logging.info(f"Board solved: {board.is_solved}")
        logging.info("\n" + board.as_visible())
        logging.info("\n" + board.as_truth())
        while not board.is_solved:
            if self.logic_solve(board):
                logging.info("Лог. реш." + "\n" + board.as_visible())
            else:
                logging.info("Логическое решение не справилось!")
                return False

    def logic_solve(self, board: Board) -> bool:
        """Логическое решение."""
        if board.is_empty:
            return False
        for cell in board.all_cells:
            if cell.is_opened:
                unopened_neighbors = [
                    n for n in board.get_neighbors(cell.row, cell.col)
                    if not n.is_opened
                ]
                unopened_adj = len(unopened_neighbors)
                flagged_adj = len(
                    [n for n in unopened_neighbors if n.is_flagged]
                )
                closed_adj = len(
                    [n for n in unopened_neighbors if n.is_closed]
                )
                # Эвристика 1: флаги=мины => ходим в непомеченные
                if flagged_adj == cell.adj_mines:
                    for n in unopened_neighbors:
                        if not n.is_flagged:
                            board.open(n.row, n.col)
                            return True
                # Эвристика 2: неоткрытые=мины => расставл. флаги
                if unopened_adj == cell.adj_mines:
                    for n in unopened_neighbors:
                        if not n.is_flagged:
                            board.flag(n.row, n.col)
                            return True
        return False

    # # Эвристики
    # def logic_flag(self, cell: Cell, board: Board):
    #     """"""


    def prob_solve(self, board: Board) -> bool:
        """Вероятностное решение."""
        # Заглушка
        return True
