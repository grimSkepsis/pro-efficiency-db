import json
from ariadne import QueryType, ObjectType
from managers.character import CharacterManager


query = QueryType()


@query.field("character")
def resolve_character(_, info):
    manager = info.context["character_manager"]
    return manager.get_character()


character = ObjectType("Character")


@character.field("name")
def resolve_name(obj, *_):
    return obj["name"]
