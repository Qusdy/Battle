from constants import *
import pygame
from game import Game
from start_menu import start_menu

running = True
pygame.init()

start_menu()
game = Game()