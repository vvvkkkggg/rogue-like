import pygame
from model.game import Game
from model.confusion_decorator import ConfusionDecorator
from model.monster import Monster

class GameController:
    """
    The GameController class is responsible for handling user input and updating the game state.
    """
    def __init__(self):
        """
        Initializes the GameController instance and creates a new Game instance.
        """
        self.game = Game()
        self.confused_monsters = []

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
            elif event.key == pygame.K_c:
                self.confuse_nearby_monsters()

    def update(self):
        """
        Updates the game state. This method should be called regularly, such as once per frame.
        """
        self.game.update()

    def get_game_state(self):
        """
        Returns the current state of the game.

        Returns:
            dict: The current state of the game.
        """
        return self.game.get_state()

    def confuse_nearby_monsters(self):
        """
        Confuses monsters that are in adjacent cells to the player.
        """
        player_distance = self.game.player.near_distance
        near_monster = self.game.player.near_monster

        if player_distance < 1:
            near_monster.strategy = ConfusionDecorator(near_monster.strategy, turns=3)
            self.confused_monsters.append(near_monster)
