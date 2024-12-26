import requests


def get_receipt_reports(receipt_id: int):

    response = requests.get(
        f'http://localhost:5004/receipt_reports/{receipt_id}',
    )
    response_data = response.json()

    return response_data


def create_medical_reports(
        report_id: int,
        receipt_id: int,
        image: str,
        description: str,
        issued_by: str
):

    response = requests.post(
        f'http://localhost:5004/medical_reports',
        json={
            'report_id': report_id,
            'receipt_id': receipt_id,
            'image': image,
            'description': description,
            'issued_by': issued_by,
        }
    )


def update_receipt_reports(receipt_id: int, report_id: int, status: str = 'Completed'):

    response = requests.put(
        f'http://localhost:5004/receipt_reports/{receipt_id}/update/{report_id}?status={status}',
    )

    if status == 'Pending':
        requests.delete(
            f'http://localhost:5004/medical_reports/{receipt_id}/delete/{report_id}'
        )


def get_medical_reports(
        receipt_id: int,
):

    response = requests.get(
        f'http://localhost:5004/medical_reports/{receipt_id}'
    )

    response_data = response.json()

    return response_data
