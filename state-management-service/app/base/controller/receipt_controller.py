from app.base.model.receipt import Receipt
from app.base.model.receipt_model import ReceiptModel


def create_receipt(receipt_data: dict) -> dict:
    """
    This function is use for create receipt for a patient/appointment

    :param receipt_data: dict of receipt data
    :return: dict of message
    """

    receipt_model: ReceiptModel = ReceiptModel()

    receipt_id: int = receipt_model.create_receipt(receipt_data)

    return {'message': "Receipt created successfully", 'id': receipt_id}


def get_receipt(receipt_id: int) -> dict:
    """
    This function is use for get receipt data

    :param receipt_id: int
    :return: dict of receipt data
    """

    receipt_model: ReceiptModel = ReceiptModel()

    receipt_data: dict = receipt_model.get_receipt(receipt_id)

    return receipt_data


def get_all_receipts() -> list:
    """
    This function is use for get receipt data

    :return: dict of receipt data
    """

    receipt_model: ReceiptModel = ReceiptModel()

    receipt_data: list = receipt_model.get_all_receipts()

    return receipt_data


def get_status_types(status_id: int) -> dict:
    """
    This function is use for get receipt status types

    :param status_id: int
    :return: dict of receipt status types
    """

    receipt_model: ReceiptModel = ReceiptModel()

    status_data: dict = receipt_model.get_status_types(status_id)

    return status_data


def get_doctor_receipts(doctor_id: int) -> list:
    """
    This function is use for get doctor receipt data

    :param doctor_id: int
    :return: dict of receipt data
    """

    receipt_model: ReceiptModel = ReceiptModel()

    receipt_data: list = receipt_model.get_doctor_receipts(doctor_id)

    return receipt_data
