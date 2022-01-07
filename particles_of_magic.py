from groups import *


class Particles_of_magic(pygame.sprite.Sprite):
    def __init__(self, obj, sheet, columns, rows, x, y, dlitel, *trans):
        super().__init__(all_sprites)
        self.frames = []
        self.trans = trans
        self.dlitel = dlitel
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        if trans:
            self.image = pygame.transform.smoothscale(self.image, trans)
        self.rect = self.rect.move(x, y)
        self.frame = 8

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                for _ in range(self.dlitel):
                    self.frames.append(sheet.subsurface(pygame.Rect(
                        frame_location, self.rect.size)))

    def update(self):
        self.frame -= 1
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        if self.trans:
            self.image = pygame.transform.smoothscale(self.image, self.trans)
        if self.frame <= 0:
            self.kill()
