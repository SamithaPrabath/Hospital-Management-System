from flask import Flask

from app.routes.cashier import cashier
from app.routes.doctor import doctor

from app.routes.receipt import receipt
from app.routes.login import login
from app.routes.dashboard import dashboard
from app.routes.report import report
from app.routes.radiologist import radiologist
from app.routes.receptionist import receptionist
from app.routes.payment import payment


def create_app():
    app = Flask(__name__)

    app.register_blueprint(login, url_prefix='/')
    app.register_blueprint(dashboard, url_prefix='/dashboard')
    app.register_blueprint(receptionist, url_prefix='/receptionist')
    app.register_blueprint(doctor, url_prefix='/doctor')
    app.register_blueprint(radiologist, url_prefix='/radiologist')
    app.register_blueprint(cashier, url_prefix='/cashier')
    app.register_blueprint(report, url_prefix='/report')
    app.register_blueprint(payment, url_prefix='/payment')
    app.register_blueprint(receipt, url_prefix='/receipt')

    return app
