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
