import pygame


class BaseFloor(pygame.sprite.Sprite):
    def __init__(self, pos, *group):
        super().__init__(*group)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
