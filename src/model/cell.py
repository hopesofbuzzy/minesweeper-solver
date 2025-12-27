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
    def __init__(self, row, col, state=CellState.CLOSED, is_mine=False):
        self.row = row
        self.col = col
        self._state = state
        self._is_mine = is_mine
        self._adj_mines = 0  # Число клетки

    def open(self) -> bool:
        if self._state == CellState.OPENED:
            logging.error("Клетка уже открыта!")
            return False
        self._state = CellState.OPENED
        return True

    def flag(self) -> bool:
        if self._state == CellState.CLOSED:
            self._state = CellState.FLAGGED
            return True
        else:
            logging.error("Открытую или помеченную клетку нельзя пометить!")
            return False

    @property
    def is_opened(self) -> bool:
        return self._state == CellState.OPENED

    @property
    def is_closed(self) -> bool:
        return self._state == CellState.CLOSED

    @property
    def is_flagged(self) -> bool:
        return self._state == CellState.FLAGGED

    @property
    def adj_mines(self) -> int:
        return self._adj_mines

    def truth_char(self) -> str:
        if self._is_mine:
            return truth_chars[self._is_mine]
        else:
            return str(self._adj_mines)

    def visible_char(self) -> str:
        if self._state is CellState.OPENED:
            return str(self._adj_mines)
        else:
            return visible_chars[self._state]
