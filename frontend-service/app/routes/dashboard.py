from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for

dashboard = Blueprint('dashboard', __name__)


@dashboard.route('/')
def index():
    staff_name = session.get('name')
    if not staff_name:
        return redirect(url_for('login.index'))
    return render_template('index.html', staff_name=staff_name)


@dashboard.route('/doctor')
def go_to_doctor_page():
    staff_name = session.get('name')
    return render_template('doctor.html', staff_name=staff_name)


@dashboard.route('/receptionist')
def go_to_receptionist_page():
    staff_name = session.get('name')
    return render_template('receptionist/doctor.html', staff_name=staff_name)


@dashboard.route('/radiologist')
def go_to_radiologist_page():
    staff_name = session.get('name')
    return render_template('radiologist.html', staff_name=staff_name)


@dashboard.route('/cashier')
def go_to_cashier_page():
    staff_name = session.get('name')
    return render_template('cashier.html', staff_name=staff_name)
