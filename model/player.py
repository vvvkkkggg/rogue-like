from model.position import Position


class Player:
    """
    The Player class represents the player character in the game.

    Attributes:
        position (Position): The current position of the player on the game field.
        hp (int): The health points of the player.
        attack (int): The attack strength of the player.
        defense (int): The defense strength of the player.
        experience (int): The experience points of the player.
        level (int): The level of the player.
    """

    def __init__(self):
        """
        Initializes a new instance of the Player class with the default position (0, 0).
        """
        self.position = Position(0, 0)
        self.hp = 100
        self.attack = 15
        self.defense = 10
        self.experience = 0
        self.level = 1
        self.near_monster = None
        self.near_distance = None

    def move(self, direction, field):
        """
        Moves the player character in the specified direction on the game field.

        Args:
            direction (str): The direction in which to move the player ('up', 'down', 'left', or 'right').
            field (Field): The game field on which the player is moving.
        """
        if direction == "up":
            self.position.y -= 1
        elif direction == "down":
            self.position.y += 1
        elif direction == "left":
            self.position.x -= 1
        elif direction == "right":
            self.position.x += 1

        self.hp = min(self.hp + 10, 100)

    def attack_monster(self, monster):
        """
        Attacks the specified monster, inflicting damage based on the player's attack strength and the monster's defense.

        Args:
            monster (Monster): The monster to attack.
        """
        damage = self.attack - monster.defense
        if damage > 0:
            monster.take_damage(damage)
        if monster.hp <= 0:
            self.gain_experience(50)

    def take_damage(self, damage):
        """
        Reduces the player's HP by the specified damage amount.

        Args:
            damage (int): The amount of damage to inflict.
        """
        self.hp -= damage * 0.1

    def gain_experience(self, exp):
        """
        Increases the player's experience points and checks for level up.

        Args:
            exp (int): The amount of experience points to gain.
        """
        self.experience += exp
        if self.experience >= self.level * 100:
            self.level_up()

    def level_up(self):
        """
        Increases the player's level and improves their attributes.
        """
        self.level += 1
        self.hp += 10
        self.attack += 5
        self.defense += 5
        self.experience = 0
