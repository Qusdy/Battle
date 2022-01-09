from constants import *
from camera import camera
from wizard import wizard
from enemy import enemy_bots
from groups import *
from map_generation import *
import pygame
from load_image import load_image
from draw_UI import *
from enemy_healthbar import draw_enemy_healthbar
from end_menu import end_menu
from terminate import terminate
from score import draw_score


# Код Алана
def game(season):
    if season == SUMMER:
        season_sheet = load_image("title_sheet.png")
    elif season == WINTER:
        season_sheet = load_image("IceTileset.png")
    else:
        season_sheet = load_image("RPG Nature Tileset Autumn.png")

    if season == WINTER:
        is_winter = True
    else:
        is_winter = False
    TITLE_SHEET.overwrite(season_sheet)
    camera_to_right = 1
    running = True
    shaking = False

    to_up = False
    to_left = False
    to_right = False
    to_down = False
    xp = 100
    load_level("data/level.txt")

    gen_map()
    gen_mana()

    gen_rubins()
    gen_diamonds()
    gen_emeralds()

    pos = (0, 0)
    attacking = False
    while running:
        SCREEN.fill("black")
        # обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                terminate()
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
                # Код Димы
                if event.key == pygame.K_e:
                    crystal_group.update(event)
                # Код Алана
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
                # Код Димы
                if event.button == 4 or event.button == 5:
                    wizard.change_spell()
                # Код Алана
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                attacking = False

        # Проверка на победу или поражение
        # Код Миши
        if wizard.health <= 0:
            running = False
            end_menu(False, len(enemy_bots) - len(enemy_group))
        if len(enemy_group) == 0:
            running = False
            end_menu(True, len(enemy_bots))

         # Дальше обновляем все объекты

        # Код Алана
        camera.update(wizard)

        if wizard.is_shaking:
            camera.dx += 10 * camera_to_right
        for i in all_sprites:
            camera.apply(i)
        bullets.update((camera.dx, camera.dy))
        wizard.update(to_right, to_left, to_up, to_down, pos, attacking)
        # Код Миши
        attacking = False
        enemy_group.update()
        bullets_group.update()
        # Код Алана
        camera_to_right *= -1
        xp = wizard.health
        map_sprites.draw(SCREEN)
        decor_group.draw(SCREEN)
        mana_group.draw(SCREEN)
        crystal_group.draw(SCREEN)
        crystal_group.update()
        player_group.draw(SCREEN)
        # Код Миши
        enemy_group.draw(SCREEN)
        bullets_group.draw(SCREEN)
        bullets.draw(SCREEN)
        articles_of_magic.draw(SCREEN)
        articles_of_magic.update()
        # Код Алана
        forest_group.draw(SCREEN)

        draw_lives(xp, is_winter)
        draw_mana(wizard.get_mana(), is_winter)
        draw_bag(wizard.spells, wizard.spell_now)
        # Код Миши
        # Отрисовка хп врага, если на него наведена мышка
        for enemy in enemy_bots:
            if enemy.in_sprite(pygame.mouse.get_pos()):
                draw_enemy_healthbar(enemy.health)
        # Отрисовка количества врагов, убитых игроком
        draw_score(len(enemy_bots) - len(enemy_group), season)
        # Код Димы
        pygame.display.flip()
        clock.tick(FPS)

