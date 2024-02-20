from ariadne import QueryType, ObjectType
from resolvers.logger import logger

query = QueryType()


@query.field("character")
def resolve_character(_, info):
    manager = info.context["character_manager"]
    logger.info("Character requested")
    return manager.get_character()


character = ObjectType("Character")


@character.field("level")
def resolve_level(obj, *_):
    return obj["level"]


@character.field("name")
def resolve_name(obj, *_):
    return obj["name"]


@character.field("race")
def resolve_race(obj, *_):
    return obj["race"]


@character.field("background")
def resolve_background(obj, *_):
    return obj["background"]


@character.field("class")
def resolve_class(obj, *_):
    return obj["class"]


@character.field("attributes")
def resolve_attributes(obj, *_):
    return obj["attributes"]


characterAttributes = ObjectType("CharacterAttributes")


@characterAttributes.field("strength")
def resolve_strength(obj, *_):
    return obj["STR"]


@characterAttributes.field("dexterity")
def resolve_dexterity(obj, *_):
    return obj["DEX"]


@characterAttributes.field("constitution")
def resolve_constitution(obj, *_):
    return obj["CON"]


@characterAttributes.field("intelligence")
def resolve_intelligernce(obj, *_):
    return obj["INT"]


@characterAttributes.field("wisdom")
def resolve_wisdom(obj, *_):
    return obj["WIS"]


@characterAttributes.field("charisma")
def resolve_charisma(obj, *_):
    return obj["CHA"]


resolvers = [query, character, characterAttributes]
