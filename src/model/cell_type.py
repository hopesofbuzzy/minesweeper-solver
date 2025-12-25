from enum import Enum


class VCellType(Enum):
    CLOSED = 1
    FLAGGED = 2


class RCellType(Enum):
    FREE = 1
    BOMBED = 2
