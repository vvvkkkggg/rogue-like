import pygame


class GameDrawer:
    """
    The GameDrawer class is responsible for drawing the game state on the screen.

    Attributes:
        screen: The Pygame screen surface to draw on.
    """

    def __init__(self, screen):
        """
        Initializes a new instance of the GameDrawer class.

        Args:
            screen: The Pygame screen surface to draw on.
        """
        self.screen = screen

    def draw(self, game_state):
        """
        Draws the game state on the screen.

        Args:
            game_state (dict): The current state of the game, including field, player, and monsters.
        """
        self.screen.fill((0, 0, 0))

        field = game_state["field"]
        for y, row in enumerate(field.cells):
            for x, cell in enumerate(row):
                if cell:
                    color = (255, 255, 255)  # White for cells with content
                else:
                    color = (0, 0, 0)  # Black for empty cells
                pygame.draw.rect(
                    self.screen, color, pygame.Rect(x * 32, y * 32, 32, 32)
                )

        player = game_state["player"]
        pygame.draw.rect(
            self.screen,
            (0, 255, 0),
            pygame.Rect(player.position.x * 32, player.position.y * 32, 32, 32),
        )

        for monster in game_state["monsters"]:
            pygame.draw.rect(
                self.screen,
                (255, 0, 0),
                pygame.Rect(monster.position.x * 32, monster.position.y * 32, 32, 32),
            )

        pygame.display.flip()
