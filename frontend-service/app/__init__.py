from flask import Flask
from app.routes.login import login
from app.routes.dashboard import dashboard


def create_app():
    app = Flask(__name__)

    app.register_blueprint(login, url_prefix='/')
    app.register_blueprint(dashboard, url_prefix='/dashboard')

    return app
