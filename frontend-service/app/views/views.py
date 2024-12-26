from datetime import datetime

import requests


def validate_user_with_patient_service(nic, password):
    try:
        response = requests.post(
            'http://127.0.0.1:5001/staff/login',
            json={"nic": nic, "password": password}
        )
        response_data = response.json()

        if response.status_code == 200 and response_data.get('is_authenticated'):
            return {"success": True, "data": response_data}
        else:
            return {"success": False, "error": response_data.get('error', 'Login failed')}
    except requests.exceptions.RequestException as e:
        return {"success": False, "error": str(e)}

def get_all_staff_roles():
    try:
        response = requests.get(
            'http://127.0.0.1:5001/staff/roles'
        )
        response_data = response.json()

        if response.status_code == 200:
            return response_data
        else:
            return []
    except requests.exceptions.RequestException as e:
        return []

def get_doctor_specializations():
    try:
        response = requests.get(
            'http://127.0.0.1:5001/staff/doctor-specializations'
        )
        response_data = response.json()

        if response.status_code == 200:
            return response_data
        else:
            return []
    except requests.exceptions.RequestException as e:
        return []

def save_staff(name, nic, role_id, specialization_id, address, phone_number_1, phone_number_2, registered_by, password):
    phone_numbers = []
    if phone_number_1:
        phone_numbers.append(phone_number_1.strip())
    if phone_number_2:
        phone_numbers.append(phone_number_2.strip())

    current_date = datetime.now().strftime("%Y-%m-%d")
    try:
        response = requests.post(
            'http://127.0.0.1:5001/staff',
            json={
                "name": name,
                "nic": nic,
                "role_id": role_id,
                "specialization_id": specialization_id,
                "address": address,
                "registered_by": registered_by,
                "password": password,
                "registered_date": current_date,
                "phone_numbers": phone_numbers
            }
        )
        response_data = response.json()

        if response.status_code == 201:
            return {"success": True, "staff_id": response_data.get('id')}
        elif 'error' in response_data:
            return {"success": False, "error": response_data.get('error')}
        else:
            return {"success": False, "error": "Error occurred while saving staff"}
    except requests.exceptions.RequestException as e:
        return {"success": False, "error": str(e)}

def update_staff_by_id(staff_id, name, nic, role_id, specialization_id, address, phone_number_1, phone_number_2, registered_by, registered_date):
    phone_numbers = []
    if phone_number_1:
        phone_numbers.append(phone_number_1.strip())
    if phone_number_2:
        phone_numbers.append(phone_number_2.strip())

    try:
        response = requests.put(
            f'http://127.0.0.1:5001/staff/{staff_id}',
            json={
                "name": name,
                "nic": nic,
                "role_id": role_id,
                "specialization_id": specialization_id,
                "address": address,
                "registered_by": registered_by,
                "registered_date": registered_date,
                "phone_numbers": phone_numbers
            }
        )
        response_data = response.json()

        if response.status_code == 200:
            return {"success": True, "message": response_data.get('message')}
        elif 'error' in response_data:
            return {"success": False, "error": response_data.get('error')}
        else:
            return {"success": False, "error": "Error occurred while updating staff"}
    except requests.exceptions.RequestException as e:
        return {"success": False, "error": str(e)}

def get_all_staff():
    try:
        response = requests.get(
            'http://127.0.0.1:5001/staff/staff-list'
        )
        response_data = response.json()

        if response.status_code == 200:
            return response_data
        else:
            return []
    except requests.exceptions.RequestException as e:
        return []

def delete_staff_member(staff_id):
    try:
        response = requests.delete(
            f'http://127.0.0.1:5001/staff/{staff_id}'
        )
        response_data = response.json()

        if response.status_code == 200:
            return {"success": True}
        elif 'error' in response_data:
            return {"success": False, "error": response_data.get('error')}
        else:
            return {"success": False, "error": "Error occurred while deleting staff"}
    except requests.exceptions.RequestException as e:
        return {"success": False, "error": str(e)}

