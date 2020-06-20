from views import ApplicationViews
from application_controllers import ApplicationControllers
from word_controllers import WordControllers


class ViewControllerManager:
    def __init__(self):
        self.application_views = ApplicationViews()
        self.application_controllers = ApplicationControllers()
        self.word_controllers = WordControllers()

    def manage_application(self):
        pressed_key = self.application_views.welcome()
        self.application_controllers.check_if_key_for_exit_pressed(pressed_key)
        pressed_key = self.application_views.choose_player_type()
        self.application_controllers.check_if_key_for_exit_pressed(pressed_key)
        player = self.application_controllers.create_player_instance(pressed_key)
        word = self.word_controllers.get_random_word()
        symbols_to_show = [word[0], word[len(word) - 1]]
        already_used_symbols = symbols_to_show
        while True:
            masked_word = self.word_controllers.mask_word_without_symbols(word, symbols_to_show)
            pressed_key = self.application_views.player_move(masked_word, already_used_symbols, player.moves_left)
            self.application_controllers.check_if_key_for_exit_pressed(pressed_key)
            player_controller = player.get_controller()
            is_key_for_joker_pressed = player_controller.check_if_key_for_joker_pressed(pressed_key)
            if is_key_for_joker_pressed and player_controller.check_if_player_can_use_joker(player):
                player.decrement_jokers_count()
                joker_symbol = self.word_controllers.get_random_symbol_in_word_without_symbols(word, symbols_to_show)
                symbols_to_show.append(joker_symbol)
            else:

                player.decrement_moves_left()
