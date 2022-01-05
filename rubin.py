from cut_title_sheet import cut_title_sheet
from load_image import load_image
import pygame
from constants import *
from groups import *
from wizard import wizard


class Rubin(pygame.sprite.Sprite):
    image = cut_title_sheet(load_image("resources_basic.png"), 11, 11, 0, 2)

    def __init__(self, pos):
        super().__init__(all_sprites)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.image = pygame.transform.scale(Rubin.image, (self.image.get_width() * 2, self.image.get_height() * 2))
        self.add(rubins_group)

    def update(self, *args):
        if pygame.sprite.spritecollideany(self, player_group):
            font = pygame.font.Font(None, 50)
            text = font.render("E", True, (100, 255, 100))
            SCREEN.blit(text, (self.rect.centerx, self.rect.y - 20))
            if args and args[0].key == pygame.K_e:
                wizard.new_spell('fireball')
                self.kill()
