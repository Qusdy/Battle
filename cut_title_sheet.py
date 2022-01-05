import pygame


def cut_title_sheet(sheet, sheets_rows, sheets_cols, row, col):
    rect = pygame.Rect(0, 0, sheet.get_width() // sheets_cols,
                       sheet.get_height() // sheets_rows)
    frame_location = (rect.w * row, rect.h * col)
    pygame.Rect(frame_location, rect.size)
    return sheet.subsurface(pygame.Rect(frame_location, rect.size))
