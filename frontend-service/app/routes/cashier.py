from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for

from app.views.radiologist.radiologist import get_medical_reports_with_price
from app.views.receptionist.receptionist import get_appointments, get_appointment_status, update_receipt_status
from app.views.views import get_patient_by_id, get_staff_by_id

cashier = Blueprint('cashier', __name__)


@cashier.route('/')
def index():
    staff_name = session.get('name')
    if not staff_name:
        return redirect(url_for('login.index'))
    return render_template('cashier/cashier.html', staff_name=staff_name)

@cashier.route('/all_receipts')
def go_to_all_receipts():
    staff_name = session.get('name')
    receipt_id = session.get('receipt_id')

    if not staff_name:
        return redirect(url_for('login.index'))

    appointments = []

    all_appointments = get_appointments()

    for appointment in all_appointments:
        activities = [
            {
                'activity': 'Appointment Charge',
                'cost': 1000
            }
        ]
        patient_name = get_patient_by_id(appointment.get('patient_id'))['data']['name']
        doctor_data = get_staff_by_id(appointment.get('doctor_id'))['data']
        doctor_name = doctor_data['name']
        doctor_fees = {
            'activity': 'Doctor Fees',
            'cost': doctor_data['price']
        }
        activities.append(doctor_fees)

        medical_reports = get_medical_reports_with_price(int(appointment.get('receipt_id')))
        for report in medical_reports:
            report_data = {
                'activity': report.get('type'),
                'cost': report.get('price')
            }
            activities.append(report_data)

        _staff_name = get_staff_by_id(appointment.get('issued_by'))['data']['name']
        appointment_status = get_appointment_status(int(appointment.get('status')))['status_name']
        appointment_data = {
            'receipt_id': appointment.get('receipt_id'),
            'patient_name': patient_name,
            'doctor_name': doctor_name,
            'doctor_id': doctor_data['staff_id'],
            'staff_name': _staff_name,
            'appointment_date': appointment.get('issued_date'),
            'activities': activities,
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
    receipt_id = request.args.get('receipt_id')

    activities = [
        {
            'activity': 'Appointment Charge',
            'cost': 1000
        }
    ]
    doctor_data = get_staff_by_id(request.args.get('doctor_id'))['data']
    doctor_fees = {
        'activity': 'Doctor Fees',
        'cost': doctor_data['price']
    }
    activities.append(doctor_fees)

    medical_reports = get_medical_reports_with_price(int(receipt_id))
    for report in medical_reports:
        report_data = {
            'activity': report.get('type'),
            'cost': report.get('price')
        }
        activities.append(report_data)

    patient_name = request.args.get('patient_name')
    doctor_name = request.args.get('doctor_name')
    _staff_name = request.args.get('staff_name')
    appointment_date = request.args.get('appointment_date')
    total_amount = request.args.get('total_amount')

    if not staff_name:
        return redirect(url_for('login.index'))


    update_receipt_status(int(receipt_id), 5)
    if not receipt_id:
        return redirect(url_for('cashier.index'))
    return render_template(
        'cashier/payment_template.html',
        receipt_id=receipt_id,
        patient_name=patient_name,
        doctor_name=doctor_name,
        staff_name=_staff_name,
        appointment_date=appointment_date,
        activities=activities,
        total_amount=total_amount
    )