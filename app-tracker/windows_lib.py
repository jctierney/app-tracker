class WindowsLib():
    """Class to handle Windows library implementation details."""
    
    @staticmethod
    def getForegroundWindowTitle():
        """Gets the active window title. This is specifically for Windows.
        Uses cytype w/ win32 dll to handle reaching into the windows API.
        Documentation: https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getforegroundwindow
        ctype documentation: https://docs.python.org/3/library/ctypes.html
        """
        from ctypes import wintypes, windll, create_unicode_buffer
        hWnd = windll.user32.GetForegroundWindow()
        length = windll.user32.GetWindowTextLengthW(hWnd)
        buf = create_unicode_buffer(length + 1)
        windll.user32.GetWindowTextW(hWnd, buf, length + 1)

        if buf.value:
            titles = buf.value.split(' - ')
            title = titles[-1]
            return title
        else:
            return None