import pygame
from load_image import load_image
from constants import *
from groups import bullets, enemy_group, forest_group, all_sprites, articles_of_magic
from particles_of_magic import Particles_of_magic


def Boom(obj):
    particle = Particles_of_magic(load_image('Boom.png'), 4, 2, obj.rect.centerx, obj.rect.centery, 3, (80, 80))
    articles_of_magic.add(particle)


def rotate(self):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
    angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
    self.image = pygame.transform.rotate(self.original_image, int(angle))
    self.rect = self.image.get_rect(center=self.position)


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
        particle = Particles_of_magic(load_image('Smoke & Fire_0.png'), 4, 2, self.rect.centerx, self.rect.y, 1, (20, 20))
        articles_of_magic.add(particle)
        all_sprites.add(particle)
        if not self.rect.colliderect(0, 0, WINDOW_HEIGHT, WINDOW_WIGHT):
            self.kill()
        if pygame.sprite.spritecollideany(self, enemy_group):
            for enemy in enemy_group:
                if pygame.sprite.spritecollideany(enemy, bullets):
                    enemy.have_damage(10)
                    Boom(self)
                    self.kill()
        if pygame.sprite.spritecollideany(self, forest_group):
            Boom(self)
            self.kill()


class Ice_dart(pygame.sprite.Sprite):
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
        particle = Particles_of_magic(load_image('Smoke & Fire_0.png'), 4, 2, self.rect.centerx, self.rect.y, 1, (20, 20))
        articles_of_magic.add(particle)
        all_sprites.add(particle)
        if not self.rect.colliderect(0, 0, WINDOW_HEIGHT, WINDOW_WIGHT):
            self.kill()
        if pygame.sprite.spritecollideany(self, enemy_group):
            for enemy in enemy_group:
                if pygame.sprite.spritecollideany(enemy, bullets):
                    enemy.have_damage(10)
                    Boom(self)
                    self.kill()
        if pygame.sprite.spritecollideany(self, forest_group):
            Boom(self)
            self.kill()
