class Monster:
    """
    The Monster class represents a monster character in the game.

    Attributes:
        position: The current position of the monster.
        strategy: The strategy used by the monster for movement.
    """
    def __init__(self, position, strategy):
        """
        Initializes a new instance of the Monster class.

        Args:
            position: The initial position of the monster.
            strategy: The strategy used by the monster for movement.
        """
        self.position = position
        self.strategy = strategy

    def move(self, field):
        """
        Moves the monster according to its strategy.

        Args:
            field: The game field where the monster is moving.
        """
        self.strategy.move(self, field)
