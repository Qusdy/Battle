import pygame
from animated_sprite import AnimatedSprite
from constants import *
from groups import forest_group, player_group
from load_image import load_image


class Wizard(AnimatedSprite):
    def __init__(self, sheet, colums, rows, x, y):
        sheet = pygame.transform.scale(sheet, (sheet.get_width() * 3, sheet.get_height() * 3))
        super(Wizard, self).__init__(sheet, colums, rows, x, y)
        self.run = self.frames[WALK_FRAMES_IND[0]:WALK_FRAMES_IND[1]]
        self.stand = self.frames[STAND_IND[0]:STAND_IND[1]]
        # self.healbar_wid = self.image.get_width()
        self.look_direction_left = False

        self.blocked_to_up = self.blocked_to_right = self.blocked_to_left = self.blocked_to_down = False

        self.touched = False

    def update(self, to_r, to_l, to_u, to_d, mouse_position=(0, 0)):
        if not any([to_d, to_r, to_l, to_u]):
            self.standing_animation(mouse_position)
        else:
            if to_l:
                self.look_direction_left = True
            if to_r:
                self.look_direction_left = False

            self.running_animation(self.look_direction_left)

        if to_d and not self.blocked_to_down:
            self.rect.y += PLAYER_SPEED
        if to_u and not self.blocked_to_up:
            self.rect.y -= PLAYER_SPEED
        if to_l and not self.blocked_to_left:
            self.rect.x -= PLAYER_SPEED
        if to_r and not self.blocked_to_right:
            self.rect.x += PLAYER_SPEED

        if pygame.sprite.spritecollideany(self, forest_group):
            if to_l:
                self.blocked_to_left = True
            if to_r:
                self.blocked_to_right = True
            if to_u:
                self.blocked_to_up = True
            if to_d:
                self.blocked_to_down = True

        else:
            self.blocked_to_up = self.blocked_to_right = self.blocked_to_left = self.blocked_to_down = False

    def standing_animation(self, mouse_position):
        if mouse_position[0] < WINDOW_WIGHT // 2:
            self.look_direction_left = True
        else:
            self.look_direction_left = False

        self.cur_frame = (self.cur_frame + 1) % len(self.stand)
        self.image = pygame.transform.flip(self.stand[self.cur_frame], self.look_direction_left, False)

    def running_animation(self, reverse):

        self.cur_frame = (self.cur_frame + 1) % len(self.run)
        self.image = pygame.transform.flip(self.run[self.cur_frame], reverse, False)
        self.look_direction_left = reverse

    def draw_healbar(self):
        pygame.draw.rect(SCREEN, color="red", rect=(self.rect.x + 10, self.rect.y, 64, 10))


wizard = Wizard(load_image("DinoSprites - doux.png"), 24, 1, 640, 640)
player_group.add(wizard)