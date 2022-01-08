import pygame
from constants import *


def draw_lives(xp, winter=False):
    margin_top = 10
    font = pygame.font.Font("data/Font.ttf", FONT_SIZE_PARAM)

    pygame.draw.rect(SCREEN, color="red", rect=(45, margin_top, 200 * (xp / 100), 30),
                     border_radius=10)
    if winter:

        pygame.draw.rect(SCREEN, color="white", rect=(45, margin_top, 200, 30), border_radius=10)
        pygame.draw.rect(SCREEN, color="black", width=5, rect=(45, margin_top, 200, 30), border_radius=10)
        text = font.render(str(xp), False, "black")
    else:
        pygame.draw.rect(SCREEN, color="white", width=5, rect=(45, margin_top, 200, 30), border_radius=10)
        text = font.render(str(xp), False, "white")

    SCREEN.blit(text, ((45 + 200 // 2) - text.get_width() // 2, margin_top + 1))
    heart = load_image("heart.png")
    SCREEN.blit(heart, (10, margin_top, 32, 32))


def draw_mana(mana, winter=False):
    margin_top = 50
    font = pygame.font.Font("data/Font.ttf", FONT_SIZE_PARAM)

    pygame.draw.rect(SCREEN, color="blue", rect=(45, margin_top, 200 * (mana / 100), 30),
                     border_radius=10)
    if winter:
        pygame.draw.rect(SCREEN, color="white", rect=(45, margin_top, 200, 30), border_radius=10)
        pygame.draw.rect(SCREEN, color="black", width=5, rect=(45, margin_top, 200, 30), border_radius=10)
        text = font.render(str(mana), False, "black")

    else:
        pygame.draw.rect(SCREEN, color="white", width=5, rect=(45, margin_top, 200, 30), border_radius=10)

        text = font.render(str(mana), False, "white")

    SCREEN.blit(text, ((45 + 200 // 2) - text.get_width() // 2, margin_top + 1))
    mana_im = load_image("mana.png")
    mana_im = pygame.transform.scale(mana_im, (mana_im.get_width() * 4, mana_im.get_height() * 4))
    SCREEN.blit(mana_im, (10, margin_top, 32, 32))