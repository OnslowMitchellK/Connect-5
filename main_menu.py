"""Main menu for Connect 5."""

import pygame
import sys
import connect5
from typing import Optional, Callable

# Initialize Pygame
pygame.init()

# Constants
ORIGINAL_WIDTH, ORIGINAL_HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LMB = 1  # left mouse button
WINDOW_TITLE = "Connect 5"
TITLE_FONT_SIZE = 72

BUTTON_COLOR = (0, 128, 255)
BUTTON_HOVER_COLOR = (0, 0, 255)
BUTTON_FONT_SIZE = 36
GIMMICKS_FONT_SIZE = 24

GIMMICKS_WIDTH = 600
GIMMICKS_HEIGHT = 400
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50

PLAY_BUTTON_X = 300
PLAY_BUTTON_Y = 250
GIMMICKS_BUTTON_X = 300
GIMMICKS_BUTTON_Y = 320
GIMMICKS_WINDOW_X = 50
GIMMICKS_WINDOW_Y_ADJUST = 30
EXIT_BUTTON_X = 300
EXIT_BUTTON_Y = 390


# Create a Button class
class Button:
    """
    A class to represent a clickable button in the game.

    Attributes:
    - x (int): The x-coordinate of the button.
    - y (int): The y-coordinate of the button.
    - width (int): The width of the button.
    - height (int): The height of the button.
    - text (str): The text displayed on the button.
    - action (function): The function to execute when the button is clicked.
    """

    def __init__(self, x: int, y: int, width: int, height: int,
                 text: str, action: Optional[Callable[[], None]] = None):
        """
        Initialize a Button instance.

        Args:
            x (int): The x-coordinate of the button.
            y (int): The y-coordinate of the button.
            width (int): The width of the button.
            height (int): The height of the button.
            text (str): The text displayed on the button.
            action (Optional[Callable[[], None]]): The
            function to execute when the button is clicked.

        The constructor initializes a Button instance with the provided
        coordinates, dimensions, text, and an optional action function.
        The color is set to BUTTON_COLOR, and the 'hovered' attribute is
        initially set to False.

        Returns:
            None
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.color = BUTTON_COLOR
        self.hovered = False

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draw the button on the screen.

        Args:
        - screen (pygame.Surface): The game screen to draw the button on.
        """
        color = self.hovered and BUTTON_HOVER_COLOR or self.color
        pygame.draw.rect(screen, color, self.rect)
        font = pygame.font.Font(None, BUTTON_FONT_SIZE)
        text = font.render(self.text, True, WHITE)
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)


# Create a MainMenu class
class MainMenu:
    """
    A class to represent the main menu of the game.

    Attributes:
    - width (int): The width of the game window.
    - height (int): The height of the game window.
    """

    def __init__(self, width: int, height: int) -> None:
        """
        Initialize an instance of YourClassName.

        Parameters:
            width (int): The width of the window.
            height (int): The height of the window.

        This constructor initializes the class instance with the specified
        window dimensions and creates various buttons for a main menu.
        """
        self.title = (pygame.font.Font(None, TITLE_FONT_SIZE).render
                      ("Connect 5", True, WHITE))
        self.title_rect = self.title.get_rect(center=(width // 2, 100))
        # dimentions and text for play button
        self.play_button = Button(PLAY_BUTTON_X, PLAY_BUTTON_Y, BUTTON_WIDTH,
                                  BUTTON_HEIGHT, "Play", self.play_game)
        # dimentions and text for gimmicks button
        self.gimmicks_button = (Button(GIMMICKS_BUTTON_X,
                                       GIMMICKS_BUTTON_Y,
                                       BUTTON_WIDTH,
                                       BUTTON_HEIGHT,
                                       "Gimmicks",
                                       self.show_gimmicks))
        # dimentions and text for exit button
        self.exit_button = Button(EXIT_BUTTON_X,
                                  EXIT_BUTTON_Y,
                                  BUTTON_WIDTH,
                                  BUTTON_HEIGHT,
                                  "Exit",
                                  self.exit_game)
        self.buttons = ([self.play_button, self.
                         gimmicks_button, self.exit_button])
        self.width = width
        self.height = height

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draw the main menu on the screen.

        Args:
        - screen (pygame.Surface): The game screen to draw the main menu on.
        """
        screen.blit(self.title, self.title_rect)
        for button in self.buttons:
            button.draw(screen)

    def play_game(self) -> None:
        """Start the game when the "Play" button is clicked."""
        game = connect5.Connect5Game()
        game.run_game()

    def show_gimmicks(self) -> None:
        """
        Display game gimmicks when clicked.

        This method opens a new window to display game gimmicks text and waits
        until the window is closed. The gimmicks_text list contains the lines
        of text describing the game's gimmicks.

        Gimmicks:
        - This is Connect 5: That means it takes 5 checkers in a row to win
        instead of the usual 4 in a row like a classic game of Connect 4.
        - Hidden Turn Timer: There is a hidden turn timer of 20 seconds which
        should add some suspense, excitement, and pressure for the players.

        Returns:
        None
        """
        # This list is for the lines that show up
        # when you click the "Gimmicks" button
        gimmicks_text = [
            "This is Connect 5:",
            "That means it takes 5 checkers in a row to win instead",
            "of the usual 4 in a row like a classic game of connect 4.",
            "Hidden Turn Timer:",
            "There is a hidden turn timer of 20 seconds which should",
            "add some suspense, excitement, and pressure for the players."
        ]

        gimmicks_window = pygame.display.set_mode((GIMMICKS_WIDTH,
                                                   GIMMICKS_HEIGHT))
        pygame.display.set_caption("Gimmicks")
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    # Reset the window size to the original size
                    pygame.display.set_mode((self.width, self.height))
            gimmicks_window.fill(BLACK)
            # Initial Y position for the first line of text
            gimmicks_window_y = 100
            font = pygame.font.Font(None, GIMMICKS_FONT_SIZE)
            for line in gimmicks_text:
                line_text = font.render(line, True, WHITE)
                gimmicks_window.blit(line_text, (GIMMICKS_WINDOW_X,
                                                 gimmicks_window_y))
                # Adjust Y position for the next line
                gimmicks_window_y += GIMMICKS_WINDOW_Y_ADJUST

            pygame.display.flip()

    def exit_game(self) -> None:
        """
        Exit the game when the "Exit" button is clicked.

        This method gracefully shuts down the game and exits the application.

        Returns:
        None
        """
        pygame.quit()
        sys.exit()


# Create the MainMenu object with the original window size
main_menu = MainMenu(ORIGINAL_WIDTH, ORIGINAL_HEIGHT)

# Create the game window
screen = pygame.display.set_mode((main_menu.width, main_menu.height))
pygame.display.set_caption(WINDOW_TITLE)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            for button in main_menu.buttons:
                if button.rect.collidepoint(event.pos):
                    button.hovered = True
                else:
                    button.hovered = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == LMB:
                for button in main_menu.buttons:
                    if button.rect.collidepoint(event.pos):
                        if button.action:
                            button.action()
    screen.fill(BLACK)
    main_menu.draw(screen)
    pygame.display.flip()

# Quit the game
pygame.quit()
sys.exit()
