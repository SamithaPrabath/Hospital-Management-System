from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for

radiologist = Blueprint('radiologist', __name__)


@radiologist.route('/')
def index():
    staff_name = session.get('name')
    if not staff_name:
        return redirect(url_for('login.index'))
    return render_template('radiologist.html', staff_name=staff_name)

@radiologist.route('/make_appointment')
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

