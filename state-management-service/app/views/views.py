from quart import request

from app.model.receipt import Receipt


async def generate_receipt() -> dict[str, str]:
    """
    This View Function is use for generate receipt for a patient/appointment

    :return: dict of message
    """
    # get the request data
    data = await request.get_json()

    response = await Receipt(
        patient_id=data['patient_id'],
        doctor_id=data['doctor_id'],
        issued_by=data['issued_by'],
        issued_date=data['issued_date'],
        total_amount=data['total_amount']
    )
    return response
