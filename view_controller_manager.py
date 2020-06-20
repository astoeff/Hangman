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
        player_controller = player.get_controller()
        symbols_to_show = [word[0], word[len(word) - 1]]
        masked_word = self.word_controllers.mask_word_without_symbols(word, symbols_to_show)
        self.application_views.player_move(masked_word)
