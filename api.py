from flask import Flask
from internal import board, configs, generate, displays, managers, picks, style

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/snake/draft/<league_name>/<manager>')
def add_player(league_name, manager):
    return 'League {}: Manager {}'.format(league_name, manager)

@app.route('/draft', methods=['GET'])
def get_draft_results():
    return 'test'
