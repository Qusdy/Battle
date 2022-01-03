from constants import *
from groups import *
from grass import Grass
from tree import Tree
from mushrooms import TwoMushrooms, OneMushroom
from random import randint
from mana import Mana
from rubin import Rubin

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

            #
            # else:
            #     road_sprite = Road((i * 32, z * 32))
            #     map_sprites.add(road_sprite)
            #     all_sprites.add(road_sprite)


def gen_mana():
    for i in range(100):
        coords = (randint(13 * 32, LEVEL_WIGHT - 13 * 32), randint(13 * 32, LEVEL_WIGHT - 13 * 32))
        # print(coords)
        mana = Mana((coords[0], coords[1]))
        mana_group.add(mana)
        all_sprites.add(mana)


def gen_rubins():
    for i in range(3):
        coords = (randint(13 * 32, LEVEL_WIGHT - 13 * 32), randint(13 * 32, LEVEL_WIGHT - 13 * 32))
        rubin = Rubin((coords[0], coords[1]))
        rubins_group.add(rubin)
        all_sprites.add(rubin)

# def add_forest():
#     for i in range(0, len(level), 2):
#         for j in range(0, 14, 2):
#             level[i][j] = TREE
#             level[i][-j] = TREE
#             #
#             level[j][i] = TREE
#             level[-j][i] = TREE
#     for i in level:
#         print(i)
