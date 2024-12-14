from quart import request


async def generate_receipt() -> dict[str, str]:
    """
    This View Function is use for generate receipt for a patient/appointment

    :return: dict of message
    """
    # get the request data
    data = await request.get_json()

    return {'message': 'success'}
