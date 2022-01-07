import pygame
from constants import *


class Slider:
    def __init__(self, x1, y1, width, height, text, index):
        self.volume = 100
        self.active = False
        self.index = index
        self.x1, self.y1 = x1, y1
        self.width, self.height = width, height
        self.text = text
        self.slider_x, self.slider_y, self.slider_width, self.slider_height = x1 + width - 25, y1 - 25, 50, 150
        self.font = pygame.font.Font('data/Font.ttf', 50)

    def draw(self):
        text = self.font.render(self.text + str(self.volume), True, 'white')
        SCREEN.blit(text, (self.x1 + self.width * 0.25, self.y1 - 100))
        pygame.draw.rect(SCREEN, 'gray', (self.x1, self.y1, self.width, self.height), border_radius=10)
        pygame.draw.rect(SCREEN, 'red', (self.x1, self.y1, self.slider_x - self.x1, self.height), border_radius=10)
        pygame.draw.rect(SCREEN, 'white', (self.x1, self.y1, self.width, self.height), 5, border_radius=10)
        pygame.draw.rect(SCREEN, '#FFAD40', (self.slider_x, self.slider_y, self.slider_width, self.slider_height), border_radius=2)

    def in_slider(self, pos):
        if self.slider_x <= pos[0] <= self.slider_x + self.width:
            if self.slider_y <= pos[1] <= self.slider_y + self.height:
                return True
        return False

    def can_change_pos(self, pos):
        if self.x1 <= pos[0] <= self.x1 + self.width:
            return True
        return False

    def change_pos(self, pos):
        self.slider_x = pos[0]

    def check_new_pos(self):
        for i in range(11):
            if i * (self.width // 10) <= self.slider_x - self.x1 < (i + 1) * (self.width // 10):
                self.slider_x = i * (self.width // 10) + 100
                self.volume = i * 10