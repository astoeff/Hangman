from views import ApplicationViews, PlayerViews
from controllers import ApplicationControllers, PlayerControllers


class ViewControllerManager:
    def __init__(self):
        self.application_views = ApplicationViews()
        self.application_controllers = ApplicationControllers()
        self.player_views = PlayerViews()
        self.player_controllers = PlayerControllers()

    def manage_application(self):
        pressed_key = self.application_views.welcome()
        self.application_controllers.check_if_key_for_exit_pressed(pressed_key)
        pressed_key = self.application_views.choose_player_type()
        self.application_controllers.check_if_key_for_exit_pressed(pressed_key)
        player = self.application_controllers.create_player_instance(pressed_key)
