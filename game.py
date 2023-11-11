import pygame
from board import Board
from constants import BLUE, BOARD, BOARD_PADDING, RED, SQUARE_SIZE
from piece import Piece


class Game:
    def __init__(self, window):
        self.board = Board()
        self.window = window
        self.selected = None
        self.valid_moves = []

    def update(self):
        self.board.create_board(self.window)
        self.draw_selected(self.selected)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def select(self, row, col):
        max_len = len(BOARD) - 1

        piece = self.board.get_piece(row, col)
        if self.selected and BOARD[row][col] == "0" and (row, col) in self.valid_moves:
            if self.selected.row == row:
                list_of_col = [col, self.selected.col]

                if col > self.selected.col:
                    skipped_col = list(range(min(list_of_col) + 1, max(list_of_col)))
                else:
                    skipped_col = list(range(min(list_of_col) + 1, max(list_of_col)))
                skipped = (row, skipped_col[0])
            else:
                list_of_row = [row, self.selected.row]

                if row > self.selected.row:
                    skipped_row = list(range(min(list_of_row) + 1, max(list_of_row)))
                else:
                    skipped_row = list(range(min(list_of_row) + 1, max(list_of_row)))
                skipped = (skipped_row[0], col)

            BOARD[self.selected.row][self.selected.col] = "0"
            BOARD[skipped[0]][skipped[1]] = "0"
            BOARD[row][col] = Piece(row, col)
            self.selected = None

        if row < 0 or col < 0 or row > max_len or col > max_len:
            return

        piece = self.board.get_piece(row, col)

        if piece != "x" and piece != "0":
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    def draw_selected(self, piece):
        if self.selected:
            pygame.draw.circle(
                self.window,
                RED,
                (piece.x + SQUARE_SIZE / 2, piece.y + SQUARE_SIZE / 2),
                SQUARE_SIZE // 8,
            )

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(
                self.window,
                BLUE,
                (
                    BOARD_PADDING + col * SQUARE_SIZE + SQUARE_SIZE // 2,
                    BOARD_PADDING + row * SQUARE_SIZE + SQUARE_SIZE // 2,
                ),
                SQUARE_SIZE // 10,
            )
