"""Connect 5 Game."""
# Videos from https://www.youtube.com/@freecodecamp/videos
# were used to aid the development of this section of code

import numpy as np
import pygame
import sys
import math
from typing import List

# Constants
PLAYER_ONE = 0
PLAYER_TWO = 1

BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BG_COLOR = (0, 0, 0)

EMPTY_CELL = 0
SQUARESIZE = 100

ROW_COUNT = 7
COLUMN_COUNT = 8
ROW_MINUS_ONE = 1

TICKRATE = 60
TIMER_MAX = 20000
TIMER_RESET = 0
AUTO_EXIT_TIME = 5000


class Connect5Game:
    """
    A class representing a Connect 5 game.

    Attributes:
        BLUE (tuple): RGB color code for blue.
        RED (tuple): RGB color code for red.
        YELLOW (tuple): RGB color code for yellow.
        BG_COLOUR (tuple): RGB color code for the background (black).
        ROW_COUNT (int): Number of rows on the game board.
        COLUMN_COUNT (int): Number of columns on the game board.
        board (List[List[int]]): 2D list representing the game board.
        turn (int): Current player's turn (0 for player 1, 1 for player 2).
        game_over (bool): Indicates if the game is over.

    Methods:
        create_board() -> List[List[int]]:
            Create an empty game board.

        drop_piece(row: int, col: int, piece: int):
            Place a game piece on the game board.

        is_valid_location(col: int) -> bool:
            Check if a given column is a valid location for placing a checker.

        get_next_open_row(col: int) -> int:
            Find the next open row in a given column.

        print_board():
            Print the game board.

        win_check(piece: int) -> bool:
            Check for a winning move on the game board.

    Usage:
    - Create an instance of Connect5Game to start a new game.
    - Use the provided methods to play and manage the game.
    """

    def __init__(self) -> None:
        """
        Initialize a Connect5Game instance.

        This constructor initializes a new Connect5Game
        instance with default values for attributes.
        - BLUE: RGB color code for blue.
        - RED: RGB color code for red.
        - YELLOW: RGB color code for yellow.
        - BG_COLOUR: RGB color code for the background.
        - ROW_COUNT: Number of rows on the game board.
        - COLUMN_COUNT: Number of columns on the game board.
        - board: 2D list representing the game board.
        - turn: Current player's turn (0 for player 1, 1 for player 2).
        - game_over: Indicates if the game is over.

        Returns:
        None
        """
        self.BLUE = BLUE
        self.RED = RED
        self.YELLOW = YELLOW
        self.BG_COLOUR = BG_COLOR
        self.ROW_COUNT = ROW_COUNT
        self.COLUMN_COUNT = COLUMN_COUNT
        self.EMPTY_CELL = EMPTY_CELL
        self.board = self.create_board()
        self.turn = 0
        self.game_over = False

    def create_board(self) -> List[List[int]]:
        """
        Create an empty game board for Connect 5.

        Returns:
        List[List[int]]: A 2D list representing the game
        board where each element is initialized to 0.
        """
        board = [[EMPTY_CELL] * self.COLUMN_COUNT
                 for _ in range(self.ROW_COUNT)]
        return board

    def drop_piece(self, row: int, col: int, piece: int) -> None:
        """
        Place a game piece on the game board.

        Args:
            row (int): The row where the piece will be placed.
            col (int): The column where the piece will be placed.
            piece (int): The piece to place on the game board.

        This method updates the game board with the
        specified piece at the given row and column.
        """
        self.board[row][col] = piece

    def is_valid_location(self, col: int) -> bool:
        """
        Check if a given column is a valid location for placing a checker.

        Args:
            col (int): The column to check.

        Returns:
            bool: True if the column is a valid location
            for placing a checker, False otherwise.
        """
        return self.board[self.ROW_COUNT -
                          ROW_MINUS_ONE][col] == EMPTY_CELL

    def get_next_open_row(self, col: int) -> int:
        """
        Find the next open row in a given column.

        Args:
            col (int): The column to find the next open row in.

        Returns:
            int: The index of the next open row, or -1 if the column is full.
        """
        for row in range(self.ROW_COUNT):
            # Checks if the row for the column is full
            if self.board[row][col] == EMPTY_CELL:
                return row
        return - ROW_MINUS_ONE  # -1 if column is full

    def print_board(self) -> None:
        """
        Print the game board.

        This method prints the current state of the game board,
        flipping it vertically (from top to bottom) for display.
        It helps visualize the game board's current layout.
        """
        print(np.flip(self.board, EMPTY_CELL))

    def win_check(self, piece: int) -> bool:
        """
        Check for a winning move on the Connect 5 game board.

        Args:
            piece (int): The piece (player) to check for a win.

        This method checks for a winning move in all possible
        directions on the Connect 5 game board.
        It returns True if a winning combination is found for
        the specified piece; otherwise, it returns False.

        Args:
            piece (int): The player (piece) to check for a win
            (0 for player 1, 1 for player 2).

        Returns:
            bool: True if a winning combination is found, False otherwise.
        """
        # Check for 5 verticle checkers in a row
        for row in range(self.ROW_COUNT - 4):
            for col in range(self.COLUMN_COUNT):
                # If 5 checkers in a row win_check will become True
                if all(self.board[row + i][col] == piece for i in range(5)):
                    return True

        # Check for 5 horizontal checkers in a row
        for row in range(self.ROW_COUNT):
            for col in range(self.COLUMN_COUNT - 4):
                # If 5 checkers in a row win_check will become True
                if all(self.board[row][col + i] == piece for i in range(5)):
                    return True

        # Checks for 5 negativly sloped diagonal checkers in a row
        for row in range(4, self.ROW_COUNT):
            for col in range(self.COLUMN_COUNT - 4):
                # If 5 checkers in a row win_check will become True
                if all(self.board[row - i][col + i]
                       == piece for i in range(5)):
                    return True

        # Checks for 5 positively sloped diagonal checkers in a row
        for row in range(self.ROW_COUNT - 4):
            for col in range(self.COLUMN_COUNT - 4):
                # If 5 checkers in a row win_check will become True
                if all(self.board[row + i][col + i]
                       == piece for i in range(5)):
                    return True

        return False

    def draw_board(self) -> None:
        """
        Draw the Connect 5 game board on the screen.

        This method visually represents the current
        state of the game board on the game screen.
        It draws the game grid and any player checkers that are on the board.

        Returns:
        None
        """
        # This part of code draws the blue grid that the checkers fall into
        for col in range(self.COLUMN_COUNT):
            for row in range(self.ROW_COUNT):
                pygame.draw.rect(self.screen, self.BLUE,
                                 (col * self.SQUARESIZE, row *
                                  self.SQUARESIZE + self.SQUARESIZE,
                                  self.SQUARESIZE, self.SQUARESIZE))
                pygame.draw.circle(
                    self.screen, self.BG_COLOUR,
                    (int(col * self.SQUARESIZE + self.SQUARESIZE / 2),
                        (row * self.SQUARESIZE + self.SQUARESIZE +
                         self.SQUARESIZE / 2)),
                    self.RADIUS
                )

        # This part of code draws the red or
        # yellow checkers that the player places
        for col in range(self.COLUMN_COUNT):
            for row in range(self.ROW_COUNT):
                if self.board[row][col] == 1:
                    pygame.draw.circle(self.screen, self.RED, (int(col *
                                       self.SQUARESIZE +
                                       self.SQUARESIZE /
                                       2), self.height -
                                       int(row * self.SQUARESIZE +
                                       self.SQUARESIZE /
                                       2)), self.RADIUS)
                elif self.board[row][col] == 2:
                    pygame.draw.circle(self.screen, self.YELLOW, (int(col *
                                       self.SQUARESIZE +
                                       self.SQUARESIZE /
                                       2), self.height -
                                       int(row * self.SQUARESIZE +
                                       self.SQUARESIZE /
                                       2)), self.RADIUS)
        pygame.display.update()

    def run_game(self) -> None:
        """
        Run the Connect 5 game.

        This method initializes the game, handles player
        moves,checks for wins, and manages the game loop.

        The game loop continues until one of the
        players wins or the game is exited.

        Returns:
        None
        """
        pygame.init()

        self.SQUARESIZE = SQUARESIZE

        # Width and height of the board
        self.width = self.COLUMN_COUNT * self.SQUARESIZE
        self.height = (self.ROW_COUNT + 1) * self.SQUARESIZE

        size = (self.width, self.height)

        self.RADIUS = int(self.SQUARESIZE/2 - 5)

        self.screen = pygame.display.set_mode(size)

        self.draw_board()
        pygame.display.update()

        myfont = pygame.font.SysFont("monospace", 75)

        clock = pygame.time.Clock()
        current_time = 0
        player_one_button_press_time = 0
        player_two_button_press_time = 0
        first_move = False
        # Check if game is still running or not
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(self.screen, self.BG_COLOUR,
                                     (0, 0, self.width, self.SQUARESIZE))
                    posx = event.pos[0]
                    if self.turn == PLAYER_ONE:
                        pygame.draw.circle(self.screen, self.RED,
                                           (posx, int(self.SQUARESIZE
                                                      / 2)), self.RADIUS)
                    else:
                        pygame.draw.circle(self.screen, self.YELLOW,
                                           (posx, int(self.SQUARESIZE
                                                      / 2)), self.RADIUS)
                    pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    first_move = True
                    pygame.draw.rect(self.screen, self.BG_COLOUR,
                                     (0, 0, self.width, self.SQUARESIZE))
                    # Player one's turn
                    if self.turn == PLAYER_ONE:
                        posx = event.pos[0]
                        col = int(math.floor(posx/self.SQUARESIZE))

                        if self.is_valid_location(col):
                            self.turn += 1
                            self.turn = self.turn % 2
                            row = self.get_next_open_row(col)
                            self.drop_piece(row, col, 1)

                            if self.win_check(1):
                                label = myfont.render("Player 1 wins!!",
                                                      1, self.RED)
                                self.screen.blit(label, (40, 10))
                                self.game_over = True

                    # Player two's turn
                    else:
                        posx = event.pos[0]
                        col = int(math.floor(posx/self.SQUARESIZE))
                        if self.is_valid_location(col):
                            self.turn += 1
                            self.turn = self.turn % 2
                            row = self.get_next_open_row(col)
                            self.drop_piece(row, col, 2)

                            if self.win_check(2):
                                label = myfont.render("Player 2 wins!!",
                                                      1, self.YELLOW)
                                self.screen.blit(label, (40, 10))
                                self.game_over = True

                    self.print_board()
                    self.draw_board()

                    # Auto closes game after 5 seconds after a win
                    if self.game_over:
                        pygame.time.wait(AUTO_EXIT_TIME)

            # Code for hidden turn timer
            current_time = pygame.time.get_ticks()
            # Checks if it is first move to start timer
            if first_move:
                match self.turn:
                    case 0:
                        player_one_button_press_time = pygame.time.get_ticks()
                    case 1:
                        player_two_button_press_time = pygame.time.get_ticks()
            else:
                player_one_button_press_time = pygame.time.get_ticks()
                player_two_button_press_time = pygame.time.get_ticks()
            # Checks if player 1's timer reaches 20 seconds
            if current_time - player_one_button_press_time > TIMER_MAX:
                print("1")
                self.turn = PLAYER_ONE
                player_two_button_press_time = pygame.time.get_ticks()
                player_one_button_press_time = TIMER_RESET
            # Checks if player 2's timer reaches 20 seconds
            if current_time - player_two_button_press_time > TIMER_MAX:
                print("2")
                self.turn = PLAYER_TWO
                player_one_button_press_time = pygame.time.get_ticks()
                player_two_button_press_time = TIMER_RESET

            clock.tick(TICKRATE)
            sys.exit


if __name__ == "__main__":
    game = Connect5Game()
    game.run_game()
