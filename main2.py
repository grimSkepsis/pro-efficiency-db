from ariadne import (
    QueryType,
    graphql_sync,
    make_executable_schema,
    load_schema_from_path,
)
from ariadne.explorer import ExplorerGraphiQL
from flask import Flask, jsonify, request
from resolvers.hello3 import query as query3, mutation
from resolvers.character import resolvers as character_resolvers
from managers.character import CharacterManager


type_defs = load_schema_from_path("schema.graphql")

query = QueryType()


character_manager = CharacterManager()


@query.field("hello")
def resolve_hello(_, info):
    request = info.context["request"]
    user_agent = request.headers.get("User-Agent", "Guest")
    return "Hello, %s!" % user_agent


@query.field("hello2")
def resolve_hello(_, info):
    request = info.context["request"]
    user_agent = request.headers.get("User-Agent", "Guest")
    return "Hello2, %s!" % user_agent


schema = make_executable_schema(
    type_defs,
    [query, query3, mutation, *character_resolvers],
)

app = Flask(__name__)

# Retrieve HTML for the GraphiQL.
# If explorer implements logic dependant on current request,
# change the html(None) call to the html(request)
# and move this line to the graphql_explorer function.
explorer_html = ExplorerGraphiQL().html(None)


@app.route("/graphql", methods=["GET"])
def graphql_explorer():
    # On GET request serve the GraphQL explorer.
    # You don't have to provide the explorer if you don't want to
    # but keep on mind this will not prohibit clients from
    # exploring your API using desktop GraphQL explorer app.
    return explorer_html, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    # GraphQL queries are always sent as POST
    data = request.get_json()

    # Note: Passing the request to the context is optional.
    # In Flask, the current request is always accessible as flask.request
    success, result = graphql_sync(
        schema,
        data,
        context_value={
            "request": request,
            "character_manager": character_manager,
        },
        debug=app.debug,
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code


if __name__ == "__main__":
    app.run(debug=True)
