from model.player import Player
from model.field import Field
from model.position import Position
from model.monster import AggressiveMonster, PassiveMonster, CowardlyMonster

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
            CowardlyMonster(Position(15, 15))
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
        player_position = self.player.position
        distance = -1
        for monster in self.monsters:
            monster.move(self.field, player_position)
            if distance == -1:
                distance = (player_position.x - monster.position.x) ** 2 + (player_position.y - monster.position.y) ** 2
                self.player.near_monster = monster
                self.player.near_distance = distance
            else:
                dist = (player_position.x - monster.position.x) ** 2 + (player_position.y - monster.position.y) ** 2
                if dist < distance:
                    distance = dist
                    self.player.near_monster = monster
                    self.player.near_distance = distance
        self.check_collisions()

    def check_collisions(self):
        """
        Checks for collisions between the player and monsters, initiating combat if necessary.
        """
        for monster in self.monsters:
            if (self.player.position.x - monster.position.x) ** 2 + (self.player.position.y - monster.position.y) ** 2 < 1:
                self.player.attack_monster(monster)
                monster.attack_player(self.player)
                if monster.hp <= 0:
                    self.monsters.remove(monster)

    def get_state(self):
        """
        Returns the current state of the game, including the player and monsters.

        Returns:
            dict: A dictionary representing the current state of the game.
        """
        return {
            'player': {
                'position': (self.player.position.x, self.player.position.y),
                'hp': self.player.hp,
                'attack': self.player.attack,
                'defense': self.player.defense,
                'experience': self.player.experience,
                'level': self.player.level
            },
            'monsters': [
                {
                    'type': type(monster).__name__,
                    'position': (monster.position.x, monster.position.y),
                    'hp': monster.hp,
                    'attack': monster.attack,
                    'defense': monster.defense
                } for monster in self.monsters
            ]
        }