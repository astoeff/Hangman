from constants import WELCOME_TEXT, WELCOME_TEXT_COLOR, CONTINUE_AND_EXIT_COMMAND_TEXT, ENTER_KEY, ESCAPE_KEY
from termcolor import colored
from utils import clear_screen
from help_library import get_character
import os


class PlayerViews:
    def startView(self):
        clear_screen()
        print(colored(WELCOME_TEXT, WELCOME_TEXT_COLOR).center(os.get_terminal_size().columns))
        print('\n')
        print(CONTINUE_AND_EXIT_COMMAND_TEXT)
        pressed_key = get_character()
        while pressed_key != ENTER_KEY and pressed_key != ESCAPE_KEY:
            pressed_key = get_character()
        return pressed_key
