from flask import request

from app.base.controller.receipt_controller import create_receipt, get_receipt, get_all_receipts, get_status_types, \
    get_doctor_receipts, update_receipt_status, update_total_amount
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


def get_all_receipts_view() -> list:
    """
    This View Function is use for get receipt data

    :return: dict of receipt data
    """
    response = get_all_receipts()
    return response


def get_status_types_view(status_id: int) -> dict:
    """
    This View Function is use for get receipt status types

    :param status_id: int
    :return: dict of receipt status types
    """

    status_data: dict = get_status_types(status_id)
    return status_data


def get_receipt_by_doc_id_view(doctor_id: int) -> list:
    """
    This View Function is use for get receipt data

    :return: dict of receipt data
    """

    receipt_data: list = get_doctor_receipts(doctor_id)
    return receipt_data


def update_receipt_status_view(receipt_id: int, status_id: int) -> dict:
    """
    This View Function is use for update receipt status

    :param receipt_id: int
    :param status_id: int
    :return: dict of message
    """
    # get the request data

    response = update_receipt_status(receipt_id, status_id)
    return {'message': 'done'}


def update_total_amount_view(receipt_id: int, total_amount: int) -> dict:
    """
    This View Function is use for update receipt status

    :param receipt_id: int
    :param total_amount: int
    :return: dict of message
    """
    # get the request data

    response = update_total_amount(receipt_id, total_amount)
    return {'message': 'done'}
