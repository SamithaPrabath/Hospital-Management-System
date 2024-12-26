import requests


def get_receipt_reports(receipt_id: int):

    response = requests.get(
        f'http://localhost:5004/receipt_reports/{receipt_id}',
    )
    response_data = response.json()

    return response_data
