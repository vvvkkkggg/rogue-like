from model.position import Position
from model.strategy import (
    AggressiveStrategy,
    PassiveStrategy,
    CowardlyStrategy,
    SameTypeCollisionAvoidanceStrategy,
)
import pygame
import copy
import random


class Monster:
    """
    The Monster class represents a monster character in the game.

    Attributes:
        position (Position): The current position of the monster.
        strategy (Strategy): The strategy used by the monster for movement.
        hp (int): The health points of the monster.
        attack (int): The attack strength of the monster.
        defense (int): The defense strength of the monster.
        copy_probability(float): Probability of monster clone.
    """

    def __init__(
        self, position, strategy, hp, attack, defense, copy_probability=0
    ):
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
        self.copy_probability = copy_probability

    def move(self, field, player_position, monsters=None):
        """
        Moves the monster according to its strategy.

        Args:
            field (Field): The game field where the monster is moving.
            player_position (Position): The current position of the player.
        """
        self.strategy.move(self, field, player_position, monsters)

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

    def should_clone(self):
        """
        Determines whether to clone the monster based on the probability.

        Returns:
            bool: True if the monster should be cloned, False otherwise.
        """
        return random.random() < self.copy_probability

    def clone(self):
        """
        Creates a copy of this Monster instance.

        Returns:
            Monster: A new instance of the Monster class with the same attributes.
        """
        return copy.deepcopy(self)


class AggressiveMonster(Monster):
    def __init__(self, position):
        super().__init__(
            position,
            AggressiveStrategy(),
            hp=30,
            attack=20,
            defense=5,
            copy_probability=-1,
        )


class PassiveMonster(Monster):
    def __init__(self, position):
        super().__init__(
            position,
            PassiveStrategy(),
            hp=20,
            attack=5,
            defense=10,
            copy_probability=-1,
        )


class CowardlyMonster(Monster):
    def __init__(self, position):
        super().__init__(
            position,
            CowardlyStrategy(),
            hp=15,
            attack=5,
            defense=5,
            copy_probability=-1,
        )


class MoldMonster(Monster):
    def __init__(self, position):
        super().__init__(
            position,
            SameTypeCollisionAvoidanceStrategy(),
            hp=1,
            attack=5,
            defense=0,
            copy_probability=0.01,
        )
