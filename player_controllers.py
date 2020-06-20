from constants import ONE_KEY


class PlayerControllers:
    def check_if_key_for_joker_pressed(self, key_pressed):
        return True if key_pressed == ONE_KEY else False

    def check_if_player_can_use_joker(self, player):
        return False  #normal player can not use a joker
