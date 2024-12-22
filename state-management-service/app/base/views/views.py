from flask import request

from app.base.controller.receipt_controller import create_receipt, get_receipt
from app.base.model.receipt import Receipt


def generate_receipt() -> dict[str, str]:
    """
    This View Function is use for generate receipt for a patient/appointment

    :return: dict of message
    """
    # get the request data
    data: dict = request.get_json()

    response = create_receipt(data)
    return response


def get_receipt_view(receipt_id: int) -> dict:
    """
    This View Function is use for get receipt data

    :param receipt_id: int
    :return: dict of receipt data
    """
    response = get_receipt(receipt_id)
    return response
