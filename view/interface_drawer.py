import pygame

class InterfaceDrawer:
    """
    The InterfaceDrawer class is responsible for drawing the game interface on the screen.

    Attributes:
        screen (pygame.Surface): The Pygame surface on which to draw the interface.
    """
    def __init__(self, screen):
        """
        Initializes a new instance of the InterfaceDrawer class.

        Args:
            screen (pygame.Surface): The Pygame surface on which to draw the interface.
        """
        self.screen = screen

    def draw(self, game_state):
        """
        Draws the game state on the screen.

        Args:
            game_state (dict): The current state of the game.
        """
        self.screen.fill((0, 0, 0))  # Clear screen with black
        self.draw_player(game_state['player'])
        for monster in game_state['monsters']:
            self.draw_monster(monster)

    def draw_player(self, player):
        """
        Draws the player on the screen.

        Args:
            player (dict): The state of the player.
        """
        x, y = player['position']
        pygame.draw.rect(self.screen, (0, 255, 0), (x * 20, y * 20, 20, 20))

        health_x = x * 20
        health_y = y * 20 - 20

        font = pygame.font.Font(None, 24)
        text_surface = font.render(f"HP: {player['hp']}", True, (255, 255, 255))
        self.screen.blit(text_surface, (health_x, health_y))

        defense_surface = font.render(f"Defense: {player['defense']}", True, (255, 255, 255))
        self.screen.blit(defense_surface, (health_x, health_y + 20))

    def draw_monster(self, monster):
        """
        Draws a monster on the screen.

        Args:
            monster (dict): The state of the monster.
        """
        x, y = monster['position']
        color = (255, 0, 0) if monster['type'] == 'AggressiveMonster' else (255, 255, 0) if monster[
                                                                                                'type'] == 'PassiveMonster' else (
        0, 0, 255)
        pygame.draw.rect(self.screen, color, (x * 20, y * 20, 20, 20))

        health_x = x * 20
        health_y = y * 20 - 20

        font = pygame.font.Font(None, 24)
        text_surface = font.render(f"HP: {monster['hp']}", True, (255, 255, 255))
        self.screen.blit(text_surface, (health_x, health_y))

        defense_surface = font.render(f"Defense: {monster['defense']}", True, (255, 255, 255))
        self.screen.blit(defense_surface, (health_x, health_y + 20))
