import hug
from bottle import run
import jwt

from handlers import hello_handler, transformer_handler, authentication_handler


@hug.post("/token_generation")  # noqa
def token_gen_call(username, password):
    """Authenticate and return a token"""
    secret_key = "super-secret-key-please-change"
    mockusername = "User2"
    mockpassword = "Mypassword"
    # This is an example. Don't do that.
    if mockpassword == password and mockusername == username:
        return {
            "token": jwt.encode({"user": username, "data": "mydata"}, secret_key, algorithm="HS256")
        }
    return "Invalid username and/or password for user: {0}".format(username)


@hug.extend_api()
def with_other_apis():
    """Join API endpoints from two other modules
    These will be at ``/part1`` and ``/part2``, the paths being automatically
    generated from function names.
    """

    return [hello, transformer_controller, authe]


if __name__ == "__main__":
    callable_app = __hug__.http.server()
    run(app=callable_app, reloader=True, port=8000)
