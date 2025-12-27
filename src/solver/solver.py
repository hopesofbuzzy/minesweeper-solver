import logging
import random
from src.model.board import Board


class Solver:
    """Решатель поля Сапёра."""
    def __init__(self, seed=42):
        random.seed(seed)

    def solve(self, board: Board) -> bool:
        """Универсальное решение."""
        i = 1
        while not board.is_solved:
            i += 1
            if self.logic_solve(board):
                return True
            else:
                self.prob_solve(board)
            logging.info("\n" + board.as_visible() + "\n")
            logging.info(f"Board solved: {board.is_solved}")
            if i == 3:
                break

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
                flagged_adj = len([n for n in unopened_neighbors if n.is_flagged])
                closed_adj = len([n for n in unopened_neighbors if n.is_closed])
                if (flagged_adj + closed_adj) == cell.adj_mines:
                    for n in unopened_neighbors:
                        n.flag()
        logging.info("\n" + board.as_visible() + "\n")

    def random_solve(self, board: Board) -> bool:
        board.open(
            random.randrange(0, board.rows),
            random.randrange(0, board.cols)
        )
        logging.info("\n" + board.as_visible() + "\n")

    def prob_solve(self, board: Board) -> bool:
        """Вероятностное решение."""
        # Заглушка
        self.random_solve(board)
        return True
