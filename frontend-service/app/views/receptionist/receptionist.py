import requests

from app.views.views import get_patient_by_nic


def create_receipt(
        patient_nic: str,
        doctor_id: int,
        staff_id: int,
):

    try:
        patient_data = get_patient_by_nic(patient_nic)
        patient_id = patient_data['data']['patient_id']

        response = requests.post(
            'http://localhost:5003/receipt',
            json={
                "patient_id": patient_id,
                "doctor_id": doctor_id,
                "staff_id": staff_id,
            }
        )
        response_data = response.json()
        return response_data
    except Exception as e:
        return False


def get_appointments():
    response = requests.get('http://localhost:5003/receipts')
    response_data = response.json()
    return response_data


def get_appointment_by_id(appointment_id: int):
    response = requests.get(f'http://localhost:5003/receipt/{appointment_id}')
    response_data = response.json()
    return response_data


def get_appointments_for_doctor(doctor_id: int):
    response = requests.get(f'http://localhost:5003/receipt/doctor/{doctor_id}')
    response_data = response.json()
    return response_data


def get_appointment_status(status_id: int):
    response = requests.get(f'http://localhost:5003/receipt/status/{status_id}')
    response_data = response.json()
    return response_data