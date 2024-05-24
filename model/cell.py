class Cell:
    """
    Represents a generic cell in the game field.

    Attributes:
        type (str): The type of the cell.
    """
    def __init__(self, type):
        """
        Initializes a Cell instance with the specified type.

        Args:
            type (str): The type of the cell.
        """
        self.type = type


class EmptyCell(Cell):
    """
    Represents an empty cell in the game field.
    """
    def __init__(self):
        """
        Initializes an EmptyCell instance with type set to "empty".
        """
        super().__init__("empty")


class HealCell(Cell):
    """
    Represents a healing cell in the game field.
    """
    def __init__(self):
        """
        Initializes a HealCell instance with type set to "heal".
        """
        super().__init__("heal")


class ObstacleCell(Cell):
    """
    Represents an obstacle cell in the game field.
    """
    def __init__(self):
        """
        Initializes an ObstacleCell instance with type set to "obstacle".
        """
        super().__init__("obstacle")
