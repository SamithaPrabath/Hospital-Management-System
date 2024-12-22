from flask import request

from app.base.controller.report_controller import create_report, get_report


def generate_report() -> dict[str, str]:
    """
    This View Function is use for generate receipt for a patient/appointment

    :return: dict of message
    """
    # get the request data
    data: dict = request.get_json()

    response = create_report(data)
    return response


def get_report_view(receipt_id: int) -> dict:
    """
    This View Function is use for get receipt data

    :param receipt_id: int
    :return: dict of receipt data
    """
    response = get_report(receipt_id)
    return response
