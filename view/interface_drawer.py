import pygame


class InterfaceDrawer:
    """
    The InterfaceDrawer class is responsible for drawing the game interface on the screen.

    Attributes:
        screen: The Pygame screen surface to draw on.
    """

    def __init__(self, screen):
        """
        Initializes a new instance of the InterfaceDrawer class.

        Args:
            screen: The Pygame screen surface to draw on.
        """
        self.screen = screen

    def draw(self, game_state):
        """
        Draws the game interface on the screen.

        Args:
            game_state (dict): The current state of the game, including field and player.
        """
        # Clear the screen
        self.screen.fill((0, 0, 0))

        # Draw the game field
        field = game_state["field"]
        for y, row in enumerate(field.cells):
            for x, cell in enumerate(row):
                if cell:
                    color = (255, 255, 255)  # White for cells with content
                else:
                    color = (0, 0, 0)  # Black for empty cells
                pygame.draw.rect(self.screen, color, pygame.Rect(x * 32, y * 32, 32, 32))

        # Draw the player
        player = game_state["player"]
        pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(player.position.x * 32, player.position.y * 32, 32, 32))
