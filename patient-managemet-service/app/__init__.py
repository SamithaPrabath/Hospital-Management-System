from flask import Flask
from app.views.patient_view import create_patient_blueprint
from db.query_executor import SyncQueryExecutor


def create_app():
    app = Flask(__name__)

    db_config = {
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "password": "",
        "database": "hospital_db",
    }

    query_executor = SyncQueryExecutor(db_config)

    app.register_blueprint(create_patient_blueprint(query_executor), url_prefix='/patient')

    return app
