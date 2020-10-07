# Architecture

_Notes on the architecture of the project._

We switch to graphne + django. Our main goal is to have a backend service that speaks graphql. FastAPI doesn’t brings much to the table in this regard.
The focus of FastAPI Is OpenAPI which is REST based. Also Swagger UI is build for REST. The graphql part is just reused from Starlette which itself uses graphene.
Its easier and better documented to just use graphne with django. The is also django-graphne which is build from the graphne guys.
