import pygame


class GameMenuDrawer:
    """
    The GameMenuDrawer class is responsible for drawing the game menu on the screen.

    Attributes:
        screen: The Pygame screen surface to draw on.
    """

    def __init__(self, screen):
        """
        Initializes a new instance of the GameMenuDrawer class.

        Args:
            screen: The Pygame screen surface to draw on.
        """
        self.screen = screen

    def draw(self):
        """
        Draws the game menu on the screen.
        """
        self.screen.fill((0, 0, 0))

        font = pygame.font.Font(None, 74)

        text = font.render("Game Menu", True, (255, 255, 255))
        self.screen.blit(text, (250, 100))

        pygame.display.flip()
