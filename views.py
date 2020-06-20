from constants import (WELCOME_TEXT, CONTINUE_AND_EXIT_COMMAND_TEXT,
                       ENTER_KEY, ESCAPE_KEY, CHOOSE_PLAYER_TYPE_TEXT, EXIT_COMMAND_TEXT,
                       ONE_KEY, TWO_KEY, MOVE_CORRECT_KEYS)
from utils import get_character_from_console_until_key_in_list_pressed, print_heading_with_content


class ApplicationViews:
    def welcome(self):
        print_heading_with_content(WELCOME_TEXT, CONTINUE_AND_EXIT_COMMAND_TEXT)
        return get_character_from_console_until_key_in_list_pressed([ENTER_KEY, ESCAPE_KEY])

    def choose_player_type(self):
        print_heading_with_content(CHOOSE_PLAYER_TYPE_TEXT, EXIT_COMMAND_TEXT)
        return get_character_from_console_until_key_in_list_pressed([ONE_KEY, TWO_KEY, ESCAPE_KEY])

    def player_move(self, word_masked, already_used_symbols, moves_left):
        content = f'Moves left: {moves_left}\nAlready used symbols: {already_used_symbols}\n\nPress ESC to quit'
        print_heading_with_content(word_masked, content)
        return get_character_from_console_until_key_in_list_pressed(MOVE_CORRECT_KEYS)
