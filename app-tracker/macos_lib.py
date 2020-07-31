class MacOSLib():
    """Class to handle MacOS specific library implementation details."""
    
    @staticmethod
    def getActiveWindowTitleMacOs():
        """Gets the active window title for a MacOS"""
        # http://stackoverflow.com/a/373310/562769
        from AppKit import NSWorkspace
        active_window_name = (NSWorkspace.sharedWorkspace()
                                .activeApplication()['NSApplicationName'])
        return active_window_name