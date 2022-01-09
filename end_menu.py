from constants import *
from button import Button
import pygame
from terminate import terminate


def end_menu(win, final_score):
    pygame.mixer.music.stop()
    pygame.mixer.music.load('data/to-be-continued.mp3')
    pygame.mixer.music.set_volume(LAST_MUSIC_VOLUME)
    pygame.mixer.music.play(-1)
    bg = pygame.transform.scale(load_image('bg.png'), (WINDOW_WIGHT, WINDOW_HEIGHT))
    SCREEN.blit(bg, (0, 0))
    font = pygame.font.Font('data/Font.ttf', 80)
    if win:
        text = font.render('Вы победили!', True, 'white')
    else:
        text = font.render('Вы проиграли :(', True, 'white')
    text2 = font.render('И победили ' + str(final_score), True, 'white')
    SCREEN.blit(text, text.get_rect(center=(WINDOW_WIGHT * 0.5, WINDOW_HEIGHT * 0.5)))
    SCREEN.blit(text2, (150, 100))
    btn = Button(BTN_SIZE, (225, 500), 'ВЫХОД', 0)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEMOTION:
                btn.active_control(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn.cursor_in_btn(event.pos):
                    SOUND_BTN_CLICKED.play()
                    terminate()
        btn.draw()
        pygame.display.flip()
        clock.tick(FPS)