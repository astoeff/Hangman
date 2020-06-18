from views import PlayerViews
from controllers import PlayerControllers


class ViewControllerManager:
    def __init__(self):
        self.player_views = PlayerViews()
        self.player_controllers = PlayerControllers()

    def manage_application(self):
        pressed_key = self.player_views.startView()
        self.player_controllers.continue_or_exit(pressed_key)
