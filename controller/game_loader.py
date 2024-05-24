import json

class GameLoader:
    """
    The GameLoader class is responsible for loading game data from a JSON file.
    """
    @staticmethod
    def load_game(file_path):
        """
        Loads game data from a JSON file.

        Args:
            file_path (str): The path to the JSON file.

        Returns:
            dict: The loaded game data.
        """
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
