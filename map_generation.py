from constants import *
from groups import *
from grass import Grass
from tree import Tree


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
            #
            # else:
            #     road_sprite = Road((i * 32, z * 32))
            #     map_sprites.add(road_sprite)
            #     all_sprites.add(road_sprite)


def add_forest():
    for i in range(0, len(level), 2):
        for j in range(0, 14, 2):
            level[i][j] = TREE
            level[i][-j] = TREE
            #
            level[j][i] = TREE
            level[-j][i] = TREE
