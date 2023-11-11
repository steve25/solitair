import copy
import pygame
from constants import (
    BOARD,
    RED,
    SQUARE_SIZE,
    LIGTH_YELLOW,
    BROWN,
    BOARD_PADDING,
)
from piece import Piece


class Board:
    def __init__(self):
        self.board = BOARD
        self.pieces_board = []
        self.board_for_border = copy.deepcopy(self.board)

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self, window):
        window.fill(LIGTH_YELLOW)

        for row in range(len(self.board)):
            first_in_col = self.board_for_border[row].index("o")
            self.board_for_border[row].reverse()
            last_in_col = (
                len(self.board_for_border[row])
                - self.board_for_border[row].index("o")
                - 1
            )
            self.board_for_border[row].reverse()

            for col in range(len(self.board[row])):
                value = self.get_piece(row, col)

                y = row * SQUARE_SIZE + BOARD_PADDING
                x = col * SQUARE_SIZE + BOARD_PADDING

                if value != "x":
                    if (row % 2 != 0 and col % 2 != 0) or (
                        row % 2 == 0 and col % 2 == 0
                    ):
                        pygame.draw.rect(
                            window, BROWN, (x, y, SQUARE_SIZE, SQUARE_SIZE)
                        )

                    if value != "x" and value != "0":
                        self.board[row][col] = Piece(row, col)
                        piece = self.board[row][col]
                        piece.draw_piece(window)

                ### draw border

                if col == first_in_col:
                    pygame.draw.line(
                        window, BROWN, (y - 1, x - 1), (y + SQUARE_SIZE - 1, x - 1), 3
                    )
                    pygame.draw.line(
                        window, BROWN, (x - 1, y - 1), (x - 1, y + SQUARE_SIZE - 1), 3
                    )
                elif col == last_in_col:
                    pygame.draw.line(
                        window,
                        BROWN,
                        (y - 1, x + SQUARE_SIZE - 1),
                        (y + SQUARE_SIZE - 1, x + SQUARE_SIZE - 1),
                        3,
                    )
                    pygame.draw.line(
                        window,
                        BROWN,
                        (x + SQUARE_SIZE - 1, y - 1),
                        (x + SQUARE_SIZE - 1, y + SQUARE_SIZE - 1),
                        3,
                    )

    def get_valid_moves(self, piece):
        moves = []
        skipped = []
        left = piece.col - 1
        right = piece.col + 1
        up = piece.row - 1
        down = piece.row + 1
        col = piece.col
        row = piece.row

        for i in range(4):
            pass

            if (
                left >= 0
                and BOARD[row][left] != "0"
                and BOARD[row][left - 1] == "0"
                and "left" not in skipped
            ):
                skipped.append("left")
                moves.append((row, left - 1))
            elif (
                right < len(BOARD[row]) - 1
                and BOARD[row][right] != "0"
                and BOARD[row][right + 1] == "0"
                and "right" not in skipped
            ):
                skipped.append("right")
                moves.append((row, right + 1))
            elif (
                up > 0
                and BOARD[up][col] != "0"
                and BOARD[up - 1][col] == "0"
                and "up" not in skipped
            ):
                skipped.append("up")
                moves.append((up - 1, col))
            elif (
                down < len(BOARD[row]) - 1
                and BOARD[down][col] != "0"
                and BOARD[down + 1][col] == "0"
                and "down" not in skipped
            ):
                skipped.append("down")
                moves.append((down + 1, col))

        return moves
