import pygame
from constants import ENEMY_SHOOT_DISTANCE, BULLET_SPEED, BULLET_SIZE, BULLET_DAMAGE
from groups import *
from load_image import load_image
from wizard import wizard


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x1, y1, vector, dead=False):
        super().__init__()
        self.x1 = x1
        self.y1 = y1
        self.dx, self.dy = vector[0], vector[1]
        self.distance = 0
        self.dead = dead
        self.image = pygame.transform.scale(load_image('bullet.png', -1), BULLET_SIZE)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x1, y1
        direction = pygame.math.Vector2(vector)
        angle = direction.angle_to((0, -1))
        self.image = pygame.transform.rotate(self.image, angle)
        bullets_group.add(self)
        all_sprites.add(self)

    def update(self):
        self.rect.x += self.dx * BULLET_SPEED
        self.rect.y += self.dy * BULLET_SPEED
        if pygame.sprite.spritecollideany(self, forest_group):
            self.kill()
        if ((self.rect.x - self.x1) ** 2 + (self.rect.y - self.y1) ** 2) ** 0.5 >= ENEMY_SHOOT_DISTANCE or pygame.sprite.spritecollideany(self, player_group):
            self.dead = True
            if pygame.sprite.spritecollideany(self, player_group):
                wizard.health -= BULLET_DAMAGE
                wizard.is_shaking = True
                if wizard.health <= 0:
                    wizard.health = 0
            self.kill()
