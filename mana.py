import pygame
from load_image import load_image


class Mana(pygame.sprite.Sprite):
    image = load_image("mana.png")

    def __init__(self, pos, *group):
        super().__init__(*group)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.image = pygame.transform.scale(Mana.image, (self.image.get_width() * 2, self.image.get_height() * 2))

