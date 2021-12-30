from constants import *
from button import Button
import pygame
import sys


def terminate():
    pygame.quit()
    sys.exit()


def start_menu():
    bg = pygame.transform.scale(load_image('bg.png'), (WINDOW_WIGHT, WINDOW_HEIGHT))
    SCREEN.blit(bg, (0, 0))
    btns = [Button(BTN_SIZE, (400, 100), 'Играть', 0), Button(BTN_SIZE, (400, 220), 'Звук', 1),
            Button(BTN_SIZE, (400, 340), 'Выход', 2)]
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
                        if btn.index == 0:
                            running = False
                        elif btn.index == 1:
                            print('звук не подвезли')
                        elif btn.index == 2:
                            terminate()
        for btn in btns:
            btn.draw()
        pygame.display.flip()
        clock.tick(FPS)
