class Ability:
    """
    The Ability class represents an ability that can be used in the game.

    Attributes:
        name (str): The name of the ability.
        effect (function): The function representing the effect of the ability.
    """

    def __init__(self, name, effect):
        """
        Initializes a new instance of the Ability class.

        Args:
            name (str): The name of the ability.
            effect (function): The function representing the effect of the ability.
        """
        self.name = name
        self.effect = effect

    def use(self, target):
        """
        Uses the ability on the specified target.

        Args:
            target: The target on which the ability will be used.
        """
        self.effect(target)
