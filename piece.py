import pygame

from constants import SQUARE_SIZE


class Piece:

    def draw_piece(window, x, y):
        pygame.draw.circle(window, (0,0,0), (x + SQUARE_SIZE / 2, y + SQUARE_SIZE / 2), SQUARE_SIZE // 3.5)