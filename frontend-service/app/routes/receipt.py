from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for

receipt = Blueprint('receipt', __name__)


@receipt.route('/')
def index():
    staff_name = session.get('name', 'samitha')
    return render_template('receipt-index.html', staff_name=staff_name)


@receipt.route('/add-appointment')
def go_add_appointment_page():
    staff_name = session.get('name', 'samitha')
    return render_template('add-appointment.html', staff_name=staff_name)


@receipt.route('/nurse')
def go_to_nurse_page():
    staff_name = session.get('name', 'samitha')
    return render_template('nurse.html', staff_name=staff_name)