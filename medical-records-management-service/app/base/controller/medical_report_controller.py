from app.base.model.report_model import MedicalReportModel


def create_medical_report(report_data: dict) -> int:
    """
    This function is use for create new medical report

    :param report_data: dict
    :return: dict of receipt data
    """

    medical_report_model: MedicalReportModel = MedicalReportModel()

    medical_report_model.create_medical_report(report_data)

    return 1


def get_medical_report(receipt_id: int) -> list:
    """
    This function is use for get medical report data

    :param receipt_id: int
    :return: dict of medical report data
    """

    medical_report_model: MedicalReportModel = MedicalReportModel()

    medical_report_data: list = medical_report_model.get_medical_report(receipt_id)

    return medical_report_data


def delete_medical_report(receipt_id: int, report_id: int) -> int:
    """
    This function is use for delete medical report

    :param receipt_id: int
    :param report_id: int
    :return: int
    """

    medical_report_model: MedicalReportModel = MedicalReportModel()

    medical_report_model.delete_medical_report(receipt_id, report_id)

    return 1