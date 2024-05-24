class Field:
    """
    The Field class represents the game field.

    Attributes:
        cells (list): A 2D list representing the cells of the field.
    """
    def __init__(self):
        """
        Initializes a new instance of the Field class with empty cells.
        """
        self.cells = [[None for _ in range(10)] for _ in range(10)]

    def get_cell(self, x, y):
        """
        Gets the content of the cell at the specified coordinates.

        Args:
            x (int): The x-coordinate of the cell.
            y (int): The y-coordinate of the cell.

        Returns:
            object: The content of the cell.
        """
        return self.cells[y][x]
