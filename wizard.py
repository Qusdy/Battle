import pygame
from animated_sprite import AnimatedSprite
from constants import *
from groups import *
from ammo import *
from load_image import load_image
from particle import create_particles


class Wizard(AnimatedSprite):
    def __init__(self, sheet, colums, rows, x, y):
        sheet = pygame.transform.scale(sheet, (sheet.get_width() * 3, sheet.get_height() * 3))
        self.SPEED = SPEED
        super(Wizard, self).__init__(sheet, colums, rows, x, y)
        self.is_attacking = False

        self.mouse_pos = (0, 0)
        self.weapon = None

        self.mana = 0
        self.health = 100
        self.attack = []
        self.run = []
        self.stand = []
        self.spells = [0]
        self.spell_now = self.spells[0]

        for i in self.frames[WALK_FRAMES_IND[0]:WALK_FRAMES_IND[1]]:
            for j in range(5):
                self.run.append(i)

        for i in self.frames[STAND_IND[0]:STAND_IND[1]]:
            for j in range(5):
                self.stand.append(i)

        for i in self.frames[ATTACK_FRAMES_IND[0]:ATTACK_FRAMES_IND[1]]:
            for j in range(5):
                self.attack.append(i)
        # self.healbar_wid = self.image.get_width()
        self.look_direction_left = False

        self.blocked_to_up = self.blocked_to_right = self.blocked_to_left = self.blocked_to_down = False

        self.touched = False

    def update(self, to_r, to_l, to_u, to_d, mouse_position=(0, 0), is_attacking=False):
        if is_attacking:
            self.cur_frame = 0
            self.is_attacking = is_attacking
        # Код Дмитрия
        self.mouse_pos = mouse_position
        SPEED_goriz = self.SPEED
        SPEED_vertik = self.SPEED
        if to_d and to_u:
            SPEED_vertik = 0
        if to_l and to_r:
            SPEED_goriz = 0
        if (to_l and to_d) or (to_l and to_u) or (to_r and to_d) or (to_r and to_u):
            x = (math.sqrt(2) * self.SPEED) // 2
            SPEED_goriz = x
            SPEED_vertik = x
        if to_d and not self.blocked_to_down:
            self.rect.y += SPEED_vertik
            self.blocked_to_up = False
        if to_u and not self.blocked_to_up:
            self.rect.y -= SPEED_vertik
            self.blocked_to_down = False
        if to_l and not self.blocked_to_left:
            self.rect.x -= SPEED_goriz
            self.blocked_to_right = False
        if to_r and not self.blocked_to_right:
            self.rect.x += SPEED_goriz
            self.blocked_to_left = False
        # Код Алана
        if self.is_attacking and self.spell_now == 0:
            if mouse_position[0] < WINDOW_WIGHT // 2:
                self.look_direction_left = True
            if mouse_position[0] > WINDOW_WIGHT // 2:
                self.look_direction_left = False
            self.attack_animation(self.look_direction_left)
        elif self.is_attacking and self.spell_now == 'fireball':
            if self.mana >= 10:
                self.shoot(mouse_position, [self.rect.centerx, self.rect.centery], self.spell_now)
                self.mana -= 10
            self.is_attacking = False
        elif self.is_attacking and self.spell_now == 'ice_dart':
            if self.mana >= 5:
                self.shoot(mouse_position, [self.rect.centerx, self.rect.centery], self.spell_now)
                self.mana -= 5
            self.is_attacking = False
        elif not any([to_r, to_l, to_u, to_d]):
            self.standing_animation(mouse_position)
        elif any([to_r, to_l, to_u, to_d]):
            if mouse_position[0] < WINDOW_WIGHT // 2:
                self.look_direction_left = True
            if mouse_position[0] > WINDOW_WIGHT // 2:
                self.look_direction_left = False
            self.running_animation(self.look_direction_left)

        if pygame.sprite.spritecollideany(self, forest_group):
            rastoyan = 4
            if to_l:
                self.blocked_to_left = True
                self.rect.x += rastoyan
            if to_r:
                self.blocked_to_right = True
                self.rect.x -= rastoyan
            if to_u:
                self.blocked_to_up = True
                self.rect.y += rastoyan
            if to_d:
                self.blocked_to_down = True
                self.rect.y -= rastoyan

        if pygame.sprite.spritecollideany(self, mana_group) and self.mana < 100:
            self.mana += 10
            pygame.sprite.groupcollide(player_group, mana_group, False, True)

        if pygame.sprite.spritecollideany(self, enemy_group) and is_attacking:
            gr = pygame.sprite.groupcollide(enemy_group, player_group, False, False)
            for i in gr:
                i.have_damage(5)

    def standing_animation(self, mouse_position):
        if mouse_position[0] < WINDOW_WIGHT // 2:
            self.look_direction_left = True
        else:
            self.look_direction_left = False

        self.cur_frame = (self.cur_frame + 1) % len(self.stand)
        self.image = pygame.transform.flip(self.stand[self.cur_frame], self.look_direction_left, False)

    def running_animation(self, reverse):
        create_particles(self.mouse_pos)
        self.cur_frame = (self.cur_frame + 1) % len(self.run)
        self.image = pygame.transform.flip(self.run[self.cur_frame], reverse, False)
        self.look_direction_left = reverse

    def attack_animation(self, reverse):
        create_particles(self.mouse_pos)
        self.cur_frame = (self.cur_frame + 1) % len(self.attack)
        self.image = pygame.transform.flip(self.attack[self.cur_frame], reverse, False)
        self.look_direction_left = reverse
        if self.cur_frame == len(self.attack) - 1:
            self.is_attacking = False

    def draw_healbar(self):
        pygame.draw.rect(SCREEN, color="red", rect=(self.rect.x + 10, self.rect.y, 64, 10))

    def attacking(self, pos):
        pass

    def get_mana(self):
        return self.mana

    # Код Димы
    def shoot(self, mousepos, perspos, spell):
        x = 0 + perspos[0]
        y = 0 + perspos[1]
        dx = mousepos[0] - perspos[1]
        dy = mousepos[1] - perspos[1]
        if abs(dx) > 0 or abs(dy) > 0:
            if spell == 'fireball':
                bullet = Fireball(x, y, dx, dy)
            if spell == 'ice_dart':
                bullet = Ice_dart(x, y, dx, dy)

    def change_spell(self):
        self.spell_now = self.spells[self.spells.index(self.spell_now) - 1]

    def new_spell(self, spell):
        self.spell_now = spell
        self.spells.append(spell)
        # if 0 in self.spells:
        #     self.spells[self.spells.index(0)] = self.spell_now


wizard = Wizard(load_image("DinoSprites - doux.png"), 24, 1, 640, 640)
player_group.add(wizard)