def get_staff_by_id(staff_id):
    try:
        response = requests.get(
            f'http://127.0.0.1:5001/staff/{staff_id}'
        )
        response_data = response.json()

        if response.status_code == 200:
            return {"success": True, "data": response_data}
        else:
            return {"success": False, "error": response_data.get('error', 'Staff not found')}
    except requests.exceptions.RequestException as e:
        return {"success": False, "error": str(e)}

def user_password_change(staff_id, current_password, new_password):
    try:
        response = requests.patch(
            f'http://127.0.0.1:5001/staff/{staff_id}/change-password',
            json={
                "current_password": current_password,
                "new_password": new_password
            }
        )
        response_data = response.json()

        if response.status_code == 200:
            return {"success": True, "message": response_data.get('message')}
        elif 'error' in response_data:
            return {"success": False, "error": response_data.get('error')}
        else:
            return {"success": False, "error": "Error occurred while updating password"}
    except requests.exceptions.RequestException as e:
        return {"success": False, "error": str(e)}

def save_patient(name, nic, age, address, phone_number_1, phone_number_2, registered_by):
    phone_numbers = []
    if phone_number_1:
        phone_numbers.append(phone_number_1.strip())
    if phone_number_2:
        phone_numbers.append(phone_number_2.strip())

    current_date = datetime.now().strftime("%Y-%m-%d")
    try:
        response = requests.post(
            'http://127.0.0.1:5002/patient',
            json={
                "name": name,
                "nic": nic,
                "age": age,
                "address": address,
                "phone_numbers": phone_numbers,
                "registered_by": registered_by,
                "registered_date": current_date,
            }
        )
        response_data = response.json()

        if response.status_code == 201:
            return {"success": True, "patient_id": response_data.get('id')}
        elif 'error' in response_data:
            return {"success": False, "error": response_data.get('error')}
        else:
            return {"success": False, "error": "Error occurred while saving staff"}
    except requests.exceptions.RequestException as e:
        return {"success": False, "error": str(e)}

def get_all_patients():
    try:
        response = requests.get(
            'http://127.0.0.1:5002/patient/patient-list'
        )
        response_data = response.json()

        if response.status_code == 200:
            return response_data
        else:
            return []
    except requests.exceptions.RequestException as e:
        return []

def delete_patient_member(patient_id):
    try:
        response = requests.delete(
            f'http://127.0.0.1:5002/patient/{patient_id}'
        )
        response_data = response.json()

        if response.status_code == 200:
            return {"success": True}
        elif 'error' in response_data:
            return {"success": False, "error": response_data.get('error')}
        else:
            return {"success": False, "error": "Error occurred while deleting staff"}
    except requests.exceptions.RequestException as e:
        return {"success": False, "error": str(e)}

def get_patient_by_id(patient_id):
    try:
        response = requests.get(
            f'http://127.0.0.1:5002/patient/{patient_id}'
        )
        response_data = response.json()

        if response.status_code == 200:
            return {"success": True, "data": response_data}
        else:
            return {"success": False, "error": response_data.get('error', 'Patient not found')}
    except requests.exceptions.RequestException as e:
        return {"success": False, "error": str(e)}

def update_patient_by_id(patient_id, name, nic, age, address, phone_number_1, phone_number_2, registered_by, registered_date):
    phone_numbers = []
    if phone_number_1:
        phone_numbers.append(phone_number_1.strip())
    if phone_number_2:
        phone_numbers.append(phone_number_2.strip())

    try:
        response = requests.put(
            f'http://127.0.0.1:5002/patient/{patient_id}',
            json={
                "name": name,
                "nic": nic,
                "age": age,
                "address": address,
                "registered_by": registered_by,
                "registered_date": registered_date,
                "phone_numbers": phone_numbers
            }
        )
        response_data = response.json()

        if response.status_code == 200:
            return {"success": True, "message": response_data.get('message')}
        elif 'error' in response_data:
            return {"success": False, "error": response_data.get('error')}
        else:
            return {"success": False, "error": "Error occurred while updating patient"}
    except requests.exceptions.RequestException as e:
        return {"success": False, "error": str(e)}
