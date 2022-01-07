from base_floor import BaseFloor
from constants import TITLE_SHEET
import pygame
from random import randrange


class TwoMushrooms(BaseFloor):

    def __init__(self, pos, *group):
        self.image = TITLE_SHEET.season.subsurface((3 * 32, 32, 32, 32))
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_width() * 2, self.image.get_height() * 2))
        super().__init__(pos, *group)


class OneMushroom(BaseFloor):

    def __init__(self, pos, *group):
        self.image = TITLE_SHEET.season.subsurface((3 * 32, 0, 32, 32))
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_width() * 2, self.image.get_height() * 2))
        super().__init__(pos, *group)