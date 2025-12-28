from src.model.board import Board
from src.solver.solver import Solver
import logging

logging.basicConfig(level=logging.DEBUG)

SEED = 56


def main():
    board = Board(9, 9, seed=SEED)
    solver = Solver(seed=SEED)
    solver.solve(board)


if __name__ == "__main__":
    main()
