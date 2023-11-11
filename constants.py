WIDTH = 800
HEIGHT = 800

LIGTH_YELLOW = (255, 250, 180)
BROWN = (200, 120, 0)
YELLOW = (240, 235, 130)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

BOARD = [
    ["x", "x", "o", "o", "o", "x", "x"],
    ["x", "x", "o", "o", "o", "x", "x"],
    ["o", "o", "o", "0", "o", "o", "o"],
    ["o", "o", "o", "0", "o", "o", "o"],
    ["o", "o", "o", "o", "o", "0", "o"],
    ["x", "x", "o", "o", "o", "x", "x"],
    ["x", "x", "o", "o", "o", "x", "x"],
]

BOARD_PADDING = WIDTH // 10
SQUARE_SIZE = (WIDTH - BOARD_PADDING * 2) // len(BOARD)
