import pygame

class Strategy:
    """
    The Strategy class represents a strategy for monster movement.

    Methods:
        move(monster, field, player_position): Defines the movement logic for the monster.
    """

    def move(self, monster, field, player_position):
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

    def move(self, monster, field, player_position):
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

    def move(self, monster, field, player_position):
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

    def move(self, monster, field, player_position):
        """
        Moves the monster aggressively towards the player on the field.

        Args:
            monster (Monster): The monster instance.
            field (Field): The game field.
            player_position (Position): The current position of the player.
        """

        distance = (player_position.x - monster.position.x) ** 2 + (player_position.y - monster.position.y) ** 2
        if distance <= monster.distance ** 2:
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

    def move(self, monster, field, player_position):
        """
        Moves the monster away from the player on the field.

        Args:
            monster (Monster): The monster instance.
            field (Field): The game field.
            player_position (Position): The current position of the player.
        """

        distance = (player_position.x - monster.position.x) ** 2 + (player_position.y - monster.position.y) ** 2
        if distance <= monster.distance ** 2:
            if player_position.x > monster.position.x:
                monster.position.x -= monster.speed
            elif player_position.x < monster.position.x:
                monster.position.x += monster.speed
            if player_position.y > monster.position.y:
                monster.position.y -= monster.speed
            elif player_position.y < monster.position.y:
                monster.position.y += monster.speed