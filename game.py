from constants import *
from camera import camera
from wizard import get_wizard
from enemy import get_enemies
from groups import *
from map_generation import *
import pygame
from load_image import load_image
from draw_UI import *
from end_menu import end_menu


def game():
    camera_to_right = 1
    running = True
    shaking = False

    wizard, enemy_bots = get_wizard(), get_enemies()
    enemy_left = len(enemy_bots)
    to_up = False
    to_left = False
    to_right = False
    to_down = False
    xp = 100
    load_level("data/level.txt")
    # add_forest()
    gen_map()
    gen_mana()
    gen_rubins()
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
                if event.key == pygame.K_e:
                    rubins_group.update(event)
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    attacking = True
                if event.button == 4 or event.button == 5:
                    wizard.change_spell()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                attacking = False

        camera.update(wizard)
        if wizard.health == 0:
            end_menu(False)
        if shaking:
            camera.dx += 10 * camera_to_right
        for i in all_sprites:
            camera.apply(i)
        bullets.update((camera.dx, camera.dy))

        wizard.update(to_right, to_left, to_up, to_down, pos, attacking)
        attacking = False
        enemy_group.update()
        bullets_group.update()
        camera_to_right *= -1
        xp = wizard.health
        map_sprites.draw(SCREEN)
        decor_group.draw(SCREEN)
        mana_group.draw(SCREEN)
        rubins_group.draw(SCREEN)
        player_group.draw(SCREEN)
        enemy_group.draw(SCREEN)
        bullets_group.draw(SCREEN)
        bullets.draw(SCREEN)
        # bullets.update()
        # all_sprites.draw(screen)
        # wizard.draw_healbar()
        forest_group.draw(SCREEN)
        rubins_group.update()
        draw_lives(xp)
        draw_mana(wizard.get_mana())
        pygame.display.flip()
        clock.tick(FPS)

