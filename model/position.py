class Position:
    """
    The Position class represents a point in a two-dimensional space.

    Attributes:
        x (int): The x-coordinate of the position.
        y (int): The y-coordinate of the position.
    """
    def __init__(self, x, y):
        """
        Initializes a new instance of the Position class with the specified coordinates.

        Args:
            x (int): The initial x-coordinate.
            y (int): The initial y-coordinate.
        """
        self.x = x
        self.y = y

    def move(self, dx, dy):
        """
        Moves the position by the specified offsets.

        Args:
            dx (int): The amount to move in the x-direction.
            dy (int): The amount to move in the y-direction.
        """
        self.x += dx
        self.y += dy
