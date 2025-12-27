from src.model.board import Board
import logging

logging.basicConfig(level=logging.DEBUG)


def main():
    board = Board(9, 9)
    board.open(5, 0)
    print(board.as_truth() + "\n")
    print(board.as_visible())


if __name__ == "__main__":
    main()
