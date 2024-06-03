from model.player import Player
from model.field import Field
from model.position import Position
from model.monster import (
    AggressiveMonster,
    PassiveMonster,
    CowardlyMonster,
    MoldMonster,
)
import random

class MapBuilder:
    """
    MapBuilder defines the interface for building a game map.
    """
    def __init__(self, width, height, filename=None):
        """
        Initializes the map builder with the given dimensions and optional file name.

        Args:
            width (int): The width of the map.
            height (int): The height of the map.
            filename (str, optional): The name of the file containing the map data. Defaults to None.
        """
        self.width = width
        self.height = height
        self.filename = filename
        self.player = None
        self.field = None
        self.monsters = []

    def set_size(self, width, height):
        """
        Sets the size of the map.

        Args:
            width (int): The width of the map.
            height (int): The height of the map.
        """
        raise NotImplementedError

    def add_monster(self, monster_type, x, y):
        """
        Adds a monster to the map.

        Args:
            monster_type (str): The type of the monster ('A', 'P', 'C', 'M').
            x (int): The x-coordinate of the monster.
            y (int): The y-coordinate of the monster.
        """
        monster = {
            'A': AggressiveMonster,
            'P': PassiveMonster,
            'C': CowardlyMonster,
            'M': MoldMonster
        }[monster_type](Position(x, y))
        self.monsters.append(monster)


    def build(self):
        """
        Builds and returns the game instance.

        Returns:
            Game: The constructed game instance.
        """
        raise NotImplementedError


class DefaultMapBuilder(MapBuilder):
    """
    DefaultMapBuilder loads a map from a file and builds the game instance.
    """
    def __init__(self, filename=None):
        """
        Initializes a new instance of the DefaultMapBuilder class.

        Args:
            filename (str): The name of the file containing the map data.
        """
        super().__init__(0, 0, filename)

    def set_size(self, width, height):
        """
        Sets the size of the map.

        Args:
            width (int): The width of the map.
            height (int): The height of the map.
        """
        self.width = width
        self.height = height

    def build(self):
        """
        Builds and returns the game instance by loading data from the file.

        Returns:
            MapBuilder: builder.
        """
        with open(self.filename, 'r') as file:
            lines = file.readlines()
            self.set_size(*map(int, lines[0].split()))
            for line in lines[1:]:
                parts = line.split()
                self.add_monster(parts[0], int(parts[1]), int(parts[2]))

        self.field = Field(self.width, self.height)
        self.player = Player()
        return self

class GenerateMapBuilder(MapBuilder):
    """
    GenerateMapBuilder generates a random map and builds the game instance.
    """
    def __init__(self, width, height):
        """
        Initializes a new instance of the GenerateMapBuilder class.

        Args:
            width (int): The width of the generated map.
            height (int): The height of the generated map.
        """
        super().__init__(width, height)
        
        self.monster_probabilities = {
            'A': 0.25,
            'P': 0.25,
            'C': 0.25,
            'M': 0.1,
        }

        self.calculate_monster_count()

    def calculate_monster_count(self):
        """
        Calculates the number of monsters based on the size of the map.
        """
        total_cells = self.width * self.height
        min_monsters = max(1, int(total_cells * 0.01))
        max_monsters = int(total_cells * 0.05)
        self.num_monsters = random.randint(min_monsters, max_monsters)


    def set_size(self, width, height):
        """
        Sets the size of the map.

        Args:
            width (int): The width of the map.
            height (int): The height of the map.
        """
        self.width = width
        self.height = height
        self.calculate_monster_count()

    def build(self):
        """
        Builds and returns the game instance by generating random data.

        Returns:
            MapBuilder: builder.
        """
        occupied_positions = set((0,0))
        monster_types = list(self.monster_probabilities.keys())
        monster_probabilities = list(self.monster_probabilities.values())

        while len(self.monsters) < self.num_monsters:
            monster_type = random.choices(monster_types, monster_probabilities)[0]
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)

            if (x, y) in occupied_positions:
                continue

            self.add_monster(monster_type, x, y)
            occupied_positions.add((x, y))

        self.field = Field(self.width, self.height)
        self.player = Player()
        return self

class HardcodeMapBuilder(MapBuilder):
    """
    HardcodeMapBuilder with harcoded objects.
    """
    def __init__(self):
        """
        Initializes a new instance of the HardcodeMapBuilder class.
        """
        super().__init__(0, 0)

    def build(self):
        """
        Builds and returns the game instance with harcodeds values.

        Returns:
            MapBuilder: builder.
        """
        self.player = Player()
        self.field = Field(20, 20)
        self.monsters = [
            AggressiveMonster(Position(5, 5)),
            PassiveMonster(Position(10, 10)),
            CowardlyMonster(Position(15, 15))
        ]
        return self
