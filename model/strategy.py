import pygame
import random


class Strategy:
    """
    The Strategy class represents a strategy for monster movement.

    Methods:
        move(monster, field, player_position): Defines the movement logic for the monster.
    """

    def move(self, monster, field, player_position, monsters=None):
        """
        Defines the movement logic for the monster.

        Args:
            monster (Monster): The monster instance.
            field (Field): The game field.
            player_position (Position): The current position of the player.
        """
        pass


class RandomStrategy(Strategy):
    """
    The RandomStrategy class represents a strategy for random movement.

    Methods:
        move(monster, field, player_position): Moves the monster randomly on the field.
    """

    def move(self, monster, field, player_position, monsters=None):
        """
        Moves the monster randomly on the field.

        Args:
            monster (Monster): The monster instance.
            field (Field): The game field.
            player_position (Position): The current position of the player.
        """
        pass


class PassiveStrategy(Strategy):
    """
    The PassiveStrategy class represents a strategy for passive movement.

    Methods:
        move(monster, field, player_position): Moves the monster passively on the field.
    """

    def move(self, monster, field, player_position, monsters=None):
        """
        Moves the monster passively on the field.

        Args:
            monster (Monster): The monster instance.
            field (Field): The game field.
            player_position (Position): The current position of the player.
        """
        pass


class AggressiveStrategy(Strategy):
    """
    The AggressiveStrategy class represents a strategy for aggressive movement.

    Methods:
        move(monster, field, player_position): Moves the monster aggressively on the field.
    """

    def move(self, monster, field, player_position, monsters=None):
        """
        Moves the monster aggressively towards the player on the field.

        Args:
            monster (Monster): The monster instance.
            field (Field): The game field.
            player_position (Position): The current position of the player.
        """

        distance = (player_position.x - monster.position.x) ** 2 + (
            player_position.y - monster.position.y
        ) ** 2
        if distance <= monster.distance**2:
            if player_position.x > monster.position.x:
                monster.position.x += monster.speed
            elif player_position.x < monster.position.x:
                monster.position.x -= monster.speed
            if player_position.y > monster.position.y:
                monster.position.y += monster.speed
            elif player_position.y < monster.position.y:
                monster.position.y -= monster.speed


class CowardlyStrategy(Strategy):
    """
    The CowardlyStrategy class represents a strategy for cowardly movement.

    Methods:
        move(monster, field, player_position): Moves the monster away from the player on the field.
    """

    def move(self, monster, field, player_position, monsters=None):
        """
        Moves the monster away from the player on the field.

        Args:
            monster (Monster): The monster instance.
            field (Field): The game field.
            player_position (Position): The current position of the player.
        """

        distance = (player_position.x - monster.position.x) ** 2 + (
            player_position.y - monster.position.y
        ) ** 2
        if distance <= monster.distance**2:
            if player_position.x > monster.position.x:
                monster.position.x -= monster.speed
            elif player_position.x < monster.position.x:
                monster.position.x += monster.speed
            if player_position.y > monster.position.y:
                monster.position.y -= monster.speed
            elif player_position.y < monster.position.y:
                monster.position.y += monster.speed


class SameTypeCollisionAvoidanceStrategy(Strategy):
    """
    The SameTypeCollisionAvoidanceStrategy class represents a strategy for avoiding collisions with monsters of the same type.

    Methods:
        get_near_monster_position(monster): Generates positions near the given monster.
        move(monster, field, player_position, monsters): Moves the monster to avoid collisions with monsters of the same type.

    Attributes:
        None
    """

    def get_near_monster_position(self, monster):
        """
        Generates positions near the given monster.

        Args:
            monster (Monster): The monster instance.

        Yields:
            tuple: A tuple representing a position near the monster.
        """

        for x in random.sample([-1, 0, 1], k=3):
            for y in random.sample([-1, 0, 1], k=3):
                yield monster.position.x + x, monster.position.y + y

    def move(self, monster, field, player_position, monsters):
        """
        Moves the monster to avoid collisions with monsters of the same type.

        Args:
            monster (Monster): The monster instance.
            field (Field): The game field.
            player_position (Position): The current position of the player.
            monsters (list): A list of all monsters on the field.
        """

        if not monsters:
            return

        monsters_positions = map(
            lambda monster: (monster.position.x, monster.position.y),
            filter(
                lambda another_monster: another_monster is not monster
                and type(another_monster) == type(monster),
                monsters,
            ),
        )

        if (monster.position.x, monster.position.y) not in monsters_positions:
            return

        for x, y in self.get_near_monster_position(monster):
            if (x, y) in monsters_positions:
                continue

            if not (0 <= x <= field.width and 0 <= y <= field.height):
                continue

            monster.position.x = x
            monster.position.y = y

            return
