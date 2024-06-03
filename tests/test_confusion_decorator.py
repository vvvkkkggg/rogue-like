import unittest
from model.confusion_decorator import ConfusionDecorator
from model.strategy import AggressiveStrategy


class TestConfusionDecorator(unittest.TestCase):
    def test_confuse_strategy(self):
        base_strategy = AggressiveStrategy()
        confuse_strategy = ConfusionDecorator(base_strategy)

        monster = type("MockMonster", (object,), {"position": (0, 0)})()
        field = None
        player_position = (5, 5)

        confuse_strategy.move(monster, field, player_position)

        self.assertIsNotNone(monster.position)


if __name__ == "__main__":
    unittest.main()
