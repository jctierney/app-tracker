import time
import json
import requests
import sys
from macos_lib import MacOSLib
from windows_lib import WindowsLib
from linux_lib import LinuxLib

apps = {}
url = 'http://localhost:8080/apps'

def getActiveWindowTitle(platform):
    '''Returns the active window title - based on the provided platform'''
    if platform in ['Windows', 'win32', 'cygwin']:
        print('running windows')
        return WindowsLib.getForegroundWindowTitle()
    elif platform in ['Mac', 'darwin', 'os2', 'os2emx']:
        print('running macos')
        return MacOSLib.getActiveWindowTitleMacOs()
    elif platform in ['linux']:
        return None

def is_user_platform_supported(platform):
    '''
    Checks whether the platform is supported.
    Returns True if the platform is supported and False if the platform is not supported.
    '''
    if platform in ['Windows', 'win32', 'cygwin']:
        return True
    elif platform in ['Mac', 'darwin', 'os2', 'os2emx']:
        return True
    elif platform in ['linux']:
        return False

def send_total_time_app(app):
    '''Sends a request to POST the apps updated time usage.'''
    total_time = apps[app]
    app_obj = {"title": app, "time": total_time}
    requests.post(url, json = app_obj)

def get_initial_apps_and_times():
    '''Makes a request to the server API to get a list of the stored apps/times.'''
    response = requests.get(url)
    apps = response.json()
    print('Connected and running')

user_platform = sys.platform
if not is_user_platform_supported(user_platform):
    print (user_platform + ' is not supported yet. Exiting program.')
    exit()

get_initial_apps_and_times()

while True:    
    app = getActiveWindowTitle(user_platform)
    if app is None:
        continue
    
    if app in apps:
        apps[app] += 1
    else:
        apps[app] = 1
    time.sleep(1)  
    send_total_time_app(app)