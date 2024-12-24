from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for

receptionist = Blueprint('receptionist', __name__)


@receptionist.route('/')
def index():
    staff_name = session.get('name')
    if not staff_name:
        return redirect(url_for('login.index'))
    return render_template('index.html', staff_name=staff_name)

@receptionist.route('/make_appointment')
def go_to_make_appointment():
    staff_name = session.get('name')
    staff_id = session.get('staff_id')

    doctors_details = {}
    # Sample Format
    doctors_details = {
        'Sam Doe': {
            'specialization': 'Cardiologist',
            'id':1
        },
        'John Doe': {
            'specialization': 'Denist',
            'id':2
        }
    }
    if not staff_name:
        return redirect(url_for('login.index'))
    return render_template(
        'receptionist/make_appointment.html',
        staff_name=staff_name,
        staff_id=staff_id,
        doctors_details=doctors_details
    )


@receptionist.route('/submit_appointment')
def submit_appointment():
    staff_name = session.get('name')
    staff_id = session.get('staff_id')

    if not staff_name:
        return redirect(url_for('login.index'))
    return render_template(
        'receptionist/make_appointment.html',
        staff_name=staff_name,
        staff_id=staff_id,
    )

@receptionist.route('/')
def view_appointments():
    staff_name = session.get('name')
    if not staff_name:
        return redirect(url_for('login.index'))
    return render_template('make_appointment.html', staff_name=staff_name)


@receptionist.route('/')
def staff_register():
    staff_name = session.get('name')
    if not staff_name:
        return redirect(url_for('login.index'))
    return render_template('make_appointment.html', staff_name=staff_name)


@receptionist.route('/')
def view_staff_members():
    staff_name = session.get('name')
    if not staff_name:
        return redirect(url_for('login.index'))
    return render_template('make_appointment.html', staff_name=staff_name)


@receptionist.route('/')
def patient_register():
    staff_name = session.get('name')
    if not staff_name:
        return redirect(url_for('login.index'))
    return render_template('make_appointment.html', staff_name=staff_name)


@receptionist.route('/')
def view_patients():
    staff_name = session.get('name')
    if not staff_name:
        return redirect(url_for('login.index'))
    return render_template('make_appointment.html', staff_name=staff_name)