import pygame
from load_image import load_image
from constants import *


class Fireball(pygame.sprite.Sprite):
    def __init__(self, x, y, dx, dy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.smoothscale(load_image('fireball.png').convert_alpha(), (20, 20))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 400 / FPS
        self.pos = pygame.math.Vector2(x, y)
        self.dir = pygame.math.Vector2(dx, dy).normalize()

    def update(self):
        self.pos += self.dir * self.speed
        self.rect.center = (round(self.pos.x), round(self.pos.y))
        if not self.rect.colliderect(0, 0, WINDOW_HEIGHT, WINDOW_WIGHT):
            self.kill()
