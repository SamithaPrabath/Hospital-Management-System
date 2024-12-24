from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for

dashboard = Blueprint('dashboard', __name__)


@dashboard.route('/')
def index():
    staff_name = session.get('name', 'samitha')
    if not staff_name:
        return redirect(url_for('login.index'))
    return render_template('index.html', staff_name=staff_name)


@dashboard.route('/doctor')
def go_to_doctor_page():
    staff_name = session.get('name')
    return render_template('doctors.html', staff_name=staff_name)


@dashboard.route('/nurse')
def go_to_nurse_page():
    staff_name = session.get('name', 'samitha')
    return render_template('nurse.html', staff_name=staff_name)
