from view_controller_manager import ViewControllerManager

if __name__ == '__main__':
    manager = ViewControllerManager()
    try:
        manager.manage_application()
    except SystemExit:
        pass
