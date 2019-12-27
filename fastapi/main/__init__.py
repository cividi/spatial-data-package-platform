import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from .graph import Query

app = FastAPI()
app.add_route("/", GraphQLApp(schema=graphene.Schema(query=Query)))

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}
