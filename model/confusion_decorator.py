import random


class ConfusionDecorator:
    """
    The ConfusionDecorator class represents a temporary confusion effect applied to a monster.

    Attributes:
        strategy (Strategy): The original strategy of the monster.
        turns_remaining (int): The number of turns the confusion effect lasts.
    """

    def __init__(self, strategy, turns):
        """
        Initializes a new instance of the ConfusionDecorator class.

        Args:
            strategy (Strategy): The original strategy of the monster.
            turns (int): The number of turns the confusion effect lasts.
        """
        self.strategy = strategy
        self.turns_remaining = turns

    def move(self, monster, field, player_position, monsters=None):
        """
        Moves the monster according to the confusion effect or its original strategy.

        Args:
            monster (Monster): The monster instance.
            field (Field): The game field.
            player_position (Position): The current position of the player.
        """
        if self.turns_remaining > 0:
            self.turns_remaining -= 1
            directions = ["up", "down", "left", "right"]
            direction = random.choice(directions)
            if direction == "up":
                monster.position.y -= 1
            elif direction == "down":
                monster.position.y += 1
            elif direction == "left":
                monster.position.x -= 1
            elif direction == "right":
                monster.position.x += 1
        else:
            self.strategy.move(monster, field, player_position)
