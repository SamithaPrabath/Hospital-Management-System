import asyncio
import uuid
from datetime import datetime

from app.base.utilities import const
from app.base.utilities.query_executor import AsyncQueryExecutor

DB_CONFIG = {
    'host': const.DB_HOST,
    'user': const.DB_USER,
    'password': const.DB_PASSWORD,
    'database': const.DB_NAME,
    'port': const.DB_PORT
}


class MedicalReportModel:
    def __init__(self):
        self.db_config = DB_CONFIG
        self.query_executor = AsyncQueryExecutor(DB_CONFIG)

    def create_medical_report(self, report_data: dict) -> int:
        """
        Create a new report in the database.
        :param report_data:
        :return:
        """
        today: datetime = datetime.now()

        query: str = (f"INSERT INTO medical_report "
                      f"(report_id, receipt_id, image, description, issued_by, issued_date) "
                      f"VALUES ({report_data['report_id']}, {report_data['receipt_id']}, '{report_data['image']}', "
                      f"'{report_data['description']}', {report_data['issued_by']}, '{today}')")

        asyncio.run(self.query_executor.execute(query))

        return 1

    def get_medical_report(self, receipt_id: int) -> list:
        """
        Get receipt data from the database.
        :param receipt_id:
        :return:
        """
        query: str = f"""
            SELECT * FROM medical_report WHERE receipt_id = {receipt_id}
        """

        report_data = asyncio.run(self.query_executor.fetch_all(query))

        medical_reports = []
        for receipt in report_data:
            receipt_data = {
                'report_id': receipt[0],
                'receipt_id': receipt[1],
                'image': receipt[2],
                'description': receipt[3],
                'issued_by': receipt[4],
                'issued_date': receipt[5]
            }
            medical_reports.append(receipt_data)

        return medical_reports


    def delete_medical_report(self, receipt_id: int, report_id: int) -> int:
        """
        Delete a report from the database.
        :param receipt_id:
        :param report_id:
        :return:
        """
        query: str = f"""
            DELETE FROM medical_report WHERE receipt_id = {receipt_id} AND report_id = {report_id}
        """

        asyncio.run(self.query_executor.execute(query))

        return 1
