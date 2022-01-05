from constants import *
from button import Button
import pygame
from terminate import terminate
from start_menu import start_menu
import game


def end_menu(win):
    SCREEN.fill('black')
    game_over_font = pygame.font.Font('data/Font.ttf', 100)
    if win:
        text = game_over_font.render('Вы выиграли!!!', True, 'white')
    else:
        text = game_over_font.render('Вы проиграли :(', True, 'white')
    SCREEN.blit(text, (50, 0))
    btns = [Button(BTN_SIZE, (400, 150), 'ИГРАТЬ СНОВА', 0), Button(BTN_SIZE, (400, 270), 'МЕНЮ', 1),
            Button(BTN_SIZE, (400, 390), 'ВЫХОД', 2)]
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
                            game.game()
                        elif btn.index == 1:
                            running = False
                            start_menu()
                        elif btn.index == 2:
                            terminate()
        for btn in btns:
            btn.draw()
        pygame.display.flip()
        clock.tick(FPS)