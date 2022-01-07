from wizard import Wizard
from groups import *
from load_image import load_image

wizard = Wizard(load_image("DinoSprites - doux.png"), 24, 1, 640, 640)
player_group.add(wizard)
