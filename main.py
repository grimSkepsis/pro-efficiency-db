import json
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])


@app.route("/character-data")
def player_data():
    with open("data/player-stats.json") as f:
        data = json.load(f)
    return data
