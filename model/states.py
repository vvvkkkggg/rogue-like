from abc import ABC, abstractmethod

from model.strategy import (
    CowardlyStrategy,
    PassiveStrategy,
    RandomStrategy,
    AggressiveStrategy,
    SameTypeCollisionAvoidanceStrategy,
)


class State(ABC):
    """
    The State class represents the state of the monster. Each state defines
    a specific strategy for monster movement and behavior.

    Methods:
        enter_state(mob): Defines the logic for entering the state.
    """

    @abstractmethod
    def enter_state(self, mob):
        """
        Defines the logic for entering the state.

        Args:
            mob (Monster): The monster instance.
        """
        pass


class PassiveState(State):
    """
    The PassiveState class represents the passive state of the monster.
    In this state, the monster moves passively using PassiveStrategy.

    Methods:
        enter_state(mob): Sets the monster's strategy to PassiveStrategy.
    """

    def enter_state(self, mob):
        """
        Sets the monster's strategy to PassiveStrategy.

        Args:
            mob (Monster): The monster instance.
        """
        mob.strategy = PassiveStrategy()


class RandomState(State):
    """
    The RandomState class represents the random state of the monster.
    In this state, the monster moves randomly using RandomStrategy.

    Methods:
        enter_state(mob): Sets the monster's strategy to RandomStrategy.
    """

    def enter_state(self, mob):
        """
        Sets the monster's strategy to RandomStrategy.

        Args:
            mob (Monster): The monster instance.
        """
        mob.strategy = RandomStrategy()


class AggressiveState(State):
    """
    The AggressiveState class represents the aggressive state of the monster.
    In this state, the monster moves aggressively towards the player using AggressiveStrategy.

    Methods:
        enter_state(mob): Sets the monster's strategy to AggressiveStrategy.
    """

    def enter_state(self, mob):
        """
        Sets the monster's strategy to AggressiveStrategy.

        Args:
            mob (Monster): The monster instance.
        """
        mob.strategy = AggressiveStrategy()


class PanicState(State):
    """
    The PanicState class represents the panic state of the monster.
    In this state, the monster moves away from the player using CowardlyStrategy.

    Methods:
        enter_state(mob): Sets the monster's strategy to CowardlyStrategy.
    """

    def enter_state(self, mob):
        """
        Sets the monster's strategy to CowardlyStrategy.

        Args:
            mob (Monster): The monster instance.
        """
        mob.strategy = CowardlyStrategy()


class CollisionAvoidanceState(State):
    """
    The CollisionAvoidanceState class represents the state where the monster
    avoids collisions with monsters of the same type using SameTypeCollisionAvoidanceStrategy.

    Methods:
        enter_state(mob): Sets the monster's strategy to SameTypeCollisionAvoidanceStrategy.
    """

    def enter_state(self, mob):
        """
        Sets the monster's strategy to SameTypeCollisionAvoidanceStrategy.

        Args:
            mob (Monster): The monster instance.
        """
        mob.strategy = SameTypeCollisionAvoidanceStrategy()
