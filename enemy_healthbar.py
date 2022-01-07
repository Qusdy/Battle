from constants import *
import pygame


def draw_enemy_healthbar(health):
    if health > 0:
        pygame.draw.rect(SCREEN, '#7147D7', (ENEMY_HB_POS_X, ENEMY_HB_POS_Y, ENEMY_HB_WIDTH, ENEMY_HB_HEIGHT), border_radius=50)
        font1 = pygame.font.Font('data/Font.ttf', 35)
        font2 = pygame.font.Font('data/Font.ttf', 60)
        text = font1.render('У этого врага:', True, 'white')
        text1 = font2.render(str(int(health)), True, 'red')
        SCREEN.blit(text, (490, 10))
        SCREEN.blit(text1, (600, 50))