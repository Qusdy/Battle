import pygame
from load_image import load_image
from cut_title_sheet import cut_title_sheet
import math
# PLAYER_SPEED = 16
FPS = 60
SPEED = 600 / FPS
ENEMY_SPEED = 580 / FPS
BULLET_SPEED = 700 / FPS
BULLET_SIZE = (50, 50)
BULLET_DAMAGE = 5
ENEMY_SHOOT_DISTANCE = 400
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


FIREBALL = {
    "class": None,
    "name": "Огненный шар ",
    "damage": 20,
    "speed": 1200 / FPS
}

ICE = {
    "class": None,
    "name": "Ледяной шип ",
    "damage": 5,
    "speed": 1200 / FPS
}

img_fireball = cut_title_sheet(load_image("resources_basic.png"), 11, 11, 0, 2)
img_ice_dart = cut_title_sheet(load_image("resources_basic.png"), 11, 11, 2, 2)
CRYSTALS = {
    "fireball": pygame.transform.scale(img_fireball, (img_fireball.get_width() * 2, img_fireball.get_height() * 2)),
    'ice_dart': pygame.transform.scale(img_ice_dart, (img_ice_dart.get_width() * 2, img_ice_dart.get_height() * 2))
}
