"""Connect 5 Game."""
# Videos from https://www.youtube.com/@freecodecamp/videos
# were used in the development of this code

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


def create_board() -> None:
    """
    Create a 7x8 game board filled with zeros.

    Returns:
        numpy.ndarray: A 7x8 display representing the connect 5
                       game board will each spot filled in with a zero.
    """
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece(board: List[List[str]], row: int, col: int,
               piece: str) -> List[List[str]]:
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


def is_valid_location(board: List[List[str]], col: int) -> bool:
    """
    Check if a given column is a valid location for placing a disc.

    Args:
        board (List[List[str]]): The game board represented
                                 as a 2D list of strings.
        col (int): The column to be checked.

    Returns:
        bool: True if the column is vacant
              (all rows are empty strings), False otherwise.
    """
    return board[5][col] != ""


def get_next_open_row(board: List[List[str]], col: int) -> int:
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


def win_check (board, piece):
    """Checks for winning move in all possible ways"""
    # Check for 5 verticle in a row
    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT-3):
            if (
                board[row][col] == piece and
                board[row + 1][col] == piece and
                board[row + 2][col] == piece and
                board[row + 3][col] == piece
               ):
                return True


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


while not game_over:
    # Ask for player 1 input
    if turn == 0:
        col = int(input("Player 1, Make your Selection(0-7):"))
        # Player 1 will drop a piece on the board
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, "1")
    # Ask for player 2 input
    else:
        col = int(input("Player 2, Make your Selection(0-7):"))
        # Player 2 will drop a piece on the board
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, "2")

    print_board(board)

    turn += 1
    turn = turn % 2
