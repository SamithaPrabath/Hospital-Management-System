from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for
from app.views.views import validate_user_with_patient_service

login = Blueprint('login', __name__)


@login.route('/')
def index():
    return render_template('login.html')


@login.route('/validate-login', methods=['POST'])
def validate_login():
    data = request.get_json()
    nic = data.get('nic')
    password = data.get('password')

    if not nic or not password:
        return jsonify({"success": False, "error": "NIC and password are required"}), 400

    result = validate_user_with_patient_service(nic, password)

    if result["success"]:
        session['staff_id'] = result['data']['staff_id']
        session['role_id'] = result['data']['role_id']
        session['name'] = result['data']['name']
        return jsonify({"success": True})
    else:
        return jsonify({"success": False, "error": result["error"]}), 401


@login.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('login.index'))
