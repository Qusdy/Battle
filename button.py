import pygame
from constants import SCREEN


class Button:
    def __init__(self, size, pos, text, index):
        self.width, self.height = size[0], size[1]
        self.x, self.y = pos[0], pos[1]
        self.index = index
        self.text = text
        self.font = pygame.font.Font('data/Font.ttf', 50)
        self.active = False

    def draw(self):
        if self.active:
            pygame.draw.rect(SCREEN, '#04396C', (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(SCREEN, '#26527C', (self.x, self.y, self.width, self.height))
        text = self.font.render(self.text, True, 'white')
        SCREEN.blit(text, text.get_rect(center=(self.x + 0.5 * self.width, self.y + 0.5 * self.height)))

    def cursor_in_btn(self, mouse_pos):
        if self.x < mouse_pos[0] < self.x + self.width:
            if self.y < mouse_pos[1] < self.y + self.height:
                return True

    def active_control(self, mouse_pos):
        if self.cursor_in_btn(mouse_pos):
            self.active = True
        else:
            self.active = False

    def action(self, actions):
        actions[self.index]()