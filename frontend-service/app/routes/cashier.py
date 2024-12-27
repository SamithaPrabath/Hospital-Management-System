from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for

from app.views.receptionist.receptionist import get_appointments, get_appointment_status
from app.views.views import get_patient_by_id, get_staff_by_id

cashier = Blueprint('cashier', __name__)


@cashier.route('/')
def index():
    staff_name = session.get('name')
    if not staff_name:
        return redirect(url_for('login.index'))
    return render_template('radiologist.html', staff_name=staff_name)

@cashier.route('/all_receipts')
def go_to_all_receipts():
    staff_name = session.get('name')
    receipt_id = session.get('receipt_id')

    if not staff_name:
        return redirect(url_for('login.index'))

    appointments = []

    all_appointments = get_appointments()

    for appointment in all_appointments:
        patient_name = get_patient_by_id(appointment.get('patient_id'))['data']['name']
        doctor_name = get_staff_by_id(appointment.get('doctor_id'))['data']['name']
        _staff_name = get_staff_by_id(appointment.get('issued_by'))['data']['name']
        appointment_status = get_appointment_status(int(appointment.get('status')))['status_name']
        appointment_data = {
            'receipt_id': appointment.get('receipt_id'),
            'patient_name': patient_name,
            'doctor_name': doctor_name,
            'staff_name': _staff_name,
            'appointment_date': appointment.get('issued_date'),
            'status': appointment_status,
            'total_amount': appointment.get('total_amount')
        }

        appointments.append(appointment_data)

    if receipt_id:
        return redirect(url_for('receptionist.view_appointments_by_filter_id', receipt_id=receipt_id))
    return render_template(
        'cashier/all_receipts.html',
        staff_name=staff_name,
        appointments=appointments
    )


@cashier.route('/make_payment')
def go_to_make_payment():
    staff_name = session.get('name')
    receipt_id = session.get('receipt_id')

    if not staff_name:
        return redirect(url_for('login.index'))

    appointments = []

    all_appointments = get_appointments()

    for appointment in all_appointments:
        patient_name = get_patient_by_id(appointment.get('patient_id'))['data']['name']
        doctor_name = get_staff_by_id(appointment.get('doctor_id'))['data']['name']
        _staff_name = get_staff_by_id(appointment.get('issued_by'))['data']['name']
        appointment_status = get_appointment_status(int(appointment.get('status')))['status_name']
        appointment_data = {
            'receipt_id': appointment.get('receipt_id'),
            'patient_name': patient_name,
            'doctor_name': doctor_name,
            'staff_name': _staff_name,
            'appointment_date': appointment.get('issued_date'),
            'status': appointment_status,
            'total_amount': appointment.get('total_amount')
        }

        appointments.append(appointment_data)

    if receipt_id:
        return redirect(url_for('cashier.index'))
    return render_template(
        'cashier/make_payment.html',
        staff_name=staff_name,
        appointments=appointments
    )