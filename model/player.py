from model.position import Position

class Player:
    """
    The Player class represents the player character in the game.

    Attributes:
        position (Position): The current position of the player on the game field.
    """
    def __init__(self):
        """
        Initializes a new instance of the Player class with the default position (0, 0).
        """
        self.position = Position(0, 0)

    def move(self, direction, field):
        """
        Moves the player character in the specified direction on the game field.

        Args:
            direction (str): The direction in which to move the player ('up', 'down', 'left', or 'right').
            field (Field): The game field on which the player is moving.
        """
        if direction == "up":
            self.position.y -= 1
        elif direction == "down":
            self.position.y += 1
        elif direction == "left":
            self.position.x -= 1
        elif direction == "right":
            self.position.x += 1
