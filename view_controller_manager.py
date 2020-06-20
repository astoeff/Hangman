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
        already_used_symbols = ', '.join(symbols_to_show)
        masked_word = None
        while masked_word != word:
            masked_word = self.word_controllers.mask_word_without_symbols(word, symbols_to_show)
            pressed_key = self.application_views.player_move(masked_word, already_used_symbols, player.moves_left)
            self.application_controllers.check_if_key_for_exit_pressed(pressed_key)
            player_controller = player.get_controller()
            is_key_for_joker_pressed = player_controller.check_if_key_for_joker_pressed(pressed_key)
            if is_key_for_joker_pressed and player_controller.check_if_player_can_use_joker(player):
                player.decrement_jokers_count()
                joker_symbol = self.word_controllers.get_random_symbol_in_word_without_symbols(word, symbols_to_show)
                symbols_to_show.append(joker_symbol)
                already_used_symbols += ', ' + joker_symbol
            else:
                if chr(pressed_key[0]) not in already_used_symbols:
                    already_used_symbols += ', ' + chr(pressed_key[0])
                    symbols_to_show.append(chr(pressed_key[0]))
                    player.decrement_moves_left()
