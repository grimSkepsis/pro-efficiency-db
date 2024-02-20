import json
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])


# @app.route("/character-data")
# def player_data():
#     with open("data/player-stats.json") as f:
#         data = json.load(f)
#     return data


@app.route("/character-data", methods=["GET", "POST"])
def player_data():
    if request.method == "POST":
        data = request.get_json()  # get the incoming data
        with open("data/player-stats.json", "w") as f:
            json.dump(data, f)  # write the data to the file
        return {"message": "Data successfully saved"}, 200
    else:
        with open("data/player-stats.json") as f:
            data = json.load(f)
        return data
