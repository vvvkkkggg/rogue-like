from model.player import Player
from model.field import Field
from model.position import Position
from model.monster import (
    AggressiveMonster,
    PassiveMonster,
    CowardlyMonster,
    MoldMonster,
)


class Game:
    """
    The Game class represents the main game logic and state.

    Attributes:
        player (Player): The player character in the game.
        field (Field): The game field where the player and monsters are located.
        monsters (list): The list of monsters in the game.
    """

    def __init__(self):
        """
        Initializes a new instance of the Game class, setting up the player, field, and monsters.
        """
        self.player = Player()
        self.field = Field(20, 20)
        self.monsters = [
            AggressiveMonster(Position(5, 5)),
            PassiveMonster(Position(10, 10)),
            CowardlyMonster(Position(15, 15)),
            MoldMonster(Position(5, 10)),
        ]

    def move_player(self, direction):
        """
        Moves the player character in the specified direction.

        Args:
            direction (str): The direction to move the player ('up', 'down', 'left', or 'right').
        """
        self.player.move(direction, self.field)

    def update(self):
        """
        Updates the game state, moving all monsters.
        """
        self.find_nearest_monster()
        self.check_collisions()
        self.clone_monsters()

    def find_nearest_monster(self):
        """
        Find the nearest monster to the current player position
        """
        player_position = self.player.position
        min_monster_distance = float("+inf")
        for monster in self.monsters:
            monster.move(self.field, player_position, self.monsters)
            monster_distance = (player_position.x - monster.position.x) ** 2 + (
                player_position.y - monster.position.y
            ) ** 2

            if monster_distance < min_monster_distance:
                min_monster_distance = monster_distance
                self.player.near_monster = monster
                self.player.near_distance = min_monster_distance

    def check_collisions(self):
        """
        Checks for collisions between the player and monsters, initiating combat if necessary.
        """
        for monster in self.monsters:
            if (self.player.position.x - monster.position.x) ** 2 + (
                self.player.position.y - monster.position.y
            ) ** 2 < 1:
                self.player.attack_monster(monster)
                monster.attack_player(self.player)
                if monster.hp <= 0:
                    self.monsters.remove(monster)

    def clone_monsters(self):
        """
        Clone monsterns with checking `should_clone` and add them to the game.
        """
        self.monsters.extend(
            [monster.clone() for monster in self.monsters if monster.should_clone()]
        )

    def get_state(self):
        """
        Returns the current state of the game, including the player and monsters.

        Returns:
            dict: A dictionary representing the current state of the game.
        """
        return {
            "player": {
                "position": (self.player.position.x, self.player.position.y),
                "hp": self.player.hp,
                "attack": self.player.attack,
                "defense": self.player.defense,
                "experience": self.player.experience,
                "level": self.player.level,
            },
            "monsters": [
                {
                    "type": type(monster).__name__,
                    "position": (monster.position.x, monster.position.y),
                    "hp": monster.hp,
                    "attack": monster.attack,
                    "defense": monster.defense,
                }
                for monster in self.monsters
            ],
        }
