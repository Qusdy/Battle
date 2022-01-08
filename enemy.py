from animated_sprite import AnimatedSprite
from bullet import Bullet
from constants import *
from groups import enemy_group, bullets, all_sprites, articles_of_magic
from load_image import load_image
from random import randrange, uniform, choice
from wizard import wizard
import pygame
from enemy_particles import Particle
from particles_of_magic import Particles_of_magic


class Enemy(AnimatedSprite):
    def __init__(self, sheet, colums, rows):
        sheet = pygame.transform.scale(sheet, (sheet.get_width() * 3, sheet.get_height() * 3))
        self.speed = uniform(10, ENEMY_SPEED)
        x, y = self.get_coord()
        super(Enemy, self).__init__(sheet, colums, rows, x, y)
        self.run = []
        self.action = 100
        for i in self.frames[WALK_FRAMES_IND[0]:WALK_FRAMES_IND[1]]:
            for j in range(5):
                self.run.append(i)
        self.stand = []
        for i in self.frames[STAND_IND[0]:STAND_IND[1]]:
            for j in range(5):
                self.stand.append(i)
        self.damage = []
        for i in self.frames[DAMAGE_IND[0]:DAMAGE_IND[1]]:
            for j in range(10):
                self.damage.append(i)
        self.shoot_distance = ENEMY_SHOOT_DISTANCE + randrange(-20, 20)
        self.bullet = Bullet(self.rect.centerx, self.rect.centery, self.get_vector().rotate(randrange(-10, 10)), True)
        self.running = False
        self.clock = pygame.time.Clock()
        self.time = 0
        self.health = 100
        self.enemy_damage = 0
        self.frieze = False
        self.sideway = False
        self.combustion = False
        self.enemy_have_damage = False
        self.damage_time = 0
        self.shoot_time = 0
        self.frieze_time = 0
        self.combustion_time = 0
        self.death_time = 0

    def update(self, **kwargs):
        if self.distance_to_wizard() >= self.shoot_distance:
            self.running = True
            self.death_time += 1
            self.sideway = False
        else:
            self.death_time = 0
            self.running = False
            if self.action <= 0:
                if self.sideway:
                    self.sideway = False
                    self.action = 100
                else:
                    self.sideway = True
                    self.action = 50
                    self.get_vector_movement()
            else:
                self.action -= 1
        self.time += self.clock.tick()
        if self.sideway and not self.running:
            self.sideways_movement()
            self.running_animation()
        if self.time >= 1500 and not self.running:
            self.time = 0
            self.shoot()
        if self.enemy_have_damage:
            self.damage_animation()
            self.damage_time += 1
            if self.damage_time >= 15:
                self.enemy_have_damage = False
                self.damage_time = 0
        elif self.running:
            self.move()
            self.running_animation()
        else:
            self.stand_animation()
        if self.health <= 0:
            self.dead_animation()
        if self.frieze and self.frieze_time >= 80:
            self.frieze = False
            self.frieze_time = 0
            self.speed += (ENEMY_SPEED / FPS) / 3
        if self.combustion and self.combustion_time >= 80:
            self.combustion = False
            self.combustion_time = 0
        if self.frieze:
            self.friezing()
        if self.combustion:
            self.combustion_is()
        if self.death_time >= 20:
            font = pygame.font.Font(None, 50)
            text = font.render("Терористы уходят! за ними", True, (255, 0, 0))
            SCREEN.blit(text, (wizard.rect.centerx, wizard.rect.y - 20))

    def in_sprite(self, pos):
        if self.rect.x <= pos[0] <= self.rect.x + self.rect.width:
            if self.rect.y <= pos[1] <= self.rect.y + self.rect.height:
                return True
        return False

    def friezing(self):
        self.frieze_time += 1
        if self.frieze_time % 2 == 0:
            speed = range(-5, 6)
            particle = Particle(self, load_image('0_ieKzfwSzaqG57--2.png'), 1, 1,
                                self.rect.x, self.rect.y, 1, choice(speed), choice(speed))
            articles_of_magic.add(particle)
            all_sprites.add(particle)

    def combustion_is(self):
        self.combustion_time += 1
        self.health -= 0.05
        if self.combustion_time % 2 == 0:
            speed = range(-5, 6)
            particle = Particle(self, load_image('0_ieKzfwSzaqG57--3.png'), 1, 1,
                                self.rect.x, self.rect.y, 1, choice(speed), choice(speed))
            articles_of_magic.add(particle)
            all_sprites.add(particle)

    def dead_animation(self):
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

    def damage_animation(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.damage)
        self.rotate(self.damage)

    def get_coord(self):
        x, y = randrange(0, LEVEL_HEIGHT), randrange(0, LEVEL_WIGHT)
        return x, y

    def move(self):
        vector = self.get_vector()
        self.rect.x += vector[0] * self.speed
        self.rect.y += vector[1] * self.speed

    def shoot(self):
        self.bullet = Bullet(self.rect.centerx, self.rect.centery, self.get_vector().rotate(randrange(-10, 10)))

    def get_vector(self):
        return pygame.math.Vector2(wizard.rect.centerx - self.rect.centerx,
                                   wizard.rect.centery - self.rect.centery).normalize()

    def have_damage(self, damage):
        self.enemy_have_damage = True
        self.enemy_damage = damage
        self.health -= self.enemy_damage

    def get_vector_movement(self):
        self.vector_move = pygame.math.Vector2(randrange(wizard.rect.centerx + self.shoot_distance,
                                                         wizard.rect.centerx - self.shoot_distance,
                                                         -1) * choice([-1, 1]),
                                               randrange(wizard.rect.centery + self.shoot_distance,
                                                         wizard.rect.centery - self.shoot_distance,
                                                         -1) * choice([-1, 1])).normalize()

    def sideways_movement(self):
        self.rect.x += self.vector_move[0] * self.speed
        self.rect.y += self.vector_move[1] * self.speed


