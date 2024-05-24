from model.monster import Monster
from model.player import Player
from model.strategy import AggressiveStrategy

class MonsterFactory:
    """
    The MonsterFactory class is responsible for creating instances of Monster.

    Attributes:
        None
    """
    def create_monster(self, position, strategy):
        """
        Creates a new instance of Monster with the given position and strategy.

        Args:
            position: The position of the monster.
            strategy: The strategy of the monster.

        Returns:
            Monster: A new instance of Monster.
        """
        return Monster(position, strategy)


class HumanFactory:
    """
    The HumanFactory class is responsible for creating instances of Player.

    Attributes:
        None
    """
    def create_human(self, position):
        """
        Creates a new instance of Player with the given position.

        Args:
            position: The position of the player.

        Returns:
            Player: A new instance of Player.
        """
        return Player(position)


class BossFactory:
    """
    The BossFactory class is responsible for creating instances of powerful Monster, also known as Boss.

    Attributes:
        None
    """
    def create_boss(self, position):
        """
        Creates a new instance of Monster with the given position and an aggressive strategy.

        Args:
            position: The position of the boss.

        Returns:
            Monster: A new instance of Monster with an aggressive strategy.
        """
        return Monster(position, AggressiveStrategy())
