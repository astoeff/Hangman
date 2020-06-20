from player_controllers import PlayerControllers


class PremiumPlayerControllers(PlayerControllers):
    def check_if_key_for_joker_pressed(self, key_pressed):
        return super().check_if_key_for_joker_pressed(key_pressed)

    def check_if_player_can_use_joker(self, player):
        return player.jokers_count != 0
