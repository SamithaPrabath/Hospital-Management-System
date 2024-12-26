from flask import request

from app.base.controller import receipt_report_controller, medical_report_controller


def get_receipt_report_view(receipt_id: int) -> list:
    """
    This View Function is use for get receipt report data

    :param receipt_id: int
    :return: dict of receipt report data
    """
    response: list = receipt_report_controller.get_receipt_report(receipt_id)
    return response


def create_medical_report_view() -> str:
    """
    This View Function is use for get receipt report data

    :return: dict of receipt report data
    """
    report_data: dict = request.json
    response: int = medical_report_controller.create_medical_report(report_data)
    return 'Done'


def update_receipt_report_view(receipt_id: int, report_id: int) -> str:
    """
    This View Function is use for update receipt report status

    :param receipt_id: int
    :param report_id: int
    :return: str
    """
    status: str = request.args.get('status')
    receipt_report_controller.update_receipt_report(receipt_id, report_id, status)
    return 'Done'

def get_medical_report_view(receipt_id: int) -> list:
    """
    This View Function is use for get medical report data

    :param receipt_id: int
    :return: dict of medical report data
    """
    response: list = medical_report_controller.get_medical_report(receipt_id)
    return response


def delete_medical_report_view(receipt_id: int, report_id: int) -> str:
    """
    This View Function is use for delete medical report

    :param receipt_id: int
    :param report_id: int
    :return: str
    """
    medical_report_controller.delete_medical_report(receipt_id, report_id)
    return 'Done'
