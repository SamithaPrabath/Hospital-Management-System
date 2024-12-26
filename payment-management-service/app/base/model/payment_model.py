import asyncio
import uuid
from datetime import datetime

from app.base.model.payment import Payment
from app.base.utilities import const
from app.base.utilities.query_executor import AsyncQueryExecutor

DB_CONFIG = {
    'host': const.DB_HOST,
    'user': const.DB_USER,
    'password': const.DB_PASSWORD,
    'database': const.DB_NAME,
    'port': const.DB_PORT
}


class PaymentModel:
    def __init__(self):
        self.db_config = DB_CONFIG
        self.query_executor = AsyncQueryExecutor(DB_CONFIG)

    def make_payment(self, payment_data: dict) -> int:
        """
        Make payment for a receipt

        :param payment_data: dict
        """
        today: datetime = datetime.now()
        # Generate a random UUID
        random_uuid = uuid.uuid4()

        # Convert the UUID to an integer
        payment_id = random_uuid.int % (10**8)

        query: str = (f"INSERT INTO payment "
                      f"(payment_id, receipt_id, collected_by, collected_date) "
                      f"VALUES ({payment_id}, {payment_data['receipt_id']}, {payment_data['collected_by']}, "
                      f"'{today}')")

        asyncio.run(self.query_executor.execute(query))

        return payment_id

    def get_payment(self, payment_id: int) -> dict:
        """
        Get payment data from the database.
        :param payment_id:
        :return:
        """
        query: str = f"SELECT * FROM payment WHERE payment_id = {payment_id}"

        payment_data = asyncio.run(self.query_executor.fetch_one(query))

        if not payment_data:
            return {}
        payment: Payment = Payment(
            payment_id=payment_data[0],
            receipt_id=payment_data[1],
            collected_by=payment_data[2],
            collected_date=payment_data[3]
        )

        return payment.get_payment_dict()
