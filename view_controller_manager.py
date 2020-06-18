from views import PlayerViews


class ViewControllerManager:
    def __init__(self):
        self.player_views = PlayerViews()

    def manage_application(self):
        self.player_views.startView()
