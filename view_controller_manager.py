from views import ApplicationViews
from application_controllers import ApplicationControllers
from word_controllers import WordControllers
from constants import LOST_GAME_TEXT, WIN_GAME_TEXT, ONE_KEY


class ViewControllerManager:
    def __init__(self):
        self.application_views = ApplicationViews()
        self.application_controllers = ApplicationControllers()
        self.word_controllers = WordControllers()

    def set_game_pre_conditions(self):
        pressed_key = self.application_views.welcome()
        self.application_controllers.check_if_key_for_exit_pressed(pressed_key)
        pressed_key = self.application_views.choose_player_type()
        self.application_controllers.check_if_key_for_exit_pressed(pressed_key)
        player = self.application_controllers.create_player_instance(pressed_key)
        return player

    def set_symbol_as_used(self, symbol, symbols_to_show, already_used_symbols):
        symbols_to_show.append(symbol)
        already_used_symbols += ', ' + symbol

    def process_joker(self, player, word, symbols_to_show, already_used_symbols):
        player.decrement_jokers_count()
        joker_symbol = self.word_controllers.get_random_symbol_in_word_without_symbols(word, symbols_to_show)
        self.set_symbol_as_used(joker_symbol, symbols_to_show, already_used_symbols)

    def process_key_entered_from_player(self, player, pressed_key, already_used_symbols, symbols_to_show):
        pressed_key_not_joker = pressed_key != ONE_KEY
        pressed_key_not_in_already_used_symbols = chr(pressed_key[0]) not in already_used_symbols
        is_pressed_key_available = pressed_key_not_joker and pressed_key_not_in_already_used_symbols
        if is_pressed_key_available:
            self.set_symbol_as_used(chr(pressed_key[0]), symbols_to_show, already_used_symbols)
            player.decrement_moves_left()

    def process_game_move(self, player, word, symbols_to_show, already_used_symbols):
        masked_word = self.word_controllers.mask_word_without_symbols(word, symbols_to_show)
        pressed_key = self.application_views.player_move(masked_word, already_used_symbols, player.moves_left)
        self.application_controllers.check_if_key_for_exit_pressed(pressed_key)
        player_controller = player.get_controller()
        is_key_for_joker_pressed = player_controller.check_if_key_for_joker_pressed(pressed_key)
        joker_conditions = is_key_for_joker_pressed and player_controller.check_if_player_can_use_joker(player)
        if joker_conditions:
            self.process_joker(player, word, symbols_to_show, already_used_symbols)
        else:
            self.process_key_entered_from_player(player, pressed_key, already_used_symbols, symbols_to_show)
        masked_word = self.word_controllers.mask_word_without_symbols(word, symbols_to_show)
        return (masked_word, player)

    def process_game(self, player, word):
        word_first_symbol = word[0]
        word_last_symbol = word[len(word) - 1]
        symbols_to_show = [word_first_symbol, word_last_symbol]
        already_used_symbols = ', '.join(symbols_to_show)
        is_game_in_process = True
        while is_game_in_process:
            (masked_word, player) = self.process_game_move(player, word, symbols_to_show, already_used_symbols)
            is_game_in_process = masked_word != word and player.moves_left != 0

    def manage_application(self):
        player = self.set_game_pre_conditions()
        word = self.word_controllers.get_random_word()
        self.process_game(player, word)
        if player.moves_left == 0:
            self.application_views.result_from_game(word, LOST_GAME_TEXT)
        else:
            self.application_views.result_from_game(word, WIN_GAME_TEXT)
