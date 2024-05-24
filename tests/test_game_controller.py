import unittest
from unittest.mock import Mock, patch
import pygame
from model.game import Game
from controller.game_controller import GameController


class TestGameController(unittest.TestCase):

    def setUp(self):
        self.game_controller = GameController()

    @patch('controller.game_controller.Game')
    def test_initialization(self, MockGame):
        # Проверка, что GameController инициализирует объект Game
        mock_game_instance = MockGame.return_value
        game_controller = GameController()
        self.assertEqual(game_controller.game, mock_game_instance)

    def test_handle_event_up(self):
        # Проверка обработки нажатия клавиши W
        self.game_controller.game.move_player = Mock()
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_w)
        self.game_controller.handle_event(event)
        self.game_controller.game.move_player.assert_called_once_with("up")

    def test_handle_event_down(self):
        # Проверка обработки нажатия клавиши S
        self.game_controller.game.move_player = Mock()
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_s)
        self.game_controller.handle_event(event)
        self.game_controller.game.move_player.assert_called_once_with("down")

    def test_handle_event_left(self):
        # Проверка обработки нажатия клавиши A
        self.game_controller.game.move_player = Mock()
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_a)
        self.game_controller.handle_event(event)
        self.game_controller.game.move_player.assert_called_once_with("left")

    def test_handle_event_right(self):
        # Проверка обработки нажатия клавиши D
        self.game_controller.game.move_player = Mock()
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_d)
        self.game_controller.handle_event(event)
        self.game_controller.game.move_player.assert_called_once_with("right")

    def test_update(self):
        # Проверка обновления состояния игры
        self.game_controller.game.update = Mock()
        self.game_controller.update()
        self.game_controller.game.update.assert_called_once()

    def test_get_game_state(self):
        # Проверка получения состояния игры
        self.game_controller.game.get_state = Mock(return_value="game_state")
        state = self.game_controller.get_game_state()
        self.assertEqual(state, "game_state")
        self.game_controller.game.get_state.assert_called_once()


if __name__ == '__main__':
    unittest.main()
