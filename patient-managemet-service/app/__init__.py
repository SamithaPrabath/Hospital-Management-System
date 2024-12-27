import os

from flask import Flask
from app.views.patient_view import create_patient_blueprint
from db.query_executor import SyncQueryExecutor


def create_app():
    app = Flask(__name__)

    db_config = {
        "host": os.getenv("DB_HOST", "localhost"),
        "port": os.getenv("DB_PORT", "3306"),
        "user": os.getenv("DB_USER", "root"),
        "password": os.getenv("DB_PASSWORD", ""),
        "database": os.getenv("DB_NAME", "hospital_db"),
    }

    query_executor = SyncQueryExecutor(db_config)

    app.register_blueprint(create_patient_blueprint(query_executor), url_prefix='/patient')

    return app
