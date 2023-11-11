import pygame

from constants import BLACK, BOARD_PADDING, SQUARE_SIZE


class Piece:
    def __init__(self, row, col):
        self.x = 0
        self.y = 0
        self.row = row
        self.col = col
        self.calculate_position()

    def calculate_position(self):
        self.y = self.row * SQUARE_SIZE + BOARD_PADDING
        self.x = self.col * SQUARE_SIZE + BOARD_PADDING

    def draw_piece(self, window):
        pygame.draw.circle(
            window,
            BLACK,
            (self.x + SQUARE_SIZE / 2, self.y + SQUARE_SIZE / 2),
            SQUARE_SIZE // 4,
        )

    def __repr__(self):
        return str("o")
