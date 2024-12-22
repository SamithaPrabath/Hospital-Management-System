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

    def create_payment(self, report_data: dict) -> int:
        """
        Create a new report in the database.
        :param receipt_data:
        :return:
        """
        today: datetime = datetime.now()
        total_amount: float = const.FIXED_AMOUNT
        # Generate a random UUID
        random_uuid = uuid.uuid4()

        # Convert the UUID to an integer
        report_id = random_uuid.int % (10**8)

        query: str = (f"INSERT INTO receipt "
                      f"(receipt_id, patient_id, doctor_id, issued_by, issued_date, total_amount, status_id)) "
                      f"VALUES ({report_id}, {report_data['patient_id']}, {report_data['doctor_id']}, "
                      f"{report_data['issued_by']}, '{today}', {total_amount}, 1)")

        asyncio.run(self.query_executor.execute(query))

        return report_id

    def get_payment(self, receipt_id: int) -> dict:
        """
        Get receipt data from the database.
        :param receipt_id:
        :return:
        """
        query: str = f"""
            SELECT * FROM receipt WHERE receipt_id = {receipt_id}
        """

        receipt_data = asyncio.run(self.query_executor.fetch_one(query))

        receipt: Payment = Payment(
            receipt_id=receipt_data[0],
            patient_id=receipt_data[1],
            doctor_id=receipt_data[2],
            issued_by=receipt_data[3],
            issued_date=receipt_data[4],
            total_amount=receipt_data[5],
            status=receipt_data[6]
        )

        return receipt.get_receipt_dict()
