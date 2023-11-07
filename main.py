from constants import BOARD, BOARD_PADDING, HEIGHT, SQUARE_SIZE, WIDTH
from game import Game
import pygame

FPS = 60

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Solitaire')

def get_position_from_mouse(pos):
    x,y = pos
    row = (y - BOARD_PADDING) // SQUARE_SIZE
    col = (x - BOARD_PADDING) // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WINDOW)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_position_from_mouse(pos)
                game.select(row, col)
        game.update()

    pygame.quit()

main()