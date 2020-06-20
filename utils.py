import subprocess
from help_library import get_character
from termcolor import colored
from constants import HEADING_TEXT_COLOR
import os


def clear_screen():
    subprocess.call('clear')


def print_heading_with_content(heading, content):
    clear_screen()
    print(colored(heading, HEADING_TEXT_COLOR).center(os.get_terminal_size().columns))
    print('\n')
    print(content)


def get_character_from_console_until_key_in_list_pressed(keys, input_text=None):
    pressed_key = None
    while pressed_key not in keys:
        if input_text:
            print(input_text)
        pressed_key = get_character()
    return pressed_key
