from model.monster import Monster
from model.player import Player
from model.strategy import AggressiveStrategy
from model.builder import DefaultMapBuilder, GenerateMapBuilder


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


class MapFactory:
    """
    MapFactory creates instances of map builders based on the builder name.
    """

    @staticmethod
    def get_builder(builder_name, width=20, height=20, filename=None):
        """
        Returns an instance of a map builder based on the given builder name.

        Args:
            builder_name (str): The name of the builder ('default', 'generate').
            width (int): The width of the map (used for 'generate' builder).
            height (int): The height of the map (used for 'generate' builder).
            filename (str, optional): The name of the file containing the map data (used for 'default' builder).

        Returns:
            MapBuilder: An instance of a map builder.
        """
        if builder_name == "default":
            return DefaultMapBuilder(filename)
        elif builder_name == "generate":
            return GenerateMapBuilder(width, height)
        else:
            raise ValueError(f"Unknown builder name: {builder_name}")
