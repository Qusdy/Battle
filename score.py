from constants import *
import pygame


def draw_score(score, season):
    font = pygame.font.Font('data/Font.ttf', 40)
    if season == WINTER:
        text = font.render('Ты победил ' + str(score), True, 'black')
    else:
        text = font.render('Ты победил ' + str(score), True, 'white')
    SCREEN.blit(text, (475, 700))