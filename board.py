import pygame
from constants import BOARD, YELLOW, SQUARE_SIZE, LIGTH_YELLOW, BROWN, BOARD_PADDING, BLACK
from piece import Piece


class Board:
    def __init__(self):
        self.board = BOARD

    def create_board(self, window):
        window.fill(LIGTH_YELLOW)


        for row in range(len(self.board)):
            first_in_col = self.board[row].index("o")
            self.board[row].reverse()
            last_in_col = len(self.board[row]) - self.board[row].index("o") - 1
            self.board[row].reverse()

            for col in range(len(self.board[row])):
                value = self.board[row][col]

                x = row*SQUARE_SIZE + BOARD_PADDING
                y = col*SQUARE_SIZE + BOARD_PADDING

                if value != "x":
                    if (row % 2 != 0 and col % 2 != 0) or (row % 2 == 0 and col % 2 == 0):
                        pygame.draw.rect(window, BROWN, (x, y, SQUARE_SIZE, SQUARE_SIZE))

                    if value == "o":
                        Piece.draw_piece(window, x, y)

                if col == first_in_col:
                    pygame.draw.line(window, BROWN, (x - 1, y - 1),
                                     (x + SQUARE_SIZE - 1 , y - 1), 3)
                    pygame.draw.line(window, BROWN, (y - 1, x - 1),
                                     (y - 1, x + SQUARE_SIZE - 1), 3)
                elif col == last_in_col:
                    pygame.draw.line(window, BROWN, (x - 1, y + SQUARE_SIZE - 1),
                                     (x + SQUARE_SIZE - 1, y + SQUARE_SIZE - 1), 3)
                    pygame.draw.line(window, BROWN, (y + SQUARE_SIZE - 1, x -1),
                                     (y + SQUARE_SIZE - 1, x + SQUARE_SIZE - 1), 3)
