
from app.base.controller import receipt_report_controller


def get_receipt_report_view(receipt_id: int) -> list:
    """
    This View Function is use for get receipt report data

    :param receipt_id: int
    :return: dict of receipt report data
    """
    response: list = receipt_report_controller.get_receipt_report(receipt_id)
    return response
