class LinuxLib():
    @staticmethod
    def getActiveWindowTitle():
        import gtk
        import wnck
        import glib
        try:
            title = wnck.screen_get_default().get_active_window().get_name()
            return title
        except AttributeError:
            pass