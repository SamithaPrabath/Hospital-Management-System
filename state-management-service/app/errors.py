import logging


def key_error_handler(e: KeyError):
    logging.error(f"KeyError: {e}")

    return {"error": f"{e.args[0]} is a required field", "missing_key": f"{e.args[0]}"}, 200
