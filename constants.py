import pygame
from load_image import load_image
from cut_title_sheet import cut_title_sheet
import math
pygame.init()


class Season:
    def __init__(self):
        self.season = None

    def overwrite(self, season):
        self.season = season


pygame.mixer.music.load('data/game_theme.mp3')
pygame.mixer.music.set_volume(50)
pygame.mixer.music.play(-1)
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
TITLE_SHEET = Season()
SUMMER = 1
WINTER = 2
AUTUMN = 3

FONT_SIZE_PARAM = 30

BTN_SIZE = (350, 100)
SIGHT = '*'
ENEMY_HB_POS_X, ENEMY_HB_POS_Y, ENEMY_HB_WIDTH, ENEMY_HB_HEIGHT = 475, 0, 325, 100
SOUND_BTN_CLICKED = pygame.mixer.Sound('data/buttonclick.mp3')
SOUND_SHOOT = pygame.mixer.Sound('data/rocket-launcher.mp3')
SOUND_BOOM = pygame.mixer.Sound('data/rocket-explode.mp3')
SOUND_CHANGE_WEAPON = pygame.mixer.Sound('data/pickup.mp3')
SOUND_FX = [SOUND_BTN_CLICKED, SOUND_SHOOT, SOUND_BOOM, SOUND_CHANGE_WEAPON]

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
    "speed": 2000 / FPS
}

img_fireball = cut_title_sheet(load_image("resources_basic.png"), 11, 11, 0, 2)
img_ice_dart = cut_title_sheet(load_image("resources_basic.png"), 11, 11, 2, 2)
CRYSTALS = {
    "fireball": pygame.transform.scale(img_fireball, (img_fireball.get_width() * 2, img_fireball.get_height() * 2)),
    'ice_dart': pygame.transform.scale(img_ice_dart, (img_ice_dart.get_width() * 2, img_ice_dart.get_height() * 2))
}
