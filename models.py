from player_controllers import PlayerControllers
from premium_player_controllers import PremiumPlayerControllers
from constants import PLAYER_STARTING_MOVES_COUNT, PREMIUM_PLAYER_JOKERS_COUNT


class Word:
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return self.content


class Player:
    def __init__(self, name):
        self.name = name
        self.moves_left = PLAYER_STARTING_MOVES_COUNT

    def get_controller(self):
        return PlayerControllers()

    def decrement_moves_left(self):
        self.moves_left -= 1

    def __str__(self):
        return self.name


class PremiumPlayer(Player):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        self.jokers_count = PREMIUM_PLAYER_JOKERS_COUNT

    def get_controller(self):
        return PremiumPlayerControllers()

    def decrement_jokers_count(self):
        self.jokers_count -= 1

    def __str__(self):
        return self.name + ' ' + str(self.age)
