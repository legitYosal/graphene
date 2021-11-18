from flask_graphql import GraphQLView
from config import app
from schema import schema
from users.middleware import AuthorizationMiddleware

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True,
        middleware=[AuthorizationMiddleware],
    )
)

if __name__ == '__main__':
    app.debug = True
    app.run()