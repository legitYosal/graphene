from config import User

class AuthorizationMiddleware:
    """
        we try to parse jwt token from Authorization
        header of the request, and then obtain the user
        for that token
    """

    AUTHORIZATION_KEY = 'Authorization'

    @staticmethod
    def get_token_from_request(request):
        header = request.headers.get(
            AuthorizationMiddleware.AUTHORIZATION_KEY
        )
        try:
            return header.split(' ')[1]
        except AttributeError:
            pass
        except IndexError:
            pass

    @staticmethod
    def resolve(next, root, info, **args):
        token = AuthorizationMiddleware \
                        .get_token_from_request(info.context)
        if token:
            user = User.get_user_from_token(token)
            info.context.user = user
            pass
        return next(root, info, **args)