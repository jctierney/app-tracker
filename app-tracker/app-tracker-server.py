from flask import Flask, json, request

apps = {}
api = Flask(__name__)

@api.route('/apps', methods=['GET'])
def get_apps():
    """GET method to return a list of all apps and their associated times."""
    return json.dumps(apps)

@api.route('/apps', methods=['POST'])
def add_app():
    """Adds an app and time."""
    is_proper_request = handle_improper_request(request)
    if not is_proper_request:
        return json.dumps("error")
    
    app_title = request.json['title']
    apps[app_title] = request.json['time']
    save_to_file(json.dumps(apps))
    return json.dumps('success')

# Helper methods start here.
def handle_improper_request(request):
    """Handles an improper request from the client."""
    if not request.json:
        return False

def save_to_file(json):
    """Saves the apps as a JSON string to a file."""
    with open('../apps.json', 'w') as file:
        file.write(json)

def open_apps_file():
    """Opens the apps.json file where the results are stored/saved between loads."""
    with open('../apps.json') as save_file:
        return json.load(save_file)

if __name__ == '__main__':
    """Main entry point for app-tracker-server.py"""
    apps = open_apps_file()

    # Need to set the host to 0.0.0.0 when running in a docker container.
    api.run(host="0.0.0.0", port="8080")