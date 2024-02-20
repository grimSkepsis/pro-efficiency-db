import json
from ariadne import QueryType, ObjectType


query = QueryType()


@query.field("character")
def resolve_character(*_):
    with open("data/player-stats.json") as f:
        data = json.load(f)
        return data


character = ObjectType("Character")


@character.field("name")
def resolve_name(obj, *_):
    return obj["name"]
