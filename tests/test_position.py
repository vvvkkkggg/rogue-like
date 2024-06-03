import unittest
from model.position import Position


class TestPosition(unittest.TestCase):
    def test_initialization(self):
        pos = Position(0, 0)
        self.assertEqual(pos.x, 0)
        self.assertEqual(pos.y, 0)

        pos = Position(10, -5)
        self.assertEqual(pos.x, 10)
        self.assertEqual(pos.y, -5)

    def test_move(self):
        pos = Position(0, 0)
        pos.move(5, -3)
        self.assertEqual(pos.x, 5)
        self.assertEqual(pos.y, -3)

        pos.move(-2, 2)
        self.assertEqual(pos.x, 3)
        self.assertEqual(pos.y, -1)


if __name__ == "__main__":
    unittest.main()
