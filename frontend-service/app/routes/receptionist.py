from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for

from app.routes.doctor import doctor
from app.views.views import get_all_staff_roles, get_doctor_specializations, save_staff, get_all_staff, \
    delete_staff_member, get_staff_by_id, update_staff_by_id

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
        return render_template('receptionist/update_staff.html', staff_name=staff_name, staff=staff, staff_roles=staff_roles, doctor_specializations=doctor_specializations)


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

    try:
        staff = update_staff_by_id(staff_id, name, nic, role_id, specialization_id, address, phone_number_1, phone_number_2, registered_by)
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
