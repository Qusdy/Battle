import pygame
from constants import *


class Slider:
    def __init__(self, x1, y1, width, height, text, index):
        self.volume = 100
        self.x1, self.y1 = x1, y1
        self.width, self.height = width, height
        self.text = text
        self.font = pygame.font.Font('data/Font.ttf', 70)
        self.index = index
        self.active = False
        self.sldr_x, self.sldr_y = 650, self.y1 - 25
        self.sldr_width, self.sldr_height = 50, self.height + 50
        self.division = (self.width - self.sldr_width) / 100

    def draw(self):
        text = self.font.render(self.text + str(self.volume), True, 'white')
        SCREEN.blit(text, (0.15 * WINDOW_WIGHT, self.sldr_y - 70))
        pygame.draw.rect(SCREEN, 'gray', (self.x1, self.y1, self.width, self.height), border_radius=10)
        pygame.draw.rect(SCREEN, 'white', (self.x1, self.y1, self.width, self.height), 4, border_radius=10)
        pygame.draw.rect(SCREEN, 'red', (self.x1, self.y1, self.sldr_x - self.x1, self.height), border_radius=5)
        pygame.draw.rect(SCREEN, '#FFAA73', (self.sldr_x, self.sldr_y, self.sldr_width, self.sldr_height), border_radius=5)

    def in_slider(self, pos):
        if self.sldr_x <= pos[0] <= self.sldr_x + self.sldr_width:
            if self.sldr_y <= pos[1] <= self.sldr_y + self.sldr_height:
                return True
        return False

    def can_change_pos(self, pos):
        if self.x1 <= pos[0] <= self.x1 + self.width - self.sldr_width + 25:
            return True
        return False

    def change_pos(self, pos):
        self.sldr_x = pos[0]

    def set_volume(self):
        for i in range(101):
            if i * self.division <= self.sldr_x - self.x1 < (i + 1) * self.division:
                self.volume = i
                self.sldr_x = self.division * i + self.x1
                break
            if i == 100:
                self.past_volume(100)

    def past_volume(self, volume):
        if volume != 100 and volume != 0:
            volume += 1
        self.volume = volume
        self.sldr_x = self.division * volume + self.x1
