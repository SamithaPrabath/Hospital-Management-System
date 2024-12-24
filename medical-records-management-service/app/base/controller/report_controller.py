from app.base.model.report_model import ReportModel


def create_report(receipt_data: dict) -> dict:
    """
    This function is use for create receipt for a patient/appointment

    :param receipt_data: dict of receipt data
    :return: dict of message
    """

    report_model: ReportModel = ReportModel()

    receipt_id: int = report_model.create_report(receipt_data)

    return {'message': "Receipt created successfully", 'id': receipt_id}


def get_report(receipt_id: int) -> dict:
    """
    This function is use for get receipt data

    :param receipt_id: int
    :return: dict of receipt data
    """

    receipt_model: ReportModel = ReportModel()

    receipt_data: dict = receipt_model.get_report(receipt_id)

    return receipt_data
