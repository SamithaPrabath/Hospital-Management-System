from app.base.model.payment_model import PaymentModel


def make_payment(payment_data: dict) -> dict:
    """
    This function is use for make payment for a receipt

    :param payment_data: dict of payment data
    :return: dict of message
    """

    payment_model: PaymentModel = PaymentModel()

    payment_id: int = payment_model.make_payment(payment_data)

    return {'message': "Paid successfully", 'id': payment_id}


def get_payment(payment_id: int) -> dict:
    """
    This function is use for get payment data

    :param payment_id: int
    :return: dict of payment data
    """

    payment_model: PaymentModel = PaymentModel()

    payment_data: dict = payment_model.get_payment(payment_id)

    return payment_data