class Enemy_bomber(Enemy):
    def __init__(self, sheet, colums, rows):
        sheet = pygame.transform.scale(sheet, (sheet.get_width() * 3, sheet.get_height() * 3))
        self.speed = uniform(10.5, ENEMY_SPEED + 0.5)
        x, y = self.get_coord()
        super(Enemy, self).__init__(sheet, colums, rows, x, y)
        self.run = []
        self.action = 100
        for i in self.frames[RUN_FRAME_IND[0]:RUN_FRAME_IND[1]]:
            for j in range(5):
                self.run.append(i)
        self.damage = []
        for i in self.frames[DAMAGE_IND[0]:DAMAGE_IND[1]]:
            for j in range(10):
                self.damage.append(i)
        self.running = False
        self.health = 20
        self.enemy_damage = 0
        self.frieze = False
        self.combustion = False
        self.enemy_have_damage = False
        self.damage_time = 0
        self.shoot_time = 0
        self.frieze_time = 0
        self.combustion_time = 0

    def update(self, **kwargs):
        if self.health <= 0:
            self.dead_animation()
        if self.distance_to_wizard() > 0:
            self.move()
            self.running_animation()
        else:
            wizard.health -= 30
            Boom_Funk(self)
            self.kill()
        if self.enemy_have_damage:
            self.damage_animation()
            self.damage_time += 1
            if self.damage_time >= 15:
                self.enemy_have_damage = False
                self.damage_time = 0
        if self.frieze and self.frieze_time >= 80:
            self.frieze = False
            self.frieze_time = 0
            self.speed += (ENEMY_SPEED / FPS) / 3
        if self.combustion and self.combustion_time >= 80:
            self.combustion = False
            self.combustion_time = 0
        if self.frieze:
            self.friezing()
        if self.combustion:
            self.combustion_is()


enemy_bots = [Enemy(load_image("DinoSprites-enemy.png"), 24, 1), Enemy(load_image("DinoSprites-enemy.png"), 24, 1),
              Enemy(load_image("DinoSprites-enemy.png"), 24, 1), Enemy(load_image("DinoSprites-enemy.png"), 24, 1),
              Enemy(load_image("DinoSprites-enemy.png"), 24, 1), Enemy(load_image("DinoSprites-enemy.png"), 24, 1),
              Enemy(load_image("DinoSprites-enemy.png"), 24, 1), Enemy(load_image("DinoSprites-enemy.png"), 24, 1),
              Enemy_bomber(load_image("DinoSprites-enemy.png"), 24, 1),
              Enemy_bomber(load_image("DinoSprites-enemy.png"), 24, 1),
              Enemy_bomber(load_image("DinoSprites-enemy.png"), 24, 1)]

for enemy in enemy_bots:
    enemy_group.add(enemy)
