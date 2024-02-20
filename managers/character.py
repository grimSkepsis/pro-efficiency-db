import json


class CharacterManager:

    def get_character(self):
        with open("data/player-stats.json") as f:
            data = json.load(f)
            return data
