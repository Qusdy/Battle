from cut_title_sheet import cut_title_sheet
from load_image import load_image
from wizard import wizard
from groups import player_group
from constants import SCREEN
import pygame


class BaseCrystal(pygame.sprite.Sprite):
    image = cut_title_sheet(load_image("resources_basic.png"), 11, 11, 0, 3)

    def __init__(self, pos, *group):
        super().__init__(*group)
        self.spell = ''
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))

    def update(self, *args):
        if pygame.sprite.spritecollideany(self, player_group):
            font = pygame.font.Font(None, 50)
            text = font.render("E", True, (100, 255, 100))
            SCREEN.blit(text, (self.rect.centerx, self.rect.y - 20))
            if args and args[0].key == pygame.K_e and self.spell \
                    not in wizard.spells and len(wizard.spells) < 3:
                wizard.new_spell(self.spell)
                self.kill()
