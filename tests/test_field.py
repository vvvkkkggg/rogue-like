import unittest
from model.field import Field


class TestField(unittest.TestCase):

    def setUp(self):
        self.field = Field()

    def test_initialization(self):
        # Проверка, что поле инициализируется правильно и все ячейки имеют значение None
        for row in self.field.cells:
            for cell in row:
                self.assertIsNone(cell)

    def test_get_cell(self):
        # Проверка метода get_cell
        self.assertIsNone(self.field.get_cell(0, 0))
        self.assertIsNone(self.field.get_cell(5, 5))
        self.assertIsNone(self.field.get_cell(9, 9))

    def test_set_and_get_cell(self):
        # Проверка установки значения в ячейку и получения этого значения
        self.field.cells[2][3] = 'X'
        self.assertEqual(self.field.get_cell(3, 2), 'X')

        self.field.cells[0][0] = 'A'
        self.assertEqual(self.field.get_cell(0, 0), 'A')


if __name__ == '__main__':
    unittest.main()
