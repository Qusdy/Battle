import pygame
from constants import ENEMY_SHOOT_DISTANCE, BULLET_SPEED, BULLET_SIZE
from groups import bullets_group
from load_image import load_image


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x1, y1, vector):
        super().__init__()
        self.x1 = x1
        self.y1 = y1
        self.dx, self.dy = vector
        self.image = pygame.transform.scale(load_image('bullet.png', -1), BULLET_SIZE)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x1, y1
        direction = pygame.math.Vector2(vector)
        angle = direction.angle_to((0, -1))
        print(angle)
        self.image = pygame.transform.rotate(self.image, angle)
        self.distance = 0
        self.dead = False
        bullets_group.add(self)

    def move(self):

        self.rect.x += self.dx * BULLET_SPEED
        self.rect.y += self.dy * BULLET_SPEED



        self.distance += ((self.dx * BULLET_SPEED) ** 2 + (self.dy * BULLET_SPEED) ** 2) ** 0.5

    def check_distance(self):
        if self.distance >= ENEMY_SHOOT_DISTANCE:
            self.dead = True
            bullets_group.remove(self)