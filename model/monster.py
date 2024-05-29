from model.position import Position
from model.strategy import AggressiveStrategy, PassiveStrategy, CowardlyStrategy
import pygame

class Monster:
    """
    The Monster class represents a monster character in the game.

    Attributes:
        position (Position): The current position of the monster.
        strategy (Strategy): The strategy used by the monster for movement.
        hp (int): The health points of the monster.
        attack (int): The attack strength of the monster.
        defense (int): The defense strength of the monster.
    """
    def __init__(self, position, strategy, hp, attack, defense, speed, distance):
        """
        Initializes a new instance of the Monster class.

        Args:
            position (Position): The initial position of the monster.
            strategy (Strategy): The strategy used by the monster for movement.
            hp (int): The health points of the monster.
            attack (int): The attack strength of the monster.
            defense (int): The defense strength of the monster.
        """
        self.position = position
        self.strategy = strategy
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.distance = distance

    def move(self, field, player_position):
        """
        Moves the monster according to its strategy.

        Args:
            field (Field): The game field where the monster is moving.
            player_position (Position): The current position of the player.
        """
        self.strategy.move(self, field, player_position)

    def attack_player(self, player):
        """
        Attacks the player, inflicting damage based on the monster's attack strength and the player's defense.

        Args:
            player (Player): The player to attack.
        """
        damage = self.attack - player.defense
        if damage > 0:
            player.take_damage(damage)

    def take_damage(self, damage):
        """
        Reduces the monster's HP by the specified damage amount.

        Args:
            damage (int): The amount of damage to inflict.
        """
        self.hp -= damage * 0.1


class AggressiveMonster(Monster):
    def __init__(self, position):
        super().__init__(position, AggressiveStrategy(), hp=30, attack=20, defense=5, speed = 0.2, distance = 4)

class PassiveMonster(Monster):
    def __init__(self, position):
        super().__init__(position, PassiveStrategy(), hp=20, attack=5, defense=10, speed = 0, distance = 1)

class CowardlyMonster(Monster):
    def __init__(self, position):
        super().__init__(position, CowardlyStrategy(), hp=15, attack=5, defense=5, speed = 0.1, distance = 4)
