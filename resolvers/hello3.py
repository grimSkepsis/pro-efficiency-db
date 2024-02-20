from ariadne import (
    QueryType,
)

query = QueryType()


@query.field("hello3")
def resolve_hello(_, info):
    request = info.context["request"]
    user_agent = request.headers.get("User-Agent", "Guest")
    return "Hello3, %s!" % user_agent


@query.field("hello4")
def resolve_hello(_, info):
    request = info.context["request"]
    user_agent = request.headers.get("User-Agent", "Guest")
    return "Hello4, %s!" % user_agent
