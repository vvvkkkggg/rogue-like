import unittest
from model.builder import DefaultMapBuilder, AggressiveMonster, PassiveMonster, CowardlyMonster, MoldMonster, Position

class TestDefaultMapBuilder(unittest.TestCase):
    def setUp(self):
        # Creating a temporary map file for testing
        self.map_data = """20 20
A 5 5
P 10 10
C 15 15
M 5 10
M 1 5
A 17 17
M 14 13
"""
        self.filename = 'test_map.txt'
        with open(self.filename, 'w') as f:
            f.write(self.map_data)

    def tearDown(self):
        import os
        os.remove(self.filename)

    def test_parsing(self):
        builder = DefaultMapBuilder(self.filename)
        game_instance = builder.build()

        self.assertEqual(game_instance.field.width, 20)
        self.assertEqual(game_instance.field.height, 20)

        expected_positions = [
            (AggressiveMonster, Position(5, 5)),
            (PassiveMonster, Position(10, 10)),
            (CowardlyMonster, Position(15, 15)),
            (MoldMonster, Position(5, 10)),
            (MoldMonster, Position(1, 5)),
            (AggressiveMonster, Position(17, 17)),
            (MoldMonster, Position(14, 13)),
        ]

        self.assertEqual(len(game_instance.monsters), len(expected_positions))
        for monster, (expected_type, expected_position) in zip(game_instance.monsters, expected_positions):
            self.assertIsInstance(monster, expected_type)
            self.assertEqual(monster.position.x, expected_position.x)
            self.assertEqual(monster.position.y, expected_position.y)

if __name__ == '__main__':
    unittest.main()
