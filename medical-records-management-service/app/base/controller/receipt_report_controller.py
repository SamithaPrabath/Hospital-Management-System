from app.base.model.receipt_report_model import ReceiptReportModel


def get_receipt_report(receipt_id: int) -> list:
    """
    This function is use for get report status data

    :param receipt_id: int
    :return: dict of receipt data
    """

    receipt_report_model: ReceiptReportModel = ReceiptReportModel()

    receipt_report_data: list = receipt_report_model.get_receipt_report(receipt_id)

    return receipt_report_data


def update_receipt_report(receipt_id: int, report_id: int, status:str) -> int:
    """
    This function is use for update receipt report status

    :param receipt_id: int
    :param report_id: int
    :param status:str
    :return: int
    """

    receipt_report_model: ReceiptReportModel = ReceiptReportModel()

    receipt_report_model.update_receipt_report(receipt_id, report_id, status)

    return 1


def create_receipt_report(report_data: dict) -> int:
    """
    This function is use for create receipt report

    :param report_data: dict
    :return: int
    """

    receipt_report_model: ReceiptReportModel = ReceiptReportModel()

    receipt_report_model.create_receipt_report(report_data)

    return 1
