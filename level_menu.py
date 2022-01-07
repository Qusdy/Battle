from constants import *
from button import Button
import pygame
from terminate import terminate
import start_menu
from game import game


def level_menu():
    bg = pygame.transform.scale(load_image('bg.png'), (WINDOW_WIGHT, WINDOW_HEIGHT))
    SCREEN.blit(bg, (0, 0))
    btns = [Button(BTN_SIZE, (400, 150), 'ЛЕТО', 0), Button(BTN_SIZE, (400, 270), 'ЗИМА', 1),
            Button(BTN_SIZE, (400, 390), 'ОСЕНЬ', 2), Button(BTN_SIZE, (400, 510), 'ВЕРНУТЬСЯ', 3)]
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEMOTION:
                for btn in btns:
                    btn.active_control(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                for btn in btns:
                    if btn.cursor_in_btn(event.pos):
                        SOUND_BTN_CLICKED.play()
                        running = False
                        if btn.index == 0:
                            game(SUMMER)
                        elif btn.index == 1:
                            game(WINTER)
                        elif btn.index == 2:
                            game(AUTUMN)
                        elif btn.index == 3:
                            start_menu.start_menu()
        for btn in btns:
            btn.draw()
        pygame.display.flip()
        clock.tick(FPS)