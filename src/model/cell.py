import logging
from src.model.cell_state import CellState

visible_chars: dict[CellState, str] = {
    CellState.CLOSED: "▣",
    CellState.OPENED: "<adj_mines>",
    CellState.FLAGGED: "f"
}

truth_chars: dict[bool, str] = {
    True: "*",
    False: "<adj_mines>"
}


class Cell:
    def __init__(self, state=CellState.CLOSED, is_mine=False):
        self.state = state
        self.is_mine = is_mine
        self.adj_mines = 0  # Число клетки

    def open(self) -> None:
        if self.state == CellState.OPENED:
            logging.error("Клетка уже открыта!")
        self.state = CellState.OPENED

    def is_opened(self) -> bool:
        return self.state == CellState.OPENED

    def truth_char(self) -> str:
        if self.is_mine:
            return truth_chars[self.is_mine]
        else:
            return str(self.adj_mines)

    def visible_char(self):
        if self.state is CellState.OPENED:
            return str(self.adj_mines)
        else:
            return visible_chars[self.state]
