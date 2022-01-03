from animated_sprite import AnimatedSprite
from bullet import Bullet
from constants import *
from groups import enemy_group
from load_image import load_image
from random import randrange, uniform, randint
from wizard import wizard
import pygame


class Enemy(AnimatedSprite):
    def __init__(self, sheet, colums, rows):
        sheet = pygame.transform.scale(sheet, (sheet.get_width() * 3, sheet.get_height() * 3))
        self.speed = randint(2, SPEED)
        x, y = self.get_coord()
        super(Enemy, self).__init__(sheet, colums, rows, x, y)
        self.run = []
        for i in self.frames[WALK_FRAMES_IND[0]:WALK_FRAMES_IND[1]]:
            for j in range(5):
                self.run.append(i)
        self.stand = []
        for i in self.frames[STAND_IND[0]:STAND_IND[1]]:
            for j in range(5):
                self.stand.append(i)
        self.running = False
        self.bullet = False

    def update(self):
        if self.distance_to_wizard():
            self.move()
            self.running = True
        else:
            self.running = False
        if not self.running:
            self.stand_animation()
            if (not self.bullet) or self.bullet.dead:
                self.shoot()
        else:
            self.running_animation()
        if self.bullet:
            self.shoot_animation()

    def distance_to_wizard(self):
        # Проверка расстояния до нашего игрока
        if self.get_distance() >= ENEMY_SHOOT_DISTANCE:
            return True
        return False

    def move(self):
        dx, dy = self.get_vector()
        self.rect.x += dx * ENEMY_SPEED
        self.rect.y += dy * ENEMY_SPEED

    def get_vector(self):
        dx = wizard.rect.x - self.rect.x
        dy = wizard.rect.y - self.rect.y
        dx /= self.get_distance()
        dy /= self.get_distance()
        return dx, dy

    def get_distance(self):
        return ((wizard.rect.x - self.rect.x) ** 2 + (wizard.rect.y - self.rect.y) ** 2) ** 0.5

    def stand_animation(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.stand)
        self.rotate(self.stand)

    def rotate(self, list_of_animation):
        if wizard.rect.x > self.rect.x:
            self.image = list_of_animation[self.cur_frame]
        else:
            self.image = pygame.transform.flip(list_of_animation[self.cur_frame], True, False)

    def running_animation(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.run)
        self.rotate(self.run)

    def get_coord(self):
        x, y = randrange(1000, 1500), randrange(1000, 1500)
        return x, y

    def shoot(self):
        dx, dy = self.get_vector()
        self.bullet = Bullet(self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height // 2,
                             (dx + uniform(-0.35, 0.35), dy + uniform(-0.35, 0.35)))

    def shoot_animation(self):
        self.bullet.move()
        self.bullet.check_distance()


enemy_bots = [Enemy(load_image("DinoSprites-enemy.png"), 24, 1)]

for enemy in enemy_bots:
    enemy_group.add(enemy)