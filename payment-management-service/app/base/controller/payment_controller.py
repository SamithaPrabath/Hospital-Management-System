from app.base.model.payment_model import PaymentModel


def create_payment(receipt_data: dict) -> dict:
    """
    This function is use for create receipt for a patient/appointment

    :param receipt_data: dict of receipt data
    :return: dict of message
    """

    report_model: PaymentModel = PaymentModel()

    receipt_id: int = report_model.create_payment(receipt_data)

    return {'message': "Receipt created successfully", 'id': receipt_id}


def get_payment(receipt_id: int) -> dict:
    """
    This function is use for get receipt data

    :param receipt_id: int
    :return: dict of receipt data
    """

    receipt_model: PaymentModel = PaymentModel()

    receipt_data: dict = receipt_model.get_payment(receipt_id)

    return receipt_data
