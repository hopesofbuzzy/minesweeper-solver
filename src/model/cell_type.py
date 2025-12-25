from enum import Enum


class VCellType(Enum):
    CLOSED = 0
    OPENED = 1
    FLAGGED = 2


class RCellType(Enum):
    SAFE = 0
    BOMBED = 1
