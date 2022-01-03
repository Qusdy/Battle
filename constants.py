import pygame
from load_image import load_image
import math
# PLAYER_SPEED = 16
FPS = 60
SPEED = 600 / FPS
ENEMY_SPEED = 580 / FPS
BULLET_SPEED = 700 / FPS
BULLET_SIZE = (30, 30)
ENEMY_SHOOT_DISTANCE = 250
LEVEL_HEIGHT = LEVEL_WIGHT = 32 * 100
SIZE = WINDOW_HEIGHT, WINDOW_WIGHT = 800, 800
clock = pygame.time.Clock()
WALK_FRAMES_IND = (4, 10)
STAND_IND = (0, 4)
ATTACK_FRAMES_IND = (11, 14)
DINO_HEALBAR = 15
SCREEN = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Батл-рояль')
level = []
GRASS = "0"
TREE = "I"
WALL = "W"
TWO_MUSHROOMS = "M"
ONE_MUSHROOM = "m"
TITLE_SHEET = load_image("title_sheet.png")

FONT_SIZE_PARAM = 30

BTN_SIZE = (200, 100)
SIGHT = '*'
