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
BUTTON_COLOR = (0, 128, 255)
BUTTON_HOVER_COLOR = (0, 0, 255)


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
        font = pygame.font.Font(None, 36)
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
        self.title = (pygame.font.Font(None, 72).render
                      ("Connect 5", True, WHITE))
        self.title_rect = self.title.get_rect(center=(width // 2, 100))
        self.play_button = Button(300, 250, 200, 50, "Play", self.play_game)
        self.gimmicks_button = (Button(300, 320, 200, 50,
                                "Gimmicks", self.show_gimmicks))
        self.exit_button = Button(300, 390, 200, 50, "Exit", self.exit_game)
        self.buttons = ([self.play_button, self.
                         gimmicks_button, self.exit_button])
        self.width = width  # Store the window size
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

        This method opens a new window to display game
        gimmicks text and waits until the window is closed.

        Returns:
        None
        """
        gimmicks_window = pygame.display.set_mode((400, 300))
        pygame.display.set_caption("Gimmicks")
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    # Reset the window size to the original size
                    pygame.display.set_mode((self.width, self.height))
            # Display gimmicks text
            gimmicks_text = (pygame.font.Font(None, 24).render
                             ("PLACEHOLDER", True, WHITE))
            gimmicks_window.fill(BLACK)
            gimmicks_window.blit(gimmicks_text, (50, 100))
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
pygame.display.set_caption("Connect 5")

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
            if event.button == 1:  # Left mouse button
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
