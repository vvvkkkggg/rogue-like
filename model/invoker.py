from abc import ABC, abstractmethod
from model.confusion_decorator import ConfusionDecorator


class Command(ABC):
    """
    Abstract base class for all commands.
    It initializes the command with a count attribute to keep track of execution count.
    """

    def __init__(self):
        self.count = 0

    @abstractmethod
    def execute(self):
        """
        Abstract method that must be implemented by subclasses to define the command's behavior.
        """
        pass


class ConfuseNearbyMonstersCommand(Command):
    """
    Command that confuses monsters located in cells adjacent to the player.
    It uses a decorator pattern to apply confusion to the monster's strategy.
    """

    def __init__(self, game):
        """
        Initializes the command with a reference to the game instance.

        Args:
            game (Game): The game instance which contains the player and monsters.
        """
        super().__init__()
        self.game = game

    def execute(self):
        """
        Executes the command by checking the player's distance to nearby monsters.
        If the distance is less than 1, it confuses the nearby monster for 3 turns.
        """
        player_distance = self.game.player.near_distance
        near_monster = self.game.player.near_monster

        if player_distance < 1:
            near_monster.strategy = ConfusionDecorator(near_monster.strategy, turns=3)

            self.count += 1
            print(f"Commands confuse executed: {self.count}")


class Invoker:
    """
    Invoker class that holds and executes commands.
    It maintains a registry of commands and provides a method to execute them by name.
    """

    def __init__(self):
        """
        Initializes the invoker with an empty command registry.
        """
        self._commands = {}

    def register(self, command_name, command):
        """
        Registers a command with a specified name in the command registry.

        Args:
            command_name (string): The name to register the command under.
            command (Command): The command instance to register.
        """
        self._commands[command_name] = command

    def execute(self, command_name):
        """
        Executes a registered command by name.

        Args:
            command_name (string): The name of the command to execute.
        """
        if command_name in self._commands:
            self._commands[command_name].execute()
        else:
            print(f"Command [{command_name}] not recognized.")
