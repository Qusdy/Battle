import pygame
from load_image import load_image
import math
# PLAYER_SPEED = 16
FPS = 60
SPEED = 400 / FPS
ENEMY_SPEED = 380 / FPS
BULLET_SPEED = 500 / FPS
BULLET_SIZE = (20, 20)
ENEMY_SHOOT_DISTANCE = 250
LEVEL_HEIGHT = LEVEL_WIGHT = 1024
SIZE = WINDOW_HEIGHT, WINDOW_WIGHT = 800, 800
clock = pygame.time.Clock()
WALK_FRAMES_IND = (4, 10)
STAND_IND = (0, 4)
ATTACK_FRAMES_IND = (11, 14)
DINO_HEALBAR = 15
SCREEN = pygame.display.set_mode(SIZE)
level = []
GRASS = "0"
TREE = "I"
WALL = "W"
TWO_MUSHROOMS = "M"
ONE_MUSHROOM = "m"
TITLE_SHEET = load_image("title_sheet.png")

BTN_SIZE = (200, 100)