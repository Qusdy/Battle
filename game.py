from constants import *
from camera import camera
from wizard import wizard
from enemy import enemy_bots
from groups import *
from map_generation import load_level, gen_map, gen_mana
import pygame
from load_image import load_image
from draw_UI import *


def game():
    running = True

    to_up = False
    to_left = False
    to_right = False
    to_down = False
    xp = 100
    load_level("data/level.txt")
    # add_forest()
    gen_map()
    gen_mana()
    # print(len(level))
    # for i in level:
    #     print(i)
    pos = (0, 0)
    attacking = False
    while running:
        SCREEN.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    to_left = True
                if event.key == pygame.K_d:
                    to_right = True
                if event.key == pygame.K_s:
                    to_down = True
                if event.key == pygame.K_w:
                    to_up = True
                if event.key == pygame.K_h:
                    shaking = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    to_left = False
                if event.key == pygame.K_d:
                    to_right = False
                if event.key == pygame.K_s:
                    to_down = False
                if event.key == pygame.K_w:
                    to_up = False
            if event.type == pygame.MOUSEMOTION:
                pos = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                attacking = True
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                attacking = False

        camera.update(wizard)
        for i in all_sprites:
            camera.apply(i)

        wizard.update(to_right, to_left, to_up, to_down, pos, attacking)
        for enemy in enemy_bots:
            enemy.update()

        map_sprites.draw(SCREEN)
        #
        # for i in forest_group:
        #     i.draw_rect()ф
        # print(len(forest_group))
        decor_group.draw(SCREEN)
        mana_group.draw(SCREEN)
        player_group.draw(SCREEN)
        enemy_group.draw(SCREEN)
        bullets_group.draw(SCREEN)
        # all_sprites.draw(screen)
        # wizard.draw_healbar()

        forest_group.draw(SCREEN)
        draw_lives(xp)
        draw_mana(wizard.get_mana())
        pygame.display.flip()
        clock.tick(FPS)

