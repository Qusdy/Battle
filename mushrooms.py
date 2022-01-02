from base_floor import BaseFloor
from constants import TITLE_SHEET
import pygame
from random import randrange


class TwoMushrooms(BaseFloor):
    image = TITLE_SHEET.subsurface((3 * 32, 32, 32, 32))

    def __init__(self, pos, *group):
        super().__init__(pos, *group)
        self.image = pygame.transform.scale(TwoMushrooms.image,
                                            (TwoMushrooms.image.get_width() * 2, TwoMushrooms.image.get_height() * 2))


class OneMushroom(BaseFloor):
    image = TITLE_SHEET.subsurface((3 * 32, 0, 32, 32))

    def __init__(self, pos, *group):
        super().__init__(pos, *group)
        self.image = pygame.transform.scale(OneMushroom.image,
                                            (OneMushroom.image.get_width() * 2, OneMushroom.image.get_height() * 2))