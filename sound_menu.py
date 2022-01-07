from constants import *
from button import Button
import pygame
from terminate import terminate
import start_menu
from slider import Slider


def sound_menu():
    btn = Button(BTN_SIZE, (225, 650), 'Поставить', 0)
    sliders = [Slider(100, 250, 600, 100, 'Звук эффектов ', 0), Slider(100, 500, 600, 100, 'Звук музыки ', 1)]
    running = True
    while running:
        bg = pygame.transform.scale(load_image('bg.png'), (WINDOW_WIGHT, WINDOW_HEIGHT))
        SCREEN.blit(bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEMOTION:
                for slider in sliders:
                    if slider.active:
                        if slider.can_change_pos(event.pos):
                            slider.change_pos(event.pos)
                        else:
                            slider.active = False
                btn.active_control(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn.cursor_in_btn(event.pos):
                    SOUND_BTN_CLICKED.play()
                    for slider in sliders:
                        if slider.index == 0:
                            for effect in SOUND_FX:
                                effect.set_volume(slider.volume / 100)
                        else:
                            pygame.mixer.music.set_volume(slider.volume / 100)
                    running = False
                for slider in sliders:
                    if slider.in_slider(event.pos):
                        slider.active = True
            if event.type == pygame.MOUSEBUTTONUP:
                for slider in sliders:
                    slider.active = False
                    slider.check_new_pos()
        btn.draw()
        for slider in sliders:
            slider.draw()
        pygame.display.flip()
        clock.tick(FPS)
    start_menu.start_menu()