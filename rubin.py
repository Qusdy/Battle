from cut_title_sheet import cut_title_sheet
from load_image import load_image
import pygame


class Rubin(pygame.sprite.Sprite):
    image = cut_title_sheet(load_image("resources_basic.png"), 11, 11, 0, 2)

    def __init__(self, pos, *group):
        super().__init__(*group)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.image = pygame.transform.scale(Rubin.image, (self.image.get_width() * 2, self.image.get_height() * 2))

