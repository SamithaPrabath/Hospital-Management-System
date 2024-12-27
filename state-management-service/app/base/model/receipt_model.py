import asyncio
import uuid
from datetime import datetime

from app.base.model.receipt import Receipt
from app.base.utilities import const
from app.base.utilities.query_executor import AsyncQueryExecutor

DB_CONFIG = {
    'host': const.DB_HOST,
    'user': const.DB_USER,
    'password': const.DB_PASSWORD,
    'database': const.DB_NAME,
    'port': const.DB_PORT
}


class ReceiptModel:
    def __init__(self):
        self.db_config = DB_CONFIG
        self.query_executor = AsyncQueryExecutor(DB_CONFIG)

    def create_receipt(self, receipt_data: dict) -> int:
        """
        Create a new receipt in the database.
        :param receipt_data:
        :return:
        """
        today: datetime = datetime.now()
        total_amount: float = const.FIXED_AMOUNT
        # Generate a random UUID
        random_uuid = uuid.uuid4()

        # Convert the UUID to an integer
        receipt_id = random_uuid.int % (10**8)

        query: str = (f"INSERT INTO receipt "
                      f"(receipt_id, patient_id, doctor_id, issued_by, issued_date, total_amount, status_id) "
                      f"VALUES ({receipt_id}, {receipt_data['patient_id']}, {receipt_data['doctor_id']}, "
                      f"{receipt_data['staff_id']}, '{today}', {total_amount}, 1)")

        asyncio.run(self.query_executor.execute(query))

        return receipt_id

    def get_receipt(self, receipt_id: int) -> dict:
        """
        Get receipt data from the database.
        :param receipt_id:
        :return:
        """
        query: str = f"""
            SELECT * FROM receipt WHERE receipt_id = {receipt_id}
        """

        receipt_data = asyncio.run(self.query_executor.fetch_one(query))

        receipt: Receipt = Receipt(
            receipt_id=receipt_data[0],
            patient_id=receipt_data[1],
            doctor_id=receipt_data[2],
            issued_by=receipt_data[3],
            issued_date=receipt_data[4],
            total_amount=receipt_data[5],
            status=receipt_data[6]
        )

        return receipt.get_receipt_dict()

    def get_all_receipts(self) -> list:
        """
        Get receipt data from the database.

        :return:
        """
        query: str = f"""
            SELECT * FROM receipt order by issued_date desc
        """

        receipt_data = asyncio.run(self.query_executor.fetch_all(query))

        receipts = []

        for rec in receipt_data:
            receipt: Receipt = Receipt(
                receipt_id=rec[0],
                patient_id=rec[1],
                doctor_id=rec[2],
                issued_by=rec[3],
                issued_date=rec[4],
                total_amount=rec[5],
                status=rec[6]
            )
            receipts.append(receipt.get_receipt_dict())

        return receipts

    def get_status_types(self, status_id: int) -> dict:
        """
        This function is use for get receipt status types

        :param status_id: int
        :return: dict of receipt status types
        """

        query = f"""
            SELECT * FROM receipt_status WHERE status_id = {status_id}
        """

        status_data = asyncio.run(self.query_executor.fetch_one(query))

        status = {
            'status_id': status_data[0],
            'status_name': status_data[1]
        }

        return status

    def get_doctor_receipts(self, doctor_id: int) -> list:
        """
        Get receipt data from the database.

        :return:
        """
        query: str = f"""
            SELECT * FROM receipt WHERE doctor_id = {doctor_id} order by issued_date desc
        """

        receipt_data = asyncio.run(self.query_executor.fetch_all(query))

        receipts = []

        for rec in receipt_data:
            receipt: Receipt = Receipt(
                receipt_id=rec[0],
                patient_id=rec[1],
                doctor_id=rec[2],
                issued_by=rec[3],
                issued_date=rec[4],
                total_amount=rec[5],
                status=rec[6]
            )
            receipts.append(receipt.get_receipt_dict())

        return receipts

    def update_receipt_status(self, receipt_id: int, status_id: int) -> int:
        """
        Update receipt status in the database.

        :param receipt_id: int Id of the receipt
        :param status_id: int Id of the status
        """
        query: str = f"""
            UPDATE receipt SET status_id = {status_id} WHERE receipt_id = {receipt_id}
        """

        asyncio.run(self.query_executor.execute(query))

        return 1


    def update_total_amount(self, receipt_id: int, amount: float) -> int:
        """
        Update receipt status in the database.

        :param receipt_id: int Id of the receipt
        :param amount: float amount to update
        """
        prv_total = self.get_receipt(receipt_id)['total_amount']
        new_total = prv_total + amount
        query: str = f"""
            UPDATE receipt SET total_amount = {new_total} WHERE receipt_id = {receipt_id}
        """

        asyncio.run(self.query_executor.execute(query))

        return 1