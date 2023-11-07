import pygame
from board import Board
from constants import BOARD


class Game:
    def __init__(self, window):
        self.board = Board()
        self.window = window
        self.selected = None

    def update(self):
        self.board.create_board(self.window)
        pygame.display.update()
    
    def select(self, row, col):
        max = len(BOARD) - 1

        if row < 0 or col < 0 or row > max or col > max:
            return
        

        
         

        # if self.selected:
        #     result = self._move(row, col)
        #     if not result:
        #         self.selected = None
        #         self.select(row, col)
        
        piece = BOARD[row][col]
        if piece != "0" and piece != "x":
            self.selected = piece
            print(self.selected)
            # self.valid_moves = self.board.get_valid_moves(piece)
            return True
    
        return False