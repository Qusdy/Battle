import pygame
from load_image import load_image
PLAYER_SPEED = 16

LEVEL_HEIGHT = LEVEL_WIGHT = 1024
SIZE = WINDOW_HEIGHT, WINDOW_WIGHT = 640, 640

WALK_FRAMES_IND = (4, 10)
STAND_IND = (0, 4)
DINO_HEALBAR = 15
SCREEN = pygame.display.set_mode(SIZE)
level = []
GRASS = "0"
TREE = "I"
TITLE_SHEET = load_image("title_sheet.png")
