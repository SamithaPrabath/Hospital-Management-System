from crypt import methods
from datetime import datetime

from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for

from app.routes.doctor import doctor
from app.views.receptionist.receptionist import create_receipt
from app.views.views import get_all_staff_roles, get_doctor_specializations, save_staff, get_all_staff, \
    delete_staff_member, get_staff_by_id, update_staff_by_id, save_patient, get_all_patients, delete_patient_member, \
    get_patient_by_id, update_patient_by_id

receptionist = Blueprint('receptionist', __name__)


@receptionist.route('/')
def index():
    staff_name = session.get('name')
    if not staff_name:
        return redirect(url_for('login.index'))
    return render_template('receptionist/receptionist.html', staff_name=staff_name)


@receptionist.route('/make_appointment')
def go_to_make_appointment():
    staff_name = session.get('name')
    staff_id = session.get('staff_id')

    doctors_details = {}
    # Sample Format
    doctors_details = {
        'Sam Doe': {
            'specialization': 'Cardiologist',
            'id': 1
        },
        'John Doe': {
            'specialization': 'Denist',
            'id': 2
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


@receptionist.route('/submit_appointment', methods=['POST'])
def submit_appointment():
    staff_name = session.get('name')
    staff_id = session.get('staff_id')

    patient_nic = request.form.get('nic')
    doctor_id = int(request.form.get('doctor'))

    response = create_receipt(patient_nic, doctor_id, staff_id)

    if not staff_name:
        return redirect(url_for('login.index'))
    return render_template(
        'receptionist/appointments.html',
        staff_name=staff_name,
        staff_id=staff_id,
    )


@receptionist.route('/appointments')
def view_appointments():
    staff_name = session.get('name')
    if not staff_name:
        return redirect(url_for('login.index'))
    return render_template('receptionist/appointments.html', staff_name=staff_name)


@receptionist.route('/staff-registration')
def staff_register():
    staff_name = session.get('name')
    staff_id = session.get('staff_id')
    staff_roles = get_all_staff_roles()
    doctor_specializations = get_doctor_specializations()
    if not staff_name:
        return redirect(url_for('login.index'))
    return render_template(
        'receptionist/staff_registration.html',
        staff_name=staff_name,
        staff_roles=staff_roles,
        doctor_specializations=doctor_specializations,
        staff_id=staff_id
    )


@receptionist.route('/create-staff', methods=['POST'])
def create_staff():
    data = request.get_json()

    name = data.get('name')
    nic = data.get('nic')
    role_id = data.get('role_id')
    specialization_id = data.get('specialization_id')
    address = data.get('address')
    phone_number_1 = data.get('phone_number_1')
    phone_number_2 = data.get('phone_number_2')
    registered_by = data.get('registered_by')
    password = data.get('password')

    try:
        staff = save_staff(name, nic, role_id, specialization_id, address, phone_number_1, phone_number_2, registered_by, password)
        if staff.get('success'):
            return jsonify({
                "success": True,
                "message": "Staff created successfully.",
                "staff_id": staff.get('staff_id')
            }), 201
        else:
            return jsonify({
                "success": False,
                "message": staff.get('error', 'Failed to create staff')
            }), 500

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 501


@receptionist.route('/view-staff-members')
def view_staff_members():
    staff_name = session.get('name')
    staff_list = get_all_staff()
    if not staff_name:
        return redirect(url_for('login.index'))
    return render_template('receptionist/view_staff.html', staff_name=staff_name, staff_list=staff_list)


@receptionist.route('/<int:staff_id>', methods=['DELETE'])
def delete_staff(staff_id):
    try:
        response = delete_staff_member(staff_id)
        if response.get('success'):
            return jsonify({"success": True, "message": "Staff deleted successfully"}), 200
        else:
            return jsonify({"success": False, "message": response.get('error', 'Failed to delete staff')}), 500
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400


@receptionist.route('/update-staff/<int:staff_id>')
def go_to_update_staff(staff_id):
    staff_name = session.get('name')
    if not staff_name:
        return redirect(url_for('login.index'))
    else:
        staff_roles = get_all_staff_roles()
        doctor_specializations = get_doctor_specializations()
        response = get_staff_by_id(staff_id)
        staff = response.get('data')
        staff_registered_date = datetime.strptime(staff.get('registered_date'),
                                                    "%a, %d %b %Y %H:%M:%S %Z").strftime("%Y-%m-%d")
        return render_template(
            'receptionist/update_staff.html',
                               staff_name=staff_name,
                               staff=staff,
                               staff_roles=staff_roles,
                               doctor_specializations=doctor_specializations,
                               staff_registered_date=staff_registered_date
        )


@receptionist.route('/update-staff', methods=['POST'])
def update_staff():
    data = request.get_json()

    staff_id = data.get('staff_id')
    name = data.get('name')
    nic = data.get('nic')
    role_id = data.get('role_id')
    specialization_id = data.get('specialization_id')
    address = data.get('address')
    phone_number_1 = data.get('phone_number_1')
    phone_number_2 = data.get('phone_number_2')
    registered_by = data.get('registered_by')
    registered_date = data.get('registered_date')

    try:
        staff = update_staff_by_id(staff_id, name, nic, role_id, specialization_id, address, phone_number_1, phone_number_2, registered_by, registered_date)
        if staff.get('success'):
            return jsonify({
                "success": True,
                "message": "Staff Updated successfully."
            }), 200
        else:
            return jsonify({
                "success": False,
                "message": staff.get('error', 'Failed to update staff')
            }), 500

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 501


@receptionist.route('/patient-register')
def patient_register():
    staff_name = session.get('name')
    staff_id = session.get('staff_id')
    if not staff_name:
        return redirect(url_for('login.index'))
    return render_template(
        'receptionist/patient_registration.html',
        staff_name=staff_name,
        staff_id=staff_id
    )


@receptionist.route('/create-patient', methods=['POST'])
def create_patient():
    data = request.get_json()

    name = data.get('name')
    nic = data.get('nic')
    age = data.get('age')
    address = data.get('address')
    phone_number_1 = data.get('phone_number_1')
    phone_number_2 = data.get('phone_number_2')
    registered_by = data.get('registered_by')

    try:
        patient = save_patient(name, nic, age, address, phone_number_1, phone_number_2, registered_by)
        if patient.get('success'):
            return jsonify({
                "success": True,
                "message": "Patient created successfully.",
                "patient_id": patient.get('patient_id')
            }), 201
        else:
            return jsonify({
                "success": False,
                "message": patient.get('error', 'Failed to create patient')
            }), 500

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 501


@receptionist.route('/view-patients')
def view_patients():
    staff_name = session.get('name')
    patient_list = get_all_patients()
    if not staff_name:
        return redirect(url_for('login.index'))
    return render_template('receptionist/view_patient.html', staff_name=staff_name, patient_list=patient_list)


@receptionist.route('/patient-delete/<int:patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    try:
        response = delete_patient_member(patient_id)
        if response.get('success'):
            return jsonify({"success": True, "message": "Patient deleted successfully"}), 200
        else:
            return jsonify({"success": False, "message": response.get('error', 'Failed to delete patient')}), 500
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400


@receptionist.route('/update-patient/<int:patient_id>')
def go_to_update_patient(patient_id):
    staff_name = session.get('name')
    if not staff_name:
        return redirect(url_for('login.index'))
    else:
        response = get_patient_by_id(patient_id)
        patient = response.get('data')
        patient_registered_date = datetime.strptime(patient.get('registered_date'), "%a, %d %b %Y %H:%M:%S %Z").strftime("%Y-%m-%d")
        return render_template('receptionist/update_patient.html', staff_name=staff_name, patient=patient, patient_registered_date=patient_registered_date)


@receptionist.route('/update-patient', methods=['POST'])
def update_patient():
    data = request.get_json()

    patient_id = data.get('patient_id')
    name = data.get('name')
    nic = data.get('nic')
    age = data.get('age')
    address = data.get('address')
    phone_number_1 = data.get('phone_number_1')
    phone_number_2 = data.get('phone_number_2')
    registered_by = data.get('registered_by')
    registered_date = data.get('registered_date')

    try:
        patient = update_patient_by_id(patient_id, name, nic, age, address, phone_number_1, phone_number_2, registered_by, registered_date)
        if patient.get('success'):
            return jsonify({
                "success": True,
                "message": "Patient Updated successfully."
            }), 200
        else:
            return jsonify({
                "success": False,
                "message": patient.get('error', 'Failed to update staff')
            }), 500

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 501
