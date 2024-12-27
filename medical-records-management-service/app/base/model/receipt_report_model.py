import asyncio

from app.base.utilities import const
from app.base.utilities.query_executor import AsyncQueryExecutor

DB_CONFIG = {
    'host': const.DB_HOST,
    'user': const.DB_USER,
    'password': const.DB_PASSWORD,
    'database': const.DB_NAME,
    'port': const.DB_PORT
}


class ReceiptReportModel:
    """
    This class is used to interact with the database to perform CRUD operations on the receipt report table
    """
    def __init__(self):
        self.db_config = DB_CONFIG
        self.query_executor = AsyncQueryExecutor(DB_CONFIG)

    def create_receipt_report(self, report_data: dict) -> int:
        """
        Insert a new data to receipt report table

        :param report_data: dict of receipt report data
        """
        receipt_id: int = report_data['receipt_id']
        report_id: int = report_data['report_id']
        doctor_notes: str = report_data['doctor_notes']

        query: str = (f"INSERT INTO receipt_reports "
                      f"(receipt_id, report_id, doctor_notes) "
                      f"VALUES ({receipt_id}, {report_id}, '{doctor_notes}')")

        asyncio.run(self.query_executor.execute(query))

        return 1

    def get_receipt_report(self, receipt_id: int) -> list:
        """
        Get receipt report data from the database.

        :param receipt_id: int Id of the receipt
        """
        query: str = f"""
            SELECT * FROM receipt_reports WHERE receipt_id = {receipt_id}
        """

        receipt_data = asyncio.run(self.query_executor.fetch_all(query))

        if not receipt_data:
            return []

        receipt_report_data: list = []
        for report in receipt_data:
            report_type_model: ReportTypeModel = ReportTypeModel()
            receipt_id = report[0]
            report_id = report[1]
            status = report[2]
            notes = report[3]

            report_type = report_type_model.get_report_type(report_id)

            receipt_report_data.append({
                'receipt_id': receipt_id,
                'report_id': report_id,
                'status': status,
                'report_type': report_type[1],
                'report_price': report_type[3],
                'notes': notes
            })


        return receipt_report_data

    def update_receipt_report(self, receipt_id: int, report_id: int, status: str = 'Completed') -> int:
        """
        Update receipt report data in the database.

        :param receipt_id: int Id of the receipt
        :param report_id: int Id of the report
        :param status: str Status of the report
        """
        query: str = f"""
            UPDATE receipt_reports SET status='{status}' WHERE report_id = {report_id} AND receipt_id = {receipt_id}
        """

        asyncio.run(self.query_executor.execute(query))

        return 1



class ReportTypeModel:
    """
    This class is used to interact with the database to perform CRUD operations on the report type table
    """
    def __init__(self):
        self.db_config = DB_CONFIG
        self.query_executor = AsyncQueryExecutor(DB_CONFIG)

    def get_report_type(self, report_type_id: int) -> dict:
        """
        Get report type data from the database.

        :param report_type_id: int Id of the report type
        """
        query: str = f"""
            SELECT * FROM report WHERE report_id = {report_type_id}
        """

        report_type_data = asyncio.run(self.query_executor.fetch_one(query))

        return report_type_data