from constants import WELCOME_TEXT, WELCOME_TEXT_COLOR
from termcolor import colored
from utils import clear_screen
import os


class PlayerViews:
    def startView(self):
        clear_screen()
        print(colored(WELCOME_TEXT, WELCOME_TEXT_COLOR).center(os.get_terminal_size().columns))
