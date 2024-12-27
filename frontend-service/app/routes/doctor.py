from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for

from app.views.radiologist.radiologist import add_reqeust_report
from app.views.receptionist.receptionist import get_appointment_status, get_appointments_for_doctor, \
    get_appointment_by_id, update_receipt_status, update_total_amount
from app.views.views import get_patient_by_id, get_staff_by_id

doctor = Blueprint('doctor', __name__)


@doctor.route('/')
def index():
    staff_name = session.get('name')
    if not staff_name:
        return redirect(url_for('login.index'))
    return render_template('radiologist.html', staff_name=staff_name)


@doctor.route('/request_reports')
def go_to_request_report():
    staff_name = session.get('name')
    staff_id = session.get('staff_id')

    doctors_details = {}

    if not staff_name:
        return redirect(url_for('login.index'))
    return render_template(
        'doctor/request_report.html',
        staff_name=staff_name,
        staff_id=staff_id,
        doctors_details=doctors_details
    )


@doctor.route('/appointments')
def view_appointments():
    staff_name = session.get('name')
    receipt_id = session.get('receipt_id')
    staff_id = int(session.get('staff_id'))

    if not staff_name:
        return redirect(url_for('login.index'))

    appointments = []

    all_appointments = get_appointments_for_doctor(staff_id)

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
        return redirect(url_for('dashboard.go_to_doctor_page', receipt_id=receipt_id))
    return render_template(
        'doctor/appointments.html',
        staff_name=staff_name,
        appointments=appointments
    )


@doctor.route('/submit_request_lab_report', methods=['POST'])
def submit_request_lab_report():
    staff_name = session.get('name')
    staff_id = session.get('staff_id')

    if not staff_name:
        return redirect(url_for('login.index'))

    try:
        receipt_id = int(request.form.get('receipt_id'))
        get_appointment_by_id(receipt_id)

        doctor_notes = request.form.get('doctor_notes')
        doctor_price = get_staff_by_id(staff_id)['data']['price']

        if doctor_price:
            update_total_amount(receipt_id, int(doctor_price))

        if 'mri' in request.form:
            add_reqeust_report(receipt_id, 1, doctor_notes)
        if 'ct' in request.form:
            add_reqeust_report(receipt_id, 2, doctor_notes)
        if 'xray' in request.form:
            add_reqeust_report(receipt_id, 3, doctor_notes)

        update_receipt_status(receipt_id, 2)

        return redirect(url_for('doctor.view_appointments'))
    except Exception as e:
        error = "Invalid Receipt ID"
        return render_template(
            'doctor/request_report.html',
            staff_name=staff_name,
            staff_id=staff_id,
            error=error
        )
