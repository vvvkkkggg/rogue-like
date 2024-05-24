import pygame
from model.game import Game

class GameController:
    """
    The GameController class is responsible for handling user input and updating the game state.
    """
    def __init__(self):
        """
        Initializes the GameController instance and creates a new Game instance.
        """
        self.game = Game()

    def handle_event(self, event):
        """
        Handles a given Pygame event, updating the game state based on user input.

        Args:
            event (pygame.event.Event): The event to handle.
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.game.move_player("up")
            elif event.key == pygame.K_s:
                self.game.move_player("down")
            elif event.key == pygame.K_a:
                self.game.move_player("left")
            elif event.key == pygame.K_d:
                self.game.move_player("right")

    def update(self):
        """
        Updates the game state. This method should be called regularly, such as once per frame.
        """
        self.game.update()

    def get_game_state(self):
        """
        Returns the current state of the game.

        Returns:
            The current state of the game, as defined by the Game class's get_state method.
        """
        return self.game.get_state()
