import pygame


def sheet_from_sheet(sheet, sheets_rows, sheets_cols, start_row, start_col, n_elems):
    rect = pygame.Rect(0, 0, sheet.get_width() // sheets_cols,
                       sheet.get_height() // sheets_rows)
    frame_location = (rect.w * start_row, rect.h * start_col)
    return sheet.subsurface(pygame.Rect(frame_location, rect.width * n_elems, rect.height * n_elems))