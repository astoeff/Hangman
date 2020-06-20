from constants import ESCAPE_KEY, ONE_KEY, WORDS
from models import Player, PremiumPlayer
import random


class ApplicationControllers:
    def check_if_key_for_exit_pressed(self, pressed_key):
        if pressed_key == ESCAPE_KEY:
            raise SystemExit

    def create_player_instance(self, number_representing_type_of_player):
        return Player('gosho') if number_representing_type_of_player == ONE_KEY else PremiumPlayer('pesho', 19)


class PlayerControllers:
    pass


class PremiumPlayerControllers:
    pass


class WordControllers:
    def get_random_word(self):
        return random.choice(WORDS)
