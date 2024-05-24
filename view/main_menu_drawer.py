import pygame

class MainMenuDrawer:
    """
    The MainMenuDrawer class is responsible for drawing the main menu on the screen.

    Attributes:
        screen: The Pygame screen surface to draw on.
    """
    def __init__(self, screen):
        """
        Initializes a new instance of the MainMenuDrawer class.

        Args:
            screen: The Pygame screen surface to draw on.
        """
        self.screen = screen

    def draw(self):
        """
        Draws the main menu on the screen.
        """
        # Clear the screen
        self.screen.fill((0, 0, 0))

        # Set up the font
        font = pygame.font.Font(None, 74)

        # Render and draw the text "Main Menu"
        text = font.render('Main Menu', True, (255, 255, 255))
        self.screen.blit(text, (250, 100))

        # Update the display
        pygame.display.flip()
