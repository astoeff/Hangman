from constants import (WELCOME_TEXT, CONTINUE_AND_EXIT_COMMAND_TEXT,
                       ENTER_KEY, ESCAPE_KEY, CHOOSE_PLAYER_TYPE_TEXT, EXIT_COMMAND_TEXT,
                       ONE_KEY, TWO_KEY)
from utils import get_character_from_console_until_key_in_list_pressed, print_heading_with_content


class ApplicationViews:
    def welcome(self):
        print_heading_with_content(WELCOME_TEXT, CONTINUE_AND_EXIT_COMMAND_TEXT)
        return get_character_from_console_until_key_in_list_pressed([ENTER_KEY, ESCAPE_KEY])

    def choose_player_type(self):
        print_heading_with_content(CHOOSE_PLAYER_TYPE_TEXT, EXIT_COMMAND_TEXT)
        return get_character_from_console_until_key_in_list_pressed([ONE_KEY, TWO_KEY, ESCAPE_KEY])


class PlayerViews:
    pass
