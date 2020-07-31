from ctypes import wintypes, windll, create_unicode_buffer
import time
import json
import requests

apps = {}
url = 'http://localhost:8080/apps'

def getForegroundWindowTitle():
    """Gets the active window title.
    Uses cytype w/ win32 dll to handle reaching into the windows API.
    Documentation: https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getforegroundwindow
    ctype documentation: https://docs.python.org/3/library/ctypes.html
    """
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

while True:
    app = getForegroundWindowTitle()
    if app in apps:
        apps[app] += 1
    else:
        apps[app] = 1
    time.sleep(1)    

    total_time = apps[app]
    app_obj = {'title': app, 'time': total_time}
    response = requests.post(url, json = app_obj)