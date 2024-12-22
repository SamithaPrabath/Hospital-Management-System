from flask import Flask

from app.base.routes import base_route
from app.errors import key_error_handler


def create_app():
    app = Flask(__name__)
    app.register_blueprint(base_route)

    app.register_error_handler(KeyError, key_error_handler)

    return app
