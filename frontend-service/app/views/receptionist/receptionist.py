import requests


def create_receipt(
        patient_nic: str,
        doctor_id: int,
        staff_id: int,
):

    # get_patient_from_nic(patient_nic)
    response = requests.get(
        f'http://localhost:5002/patients/{patient_nic}',
    )
    return response_data
