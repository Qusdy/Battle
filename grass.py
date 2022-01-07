from base_floor import BaseFloor
from constants import TITLE_SHEET


class Grass(BaseFloor):
    def __init__(self, pos, *group):
        self.image = TITLE_SHEET.season.subsurface((0, 64, 32, 32))
        super().__init__(pos, *group)
