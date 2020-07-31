from flask import Flask, json, request

apps = {}

with open('apps.json') as save_file:
    apps = json.load(save_file)

api = Flask(__name__)

@api.route('/apps', methods=['GET'])
def get_apps():
    """GET method to return a list of all apps and their associated times."""
    return json.dumps(apps)

@api.route('/apps', methods=['POST'])
def add_app():
    """Adds an app and time."""
    if not request.json:
        return json.dumps('error')
    apps[request.json['title']] = request.json['time']
    with open('apps.json', 'w') as file:
        file.write(json.dumps(apps))

    return json.dumps('success')
    

if __name__ == '__main__':
    # Need to set the host to 0.0.0.0 when running in a docker container.
    api.run(host="0.0.0.0", port="8080")