import random
from model.field import Field

class Generator:
    """
    The Generator class is responsible for generating game fields.
    """
    @staticmethod
    def generate_field(width: int, height: int):
        """
        Generates a new game field with the specified width and height.

        Args:
            width (int): The width of the field.
            height (int): The height of the field.

        Returns:
            Field: The generated game field.
        """
        # Создаем новый экземпляр класса Field
        field = Field(width, height)

        # Заполняем поле ячейками со случайными препятствиями (стенами)
        for y in range(height):
            for x in range(width):
                if random.random() < 0.1:  # Вероятность создания стены
                    field.cells[y][x] = "wall"
                else:
                    field.cells[y][x] = None
        return field
