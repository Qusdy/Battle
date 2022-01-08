import pygame
from load_image import load_image
from constants import *
from random import choice
from groups import bullets, enemy_group, forest_group, all_sprites, articles_of_magic
from particles_of_magic import *


def rotate(self):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
    angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
    self.image = pygame.transform.rotate(self.image, int(angle))
    self.rect = self.image.get_rect(center=self.position)


class Fireball(pygame.sprite.Sprite):
    def __init__(self, x, y, dx, dy):
        pygame.sprite.Sprite.__init__(self)
        SOUND_SHOOT.play()
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
        self.combustion = [True, False]
        bullets.add(self)

    def update(self, camera=(0, 0)):
        self.pos.x += (self.dir.x * self.speed) + camera[0]
        self.pos.y += (self.dir.y * self.speed) + camera[1]
        self.rect.center = (self.pos.x, self.pos.y)
        particle = Particles_of_magic(self, load_image('Smoke & Fire_0.png'), 4, 2, self.rect.centerx, self.rect.y, 1,
                                      (20, 20))
        articles_of_magic.add(particle)
        all_sprites.add(particle)
        if not self.rect.colliderect(0, 0, WINDOW_HEIGHT, WINDOW_WIGHT):
            self.kill()
        if pygame.sprite.spritecollideany(self, enemy_group):
            for enemy in enemy_group:
                if pygame.sprite.spritecollideany(enemy, bullets):
                    enemy.have_damage(10)
                    SOUND_BOOM.play()
                    Boom_Funk(self)
                    if not enemy.combustion and choice(self.combustion):
                        enemy.combustion = True
                    self.kill()
        if pygame.sprite.spritecollideany(self, forest_group):
            SOUND_BOOM.play()
            Boom_Funk(self)
            self.kill()


class Ice_dart(pygame.sprite.Sprite):
    def __init__(self, x, y, dx, dy):
        pygame.sprite.Sprite.__init__(self)
        SOUND_SHOOT.play()
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.original_image = load_image('hadouken-all-you-can.png')
        self.position = (x, y)
        self.image = pygame.transform.smoothscale(self.original_image.convert_alpha(), (20, 20))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = ICE['speed']
        self.pos = pygame.math.Vector2(self.x, self.y)
        self.dir = pygame.math.Vector2(self.dx, self.dy).normalize()
        self.frize = [True, False, False, False]
        bullets.add(self)
        rotate_Funk(self)

    def update(self, camera=(0, 0)):
        particle = Particles_of_magic(self, load_image('kisspng-rpg-maker-vx-rpg-maker-mv-animated-film-role-playi'
                                                       '-5b329b11993981.2440375915300431536276.png'), 5, 2,
                                      self.rect.x, self.rect.y, 1,
                                      (30, 30))
        articles_of_magic.add(particle)
        all_sprites.add(particle)
        self.pos.x += (self.dir.x * self.speed) + camera[0]
        self.pos.y += (self.dir.y * self.speed) + camera[1]
        self.rect.center = (self.pos.x, self.pos.y)
        if not self.rect.colliderect(0, 0, WINDOW_HEIGHT, WINDOW_WIGHT):
            self.kill()
        if pygame.sprite.spritecollideany(self, enemy_group):
            for enemy in enemy_group:
                if pygame.sprite.spritecollideany(enemy, bullets):
                    enemy.have_damage(5)
                    if not enemy.frieze and choice(self.frize):
                        enemy.frieze = True
                        enemy.speed -= (ENEMY_SPEED / FPS) / 3
                    self.kill()
        if pygame.sprite.spritecollideany(self, forest_group):
            self.kill()


class SnowBall(pygame.sprite.Sprite):
    def __init__(self, x, y, dx, dy):
        pygame.sprite.Sprite.__init__(self)
        SOUND_SHOOT.play()
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.original_image = load_image('hadouken-all-you-can.png')
        self.position = (x, y)
        self.image = pygame.transform.smoothscale(self.original_image.convert_alpha(), (20, 20))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = SNOWBALL['speed']
        self.pos = pygame.math.Vector2(self.x, self.y)
        self.dir = pygame.math.Vector2(self.dx, self.dy).normalize()
        bullets.add(self)
        rotate(self)

    def update(self, camera=(0, 0)):
        print(123)
        # particle = Particles_of_magic(load_image('kisspng-rpg-maker-vx-rpg-maker-mv-animated-film-role-playi'
        #                                          '-5b329b11993981.2440375915300431536276.png'), 5, 2,
        #                               self.rect.x, self.rect.y, 1,
        #                               (30, 30))
        # articles_of_magic.add(particle)
        # all_sprites.add(particle)
        self.pos.x += (self.dir.x * self.speed) + camera[0]
        self.pos.y += (self.dir.y * self.speed) + camera[1]
        self.rect.center = (self.pos.x, self.pos.y)
        if not self.rect.colliderect(0, 0, WINDOW_HEIGHT, WINDOW_WIGHT):
            self.kill()
        if pygame.sprite.spritecollideany(self, enemy_group):
            for enemy in enemy_group:
                if pygame.sprite.spritecollideany(enemy, bullets):
                    enemy.have_damage(1)
                    enemy.speed -= 0.5
                    self.kill()
        if pygame.sprite.spritecollideany(self, forest_group):
            self.kill()