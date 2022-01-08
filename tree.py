from base_floor import BaseFloor
from constants import *


class Tree(BaseFloor):
    def __init__(self, pos, *group):
        self.image = TITLE_SHEET.season.subsurface((0, 0, 32, 64))
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.rect.height -= 10
        super().__init__(pos, *group)

    def draw_rect(self):
        pygame.draw.rect(SCREEN, "red", self.rect)
