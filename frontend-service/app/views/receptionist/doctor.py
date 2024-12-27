import requests


def get_doctors_details():
    """
    This function is use for get doctor details

    :return: dict of doctor details
    """

    response = requests.get(
        'http://localhost:5001/staff/doctors'
    )

    doctor_details = response.json()

    return doctor_details
