from src.model.board import Board
from src.solver.solver import Solver
import logging

logging.basicConfig(level=logging.DEBUG)

SEED = 45


def main():
    # Зерно задаёт рандомизацию расположения бомб
    # Но зерно решателя способно "удалить" некоторые бомбы
    # Из-за особенностей первого хода
    # Для полной детерминированности меняйте глобальное зерно
    board = Board(9, 9, seed=SEED)
    solver = Solver(seed=SEED)
    solver.solve(board)
    logging.info("\n" + board.as_truth() + "\n")


if __name__ == "__main__":
    main()
