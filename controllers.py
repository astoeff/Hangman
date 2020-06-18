from constants import ESCAPE_KEY


class PlayerControllers:
    def continue_or_exit(self, pressed_key):
        if pressed_key == ESCAPE_KEY:
            raise SystemExit
        else:
            print('NEXT VIEW in 3 2 1 ...')
