from flask import Blueprint, render_template, request, jsonify

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/')
def index():
    return render_template('index.html')
