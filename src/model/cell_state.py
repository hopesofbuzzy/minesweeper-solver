from enum import Enum


class CellState(Enum):
    CLOSED = 0
    OPENED = 1
    FLAGGED = 2
