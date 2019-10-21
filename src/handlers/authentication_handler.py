import hug

authentication = hug.authentication.basic(
    hug.authentication.verify("joe", "pwd"))


@hug.get("/authenticated", requires=authentication)
def basic_auth_api_call(user: hug.directives.user):
    return "Successfully authenticated with user: {0}".format(user)


# First, the user object stored in the context need not be a string,
# but can be any Python object.
class APIUser(object):
    """A minimal example of a rich User object"""

    def __init__(self, user_id, api_key):
        self.user_id = user_id
        self.api_key = api_key


def api_key_verify(api_key):
    # Obviously, this would hit your database
    magic_key = "5F00832B-DE24-4CAF-9638-C10D1C642C6C"
    if api_key == magic_key:
        # Success!
        return APIUser("user_foo", api_key)
    else:
        # Invalid key
        return None


api_key_authentication = hug.authentication.api_key(api_key_verify)


@hug.get("/key_authenticated", requires=api_key_authentication)  # noqa
def basic_auth_api_call(user: hug.directives.user):
    return "Successfully authenticated with user: {0}".format(user.user_id)


def token_verify(token):
    secret_key = "super-secret-key-please-change"
    try:
        return jwt.decode(token, secret_key, algorithm="HS256")
    except jwt.DecodeError:
        return False


token_key_authentication = hug.authentication.token(token_verify)


@hug.get("/token_authenticated", requires=token_key_authentication)  # noqa
def token_auth_call(user: hug.directives.user):
    return "You are user: {0} with data {1}".format(user["user"], user["data"])
