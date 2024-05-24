class Strategy:
    """
    The Strategy class represents a strategy for monster movement.

    Methods:
        move(monster, field): Defines the movement logic for the monster.
    """
    def move(self, monster, field):
        """
        Defines the movement logic for the monster.

        Args:
            monster: The monster instance.
            field: The game field.
        """
        pass


class RandomStrategy(Strategy):
    """
    The RandomStrategy class represents a strategy for random movement.

    Methods:
        move(monster, field): Moves the monster randomly on the field.
    """
    def move(self, monster, field):
        """
        Moves the monster randomly on the field.

        Args:
            monster: The monster instance.
            field: The game field.
        """
        pass


class PassiveStrategy(Strategy):
    """
    The PassiveStrategy class represents a strategy for passive movement.

    Methods:
        move(monster, field): Moves the monster passively on the field.
    """
    def move(self, monster, field):
        """
        Moves the monster passively on the field.

        Args:
            monster: The monster instance.
            field: The game field.
        """
        pass


class AggressiveStrategy(Strategy):
    """
    The AggressiveStrategy class represents a strategy for aggressive movement.

    Methods:
        move(monster, field): Moves the monster aggressively on the field.
    """
    def move(self, monster, field):
        """
        Moves the monster aggressively on the field.

        Args:
            monster: The monster instance.
            field: The game field.
        """
        pass
