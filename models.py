from player_controllers import PlayerControllers
from premium_player_controllers import PremiumPlayerControllers


class Word:
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return self.content


class Player:
    def __init__(self, name):
        self.name = name

    def get_controller(self):
        return PlayerControllers()

    def __str__(self):
        return self.name


class PremiumPlayer(Player):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def get_controller(self):
        return PremiumPlayerControllers()

    def __str__(self):
        return self.name + ' ' + str(self.age)
