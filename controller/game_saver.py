import json

class GameSaver:
    """
    The GameSaver class is responsible for saving game state to a JSON file.
    """
    @staticmethod
    def save_game(game_state, file_path):
        """
        Saves the game state to a JSON file.

        Args:
            game_state (dict): The game state to be saved.
            file_path (str): The path to the JSON file where the game state will be saved.
        """
        with open(file_path, 'w') as file:
            json.dump(game_state, file)
