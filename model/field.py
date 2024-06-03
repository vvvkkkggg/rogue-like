class Field:
    """
    The Field class represents the game field, a 2D grid of cells.

    Attributes:
        width (int): The width of the field.
        height (int): The height of the field.
        grid (list): The 2D grid of cells representing the field.
    """

    def __init__(self, width, height):
        """
        Initializes a new instance of the Field class with the given width and height.

        Args:
            width (int): The width of the field.
            height (int): The height of the field.
        """
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]

    def get_cell(self, x, y):
        """
        Returns the object at the given cell coordinates.

        Args:
            x (int): The x-coordinate of the cell.
            y (int): The y-coordinate of the cell.

        Returns:
            The object at the given cell coordinates.
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
        return None

    def set_cell(self, x, y, obj):
        """
        Sets the object at the given cell coordinates.

        Args:
            x (int): The x-coordinate of the cell.
            y (int): The y-coordinate of the cell.
            obj: The object to place at the cell coordinates.
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = obj
