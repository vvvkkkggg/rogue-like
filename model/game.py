from model.field import Field
from model.player import Player

class Game:
    """
    The Game class represents the game state and logic.

    Attributes:
        field (Field): The game field.
        player (Player): The player character.
    """
    def __init__(self):
        """
        Initializes a new instance of the Game class with a field and a player.
        """
        self.field = Field()
        self.player = Player()

    def move_player(self, direction):
        """
        Moves the player character in the specified direction.

        Args:
            direction (str): The direction in which to move the player ('up', 'down', 'left', or 'right').
        """
        self.player.move(direction, self.field)

    def update(self):
        """
        Updates the game state. This method could be used for game logic updates or animations.
        """
        pass

    def get_state(self):
        """
        Returns the current state of the game.

        Returns:
            dict: A dictionary containing the current state of the game, including the player and field.
        """
        return {
            "player": self.player,
            "field": self.field
        }
