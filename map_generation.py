from constants import *
from groups import *
from grass import Grass
from tree import Tree
from mushrooms import TwoMushrooms, OneMushroom
from random import randint
from mana import Mana
from rubin import Rubin
from emerald import Emerald
from diamond import Diamond


def load_level(file):
    file = open(file, mode="rt", encoding="UTF-8")
    for st in file.readlines():
        simvols = list(st.strip())
        level.append(simvols)


def gen_map():
    for i in range(len(level)):
        for z in range(len(level[i])):
            if level[i][z] == GRASS:
                grass_sprite = Grass((i * 32, z * 32))
                map_sprites.add(grass_sprite)
                all_sprites.add(grass_sprite)
            elif level[i][z] == TREE:
                tree_sprite = Tree((i * 32, z * 32))
                grass_sprite = Grass((i * 32, z * 32))

                map_sprites.add(grass_sprite)

                forest_group.add(tree_sprite)

                all_sprites.add(grass_sprite)
                all_sprites.add(tree_sprite)
            elif level[i][z] == TWO_MUSHROOMS:
                mushroom_sprite = TwoMushrooms((i * 32, z * 32))
                grass_sprite = Grass((i * 32, z * 32))

                decor_group.add(mushroom_sprite)

                map_sprites.add(grass_sprite)
                all_sprites.add(grass_sprite)
                all_sprites.add(mushroom_sprite)

            elif level[i][z] == ONE_MUSHROOM:
                mushroom_sprite = OneMushroom((i * 32, z * 32))
                grass_sprite = Grass((i * 32, z * 32))

                decor_group.add(mushroom_sprite)

                map_sprites.add(grass_sprite)
                all_sprites.add(grass_sprite)
                all_sprites.add(mushroom_sprite)


def gen_mana():
    for i in range(100):
        coords = (randint(20 * 32, LEVEL_WIGHT - 20 * 32), randint(20 * 32, LEVEL_WIGHT - 20 * 32))

        mana = Mana((coords[0], coords[1]))
        mana_group.add(mana)
        all_sprites.add(mana)


def gen_rubins():
    for i in range(3):
        coords = (randint(20 * 32, LEVEL_WIGHT - 20 * 32), randint(20 * 32, LEVEL_WIGHT - 20 * 32))
        rubin = Rubin((coords[0], coords[1]))
        crystal_group.add(rubin)
        rubins_group.add(rubin)
        all_sprites.add(rubin)


def gen_diamonds():
    for i in range(3):
        coords = (randint(20 * 32, LEVEL_WIGHT - 20 * 32), randint(20 * 32, LEVEL_WIGHT - 20 * 32))
        diamond = Diamond((coords[0], coords[1]))
        crystal_group.add(diamond)
        diamond_group.add(diamond)
        all_sprites.add(diamond)


def gen_emeralds():
    for i in range(3):
        coords = (randint(20 * 32, LEVEL_WIGHT - 20 * 32), randint(20 * 32, LEVEL_WIGHT - 20 * 32))
        emerald = Emerald((coords[0], coords[1]))
        crystal_group.add(emerald)
        emeralds_group.add(emerald)
        all_sprites.add(emerald)

