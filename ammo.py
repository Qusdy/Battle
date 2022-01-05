import pygame
from load_image import load_image
from constants import *
from groups import bullets, enemy_group, forest_group


class Fireball(pygame.sprite.Sprite):
    def __init__(self, x, y, dx, dy):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.image = pygame.transform.smoothscale(load_image('fireball.png').convert_alpha(), (20, 20))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = FIREBALL['speed']
        self.pos = pygame.math.Vector2(self.x, self.y)
        self.dir = pygame.math.Vector2(self.dx, self.dy).normalize()
        bullets.add(self)

    def update(self, camera=(0, 0)):
        self.pos.x += (self.dir.x * self.speed) + camera[0]
        self.pos.y += (self.dir.y * self.speed) + camera[1]
        self.rect.center = (self.pos.x, self.pos.y)
        if not self.rect.colliderect(0, 0, WINDOW_HEIGHT, WINDOW_WIGHT):
            self.kill()
        if pygame.sprite.spritecollideany(self, enemy_group):
            for enemy in enemy_group:
                if pygame.sprite.spritecollideany(enemy, bullets):
                    enemy.have_damage()
                    self.kill()
        if pygame.sprite.spritecollideany(self, forest_group):
            self.kill()
