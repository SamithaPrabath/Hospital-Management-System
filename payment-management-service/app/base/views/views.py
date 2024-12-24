from flask import request

from app.base.controller.payment_controller import get_payment, make_payment


def make_payment_view() -> dict[str, str]:
    """
    This View Function is use for make payment for a receipt

    :return: dict of message
    """
    # get the request data
    data: dict = request.get_json()

    response = make_payment(data)
    return response


def get_payment_view(payment_id: int) -> dict:
    """
    This View Function is use for get payment data

    :param payment_id: int
    :return: dict of receipt data
    """
    response = get_payment(payment_id)
    return response
