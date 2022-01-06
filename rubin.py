from cut_title_sheet import cut_title_sheet
from load_image import load_image
import pygame
from constants import *
from base_crystal import BaseCrystal
from groups import *
from wizard import wizard


class Rubin(BaseCrystal):

    def __init__(self, pos, *group):
        self.image = cut_title_sheet(load_image("resources_basic.png"), 11, 11, 0, 2)
        super().__init__(pos, *group)
        self.spell = 'fireball'
