from src.model.cell_type import VCellType, RCellType

vicon = {
    VCellType.CLOSED: "?",
    VCellType.OPENED: "",
    VCellType.FLAGGED: "!"
}

ricon = {
    RCellType.SAFE: "0",
    RCellType.BOMBED: "*"
}


class Cell:
    def __init__(self, vtype=VCellType.CLOSED, rtype=RCellType.SAFE):
        self.vtype = vtype  # Видимый тип
        self.rtype = rtype  # Реальный тип
        self.value = 0

    def open(self):
        self.vtype = VCellType.OPENED

    def is_opened(self):
        return self.vtype == VCellType.OPENED

    def is_bombed(self):
        return self.rtype == RCellType.BOMBED

    def __str__(self):
        return self.show()

    def show(self, real=False):
        if real:
            return ricon[self.rtype]
        else:
            if self.vtype is VCellType.OPENED:
                return str(self.value)
            else:
                return vicon[self.vtype]
            
