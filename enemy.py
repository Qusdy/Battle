from animated_sprite import AnimatedSprite
from bullet import Bullet
from constants import *
from groups import enemy_group, bullets, all_sprites
from load_image import load_image
from random import randrange, uniform
from wizard import wizard
import pygame


class Enemy(AnimatedSprite):
    def __init__(self, sheet, colums, rows):
        sheet = pygame.transform.scale(sheet, (sheet.get_width() * 3, sheet.get_height() * 3))
        self.speed = uniform(10, ENEMY_SPEED)
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
        self.shoot_distance = ENEMY_SHOOT_DISTANCE + randrange(-20, 20)
        self.bullet = Bullet(self.rect.centerx, self.rect.centery, self.get_vector().rotate(randrange(-10, 10)), True)
        self.running = False
        self.clock = pygame.time.Clock()
        self.time = 0
        self.health = 50

    def update(self):
        if self.distance_to_wizard() >= self.shoot_distance:
            self.running = True
        else:
            self.running = False
        if self.running:
            self.move()
            self.running_animation()
        else:
            self.time += self.clock.tick()
            if self.bullet.dead and self.time >= 1500:
                self.time = 0
                self.shoot()
            self.stand_animation()
        if self.health <= 0:
            self.dead_animation()

    def in_sprite(self, pos):
        if self.rect.x <= pos[0] <= self.rect.x + self.rect.width:
            if self.rect.y <= pos[1] <= self.rect.y + self.rect.height:
                return True
        return False

    def dead_animation(self):
        self.speed = 0
        self.kill()

    def distance_to_wizard(self):
        return ((self.rect.centerx - wizard.rect.centerx) ** 2 + (self.rect.centery - wizard.rect.centery) ** 2) ** 0.5

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
        x, y = randrange(600, 2000), randrange(600, 2000)
        return x, y

    def move(self):
        vector = self.get_vector()
        self.rect.x += vector[0] * self.speed
        self.rect.y += vector[1] * self.speed

    def shoot(self):
        self.bullet = Bullet(self.rect.centerx, self.rect.centery, self.get_vector().rotate(randrange(-10, 10)))

    def get_vector(self):
        return pygame.math.Vector2(wizard.rect.centerx - self.rect.centerx, wizard.rect.centery - self.rect.centery).normalize()

    def have_damage(self, damage):
        # if pygame.sprite.spritecollideany(self, bullets):
        self.health -= damage


enemy_bots = [Enemy(load_image("DinoSprites-enemy.png"), 24, 1), Enemy(load_image("DinoSprites-enemy.png"), 24, 1),
              Enemy(load_image("DinoSprites-enemy.png"), 24, 1), Enemy(load_image("DinoSprites-enemy.png"), 24, 1),
              Enemy(load_image("DinoSprites-enemy.png"), 24, 1), Enemy(load_image("DinoSprites-enemy.png"), 24, 1)]

for enemy in enemy_bots:
    enemy_group.add(enemy)
