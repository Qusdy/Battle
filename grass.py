from base_floor import BaseFloor
from constants import TITLE_SHEET


class Grass(BaseFloor):
    image = TITLE_SHEET.subsurface((0, 64, 32, 32))

    def __init__(self, pos, *group):
        super().__init__(pos, *group)
        self.image = Grass.image
