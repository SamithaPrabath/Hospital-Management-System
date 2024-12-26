from app.base.model.receipt_report_model import ReceiptReportModel
from app.base.model.report_model import ReportModel



def get_receipt_report(receipt_id: int) -> list:
    """
    This function is use for get report status data

    :param receipt_id: int
    :return: dict of receipt data
    """

    receipt_report_model: ReceiptReportModel = ReceiptReportModel()

    receipt_report_data: list = receipt_report_model.get_receipt_report(receipt_id)

    return receipt_report_data
