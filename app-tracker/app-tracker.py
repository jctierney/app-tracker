import time
import json
import requests
import sys
from macos_lib import MacOSLib
from windows_lib import WindowsLib

apps = {}
url = 'http://localhost:8080/apps'

def getActiveWindowTitle():
    '''Returns the active window title - based on the system'''
    if sys.platform in ['Windows', 'win32', 'cygwin']:
        return WindowsLib.getForegroundWindowTitle()
    elif sys.platform in ['Mac', 'darwin', 'os2', 'os2emx']:
        return MacOSLib.getActiveWindowTitleMacOs()

def send_total_time_app(app):
    '''Sends a request to POST the apps updated time usage.'''
    total_time = apps[app]
    app_obj = {"title": app, "time": total_time}
    requests.post(url, json = app_obj)

def get_initial_apps_and_times():
    '''Makes a request to the server API to get a list of the stored apps/times.'''
    response = requests.get(url)
    apps = response.json()

get_initial_apps_and_times()

while True:
    app = getActiveWindowTitle()
    if app in apps:
        apps[app] += 1
    else:
        apps[app] = 1
    time.sleep(1)  
    send_total_time_app(app) 

    