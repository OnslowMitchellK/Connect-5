"""Connect 5 Game."""
# Videos from https://www.youtube.com/@freecodecamp/videos
# were used to aid the development of this code

import numpy as np
import pygame
import sys
import math
from typing import List

# Colour variables
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BG_COLOUR = (0, 0, 0)

ROW_COUNT = 7
COLUMN_COUNT = 8


def create_board() -> List[List[int]]:
    """
    Create a 7x8 game board filled with zeros.

    Returns:
        List[List[int]]: A 7x8 display representing the connect 5
                        game board with each spot filled in with 0.
    """
    board = [[0] * COLUMN_COUNT for _ in range(ROW_COUNT)]
    return board


def drop_piece(board: List[List[int]], row: int,
               col: int, piece: int) -> List[List[int]]:
    """
    Place a game piece on the game board.

    Args:
        board (List[List[str]]): The game board represented
                                 as a 2D list of strings.
        row (int): The row where the piece will be placed.
        col (int): The column where the piece will be placed.
        piece (str): The game piece to be placed on the board.

    Returns:
        List[List[str]]: The updated game board after placing the piece.
    """
    board[row][col] = piece
    return board


def is_valid_location(board: List[List[int]], col: int) -> bool:
    """
    Check if a given column is a valid location for placing a checker.

    Args:
        board (List[List[str]]): The game board represented
                                 as a 2D list of strings.
        col (int): The column to be checked.

    Returns:
        bool: True if the column is vacant
              (all rows are empty strings), False otherwise.
    """
    return board[6][col] == 0


def get_next_open_row(board: List[List[int]], col: int) -> int:
    """
    Find the next open row in a given column.

    Args:
        board (List[List[str]]): The game board represented
                                 as a 2D list of strings.
        col (int): The column to be checked.

    Returns:
        int: The row index of the next open row in the column.
    """
    for row in range(ROW_COUNT):
        if board[row][col] == 0:
            return row
    return -1  # -1 if column is full


def print_board(board: List[List[int]]) -> None:
    """Print the game board."""
    print(np.flip(board, 0))


def win_check(board: List[List[int]], piece: int) -> bool:
    """
    Check for a winning move in all possible ways on the Connect 5 game board.

    Args:
        board (List[List[int]]): A 2D list representing the game board
            with integer values where 0 represents an empty spot, 1 represents
            player one's checker, and 2 represents player two's checker.
        piece (int): The player's checker to check for a winning
            combination (1 or 2).

    Returns:
        bool: True if a winning combination of five checkers of the
            specified 'checker' is found in any direction (vertical,
            horizontal, or diagonal); otherwise, False.
    """
    # Check for 5 verticle in a row
    # https://www.geeksforgeeks.org/python-all-function/
    for row in range(ROW_COUNT - 4):
        for col in range(COLUMN_COUNT):
            if all(board[row + i][col] == piece for i in range(5)):
                return True

    # Check for 5 horizontal in a row
    for row in range(ROW_COUNT):
        for col in range(COLUMN_COUNT - 4):
            if all(board[row][col + i] == piece for i in range(5)):
                return True
            
    # Check for 5 negatively sloped diaganol
    for col in range(COLUMN_COUNT-4):
        for row in range(4, ROW_COUNT):
            if (
                board[row][col] == piece and
                board[row-1][col+1] == piece and
                board[row-2][col+2] == piece and
                board[row-3][col+3] == piece and
                board[row-4][col+4] == piece
                ):
                return True

    # Check for 5 negatively sloped diaganol in a row
    for row in range(4, ROW_COUNT):
        for col in range(COLUMN_COUNT - 4):
            if all(board[row - i][col + i] == piece for i in range(5)):
                return True

    # Check for 5 positivly sloped diaganol in  a row
    for row in range(ROW_COUNT - 4):
        for col in range(COLUMN_COUNT - 4):
            if all(board[row + i][col + i] == piece for i in range(5)):
                return True
            
    # If no win is detected, return False
    return False


def draw_board(board: List[List[int]]) -> None:
    """
    Draw the Connect 5 game board on the screen with the current game state.

    Args:
        board (List[List[int]]): A 2D list representing the game board
            with integer values where 0 represents an empty spot, 1 represents
            player one's piece (red checker), and 2 represents player
            two's piece (yellow checker).
    """
    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (col * SQUARESIZE,
                                            row * SQUARESIZE + SQUARESIZE,
                                            SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BG_COLOUR, (int(col * SQUARESIZE +
                                                       SQUARESIZE / 2),
                                                   int(row * SQUARESIZE +
                                                       SQUARESIZE +
                                                       SQUARESIZE /
                                                       2)), RADIUS)

    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT):
            if board[row][col] == 1:
                pygame.draw.circle(screen, RED, (int(col *
                                                     SQUARESIZE +
                                                     SQUARESIZE /
                                                     2), height -
                                                 int(row * SQUARESIZE +
                                                     SQUARESIZE /
                                                     2)), RADIUS)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, YELLOW, (int(col *
                                                        SQUARESIZE +
                                                        SQUARESIZE /
                                                        2), height -
                                                    int(row * SQUARESIZE +
                                                        SQUARESIZE /
                                                        2)), RADIUS)
    pygame.display.update()


board = create_board()
print_board(board)
game_over = False
turn = 0

# Initialize pygame
pygame.init()

# Define screen size
SQUARESIZE = 100

# Width and heigh of the board
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE/2 - 5)

screen = pygame.display.set_mode(size)

draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)

clock = pygame.time.Clock()
current_time = 0

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BG_COLOUR, (0, 0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED,
                                   (posx, int(SQUARESIZE/2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW,
                                   (posx, int(SQUARESIZE/2)), RADIUS)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BG_COLOUR, (0, 0, width, SQUARESIZE))
            # PLayer one turn
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))

                if is_valid_location(board, col):
                    turn += 1
                    turn = turn % 2
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    if win_check(board, 1):
                        label = myfont.render("Player 1 wins!!", 1, RED)
                        screen.blit(label, (40, 10))
                        game_over = True

            # PLayer two turn
            else:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
                if is_valid_location(board, col):
                    turn += 1
                    turn = turn % 2
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    if win_check(board, 2):
                        label = myfont.render("Player 1 wins!!", 1, YELLOW)
                        screen.blit(label, (40, 10))
                        game_over = True

            print_board(board)
            draw_board(board)

            if game_over:
                pygame.time.wait(5000)
    
    current_time = pygame.time.get_ticks()
    print(current_time)

    clock.tick(60)
