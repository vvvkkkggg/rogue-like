import unittest
from model.position import Position
from model.states import AggressiveState, PassiveState, PanicState
from model.strategy import AggressiveStrategy, PassiveStrategy, CowardlyStrategy
from model.monster import Monster, AggressiveMonster, PassiveMonster, CowardlyMonster


class TestMonster(unittest.TestCase):
    def test_monster_initialization(self):
        position = Position(0, 0)
        state = AggressiveState()
        hp, attack, defense = 30, 10, 5
        monster = Monster(position, state, hp, attack, defense)

        self.assertEqual(monster.position, position)
        self.assertEqual(type(monster.strategy), AggressiveStrategy)
        self.assertEqual(monster.hp, hp)
        self.assertEqual(monster.attack, attack)
        self.assertEqual(monster.defense, defense)

    def test_monster_take_damage(self):
        position = Position(0, 0)
        state = AggressiveState()
        monster = Monster(position, state, 30, 10, 5)

        monster.take_damage(10)
        self.assertEqual(monster.hp, 29)

        monster.take_damage(30)
        self.assertEqual(monster.hp, 26)

    def test_aggressive_monster(self):
        position = Position(0, 0)
        monster = AggressiveMonster(position)
        self.assertIsInstance(monster.strategy, AggressiveStrategy)
        self.assertEqual(monster.hp, 30)

    def test_passive_monster(self):
        position = Position(0, 0)
        monster = PassiveMonster(position)
        self.assertIsInstance(monster.strategy, PassiveStrategy)
        self.assertEqual(monster.hp, 20)

    def test_cowardly_monster(self):
        position = Position(0, 0)
        monster = CowardlyMonster(position)
        self.assertIsInstance(monster.strategy, CowardlyStrategy)
        self.assertEqual(monster.hp, 15)


if __name__ == "__main__":
    unittest.main()
