from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for

from app.views.views import user_password_change

dashboard = Blueprint('dashboard', __name__)


@dashboard.route('/')
def index():
    staff_name = session.get('name')
    role_id = session.get('role_id')
    if not staff_name or not role_id:
        return redirect(url_for('login.index'))

    if session['role_id'] == 1:
        return redirect(url_for('dashboard.go_to_receptionist_page'))
    elif session['role_id'] == 2:
        return redirect(url_for('dashboard.go_to_doctor_page'))
    elif session['role_id'] == 3:
        return redirect(url_for('dashboard.go_to_radiologist_page'))
    return redirect(url_for('dashboard.cashier'))


@dashboard.route('/doctor')
def go_to_doctor_page():
    staff_name = session.get('name')
    return render_template('doctor/doctor.html', staff_name=staff_name)


@dashboard.route('/receptionist')
def go_to_receptionist_page():
    staff_name = session.get('name')
    return render_template('receptionist/receptionist.html', staff_name=staff_name)


@dashboard.route('/radiologist')
def go_to_radiologist_page():
    staff_name = session.get('name')
    return render_template('radiologist/radiologist.html', staff_name=staff_name)


@dashboard.route('/cashier')
def go_to_cashier_page():
    staff_name = session.get('name')
    return render_template('cashier.html', staff_name=staff_name)


@dashboard.route('/change-password')
def go_to_password_change_page():
    staff_name = session.get('name')
    staff_id = session.get('staff_id')
    return render_template('receptionist/change_password.html', staff_name=staff_name, staff_id=staff_id)

@dashboard.route('/change-password', methods=['POST'])
def change_password():
    data = request.get_json()

    staff_id = session.get('staff_id')
    current_password = data.get('current_password')
    new_password = data.get('new_password')

    try:
        response = user_password_change(staff_id, current_password, new_password)
        if response.get('success'):
            return jsonify({
                "success": True,
                "message": response.get('message'),
            }), 201
        else:
            return jsonify({
                "success": False,
                "message": response.get('error')
            }), 500

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 501
