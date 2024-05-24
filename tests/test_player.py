import unittest
from model.position import Position
from model.player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player()

    def test_initial_position(self):
        self.assertEqual(self.player.position.x, 0)
        self.assertEqual(self.player.position.y, 0)

    def test_move_up(self):
        self.player.move("up", None)
        self.assertEqual(self.player.position.x, 0)
        self.assertEqual(self.player.position.y, -1)

    def test_move_down(self):
        self.player.move("down", None)
        self.assertEqual(self.player.position.x, 0)
        self.assertEqual(self.player.position.y, 1)

    def test_move_left(self):
        self.player.move("left", None)
        self.assertEqual(self.player.position.x, -1)
        self.assertEqual(self.player.position.y, 0)

    def test_move_right(self):
        self.player.move("right", None)
        self.assertEqual(self.player.position.x, 1)
        self.assertEqual(self.player.position.y, 0)


if __name__ == '__main__':
    unittest.main()
