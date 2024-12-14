from quart import Quart

from app.routes import base_route


def create_app():
    app = Quart(__name__)
    app.register_blueprint(base_route)

    return app
