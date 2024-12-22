from flask import request

from app.base.controller.payment_controller import create_payment, get_payment


def generate_payment() -> dict[str, str]:
    """
    This View Function is use for generate receipt for a patient/appointment

    :return: dict of message
    """
    # get the request data
    data: dict = request.get_json()

    response = create_payment(data)
    return response


def get_payment_view(receipt_id: int) -> dict:
    """
    This View Function is use for get receipt data

    :param receipt_id: int
    :return: dict of receipt data
    """
    response = get_payment(receipt_id)
    return response
